"""Performance test for Dakota Benchmarks tab."""

import allure

from salesforce_tab_performance.tab_test_runner import run_tab_performance_test

@allure.feature("Salesforce Tab Performance")
@allure.story("Dakota Benchmarks Tab Component Render Completion")
def test_dakota_benchmarks_tab_render_performance(driver):
    run_tab_performance_test(
        driver,
        tab_key="dakota_benchmarks",
    )
