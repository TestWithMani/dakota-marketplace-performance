pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '30', artifactNumToKeepStr: '30'))
        timeout(time: 200, unit: 'MINUTES')
    }

    triggers {
        cron('40 16 * * 3')
    }

    parameters {
        choice(
            name: 'TEST_SELECTION_MODE',
            choices: ['ALL_TABS', 'SMOKE', 'CHECKBOX_SELECTION'],
            description: 'Execution mode: ALL_TABS runs full suite, SMOKE runs predefined critical tabs, CHECKBOX_SELECTION runs selected TAB_* checkboxes.'
        )
        booleanParam(
            name: 'FRESH_REPORT_OUTPUT',
            defaultValue: false,
            description: 'Clear old report artifacts before this run and generate fresh Excel + Allure output.'
        )
        booleanParam(
            name: 'RESET_JOB_BUILD_HISTORY',
            defaultValue: false,
            description: 'Safe mode: clean workspace report artifacts only (does not delete Jenkins build records or reset build numbers).'
        )
        string(
            name: 'ADDITIONAL_EMAILS',
            defaultValue: '',
            description: 'Additional email recipients (comma-separated list).'
        )
        string(
            name: 'DEFAULT_EMAIL',
            defaultValue: 'usman.arshad@gmail.com',
            description: 'Primary recipient for pipeline report emails.'
        )
        string(
            name: 'SF_CREDENTIALS_ID',
            defaultValue: 'sf-marketplace-creds',
            description: 'Jenkins credentials ID for Salesforce login automation.'
        )
        booleanParam(
            name: 'ENABLE_INFRA_RETRY',
            defaultValue: true,
            description: 'Automatically retry only flaky/infrastructure Selenium failures.'
        )
        string(
            name: 'INFRA_RETRY_COUNT',
            defaultValue: '1',
            description: 'Maximum retries for allowed infra failures (0 disables retries).'
        )
        choice(
            name: 'BROWSER',
            choices: ['chrome', 'edge', 'firefox'],
            description: 'Browser used for Selenium test execution.'
        )
        string(
            name: 'PARALLEL_WORKERS',
            defaultValue: '1',
            description: "Pytest xdist workers: '1' disables parallel, use integer >1 or 'auto'."
        )
        booleanParam(
            name: 'RUN_ALLURE',
            defaultValue: true,
            description: 'Generate and publish Allure report in Jenkins.'
        )
        booleanParam(
            name: 'SEND_EMAIL',
            defaultValue: true,
            description: 'Send HTML email summary after pipeline completion.'
        )
        booleanParam(name: 'TAB_13F_FILINGS_INVESTMENTS_SEARCH', defaultValue: false, description: 'Run 13F Filings Investments Search tab test.')
        booleanParam(name: 'TAB_13F_FILINGS', defaultValue: false, description: 'Run 13F Filings tab test.')
        booleanParam(name: 'TAB_ACCOUNTS', defaultValue: false, description: 'Run Accounts tab test.')
        booleanParam(name: 'TAB_ALL_DOCUMENTS', defaultValue: false, description: 'Run All Documents tab test.')
        booleanParam(name: 'TAB_BENCHMARKING', defaultValue: false, description: 'Run Benchmarking tab test.')
        booleanParam(name: 'TAB_CONFERENCE_DASHBOARD', defaultValue: false, description: 'Run Conference Dashboard tab test.')
        booleanParam(name: 'TAB_CONFERENCE', defaultValue: false, description: 'Run Conference tab test.')
        booleanParam(name: 'TAB_CONSULTANT_REVIEWS_DASHBOARD', defaultValue: false, description: 'Run Consultant Reviews Dashboard tab test.')
        booleanParam(name: 'TAB_CONTACT', defaultValue: false, description: 'Run Contact tab test.')
        booleanParam(name: 'TAB_CUSTOM_PORTFOLIO_DASHBOARD', defaultValue: false, description: 'Run Custom Portfolio Dashboard tab test.')
        booleanParam(name: 'TAB_DAKOTA_CITY_GUIDES', defaultValue: false, description: 'Run Dakota City Guides tab test.')
        booleanParam(name: 'TAB_DAKOTA_JOE_REPORTS', defaultValue: false, description: 'Run Dakota Joe Reports tab test.')
        booleanParam(name: 'TAB_DAKOTA_VIDEOS', defaultValue: false, description: 'Run Dakota Videos tab test.')
        booleanParam(name: 'TAB_EVERGREEN_FUND_PERFORMANCE', defaultValue: false, description: 'Run Evergreen Fund Performance tab test.')
        booleanParam(name: 'TAB_FEE_SCHEDULES_DASHBOARD', defaultValue: false, description: 'Run Fee Schedules Dashboard tab test.')
        booleanParam(name: 'TAB_FORECASTED_TRANSACTIONS', defaultValue: false, description: 'Run Forecasted Transactions tab test.')
        booleanParam(name: 'TAB_FUND_FAMILY_MEMOS', defaultValue: false, description: 'Run Fund Family Memos tab test.')
        booleanParam(name: 'TAB_FUND_LAUNCHES', defaultValue: false, description: 'Run Fund Launches tab test.')
        booleanParam(name: 'TAB_FUNDRAISING_NEWS', defaultValue: false, description: 'Run Fundraising News tab test.')
        booleanParam(name: 'TAB_HEDGE_FUND_PERFORMANCE', defaultValue: false, description: 'Run Hedge Fund Performance tab test.')
        booleanParam(name: 'TAB_INVESTMENT_ALLOCATOR_CONTACTS', defaultValue: false, description: 'Run Investment Allocator Contacts tab test.')
        booleanParam(name: 'TAB_INVESTMENT_ALLOCATOR_METRO_AREAS', defaultValue: false, description: 'Run Investment Allocator Metro Areas tab test.')
        booleanParam(name: 'TAB_INVESTMENT_ALLOCATOR', defaultValue: false, description: 'Run Investment Allocator tab test.')
        booleanParam(name: 'TAB_INVESTMENT_FIRM_CONTACTS', defaultValue: false, description: 'Run Investment Firm Contacts tab test.')
        booleanParam(name: 'TAB_INVESTMENT_FIRM_METRO_AREA', defaultValue: false, description: 'Run Investment Firm Metro Area tab test.')
        booleanParam(name: 'TAB_INVESTMENT_FIRM', defaultValue: false, description: 'Run Investment Firm tab test.')
        booleanParam(name: 'TAB_MANAGER_PRESENTATION_DASHBOARD', defaultValue: false, description: 'Run Manager Presentation Dashboard tab test.')
        booleanParam(name: 'TAB_MARKETPLACE_HOME', defaultValue: false, description: 'Run Marketplace Home tab test.')
        booleanParam(name: 'TAB_MARKETPLACE_SEARCHES', defaultValue: false, description: 'Run Marketplace Searches tab test.')
        booleanParam(name: 'TAB_METRO_AREA', defaultValue: false, description: 'Run Metro Area tab test.')
        booleanParam(name: 'TAB_MY_ACCOUNT', defaultValue: false, description: 'Run My Account tab test.')
        booleanParam(name: 'TAB_PENSION_DOCUMENTS', defaultValue: false, description: 'Run Pension Documents tab test.')
        booleanParam(name: 'TAB_PORTFOLIO_COMPANIES_METRO_AREA', defaultValue: false, description: 'Run Portfolio Companies Metro Area tab test.')
        booleanParam(name: 'TAB_PORTFOLIO_COMPANIES_METRO_AREAS', defaultValue: false, description: 'Run Portfolio Companies Metro Areas tab test.')
        booleanParam(name: 'TAB_PORTFOLIO_COMPANIES', defaultValue: false, description: 'Run Portfolio Companies tab test.')
        booleanParam(name: 'TAB_PRIVATE_COMPANIES_TRANSACTIONS', defaultValue: false, description: 'Run Private Companies Transactions tab test.')
        booleanParam(name: 'TAB_PRIVATE_FUND_SEARCH', defaultValue: false, description: 'Run Private Fund Search tab test.')
        booleanParam(name: 'TAB_PUBLIC_COMPANY_SEARCH', defaultValue: false, description: 'Run Public Company Search tab test.')
        booleanParam(name: 'TAB_PUBLIC_INVESTMENTS_SEARCH', defaultValue: false, description: 'Run Public Investments Search tab test.')
        booleanParam(name: 'TAB_PUBLIC_PLAN_MINUTE', defaultValue: false, description: 'Run Public Plan Minute tab test.')
        booleanParam(name: 'TAB_RECENT_TRANSACTIONS', defaultValue: false, description: 'Run Recent Transactions tab test.')
        booleanParam(name: 'TAB_REPORTS_EVERYTHING', defaultValue: false, description: 'Run Reports Everything tab test.')
        booleanParam(name: 'TAB_REPORTS_MRU', defaultValue: false, description: 'Run Reports MRU tab test.')
        booleanParam(name: 'TAB_REPORTS_USER_FOLDERS', defaultValue: false, description: 'Run Reports User Folders tab test.')
        booleanParam(name: 'TAB_SEARCHES_DASHBOARD', defaultValue: false, description: 'Run Searches Dashboard tab test.')
        booleanParam(name: 'TAB_UNIVERSITY_ALUMNI', defaultValue: false, description: 'Run University Alumni tab test.')
        booleanParam(name: 'TAB_WEALTH_CHANNEL_METRO_AREAS', defaultValue: false, description: 'Run Wealth Channel Metro Areas tab test.')
    }

    environment {
        VENV_DIR = '.venv-jenkins'
        PYTEST_JUNIT = 'test-results/pytest.xml'
        PYTEST_HTML = 'test-results/report.html'
        PYTEST_JSON = 'test-results/report.json'
        ALLURE_DIR = 'allure-results'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    if (fileExists('salesforce_tab_performance/requirements.txt')) {
                        echo 'Repository already present in workspace; skipping checkout.'
                    } else {
                        error(
                            "Workspace has no source code. Configure this job as 'Pipeline script from SCM' " +
                            "or use a Multibranch Pipeline so checkout can pull repository contents."
                        )
                    }
                    def shortCommit = env.GIT_COMMIT ? env.GIT_COMMIT.take(7) : 'N/A'
                    echo "Branch: ${env.BRANCH_NAME ?: 'main'} | Commit: ${shortCommit}"
                    def effectiveCfg = getEffectiveRunConfig()
                    if (effectiveCfg.scheduledBuild) {
                        echo 'Scheduled run detected: applying Wednesday 4:40 PM preset parameters.'
                    }
                }
            }
        }

        stage('Reset Build History (Optional)') {
            when {
                expression { return params.RESET_JOB_BUILD_HISTORY == true }
            }
            steps {
                echo "Reset Build History is ENABLED but running SAFE mode (no Jenkins internal API usage)."

                script {
                    // Instead of touching Jenkins builds, just clean workspace artifacts.
                    if (fileExists('test-results')) {
                        runShell(
                            'rm -rf test-results || true',
                            'rmdir /s /q test-results'
                        )
                    }
                    if (fileExists('allure-results')) {
                        runShell(
                            'rm -rf allure-results || true',
                            'rmdir /s /q allure-results'
                        )
                    }

                    echo 'Workspace history reset completed safely.'
                }
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    runShell(
                        '''
                            python3 -m venv ${VENV_DIR}
                            ${VENV_DIR}/bin/python -m pip install --upgrade pip
                            ${VENV_DIR}/bin/python -m pip install -r salesforce_tab_performance/requirements.txt
                            ${VENV_DIR}/bin/python -m pip install pytest-html pytest-json-report allure-pytest pytest-rerunfailures
                        ''',
                        '''
                            py -m venv %VENV_DIR%
                            %VENV_DIR%\\Scripts\\python -m pip install --upgrade pip
                            %VENV_DIR%\\Scripts\\python -m pip install -r salesforce_tab_performance/requirements.txt
                            %VENV_DIR%\\Scripts\\python -m pip install pytest-html pytest-json-report allure-pytest pytest-rerunfailures
                        '''
                    )
                }
            }
        }

        stage('Prepare Report Directories') {
            steps {
                script {
                    def effectiveCfg = getEffectiveRunConfig()
                    if (effectiveCfg.freshReportOutput) {
                        echo 'Fresh report mode enabled: clearing previous Excel and Allure history artifacts.'
                        runShell(
                            '''
                                rm -f salesforce_tab_performance/performance_results.xlsx || true
                                rm -f "salesforce_tab_performance/Dakota Marketplace Performance.xlsx" || true
                                rm -f salesforce_tab_performance/*.xlsx || true
                                rm -rf allure-report || true
                            ''',
                            '''
                                if exist "salesforce_tab_performance\\performance_results.xlsx" del /q "salesforce_tab_performance\\performance_results.xlsx"
                                if exist "salesforce_tab_performance\\Dakota Marketplace Performance.xlsx" del /q "salesforce_tab_performance\\Dakota Marketplace Performance.xlsx"
                                del /q "salesforce_tab_performance\\Dakota Marketplace Performance - *.xlsx" 2>nul
                                if exist allure-report rmdir /s /q allure-report
                            '''
                        )
                    }
                    runShell(
                        '''
                            rm -rf test-results allure-results || true
                            mkdir -p test-results allure-results
                        ''',
                        '''
                            if exist test-results rmdir /s /q test-results
                            if exist allure-results rmdir /s /q allure-results
                            mkdir test-results
                            mkdir allure-results
                        '''
                    )
                }
            }
        }

        stage('Static Validation') {
            steps {
                script {
                    def effectiveCfg = getEffectiveRunConfig()
                    validateRuntimeParameters(
                        effectiveCfg.testSelectionMode as String,
                        effectiveCfg.infraRetryCount as String,
                        effectiveCfg.browser as String,
                        params.PARALLEL_WORKERS as String
                    )
                    def selectedTestFiles = resolveSelectedTestFiles(
                        effectiveCfg.testSelectionMode as String,
                        params
                    )
                    echo "Selection mode -> ${effectiveCfg.testSelectionMode}"
                    echo "Selected ${selectedTestFiles.size()} test files."
                    runPytest('--version')
                    runPytest("--collect-only -q ${selectedTestFiles.join(' ')}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def effectiveCfg = getEffectiveRunConfig()
                    def runCmd = buildPytestCommand(
                        resolveSelectedTestFiles(
                            effectiveCfg.testSelectionMode as String,
                            params
                        ),
                        effectiveCfg.runAllure as boolean,
                        effectiveCfg.enableInfraRetry as boolean,
                        effectiveCfg.infraRetryCount as String,
                        effectiveCfg.browser as String,
                        params.PARALLEL_WORKERS as String
                    )
                    echo "Pytest command: pytest ${runCmd}"

                    withCredentials([usernamePassword(
                        credentialsId: "${params.SF_CREDENTIALS_ID}",
                        usernameVariable: 'SF_USERNAME',
                        passwordVariable: 'SF_PASSWORD'
                    )]) {
                        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                            runPytest(runCmd)
                        }
                    }

                }
            }
        }

        stage('Publish Reports') {
            steps {
                script {
                    def effectiveCfg = getEffectiveRunConfig()
                    if (fileExists(env.PYTEST_JUNIT)) {
                        junit testResults: env.PYTEST_JUNIT, allowEmptyResults: true
                    }

                    try {
                        publishHTML(target: [
                            reportName: 'Pytest HTML Report',
                            reportDir: 'test-results',
                            reportFiles: 'report.html',
                            keepAll: true,
                            alwaysLinkToLastBuild: true,
                            allowMissing: true
                        ])
                    } catch (MissingMethodException ex) {
                        echo 'HTML Publisher plugin not installed; skipping publishHTML step.'
                    }

                    if (effectiveCfg.runAllure && fileExists(env.ALLURE_DIR)) {
                        def allureArgs = [
                            includeProperties: false,
                            jdk: '',
                            properties: [],
                            reportBuildPolicy: 'ALWAYS',
                            results: [[path: env.ALLURE_DIR]],
                            reportName: 'Allure Report'
                        ]
                        allure(allureArgs)
                    } else if (effectiveCfg.runAllure) {
                        echo "Skipping Allure publish: ${env.ALLURE_DIR} directory not found."
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                def effectiveCfg = getEffectiveRunConfig()
                logTestSummaryToConsole('Post pipeline summary')
                if (fileExists('test-results')) {
                    archiveArtifacts artifacts: 'test-results/**', allowEmptyArchive: true
                }
                if (fileExists('allure-results')) {
                    archiveArtifacts artifacts: 'allure-results/**', allowEmptyArchive: true
                }
                def excelArtifact = prepareExcelArtifactPath()
                if (excelArtifact) {
                    archiveArtifacts artifacts: excelArtifact, allowEmptyArchive: true
                }
                if (effectiveCfg.sendEmail) {
                    sendEmailNotification(
                        currentBuild.currentResult ?: 'UNKNOWN',
                        effectiveCfg.defaultEmail as String,
                        effectiveCfg.additionalEmails as String
                    )
                }
            }
        }
    }
}

