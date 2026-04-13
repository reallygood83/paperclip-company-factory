from paperclip_company_factory.config import FactoryConfig
from paperclip_company_factory.paperclip_api import bootstrap_company
from paperclip_company_factory.planner import build_company_plan


def test_bootstrap_company_dry_run_contains_company_agents_and_issues():
    config = FactoryConfig()
    plan = build_company_plan('Atlas Research', 'research-company', template_root='.')
    result = bootstrap_company(config, plan, dry_run=True)
    assert result['company']['dry_run'] is True
    assert len(result['agents']) == 4
    assert len(result['issues']) >= 1
