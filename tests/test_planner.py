from paperclip_company_factory.planner import build_company_plan


def test_build_company_plan_uses_template_data():
    plan = build_company_plan('Atlas Research', 'research-company', template_root='.')
    assert plan.company_prefix == 'AR'
    assert any(role['role'] == 'ceo' for role in plan.agent_roles)
    assert 'Confirm provider credentials' in plan.launch_checklist