def isScheduledBuild() {
    try {
        // Prefer sandbox-friendly API (avoids Script Approval on rawBuild.getCauses()).
        def timerCauses = currentBuild?.getBuildCauses('hudson.triggers.TimerTrigger$TimerTriggerCause') ?: []
        if (!timerCauses.isEmpty()) {
            return true
        }
        // Backward compatibility for older Jenkins versions where typed causes may not resolve.
        def genericCauses = currentBuild?.getBuildCauses() ?: []
        return genericCauses.any { cause ->
            def cls = cause?._class ?: ''
            return cls.contains('TimerTriggerCause')
        }
    } catch (Exception ignored) {
        return false
    }
}

def getEffectiveRunConfig() {
    def scheduled = isScheduledBuild()
    return [
        scheduledBuild   : scheduled,
        testSelectionMode: scheduled ? 'ALL_TABS' : (params.TEST_SELECTION_MODE as String),
        freshReportOutput: scheduled ? true : (params.FRESH_REPORT_OUTPUT as boolean),
        additionalEmails : scheduled
            ? 'pstanley@dakota.com, draftcrm@rolustech.com'
            : (params.ADDITIONAL_EMAILS as String),
        defaultEmail     : scheduled
            ? 'omer.shafiq@rolustech.com'
            : (params.DEFAULT_EMAIL as String),
        enableInfraRetry : scheduled ? true : (params.ENABLE_INFRA_RETRY as boolean),
        infraRetryCount  : scheduled ? '2' : (params.INFRA_RETRY_COUNT as String),
        browser          : scheduled ? 'chrome' : (params.BROWSER as String),
        runAllure        : scheduled ? true : (params.RUN_ALLURE as boolean),
        sendEmail        : scheduled ? true : (params.SEND_EMAIL as boolean)
    ]
}

