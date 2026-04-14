from paperclip_company_factory.formatter import format_bootstrap_result


def test_format_bootstrap_result_dry_run_mentions_next_step():
    payload = {
        'interpreted_request': {
            'prompt': 'Create a research company',
            'template': 'research-company',
            'visibility': 'private',
            'deploy_target': 'local',
        },
        'bootstrap': {
            'plan': {
                'company_name': 'Atlas Research',
                'mission': 'Mission text',
                'template_id': 'research-company',
                'provider_profile': 'openai-codex',
            },
            'company': {'dry_run': True, 'payload': {'name': 'Atlas Research'}},
            'agents': [{'dry_run': True, 'payload': {'name': 'CEO', 'adapterType': 'hermes_local'}}],
            'issues': [{'dry_run': True, 'payload': {'title': 'Define ICP', 'priority': 'high'}}],
        },
    }
    text = format_bootstrap_result(payload)
    assert 'Paperclip Company Factory Report' in text
    assert 'Next actions' in text
    assert 'Ask Hermes:' in text
