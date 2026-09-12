"""Pytest fixtures for Selenium driver lifecycle."""

from __future__ import annotations

import sys
from pathlib import Path

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from salesforce_tab_performance.credentials_utils import bootstrap_credentials
from salesforce_tab_performance.infra_errors import (
    INFRA_SKIP_PREFIX,
    infrastructure_error_summary,
    is_infrastructure_error,
)

SMOKE_TEST_FILES = {
    "test_accounts_tab_performance.py",
    "test_all_documents_tab_performance.py",
    "test_13f_filings_tab_performance.py",
    "test_contact_tab_performance.py",
    "test_marketplace_home_tab_performance.py",
    "test_portfolio_companies_tab_performance.py",
    "test_public_company_search_tab_performance.py",
}


@pytest.fixture(scope="session", autouse=True)
def preload_credentials() -> None:
    """Load persisted credentials before any tests execute."""
    bootstrap_credentials()


def pytest_addoption(parser):
    """Register runtime browser selection from CLI/Jenkins."""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "edge", "firefox"],
        help="Browser for Selenium tests: chrome, edge, or firefox.",
    )


@pytest.fixture(scope="function")
def driver(request):
    """Provide a clean WebDriver instance for each test."""
    browser = (request.config.getoption("--browser") or "chrome").strip().lower()

    if browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-gpu")
        web_driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
    elif browser == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--start-maximized")
        edge_options.add_argument("--disable-notifications")
        edge_options.add_argument("--disable-gpu")
        web_driver = webdriver.Edge(service=EdgeService(), options=edge_options)
    else:
        firefox_options = FirefoxOptions()
        web_driver = webdriver.Firefox(service=FirefoxService(), options=firefox_options)
        web_driver.maximize_window()

    web_driver.implicitly_wait(0)
    yield web_driver
    try:
        web_driver.quit()
    except Exception:
        # Browser process may already be gone for crashed/disconnected sessions.
        pass


def pytest_collection_modifyitems(items):
    """Auto-tag tests by category and smoke suite."""
    for item in items:
        file_name = Path(item.fspath).name.lower()

        item.add_marker(pytest.mark.full)

        if file_name in SMOKE_TEST_FILES:
            item.add_marker(pytest.mark.smoke)

        if "home_tab" in file_name:
            item.add_marker(pytest.mark.Test)

        if "contact" in file_name:
            item.add_marker(pytest.mark.contacts)

        if "account" in file_name:
            item.add_marker(pytest.mark.accounts)

        if any(token in file_name for token in ("document", "memo")):
            item.add_marker(pytest.mark.documents)

        if "transaction" in file_name:
            item.add_marker(pytest.mark.transactions)

        if "metro_area" in file_name or "metro_areas" in file_name:
            item.add_marker(pytest.mark.metro_areas)

        if "report" in file_name or "reports" in file_name:
            item.add_marker(pytest.mark.reports)

        if "dashboard" in file_name:
            item.add_marker(pytest.mark.custom_dashboards)


def _configured_reruns(item) -> int:
    """Return --reruns count when pytest-rerunfailures is active."""
    for option_name in ("reruns", "--reruns"):
        try:
            value = item.config.getoption(option_name, default=0)
        except (TypeError, ValueError):
            continue
        try:
            return max(int(value or 0), 0)
        except (TypeError, ValueError):
            continue
    return 0


def _infra_reruns_exhausted(item) -> bool:
    """True when pytest-rerunfailures will not run another attempt."""
    reruns = _configured_reruns(item)
    if reruns <= 0:
        return False
    execution_count = getattr(item, "execution_count", 1)
    return execution_count >= reruns + 1


def _attach_failure_diagnostics(item, driver) -> None:
    """Attach URL, page source, and screenshot for real tab failures."""
    try:
        allure.attach(
            body=driver.current_url,
            name="Current URL",
            attachment_type=allure.attachment_type.TEXT,
        )
    except Exception:
        pass

    try:
        allure.attach(
            body=driver.page_source,
            name="Page Source",
            attachment_type=allure.attachment_type.HTML,
        )
    except Exception:
        pass

    try:
        allure.attach(
            body=driver.get_screenshot_as_png(),
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG,
        )
    except Exception:
        pass


@pytest.hookimpl(hookwrapper=True, trylast=True)
def pytest_runtest_makereport(item, call):
    """Rerun via Jenkins handles infra errors; skip in reports if still failing after retries."""
    outcome = yield
    report = outcome.get_result()

    if call.when != "call" or not report.failed:
        return

    exc = call.excinfo.value if call.excinfo else None
    if is_infrastructure_error(exc):
        if not _infra_reruns_exhausted(item):
            # Rerun pending: avoid screenshot/page-source calls on a dead WebDriver session.
            return

        attempts = getattr(item, "execution_count", 1)
        reruns = _configured_reruns(item)
        reason = (
            f"{INFRA_SKIP_PREFIX} WebDriver/browser connection issue after "
            f"{attempts} attempt(s) (configured reruns={reruns}): "
            f"{infrastructure_error_summary(exc)}"
        )
        report.outcome = "skipped"
        # pytest 8+/9 terminal expects skip longrepr as (path, lineno, reason).
        # A plain string crashes pytest_runtest_logreport and aborts the suite.
        try:
            path = str(getattr(item, "path", None) or item.fspath)
        except Exception:
            path = str(item.nodeid)
        try:
            lineno = int((item.location or (None, 0, None))[1] or 0)
        except Exception:
            lineno = 0
        report.longrepr = (path, lineno, reason)
        allure.dynamic.tag("infra_skip")
        allure.attach(
            body=reason,
            name="Infrastructure Skip",
            attachment_type=allure.attachment_type.TEXT,
        )
        return

    driver = item.funcargs.get("driver")
    if driver:
        _attach_failure_diagnostics(item, driver)