def shellQuotePytestArgs(List parts) {
    // Windows cmd splits on spaces unless quoted; keep pytest args intact.
    parts.collect { arg ->
        if (!arg.contains(' ')) {
            return arg
        }
        return '"' + arg.replace('"', '""') + '"'
    }.join(' ')
}

def buildPytestCommand(
    List selectedTestFiles,
    boolean runAllure,
    boolean enableInfraRetry,
    String infraRetryCount,
    String browser,
    String parallelWorkers
) {
    def allureArg = runAllure ? "--alluredir=${env.ALLURE_DIR}" : ''
    def parts = []

    // Show richer live output in Jenkins console:
    // -vv  : print each test node id as it runs
    // -ra  : include skip/xfail/etc summary in terminal output
    // --tb=short : concise failure tracebacks for readability
    // --color=no : avoid ANSI artifacts in Jenkins logs
    // -o console_output_style=progress : keep visible progress counters
    parts << '-vv'
    parts << '-ra'
    parts << '--tb=short'
    parts << '--color=no'
    parts << '-o'
    parts << 'console_output_style=progress'
    parts << "--browser=${(browser ?: 'chrome').trim().toLowerCase()}"

    def workers = (parallelWorkers ?: '1').trim().toLowerCase()
    if (workers != '1') {
        parts << '-n'
        parts << workers
    }

    if (allureArg) {
        parts << allureArg
    }

    if (enableInfraRetry) {
        def retries = 0
        try {
            retries = Math.max((infraRetryCount ?: '0').trim() as int, 0)
        } catch (Exception ignored) {
            retries = 1
        }

        if (retries > 0) {
            // Requires pytest-rerunfailures plugin.
            // Match short and fully-qualified Selenium exception names so retry works across traceback formats.
            parts << "--reruns=${retries}"
            parts << '--reruns-delay=2'
            parts << '--only-rerun=(selenium\\.common\\.exceptions\\.)?TimeoutException'
            parts << '--only-rerun=(selenium\\.common\\.exceptions\\.)?NoSuchElementException'
            parts << '--only-rerun=(selenium\\.common\\.exceptions\\.)?StaleElementReferenceException'
            parts << '--only-rerun=(selenium\\.common\\.exceptions\\.)?ElementClickInterceptedException'
            parts << '--only-rerun=(selenium\\.common\\.exceptions\\.)?WebDriverException'
            parts << '--only-rerun=SessionNotCreatedException'
            parts << '--only-rerun=urllib3\\.exceptions\\.ReadTimeoutError'
            parts << '--only-rerun=ReadTimeoutError'
            parts << '--only-rerun=HTTPConnectionPool\\(host='
            // Use \\s+ regex (no literal spaces) so Windows cmd does not split arguments.
            parts << '--only-rerun=Read\\s+timed\\s+out'
            parts << '--only-rerun=TimeoutError'
            parts << '--only-rerun=timed\\s+out'
            parts << '--only-rerun=disconnected:\\s+not\\s+connected\\s+to\\s+DevTools'
            parts << '--only-rerun=chrome\\s+not\\s+reachable'
            parts << '--only-rerun=ERR_CONNECTION_RESET'
        }
    }

    parts << "--junitxml=${env.PYTEST_JUNIT}"
    parts << "--html=${env.PYTEST_HTML}"
    parts << '--self-contained-html'
    parts << '--json-report'
    parts << "--json-report-file=${env.PYTEST_JSON}"
    if (selectedTestFiles && !selectedTestFiles.isEmpty()) {
        parts.addAll(selectedTestFiles)
    }

    return shellQuotePytestArgs(parts)
}

def resolveSelectedTestFiles(String selectionMode, def paramsObj) {
    def allFiles = getAvailableTestCaseFiles()
    def smokeFiles = getSmokeTestCaseFiles()
    def mode = (selectionMode ?: 'ALL_TABS').trim().toUpperCase()
    def checkboxMap = getTestCaseCheckboxMap()
    def resolved = checkboxMap
        .findAll { row -> (paramsObj."${row.param}" as boolean) }
        .collect { row -> row.file }
        .unique()
        .sort()

    if (mode == 'ALL_TABS') {
        if (!resolved.isEmpty()) {
            echo "Checkboxes detected (${resolved.size()}) but TEST_SELECTION_MODE=ALL_TABS; ignoring checkboxes and running full suite."
        }
        return allFiles
    }

    if (mode == 'SMOKE') {
        if (!resolved.isEmpty()) {
            echo "Checkboxes detected (${resolved.size()}) but TEST_SELECTION_MODE=SMOKE; ignoring checkboxes and running predefined SMOKE suite."
        }
        return smokeFiles
    }

    if (mode != 'CHECKBOX_SELECTION') {
        error("Unsupported TEST_SELECTION_MODE='${selectionMode}'. Allowed values: ALL_TABS, SMOKE, CHECKBOX_SELECTION.")
    }

    if (resolved.isEmpty()) {
        error('No tab checkbox selected. Either select one or more tab checkboxes, or set TEST_SELECTION_MODE=ALL_TABS.')
    }
    return resolved
}

