"""Performance test for Hedge Fund Performance Benchmarking tab."""

import allure

from salesforce_tab_performance.tab_test_runner import run_tab_performance_test

@allure.feature("Salesforce Tab Performance")
@allure.story("Hedge Fund Performance Benchmarking Tab Component Render Completion")
def test_hedge_fund_performance_benchmarking_tab_render_performance(driver):
    run_tab_performance_test(
        driver,
        tab_key="hedge_fund_performance_benchmarking",
    )
