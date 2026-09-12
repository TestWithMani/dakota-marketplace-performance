"""Performance test for Family Office Investments tab."""

import allure

from salesforce_tab_performance.tab_test_runner import run_tab_performance_test

@allure.feature("Salesforce Tab Performance")
@allure.story("Family Office Investments Tab Component Render Completion")
def test_family_office_investments_tab_render_performance(driver):
    run_tab_performance_test(
        driver,
        tab_key="family_office_investments",
    )