def validateRuntimeParameters(String selectionMode, String infraRetryCount, String browser, String parallelWorkers) {
    def mode = (selectionMode ?: '').trim().toUpperCase()
    if (!(mode in ['ALL_TABS', 'SMOKE', 'CHECKBOX_SELECTION'])) {
        error("Invalid TEST_SELECTION_MODE='${selectionMode}'. Allowed values: ALL_TABS, SMOKE, CHECKBOX_SELECTION.")
    }

    def rawRetry = (infraRetryCount ?: '').trim()
    if (!(rawRetry ==~ /^\d+$/)) {
        error("INFRA_RETRY_COUNT must be a non-negative integer, but got '${infraRetryCount}'.")
    }

    def browserChoice = (browser ?: '').trim().toLowerCase()
    if (!(browserChoice in ['chrome', 'edge', 'firefox'])) {
        error("BROWSER must be one of: chrome, edge, firefox. Got '${browser}'.")
    }

    def workers = (parallelWorkers ?: '').trim().toLowerCase()
    if (workers == 'auto') {
        return
    }
    if (!(workers ==~ /^\d+$/)) {
        error("PARALLEL_WORKERS must be a non-negative integer or 'auto', but got '${parallelWorkers}'.")
    }
    if ((workers as int) < 1) {
        error("PARALLEL_WORKERS must be >= 1, but got '${parallelWorkers}'.")
    }
}

def getSmokeTestCaseFiles() {
    return [
        'tests/test_accounts_tab_performance.py',
        'tests/test_contact_tab_performance.py',
        'tests/test_marketplace_home_tab_performance.py',
        'tests/test_public_company_search_tab_performance.py',
        'tests/test_13f_filings_tab_performance.py',
        'tests/test_portfolio_companies_tab_performance.py',
        'tests/test_all_documents_tab_performance.py'
    ]
}

def getAvailableTestCaseFiles() {
    return [
        'tests/test_13f_filings_investments_search_tab_performance.py',
        'tests/test_13f_filings_tab_performance.py',
        'tests/test_accounts_tab_performance.py',
        'tests/test_all_documents_tab_performance.py',
        'tests/test_benchmarking_tab_performance.py',
        'tests/test_conference_dashboard_tab_performance.py',
        'tests/test_conference_tab_performance.py',
        'tests/test_consultant_reviews_dashboard_tab_performance.py',
        'tests/test_contact_tab_performance.py',
        'tests/test_custom_portfolio_dashboard_tab_performance.py',
        'tests/test_dakota_city_guides_tab_performance.py',
        'tests/test_dakota_joe_reports_tab_performance.py',
        'tests/test_dakota_videos_tab_performance.py',
        'tests/test_evergreen_fund_performance_tab_performance.py',
        'tests/test_fee_schedules_dashboard_tab_performance.py',
        'tests/test_forecasted_transactions_tab_performance.py',
        'tests/test_fund_family_memos_tab_performance.py',
        'tests/test_fund_launches_tab_performance.py',
        'tests/test_fundraising_news_tab_performance.py',
        'tests/test_hedge_fund_performance_tab_performance.py',
        'tests/test_investment_allocator_contacts_tab_performance.py',
        'tests/test_investment_allocator_metro_areas_tab_performance.py',
        'tests/test_investment_allocator_tab_performance.py',
        'tests/test_investment_firm_contacts_tab_performance.py',
        'tests/test_investment_firm_metro_area_tab_performance.py',
        'tests/test_investment_firm_tab_performance.py',
        'tests/test_manager_presentation_dashboard_tab_performance.py',
        'tests/test_marketplace_home_tab_performance.py',
        'tests/test_marketplace_searches_tab_performance.py',
        'tests/test_metro_area_tab_performance.py',
        'tests/test_my_account_tab_performance.py',
        'tests/test_pension_documents_tab_performance.py',
        'tests/test_portfolio_companies_metro_area_tab_performance.py',
        'tests/test_portfolio_companies_metro_areas_tab_performance.py',
        'tests/test_portfolio_companies_tab_performance.py',
        'tests/test_private_companies_transactions_tab_performance.py',
        'tests/test_private_fund_search_tab_performance.py',
        'tests/test_public_company_search_tab_performance.py',
        'tests/test_public_investments_search_tab_performance.py',
        'tests/test_public_plan_minute_tab_performance.py',
        'tests/test_recent_transactions_tab_performance.py',
        'tests/test_reports_everything_tab_performance.py',
        'tests/test_reports_mru_tab_performance.py',
        'tests/test_reports_user_folders_tab_performance.py',
        'tests/test_searches_dashboard_tab_performance.py',
        'tests/test_university_alumni_tab_performance.py',
        'tests/test_wealth_channel_metro_areas_tab_performance.py'
    ]
}

