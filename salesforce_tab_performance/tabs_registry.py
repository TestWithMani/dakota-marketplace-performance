"""Central registry for Salesforce tab metadata used by tests."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Mapping

from . import config

EndCondition = Literal["visible", "clickable"]


@dataclass(frozen=True)
class TabDefinition:
    display_name: str
    url: str
    end_element_xpath: str | None = None
    end_condition: EndCondition | None = None


TAB_REGISTRY: Mapping[str, TabDefinition] = {
    "accounts": TabDefinition(
        display_name="Accounts",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/account/Account/Default",
    ),
    "all_documents": TabDefinition(
        display_name="All Documents",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/all-documents",
    ),
    "benchmarking": TabDefinition(
        display_name="Benchmarking",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/benchmarking-tab",
    ),
    "conference": TabDefinition(
        display_name="Conference",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/conference/Conference__c/Default",
    ),
    "conference_dashboard": TabDefinition(
        display_name="Conference Dashboard",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/conference-dashboard",
    ),
    "conference_speakers": TabDefinition(
        display_name="Conference Speakers",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/conference-speakers",
    ),
    "consultant_reviews_dashboard": TabDefinition(
        display_name="Consultant Reviews Dashboard",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/consultant-reviews-dashboard",
    ),
    "contact": TabDefinition(
        display_name="Contact",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/contact/Contact/Default",
    ),
    "custom_portfolio_dashboard": TabDefinition(
        display_name="Custom Portfolio Dashboard",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/custom-portfolio-dashboard",
        end_element_xpath=config.CUSTOM_DASHBOARD_END_ELEMENT_XPATH,
        end_condition="clickable",
    ),
    "dakota_benchmarks": TabDefinition(
        display_name="Dakota Benchmarks",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/dakota-benchmarks",
    ),
    "dakota_city_guides": TabDefinition(
        display_name="Dakota City Guides",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/dakota-city-guides",
    ),
    "dakota_joe_reports": TabDefinition(
        display_name="Dakota Joe Reports",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/dakota-joe-reports",
        end_element_xpath=config.REPORTS_END_ELEMENT_XPATH,
        end_condition="clickable",
    ),
    "dakota_videos": TabDefinition(
        display_name="Dakota Videos",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/dakota-videos",
    ),
    "evergreen_fund_performance": TabDefinition(
        display_name="Evergreen Fund Performance",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/evergreen-fund-performance",
    ),
    "fee_schedules_dashboard": TabDefinition(
        display_name="Fee Schedules Dashboard",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/fee-schedules-dashboard",
    ),
    "family_office_investments": TabDefinition(
        display_name="Family Office Investments",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/family-office-investments",
    ),
    "forecasted_transactions": TabDefinition(
        display_name="Forecasted Transactions",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/forecasted-transactions",
    ),
    "fund_family_memos": TabDefinition(
        display_name="Fund Family Memos",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/fund-family-memos",
    ),
    "fund_launches": TabDefinition(
        display_name="Fund Launches",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/fund-launches",
    ),
    "fundraising_news": TabDefinition(
        display_name="Fundraising News",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/fundraising-news",
    ),
    "hedge_fund_performance": TabDefinition(
        display_name="Hedge Fund Performance",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/hedge-fund-performance",
    ),
    "hedge_fund_performance_benchmarking": TabDefinition(
        display_name="Hedge Fund Performance Benchmarking",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/hedge-fund-performance-benchmarking",
    ),
    "investment_allocator": TabDefinition(
        display_name="Investment Allocator Accounts",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/investment-allocator-list",
    ),
    "investment_allocator_contacts": TabDefinition(
        display_name="Investment Allocator Contacts",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/investment-allocator-contacts",
    ),
    "investment_allocator_metro_areas": TabDefinition(
        display_name="Investment Allocator Metro Areas",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/investment-allocator-metro-areas",
        end_element_xpath=config.METRO_AREA_END_ELEMENT_XPATH,
        end_condition="clickable",
    ),
    "investment_firm": TabDefinition(
        display_name="Investment Firm Accounts",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/investment-firm-list",
    ),
    "investment_firm_contacts": TabDefinition(
        display_name="Investment Firm Contacts",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/investment-firm-contacts",
    ),
    "investment_firm_metro_area": TabDefinition(
        display_name="Investment Firm Metro Area",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/investment-firm-metro-area",
        end_element_xpath=config.METRO_AREA_END_ELEMENT_XPATH,
        end_condition="clickable",
    ),
    "manager_presentation_dashboard": TabDefinition(
        display_name="Manager Presentation Dashboard",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/manager-presentation-dashboard",
    ),
    "marketplace_home": TabDefinition(
        display_name="Marketplace Home",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/",
        end_element_xpath="(//button[@title='Click To Follow'])[1]",
        end_condition="clickable",
    ),
    "marketplace_searches": TabDefinition(
        display_name="Marketplace Searches",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/marketplace-searches/Marketplace_Searches__c/Default",
    ),
    "metro_area": TabDefinition(
        display_name="Metro Area",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/metro-area/Metro_Area__c/Default",
        end_element_xpath=config.METRO_AREA_END_ELEMENT_XPATH,
        end_condition="clickable",
    ),
    "my_account": TabDefinition(
        display_name="My Account",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/my-account/My_Account__c/Default",
    ),
    "pension_documents": TabDefinition(
        display_name="Pension Documents",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/pension-documents",
    ),
    "portfolio_companies": TabDefinition(
        display_name="Portfolio Companies",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/portfolio-companies",
    ),
    "portfolio_companies_metro_area": TabDefinition(
        display_name="Portfolio Companies Metro Area",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/portfolio-companies-metro-area",
        end_element_xpath=config.METRO_AREA_END_ELEMENT_XPATH,
        end_condition="clickable",
    ),
    "portfolio_companies_metro_areas": TabDefinition(
        display_name="Portfolio Companies Metro Areas",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/portfolio-companies-metro-areas",
        end_element_xpath=config.METRO_AREA_END_ELEMENT_XPATH,
        end_condition="clickable",
    ),
    "private_companies_transactions": TabDefinition(
        display_name="Private Companies Transactions",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/private-companies-transactions",
    ),
    "private_fund_search": TabDefinition(
        display_name="Private Fund Search",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/private-fund-search-tab",
    ),
    "public_company_search": TabDefinition(
        display_name="Public Company Search",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/public-company-search-tab",
    ),
    "public_investments_search": TabDefinition(
        display_name="Public Investments Search",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/public-investments-search-tab",
    ),
    "public_plan_minute": TabDefinition(
        display_name="Public Plan Minute",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/public-plan-minute/Public_Plan_Minute__c/Default",
    ),
    "recent_transactions": TabDefinition(
        display_name="Recent Transactions",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/recent-transactions",
    ),
    "research_report": TabDefinition(
        display_name="Research Report",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/research-report",
    ),
    "reports_everything": TabDefinition(
        display_name="Reports All",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/report/Report/Recent/Report/?queryScope=everything",
        end_element_xpath=config.REPORTS_END_ELEMENT_XPATH,
        end_condition="clickable",
    ),
    "reports_mru": TabDefinition(
        display_name="Reports Recent",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/report/Report/Recent/Report/?queryScope=mru",
        end_element_xpath=config.REPORTS_END_ELEMENT_XPATH,
        end_condition="clickable",
    ),
    "reports_user_folders": TabDefinition(
        display_name="Reports All Folders",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/report/Report/Recent/Report/?queryScope=userFolders",
        end_element_xpath=config.REPORTS_END_ELEMENT_XPATH,
        end_condition="clickable",
    ),
    "searches_dashboard": TabDefinition(
        display_name="Searches Dashboard",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/searches-dashboard",
        end_element_xpath=config.CUSTOM_DASHBOARD_END_ELEMENT_XPATH,
        end_condition="clickable",
    ),
    "university_alumni": TabDefinition(
        display_name="University Alumni",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/university-alumni/University_Alumni__c/Default",
    ),
    "wealth_channel_metro_areas": TabDefinition(
        display_name="Wealth Channel Metro Areas",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/wealth-channel-metro-areas",
        end_element_xpath=config.METRO_AREA_END_ELEMENT_XPATH,
        end_condition="clickable",
    ),
    "13f_filings": TabDefinition(
        display_name="13F Filings",
        url="https://dakotanetworks.my.site.com/dakotaMarketplace/s/13f-filings",
    ),
}


def get_tab_definition(tab_key: str) -> TabDefinition:
    """Return tab metadata for a known key."""
    try:
        return TAB_REGISTRY[tab_key]
    except KeyError as exc:
        valid_keys = ", ".join(sorted(TAB_REGISTRY))
        raise ValueError(f"Unknown tab_key '{tab_key}'. Valid keys: {valid_keys}") from exc
