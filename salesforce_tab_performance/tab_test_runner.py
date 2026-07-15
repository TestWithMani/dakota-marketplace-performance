"""Shared runner for Salesforce tab performance tests."""

from __future__ import annotations

import time
from statistics import mean

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from . import config
from .credentials_utils import get_credential
from .excel_logger import log_performance_results
from .performance_utils import measure_component_render_time
from .tabs_registry import get_tab_definition


def run_tab_performance_test(
    driver,
    tab_name: str | None = None,
    tab_url: str | None = None,
    tab_key: str | None = None,
    start_element_xpath: str | None = None,
    end_element_xpath: str | None = None,
    end_condition: str | None = None,
) -> None:
    """Run login, navigate to tab, measure render times, and assert SLA."""
    tab_definition = get_tab_definition(tab_key) if tab_key else None
    tab_name = tab_name or (tab_definition.display_name if tab_definition else None)
    tab_url = tab_url or (tab_definition.url if tab_definition else None)
    end_element_xpath = (
        end_element_xpath
        if end_element_xpath is not None
        else (tab_definition.end_element_xpath if tab_definition else None)
    )
    end_condition = (
        end_condition
        if end_condition is not None
        else (tab_definition.end_condition if tab_definition and tab_definition.end_condition else "visible")
    )

    if not tab_name or not tab_url:
        raise ValueError("run_tab_performance_test requires tab_name/tab_url or a valid tab_key")

    wait = WebDriverWait(driver, 60)

    with allure.step("Open login page and authenticate"):
        _login_to_salesforce(driver, wait)

    with allure.step(f"Open {tab_name} tab URL directly"):
        driver.get(tab_url)

    with allure.step(f"Stabilize for {config.STABILIZATION_WAIT} seconds before measurement"):
        time.sleep(config.STABILIZATION_WAIT)

    execution_times = []
    with allure.step(f"Measure render completion for {config.ITERATIONS} iterations"):
        for iteration in range(1, config.ITERATIONS + 1):
            driver.refresh()
            duration = measure_component_render_time(
                driver,
                start_element_xpath=start_element_xpath,
                end_element_xpath=end_element_xpath,
                end_condition=end_condition,
            )
            execution_times.append(duration)
            allure.attach(
                body=f"Iteration {iteration}: {duration:.3f} seconds",
                name=f"Iteration {iteration} Result",
                attachment_type=allure.attachment_type.TEXT,
            )

    average_time = round(mean(execution_times), 3)
    sla_status = "PASS" if average_time <= config.SLA_SECONDS else "FAIL"
    capabilities = driver.capabilities or {}
    browser_name = str(capabilities.get("browserName", "chrome")).title()
    browser_version = str(capabilities.get("browserVersion", "Unknown"))
    browser_label = f"{browser_name} {browser_version}"
    platform = str(
        capabilities.get("platformName")
        or capabilities.get("platform")
        or capabilities.get("os")
        or "Unknown"
    )
    os_version = str(
        capabilities.get("osVersion")
        or capabilities.get("platformVersion")
        or "Unknown"
    )

    with allure.step("Write iteration and average results to Excel"):
        excel_path = log_performance_results(
            tab_name=tab_name,
            execution_times=execution_times,
            average_time=average_time,
            sla_seconds=config.SLA_SECONDS,
            browser=browser_label,
            platform=platform,
            os_version=os_version,
        )
        allure.attach(
            body=f"Results saved to: {excel_path}",
            name="Excel Output Path",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Attach final performance summary"):
        summary = (
            f"Tab Name: {tab_name}\n"
            f"Iterations: {config.ITERATIONS}\n"
            f"Execution Times: {execution_times}\n"
            f"Average Time: {average_time:.3f} seconds\n"
            f"SLA Threshold: {config.SLA_SECONDS:.3f} seconds\n"
            f"SLA Status: {sla_status}"
        )
        allure.attach(
            body=summary,
            name="Performance Summary",
            attachment_type=allure.attachment_type.TEXT,
        )

    assert average_time <= config.SLA_SECONDS, (
        f"{tab_name} average render time {average_time:.3f}s exceeded SLA "
        f"{config.SLA_SECONDS:.3f}s"
    )


# Login attempts a full username+password fill cycle this many times before failing.
LOGIN_FILL_RETRIES = 3

# Ordered fallback locators. The configured Salesforce IDs are tried first, then
# generic attribute-based locators for resilience against Experience Cloud markup drift.
USERNAME_LOCATORS = (
    (By.ID, config.USERNAME_FIELD_ID),
    (By.NAME, "username"),
    (By.CSS_SELECTOR, "input[type='email']"),
    (By.CSS_SELECTOR, "input[autocomplete='username']"),
)
PASSWORD_LOCATORS = (
    (By.ID, config.PASSWORD_FIELD_ID),
    (By.NAME, "password"),
    (By.CSS_SELECTOR, "input[type='password']"),
    (By.CSS_SELECTOR, "input[autocomplete='current-password']"),
)
SUBMIT_LOCATORS = (
    (By.ID, config.SUBMIT_BUTTON_ID),
    (By.CSS_SELECTOR, "button[type='submit']"),
    (By.CSS_SELECTOR, "input[type='submit']"),
    (By.XPATH, "//button[contains(.,'Log In') or contains(.,'Login')]"),
)


def _login_to_salesforce(driver, wait: WebDriverWait) -> None:
    """Authenticate with credentials provided via environment variables.

    The Experience Cloud login form is flaky: password focus / partial page
    settle can leave the username blank. We re-find fields, verify both values,
    and refill the username if it was cleared before submitting.
    """
    username = _required_env("SF_USERNAME")
    password = _required_env("SF_PASSWORD")

    driver.get(config.LOGIN_URL)
    _wait_for_visible_field(driver, wait, USERNAME_LOCATORS)
    _wait_for_visible_field(driver, wait, PASSWORD_LOCATORS)
    # Allow Experience Cloud / Aura handlers to attach before interacting.
    time.sleep(1.0)

    last_error: Exception | None = None
    for attempt in range(1, LOGIN_FILL_RETRIES + 1):
        try:
            print(f"[Login] Filling credentials (attempt {attempt}/{LOGIN_FILL_RETRIES})...")
            _fill_credentials(driver, wait, username, password)
            last_error = None
            break
        except Exception as exc:
            last_error = exc
            print(f"[Login] Fill attempt {attempt} failed: {exc}")
            time.sleep(1.0)

    if last_error is not None:
        raise last_error

    login_button = _find_first_visible(driver, SUBMIT_LOCATORS)
    if login_button is None:
        raise RuntimeError("Login submit button not found")

    wait.until(ec.element_to_be_clickable(login_button))
    try:
        login_button.click()
    except Exception:
        driver.execute_script("arguments[0].click();", login_button)

    wait.until(ec.visibility_of_element_located((By.XPATH, config.START_ELEMENT_XPATH)))


def _wait_for_visible_field(driver, wait: WebDriverWait, locators):
    """Wait until any locator in the set resolves to a visible, enabled field."""
    return wait.until(lambda _driver: _find_first_visible(driver, locators))


def _find_first_visible(driver, locators):
    """Return the first displayed and enabled element across ordered locators."""
    for locator in locators:
        for element in driver.find_elements(*locator):
            try:
                if element.is_displayed() and element.is_enabled():
                    return element
            except Exception:
                continue
    return None


def _field_value(driver, field) -> str:
    """Read the current input value via attribute, falling back to JS."""
    try:
        raw = field.get_attribute("value")
        if raw is not None and str(raw).strip():
            return str(raw).strip()
    except Exception:
        pass
    try:
        via_js = driver.execute_script("return arguments[0].value || '';", field)
        return str(via_js or "").strip()
    except Exception:
        return ""


def _js_set_value(driver, field, value: str) -> None:
    """Set value with the native setter + events (Aura / Lightning-safe)."""
    driver.execute_script(
        """
        const el = arguments[0];
        const val = arguments[1];
        el.focus();
        const proto = window.HTMLInputElement.prototype;
        const descriptor = Object.getOwnPropertyDescriptor(proto, 'value');
        if (descriptor && descriptor.set) {
            descriptor.set.call(el, val);
        } else {
            el.value = val;
        }
        el.dispatchEvent(new Event('input', { bubbles: true }));
        el.dispatchEvent(new Event('change', { bubbles: true }));
        el.dispatchEvent(new KeyboardEvent('keyup', { bubbles: true }));
        """,
        field,
        value,
    )


def _set_input_value(driver, wait: WebDriverWait, field, value: str, *, label: str) -> None:
    """Populate a login field reliably: JS set first, then send_keys fallback."""
    wait.until(lambda _driver: field.is_displayed() and field.is_enabled())
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", field)
    try:
        driver.execute_script("arguments[0].click();", field)
    except Exception:
        pass
    time.sleep(0.25)

    # Prefer JS set first — more reliable on Salesforce login than send_keys alone.
    _js_set_value(driver, field, value)
    time.sleep(0.2)

    if _field_value(driver, field) != value.strip():
        try:
            field.send_keys(Keys.CONTROL, "a")
            field.send_keys(Keys.BACKSPACE)
        except Exception:
            try:
                field.clear()
            except Exception:
                pass
        field.send_keys(value)
        time.sleep(0.3)

    if _field_value(driver, field) != value.strip():
        _js_set_value(driver, field, value)
        time.sleep(0.2)

    actual = _field_value(driver, field)
    if actual != value.strip():
        raise ValueError(
            f"Could not populate login {label}. Expected '{value}', got '{actual}'"
        )


def _fill_credentials(driver, wait: WebDriverWait, user: str, pwd: str) -> None:
    """Fill username then password, and re-check username after password."""
    username_field = _wait_for_visible_field(driver, wait, USERNAME_LOCATORS)
    _set_input_value(driver, wait, username_field, user, label="username")

    password_field = _wait_for_visible_field(driver, wait, PASSWORD_LOCATORS)
    _set_input_value(driver, wait, password_field, pwd, label="password")

    # Password focus / autofill often clears username on this form.
    username_field = _wait_for_visible_field(driver, wait, USERNAME_LOCATORS)
    if _field_value(driver, username_field) != user.strip():
        print("[Login] Username was empty/cleared after password fill — refilling.")
        _set_input_value(driver, wait, username_field, user, label="username")

    password_field = _wait_for_visible_field(driver, wait, PASSWORD_LOCATORS)
    if _field_value(driver, password_field) != pwd.strip():
        print("[Login] Password missing after username refill — refilling.")
        _set_input_value(driver, wait, password_field, pwd, label="password")
        # Final username check after the second password fill.
        username_field = _wait_for_visible_field(driver, wait, USERNAME_LOCATORS)
        if _field_value(driver, username_field) != user.strip():
            _set_input_value(driver, wait, username_field, user, label="username")

    username_field = _wait_for_visible_field(driver, wait, USERNAME_LOCATORS)
    password_field = _wait_for_visible_field(driver, wait, PASSWORD_LOCATORS)
    user_actual = _field_value(driver, username_field)
    pwd_actual = _field_value(driver, password_field)
    if user_actual != user.strip() or pwd_actual != pwd.strip():
        raise ValueError(
            f"Login fields not ready. username='{user_actual}', "
            f"password_len={len(pwd_actual)} (expected {len(pwd.strip())})"
        )
    print(
        f"[Login] Credentials verified "
        f"(username_len={len(user_actual)}, password_len={len(pwd_actual)})."
    )


def _required_env(variable_name: str) -> str:
    """Fail clearly if required credential variable is missing."""
    value = get_credential(variable_name)
    if not value:
        pytest.fail(
            f"Missing required environment variable: {variable_name}. "
            "Set it via setx, current shell env, or .env in project root."
        )
    return value