def getTestCaseCheckboxMap() {
    return [
        [param: 'TAB_13F_FILINGS_INVESTMENTS_SEARCH', file: 'tests/test_13f_filings_investments_search_tab_performance.py'],
        [param: 'TAB_13F_FILINGS', file: 'tests/test_13f_filings_tab_performance.py'],
        [param: 'TAB_ACCOUNTS', file: 'tests/test_accounts_tab_performance.py'],
        [param: 'TAB_ALL_DOCUMENTS', file: 'tests/test_all_documents_tab_performance.py'],
        [param: 'TAB_BENCHMARKING', file: 'tests/test_benchmarking_tab_performance.py'],
        [param: 'TAB_CONFERENCE_DASHBOARD', file: 'tests/test_conference_dashboard_tab_performance.py'],
        [param: 'TAB_CONFERENCE', file: 'tests/test_conference_tab_performance.py'],
        [param: 'TAB_CONSULTANT_REVIEWS_DASHBOARD', file: 'tests/test_consultant_reviews_dashboard_tab_performance.py'],
        [param: 'TAB_CONTACT', file: 'tests/test_contact_tab_performance.py'],
        [param: 'TAB_CUSTOM_PORTFOLIO_DASHBOARD', file: 'tests/test_custom_portfolio_dashboard_tab_performance.py'],
        [param: 'TAB_DAKOTA_CITY_GUIDES', file: 'tests/test_dakota_city_guides_tab_performance.py'],
        [param: 'TAB_DAKOTA_JOE_REPORTS', file: 'tests/test_dakota_joe_reports_tab_performance.py'],
        [param: 'TAB_DAKOTA_VIDEOS', file: 'tests/test_dakota_videos_tab_performance.py'],
        [param: 'TAB_EVERGREEN_FUND_PERFORMANCE', file: 'tests/test_evergreen_fund_performance_tab_performance.py'],
        [param: 'TAB_FEE_SCHEDULES_DASHBOARD', file: 'tests/test_fee_schedules_dashboard_tab_performance.py'],
        [param: 'TAB_FORECASTED_TRANSACTIONS', file: 'tests/test_forecasted_transactions_tab_performance.py'],
        [param: 'TAB_FUND_FAMILY_MEMOS', file: 'tests/test_fund_family_memos_tab_performance.py'],
        [param: 'TAB_FUND_LAUNCHES', file: 'tests/test_fund_launches_tab_performance.py'],
        [param: 'TAB_FUNDRAISING_NEWS', file: 'tests/test_fundraising_news_tab_performance.py'],
        [param: 'TAB_HEDGE_FUND_PERFORMANCE', file: 'tests/test_hedge_fund_performance_tab_performance.py'],
        [param: 'TAB_INVESTMENT_ALLOCATOR_CONTACTS', file: 'tests/test_investment_allocator_contacts_tab_performance.py'],
        [param: 'TAB_INVESTMENT_ALLOCATOR_METRO_AREAS', file: 'tests/test_investment_allocator_metro_areas_tab_performance.py'],
        [param: 'TAB_INVESTMENT_ALLOCATOR', file: 'tests/test_investment_allocator_tab_performance.py'],
        [param: 'TAB_INVESTMENT_FIRM_CONTACTS', file: 'tests/test_investment_firm_contacts_tab_performance.py'],
        [param: 'TAB_INVESTMENT_FIRM_METRO_AREA', file: 'tests/test_investment_firm_metro_area_tab_performance.py'],
        [param: 'TAB_INVESTMENT_FIRM', file: 'tests/test_investment_firm_tab_performance.py'],
        [param: 'TAB_MANAGER_PRESENTATION_DASHBOARD', file: 'tests/test_manager_presentation_dashboard_tab_performance.py'],
        [param: 'TAB_MARKETPLACE_HOME', file: 'tests/test_marketplace_home_tab_performance.py'],
        [param: 'TAB_MARKETPLACE_SEARCHES', file: 'tests/test_marketplace_searches_tab_performance.py'],
        [param: 'TAB_METRO_AREA', file: 'tests/test_metro_area_tab_performance.py'],
        [param: 'TAB_MY_ACCOUNT', file: 'tests/test_my_account_tab_performance.py'],
        [param: 'TAB_PENSION_DOCUMENTS', file: 'tests/test_pension_documents_tab_performance.py'],
        [param: 'TAB_PORTFOLIO_COMPANIES_METRO_AREA', file: 'tests/test_portfolio_companies_metro_area_tab_performance.py'],
        [param: 'TAB_PORTFOLIO_COMPANIES_METRO_AREAS', file: 'tests/test_portfolio_companies_metro_areas_tab_performance.py'],
        [param: 'TAB_PORTFOLIO_COMPANIES', file: 'tests/test_portfolio_companies_tab_performance.py'],
        [param: 'TAB_PRIVATE_COMPANIES_TRANSACTIONS', file: 'tests/test_private_companies_transactions_tab_performance.py'],
        [param: 'TAB_PRIVATE_FUND_SEARCH', file: 'tests/test_private_fund_search_tab_performance.py'],
        [param: 'TAB_PUBLIC_COMPANY_SEARCH', file: 'tests/test_public_company_search_tab_performance.py'],
        [param: 'TAB_PUBLIC_INVESTMENTS_SEARCH', file: 'tests/test_public_investments_search_tab_performance.py'],
        [param: 'TAB_PUBLIC_PLAN_MINUTE', file: 'tests/test_public_plan_minute_tab_performance.py'],
        [param: 'TAB_RECENT_TRANSACTIONS', file: 'tests/test_recent_transactions_tab_performance.py'],
        [param: 'TAB_REPORTS_EVERYTHING', file: 'tests/test_reports_everything_tab_performance.py'],
        [param: 'TAB_REPORTS_MRU', file: 'tests/test_reports_mru_tab_performance.py'],
        [param: 'TAB_REPORTS_USER_FOLDERS', file: 'tests/test_reports_user_folders_tab_performance.py'],
        [param: 'TAB_SEARCHES_DASHBOARD', file: 'tests/test_searches_dashboard_tab_performance.py'],
        [param: 'TAB_UNIVERSITY_ALUMNI', file: 'tests/test_university_alumni_tab_performance.py'],
        [param: 'TAB_WEALTH_CHANNEL_METRO_AREAS', file: 'tests/test_wealth_channel_metro_areas_tab_performance.py']
    ]
}

def runShell(String unixCommand, String windowsCommand) {
    if (isUnix()) {
        sh(unixCommand)
    } else {
        bat(windowsCommand)
    }
}

def runPytest(String args) {
    runShell(
        """
            ${env.VENV_DIR}/bin/python -m pytest ${args}
        """,
        """
            %VENV_DIR%\\Scripts\\python -m pytest ${args}
        """
    )
}

def getTestStatistics() {
    def stats = [total: 0, passed: 0, failed: 0, skipped: 0, collected: 0, not_run: 0]
    def junitPath = env.PYTEST_JUNIT ?: 'test-results/pytest.xml'
    def jsonSnapshot = getFinalOutcomesFromPytestJson()

    if (jsonSnapshot.hasData as boolean) {
        return jsonSnapshot.stats as Map
    }

    if (fileExists(junitPath)) {
        try {
            def xmlText = readFile(junitPath)
            def tests = extractIntFromXmlAttribute(xmlText, 'tests')
            def failures = extractIntFromXmlAttribute(xmlText, 'failures')
            def errors = extractIntFromXmlAttribute(xmlText, 'errors')
            def skipped = extractIntFromXmlAttribute(xmlText, 'skipped')
            def passed = Math.max(tests - failures - errors - skipped, 0)

            stats.total = tests
            stats.failed = failures + errors
            stats.skipped = skipped
            stats.passed = passed
            stats.collected = tests
            stats.not_run = 0
            echo "Using JUnit fallback stats -> total:${stats.total}, passed:${stats.passed}, failed:${stats.failed}, skipped:${stats.skipped}"
        } catch (Exception ex) {
            echo "Could not parse JUnit XML fallback: ${ex.message}"
        }
    } else {
        echo "JUnit XML report not found at ${junitPath}; no fallback stats available."
    }

    return stats
}

def getFailedTestNames() {
    def jsonSnapshot = getFinalOutcomesFromPytestJson()
    if (jsonSnapshot.hasData as boolean) {
        return (jsonSnapshot.failedTests ?: []) as List
    }

    def failures = []
    def junitPath = env.PYTEST_JUNIT ?: 'test-results/pytest.xml'
    if (!fileExists(junitPath)) {
        return failures
    }

    try {
        def xmlText = readFile(junitPath)
        def matcher = (xmlText =~ /(?si)<testcase\b([^>]*)>(?:(?!<\/testcase>).)*<(failure|error)\b/)
        while (matcher.find()) {
            def attrs = matcher.group(1) ?: ''
            def nameMatcher = (attrs =~ /\bname=(["'])(.*?)\1/)
            def classMatcher = (attrs =~ /\bclassname=(["'])(.*?)\1/)
            def name = nameMatcher.find() ? nameMatcher.group(2)?.trim() : ''
            def className = classMatcher.find() ? classMatcher.group(2)?.trim() : ''

            // Some pytest/JUnit variants emit a generic testcase name and keep tab identity in classname.
            def candidate = name
            if (
                (!candidate || !(candidate ==~ /(?i).*(tab|dashboard|metro|reports|documents|accounts|contacts|transactions).*/ || candidate.startsWith('test_')))
                && className
            ) {
                candidate = className.tokenize('.').last()
            }

            if (candidate) {
                failures << candidate
            }
        }
    } catch (Exception ex) {
        echo "Could not parse failed test names from JUnit XML: ${ex.message}"
    }

    return failures.unique()
}

def getSkippedInfraTestNames() {
    def skipped = []
    def junitPath = env.PYTEST_JUNIT ?: 'test-results/pytest.xml'
    if (fileExists(junitPath)) {
        try {
            def xmlText = readFile(junitPath)
            def matcher = (xmlText =~ /(?si)<testcase\b([^>]*)>(?:(?!<\/testcase>).)*<skipped\b[^>]*message=(["'])(.*?)\2/)
            while (matcher.find()) {
                def message = (matcher.group(3) ?: '').trim()
                if (!message.contains('INFRA_SKIP:')) {
                    continue
                }
                def attrs = matcher.group(1) ?: ''
                def nameMatcher = (attrs =~ /\bname=(["'])(.*?)\1/)
                def classMatcher = (attrs =~ /\bclassname=(["'])(.*?)\1/)
                def name = nameMatcher.find() ? nameMatcher.group(2)?.trim() : ''
                def className = classMatcher.find() ? classMatcher.group(2)?.trim() : ''
                def candidate = name
                if (
                    (!candidate || !(candidate ==~ /(?i).*(tab|dashboard|metro|reports|documents|accounts|contacts|transactions).*/ || candidate.startsWith('test_')))
                    && className
                ) {
                    candidate = className.tokenize('.').last()
                }
                if (candidate) {
                    skipped << candidate
                }
            }
        } catch (Exception ex) {
            echo "Could not parse infra-skipped test names from JUnit XML: ${ex.message}"
        }
    }

    def reportPath = env.PYTEST_JSON ?: 'test-results/report.json'
    if (fileExists(reportPath)) {
        try {
            def jsonText = readFile(reportPath)
            def testMatcher = (jsonText =~ /"nodeid"\s*:\s*"((?:\\.|[^"\\])*)".*?"outcome"\s*:\s*"skipped".*?"longrepr"\s*:\s*"((?:\\.|[^"\\])*)"/)
            while (testMatcher.find()) {
                def longrepr = (testMatcher.group(2) ?: '')
                    .replaceAll(/\\n/, '\n')
                    .replaceAll(/\\"/, '"')
                    .trim()
                if (!longrepr.contains('INFRA_SKIP:')) {
                    continue
                }
                def nodeId = (testMatcher.group(1) ?: '')
                    .replaceAll(/\\\//, '/')
                    .replaceAll(/\\"/, '"')
                    .trim()
                def displayName = extractDisplayNameFromNodeId(nodeId)
                if (displayName) {
                    skipped << displayName
                }
            }
        } catch (Exception ex) {
            echo "Could not parse infra-skipped test names from pytest JSON: ${ex.message}"
        }
    }

    return skipped.unique()
}

def getFinalOutcomesFromPytestJson() {
    def reportPath = env.PYTEST_JSON ?: 'test-results/report.json'
    def emptyStats = [total: 0, passed: 0, failed: 0, skipped: 0, collected: 0, not_run: 0]
    def result = [hasData: false, stats: emptyStats, failedTests: []]

    if (!fileExists(reportPath)) {
        echo "Pytest JSON report not found at ${reportPath}; trying JUnit fallback."
        return result
    }

    try {
        // Parse JSON report using regex so it works without Pipeline Utility Steps
        // (readJSON) and without Script Approval exceptions from JsonSlurper.
        def jsonText = readFile(reportPath)
        def finalOutcomeByNodeId = [:]

        // Capture nodeid/outcome pairs from each test object.
        // IMPORTANT: pytest-json-report also emits collectors with
        //   "nodeid": "tests/foo.py", "outcome": "passed"
        // meaning collection succeeded — NOT that the test passed.
        // Real executed tests always use nodeids containing "::".
        def testMatcher = (jsonText =~ /"nodeid"\s*:\s*"((?:\\.|[^"\\])*)".*?"outcome"\s*:\s*"((?:\\.|[^"\\])*)"/)
        while (testMatcher.find()) {
            def nodeId = (testMatcher.group(1) ?: '')
                .replaceAll(/\\\//, '/')
                .replaceAll(/\\"/, '"')
                .trim()
            def outcome = (testMatcher.group(2) ?: '').trim().toLowerCase()
            if (!nodeId || !outcome) {
                continue
            }
            // Ignore collector / file-level outcomes (no "::").
            if (!nodeId.contains('::')) {
                continue
            }

            // Retry attempts are intermediate; only final terminal outcome should count.
            if (outcome in ['rerun', 're-run']) {
                continue
            }
            if (outcome == 'error') {
                outcome = 'failed'
            }
            if (outcome in ['xfailed', 'xpassed']) {
                outcome = 'skipped'
            }
            if (!(outcome in ['passed', 'failed', 'skipped'])) {
                continue
            }

            // Keep last terminal state for each testcase id (important for retry flows).
            finalOutcomeByNodeId[nodeId] = outcome
        }

        def parseSummaryInt = { String key ->
            def m = (jsonText =~ /"summary"\s*:\s*\{(?s).*?"${java.util.regex.Pattern.quote(key)}"\s*:\s*(\d+)/)
            return m.find() ? (m.group(1) ?: '0') as int : 0
        }
        def collected = parseSummaryInt('collected')

        if (!finalOutcomeByNodeId.isEmpty()) {
            def passed = finalOutcomeByNodeId.findAll { _, status -> status == 'passed' }.size()
            def failed = finalOutcomeByNodeId.findAll { _, status -> status == 'failed' }.size()
            def skipped = finalOutcomeByNodeId.findAll { _, status -> status == 'skipped' }.size()
            def total = passed + failed + skipped
            // Do NOT invent passes from (collected - completed). Aborted/interrupted
            // runs leave unexecuted tests; counting them as passed is wrong.
            if (collected > 0 && total > collected) {
                // Cap only when plugin artifacts overcount beyond collected.
                echo "Pytest JSON overcount detected (completed=${total}, collected=${collected}); capping to executed outcomes without inventing passes."
                // Prefer keeping real failed/skipped; trim excess from passed first.
                def overflow = total - collected
                passed = Math.max(passed - overflow, 0)
                total = passed + failed + skipped
                if (total > collected) {
                    def stillOver = total - collected
                    skipped = Math.max(skipped - stillOver, 0)
                    total = passed + failed + skipped
                }
                if (total > collected) {
                    failed = Math.max(failed - (total - collected), 0)
                    total = passed + failed + skipped
                }
            }
            def notRun = collected > 0 ? Math.max(collected - total, 0) : 0
            def failedTests = finalOutcomeByNodeId
                .findAll { _, status -> status == 'failed' }
                .collect { nodeId, _ -> extractDisplayNameFromNodeId(nodeId as String) }
                .findAll { it }
                .unique()
            if (notRun > 0) {
                echo "Pytest JSON incomplete run -> completed:${total}, collected:${collected}, not_run:${notRun}, passed:${passed}, failed:${failed}, skipped:${skipped}"
            }
            return [
                hasData: true,
                stats: [total: total, passed: passed, failed: failed, skipped: skipped, collected: collected, not_run: notRun],
                failedTests: failedTests
            ]
        }

        // Fallback to summary counters if per-test entries are unavailable.
        // Use only explicit passed/failed/skipped — never treat "collected" as passed.
        def passed = parseSummaryInt('passed')
        def failed = parseSummaryInt('failed') + parseSummaryInt('error')
        def skipped = parseSummaryInt('skipped') + parseSummaryInt('xfailed') + parseSummaryInt('xpassed')
        def total = passed + failed + skipped
        if (collected > 0 && total > collected) {
            echo "Pytest JSON summary overcount detected (completed=${total}, collected=${collected}); capping without inventing passes."
            def overflow = total - collected
            passed = Math.max(passed - overflow, 0)
            total = passed + failed + skipped
        }
        def notRun = collected > 0 ? Math.max(collected - total, 0) : 0
        // hasData when we have either executed outcomes OR a collected count from an aborted run.
        if (total > 0 || collected > 0) {
            if (notRun > 0) {
                echo "Pytest JSON summary incomplete run -> completed:${total}, collected:${collected}, not_run:${notRun}, passed:${passed}, failed:${failed}, skipped:${skipped}"
            }
            return [
                hasData: true,
                stats: [total: total, passed: passed, failed: failed, skipped: skipped, collected: collected, not_run: notRun],
                failedTests: []
            ]
        }
    } catch (Exception ex) {
        echo "Could not parse pytest JSON report: ${ex.message}"
    }

    return result
}

def extractDisplayNameFromNodeId(String nodeId) {
    def value = (nodeId ?: '').trim()
    if (!value) {
        return value
    }

    if (value.contains('::')) {
        value = value.tokenize('::').last()
    } else if (value.contains('/')) {
        value = value.tokenize('/').last()
    } else if (value.contains('\\')) {
        value = value.tokenize('\\').last()
    }
    return value.replaceFirst(/\[.*\]$/, '')
}

def extractIntFromXmlAttribute(String xmlText, String attr) {
    if (!xmlText?.trim()) {
        return 0
    }
    def matcher = (xmlText =~ /${java.util.regex.Pattern.quote(attr)}\s*=\s*["'](\d+)["']/)
    if (matcher.find()) {
        return (matcher.group(1) ?: '0') as int
    }
    return 0
}

def logTestSummaryToConsole(String label = 'Test summary') {
    def stats = getTestStatistics()
    def skippedInfraTests = getSkippedInfraTestNames()
    def infraSkipLine = skippedInfraTests
        ? "Infra skipped tabs: ${skippedInfraTests.join(', ')}"
        : 'Infra skipped tabs: none'
    def collected = (stats.collected ?: 0) as int
    def notRun = (stats.not_run ?: 0) as int
    def collectedLine = collected > 0 ? "Collected: ${collected}" : null
    def notRunLine = notRun > 0 ? "Not run : ${notRun}" : null
    def abortNote = ((currentBuild?.result ?: currentBuild?.currentResult ?: '') == 'ABORTED')
        ? 'NOTE    : Build was ABORTED — counts reflect only tests that actually finished.'
        : null
    def extraLines = [collectedLine, notRunLine, abortNote].findAll { it }.join('\n')
    def extraBlock = extraLines ? "\n${extraLines}" : ''
    echo """
================ ${label} ================
Total  : ${stats.total}
Passed : ${stats.passed}
Failed : ${stats.failed}
Skipped: ${stats.skipped}${extraBlock}
${infraSkipLine}
==========================================
""".stripIndent()
}

def sendEmailNotification(String buildStatus, String defaultEmail, String additionalEmails) {
    def stats = getTestStatistics()
    def failedTests = getFailedTestNames()
    def actualStatus = currentBuild.result ?: buildStatus
    def notRun = (stats.not_run ?: 0) as int
    def collected = (stats.collected ?: 0) as int

    // Preserve Jenkins infra/build failures as source of truth.
    if (!(actualStatus in ['FAILURE', 'ABORTED'])) {
        if (stats.total == 0) {
            actualStatus = 'UNSTABLE'
        } else if (stats.failed > 0) {
            actualStatus = 'FAILURE'
        } else {
            actualStatus = 'SUCCESS'
        }
    }

    def recipients = collectRecipientEmails(
        defaultEmail,
        additionalEmails
    )
    if (recipients.isEmpty()) {
        echo 'No email recipients configured; skipping email notification.'
        return
    }

    def jobUrl = env.BUILD_URL ?: ''
    def excelRelPath = prepareExcelArtifactPath()
    def excelExists = excelRelPath ? fileExists(excelRelPath) : false
    def allureUrl = "${jobUrl}allure"
    def durationString = (currentBuild.durationString ?: 'N/A').replace(' and counting', '')
    def passRate = stats.total > 0 ? ((stats.passed * 100) / stats.total) as int : 0
    def cleanedFailedTests = failedTests.collect { name ->
        def prettyName = normalizeFailedTestNameToTab(name ?: '')
        prettyName
            .replaceAll(/(?i)exccedded/, 'exceeded')
            .replaceAll(/(?i)\btab\(s\)\b/, 'Tabs')
            .trim()
    }.findAll { it }
    def failedTestSummary
    if (actualStatus == 'ABORTED' && stats.total == 0) {
        failedTestSummary = '<span style="color:#334155;font-weight:600;">Build was aborted before any tests completed. Passed count is 0 (not a successful run).</span>'
    } else if (actualStatus == 'ABORTED' && notRun > 0) {
        failedTestSummary = cleanedFailedTests
            ? cleanedFailedTests.collect { item ->
                "<div style=\"margin:0 0 6px;padding:7px 10px;background:#fff7ed;border:1px solid #fed7aa;border-radius:8px;color:#9a3412;\">${item}</div>"
            }.join('') + "<div style=\"margin-top:8px;color:#334155;font-weight:600;\">Build aborted — ${notRun} of ${collected} collected tests did not run.</div>"
            : "<span style=\"color:#334155;font-weight:600;\">Build aborted — ${notRun} of ${collected} collected tests did not run. Counts above are only for finished tests.</span>"
    } else {
        failedTestSummary = cleanedFailedTests
            ? cleanedFailedTests.collect { item ->
                "<div style=\"margin:0 0 6px;padding:7px 10px;background:#fff7ed;border:1px solid #fed7aa;border-radius:8px;color:#9a3412;\">${item}</div>"
            }.join('')
            : '<span style="color:#065f46;font-weight:600;">No failed tests or tab timeouts were detected in this run.</span>'
    }

    def notRunRow = (notRun > 0 || actualStatus == 'ABORTED') ? """
                <tr>
                  <td style="padding:10px 12px;background:linear-gradient(180deg,#dbeafe 0%,#bfdbfe 100%);border-bottom:1px solid #bfdbfe;"><strong>Not Run</strong></td>
                  <td style="padding:10px 12px;border-bottom:1px solid #dbe3f3;font-weight:600;color:#334155;">${notRun}${collected > 0 ? " / ${collected} collected" : ''}</td>
                </tr>""" : ''

    def statusCfg = [
        SUCCESS : [bg: '#ecfdf5', border: '#10b981', text: '#065f46', pillBg: '#dcfce7'],
        FAILURE : [bg: '#fef2f2', border: '#ef4444', text: '#991b1b', pillBg: '#fee2e2'],
        ABORTED : [bg: '#f8fafc', border: '#64748b', text: '#334155', pillBg: '#e2e8f0'],
        UNSTABLE: [bg: '#fffbeb', border: '#f59e0b', text: '#92400e', pillBg: '#fef3c7']
    ]
    def subject = "Dakota Marketplace Performance | ${new Date().format('MMMM d, yyyy')}"
    if (actualStatus == 'ABORTED') {
        subject = "Dakota Marketplace Performance | ABORTED | ${new Date().format('MMMM d, yyyy')}"
    }

    def body = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Dakota Performance Report</title>
</head>
<body style="margin:0;padding:0;background:linear-gradient(140deg,#e0ecff 0%,#efe7ff 45%,#fff6e5 100%);font-family:'Segoe UI',Roboto,Arial,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0">
    <tr>
      <td align="center" style="padding:24px;">
        <table width="760" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:16px;overflow:hidden;border:1px solid #dbe3ee;box-shadow:0 14px 32px rgba(30,64,175,0.14);">
          <tr>
            <td style="padding:26px 30px;background:linear-gradient(135deg,#0f172a 0%,#1e40af 52%,#7c3aed 100%);color:#ffffff;">
              <h2 style="margin:0;font-size:30px;letter-spacing:0.2px;">Dakota Marketplace Performance</h2>
              <div style="margin-top:8px;font-size:14px;opacity:0.9;">Status: <strong>${actualStatus}</strong></div>
            </td>
          </tr>

          <tr>
            <td style="padding:24px 30px 10px;">
              <h3 style="margin:0 0 12px;color:#0f172a;font-size:17px;">Build Details</h3>
              <table width="100%" cellpadding="8" cellspacing="8" style="font-size:13px;margin-bottom:12px;">
                <tr align="center">
                  <td style="background:linear-gradient(180deg,#ccfbf1 0%,#99f6e4 100%);color:#134e4a;border-radius:12px;box-shadow:0 6px 14px rgba(20,184,166,0.22);"><div style="font-size:11px;letter-spacing:0.4px;">TOTAL</div><div style="font-size:24px;font-weight:800;">${stats.total}</div></td>
                  <td style="background:linear-gradient(180deg,#dcfce7 0%,#86efac 100%);color:#14532d;border-radius:12px;box-shadow:0 6px 14px rgba(34,197,94,0.25);"><div style="font-size:11px;letter-spacing:0.4px;">PASSED</div><div style="font-size:24px;font-weight:800;">${stats.passed}</div></td>
                  <td style="background:linear-gradient(180deg,#fee2e2 0%,#fca5a5 100%);color:#7f1d1d;border-radius:12px;box-shadow:0 6px 14px rgba(239,68,68,0.22);"><div style="font-size:11px;letter-spacing:0.4px;">FAILED</div><div style="font-size:24px;font-weight:800;">${stats.failed}</div></td>
                  <td style="background:linear-gradient(180deg,#ede9fe 0%,#c4b5fd 100%);color:#4c1d95;border-radius:12px;box-shadow:0 6px 14px rgba(124,58,237,0.22);"><div style="font-size:11px;letter-spacing:0.4px;">SKIPPED</div><div style="font-size:24px;font-weight:800;">${stats.skipped}</div></td>
                </tr>
              </table>
              <table width="100%" cellpadding="0" cellspacing="0" style="font-size:14px;color:#1e293b;border:1px solid #bfdbfe;border-radius:12px;overflow:hidden;background:linear-gradient(180deg,#f8fbff 0%,#ffffff 100%);table-layout:fixed;">
                <tr>
                  <td width="32%" style="padding:10px 12px;background:linear-gradient(180deg,#dbeafe 0%,#bfdbfe 100%);border-bottom:1px solid #bfdbfe;"><strong>Duration</strong></td>
                  <td style="padding:10px 12px;border-bottom:1px solid #dbe3f3;font-weight:600;color:#1e3a8a;">${durationString}</td>
                </tr>
                <tr>
                  <td style="padding:10px 12px;background:linear-gradient(180deg,#dbeafe 0%,#bfdbfe 100%);border-bottom:1px solid #bfdbfe;"><strong>Passed Percentage</strong></td>
                  <td style="padding:10px 12px;border-bottom:1px solid #dbe3f3;color:#0f766e;font-weight:700;">${passRate}%</td>
                </tr>${notRunRow}
                <tr>
                  <td style="padding:10px 12px;background:linear-gradient(180deg,#dbeafe 0%,#bfdbfe 100%);"><strong>Failed Tests / Affected Tabs</strong></td>
                  <td style="padding:10px 12px;line-height:1.45;">${failedTestSummary}</td>
                </tr>
              </table>
            </td>
          </tr>

          <tr>
            <td style="padding:8px 30px 24px;">
              <h3 style="margin:0 0 12px;color:#0f172a;font-size:17px;">Report Access</h3>
              <table width="100%" cellpadding="0" cellspacing="0" style="font-size:14px;color:#1e293b;border:1px solid #c4b5fd;border-radius:10px;overflow:hidden;background:linear-gradient(180deg,#faf5ff 0%,#f3f0ff 100%);">
                <tr>
                  <td width="32%" style="padding:10px 12px;background:linear-gradient(180deg,#ede9fe 0%,#ddd6fe 100%);"><strong>Allure Report</strong></td>
                  <td style="padding:10px 12px;">
                    <a style="color:#6d28d9;text-decoration:underline;font-weight:700;" href="${allureUrl}">Open Allure Report</a>
                  </td>
                </tr>
              </table>
              <p style="margin:12px 0 0;color:#64748b;font-size:12px;">Please see the attached Excel performance sheet for detailed run metrics.</p>
            </td>
          </tr>

          <tr>
            <td style="padding:13px 30px;background:#0f172a;color:#cbd5e1;font-size:12px;">
              Jenkins CI/CD • Dakota Marketplace Test Framework
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>
"""

    def baseArgs = [
        subject: subject,
        body: body,
        mimeType: 'text/html',
        attachLog: false,
        compressLog: false
    ]
    if (excelExists) {
        baseArgs.attachmentsPattern = excelRelPath
    }

    def recipientList = recipients.join(', ')
    echo "Sending email to: ${recipientList}"

    try {
        // Primary path: single send with comma-separated recipients (same as prior working pipeline).
        emailext(baseArgs + [to: recipientList])
    } catch (Exception ex) {
        echo "Combined email send failed: ${ex.getMessage()}"
        echo "Falling back to one-by-one recipient delivery."
        recipients.each { recipient ->
            try {
                echo "Sending fallback email to: ${recipient}"
                emailext(baseArgs + [to: recipient])
            } catch (Exception innerEx) {
                echo "Failed to send email to ${recipient}: ${innerEx.getMessage()}"
            }
        }
    }
}

def normalizeFailedTestNameToTab(String testName) {
    def value = (testName ?: '').trim()
    if (!value) {
        return value
    }

    // Handle JUnit forms like package.module::test_name or tests.test_file.py::test_name.
    value = value
        .replaceFirst(/^.*::/, '')
        .replaceFirst(/^.*[\\\/]/, '')
        .replaceFirst(/\.py$/, '')
    if (value.contains('.') && value.tokenize('.').last().startsWith('test_')) {
        value = value.tokenize('.').last()
    }

    // Convert pytest case names like test_foo_bar_tab_render_performance to tab labels.
    value = value
        .replaceFirst(/^test_/, '')
        .replaceFirst(/_tab_render_performance$/, '')
        .replaceFirst(/_tab_performance$/, '')
        .replaceFirst(/_render_performance$/, '')
        .replaceFirst(/_performance$/, '')
        .replaceFirst(/_tab$/, '')

    // Remove parameterized-test suffix if present (e.g., name[param]).
    value = value.replaceFirst(/\[.*\]$/, '')

    // Preserve common acronyms while keeping other words title-cased.
    def acronyms = ['mru', 'v2'] as Set
    def words = value
        .split(/_+/)
        .findAll { it?.trim() }
        .collect { token ->
            def lower = token.toLowerCase()
            if (acronyms.contains(lower) || lower ==~ /\d+[a-z]+/) {
                return lower.toUpperCase()
            }
            return lower.capitalize()
        }

    if (!words) {
        return testName
    }

    def label = words.join(' ')
    return label.toLowerCase().endsWith(' tab') ? label : "${label} Tab"
}

def prepareExcelArtifactPath() {
    def baseDir = 'salesforce_tab_performance'
    def defaultExcel = "${baseDir}/performance_results.xlsx"
    def rootExcel = 'performance_results.xlsx'
    def finalExcel = "${baseDir}/Dakota Marketplace Performance.xlsx"

    def sourceExcel = null
    if (fileExists(defaultExcel)) {
        sourceExcel = defaultExcel
    } else if (fileExists(rootExcel)) {
        sourceExcel = rootExcel
    } else if (fileExists(finalExcel)) {
        sourceExcel = finalExcel
    } else {
        echo "Excel artifact not found at expected paths: ${defaultExcel}, ${rootExcel}, or ${finalExcel}"
        return null
    }

    if (sourceExcel != finalExcel) {
        def sourceExcelWin = sourceExcel.replace('/', '\\')
        def finalExcelWin = finalExcel.replace('/', '\\')
        runShell(
            """
                if [ -f "${sourceExcel}" ]; then cp "${sourceExcel}" "${finalExcel}"; fi
            """,
            """
                if exist "${sourceExcelWin}" (
                    copy /Y "${sourceExcelWin}" "${finalExcelWin}" >nul 2>nul
                )
                exit /b 0
            """
        )
    }
    if (fileExists(finalExcel)) {
        return finalExcel
    }
    return sourceExcel
}

def collectRecipientEmails(String defaultEmail, String additionalEmails) {
    def recipients = []
    def seen = [] as Set

    // Pass through any domain and keep parsing tolerant for separators/whitespace.
    [defaultEmail, additionalEmails].findAll { it?.trim() }.each { source ->
        source
            .split(/[,\s;]+/)
            .collect { it.trim() }
            .findAll { it }
            .each { mail ->
                def normalized = mail.toLowerCase()
                if (!seen.contains(normalized)) {
                    seen.add(normalized)
                    recipients.add(mail)
                }
            }
    }

    echo "Email recipients resolved: ${recipients.join(', ')}"
    return recipients
}

