from __future__ import annotations


def _company_line(company: dict) -> str:
    if company.get('dry_run'):
        payload = company.get('payload', {})
        return f"Company (dry-run): {payload.get('name', 'unknown')}"
    return f"Company created: {company.get('name', 'unknown')} ({company.get('id', '-')})"


def _agent_lines(agents: list[dict]) -> list[str]:
    lines: list[str] = []
    if not agents:
        return ["Agents: none"]
    if agents[0].get('dry_run'):
        lines.append(f"Agents planned: {len(agents)}")
        for agent in agents:
            payload = agent.get('payload', {})
            lines.append(f"- {payload.get('name', 'unknown')} | {payload.get('adapterType', '-')}")
        return lines
    lines.append(f"Agents created: {len(agents)}")
    for agent in agents:
        lines.append(f"- {agent.get('name', 'unknown')} ({agent.get('id', '-')})")
    return lines


def _issue_lines(issues: list[dict]) -> list[str]:
    lines: list[str] = []
    if not issues:
        return ["Starter issues: none"]
    if issues[0].get('dry_run'):
        lines.append(f"Starter issues planned: {len(issues)}")
        for issue in issues:
            payload = issue.get('payload', {})
            lines.append(f"- {payload.get('title', 'unknown')} | {payload.get('priority', '-')}")
        return lines
    lines.append(f"Starter issues created: {len(issues)}")
    for issue in issues:
        lines.append(f"- {issue.get('identifier', issue.get('id', '-'))}: {issue.get('title', 'unknown')}")
    return lines


def _next_commands(company_name: str, template_id: str, dry_run: bool) -> list[str]:
    if dry_run:
        return [
            f'PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-company "{company_name}" --template {template_id}',
            'python3 scripts/first_run_wizard.py',
            'Ask Hermes: "리서치 회사 하나 만들어줘"',
        ]
    return [
        'Open dashboard: http://127.0.0.1:3100',
        'Run: ./scripts/status.sh',
        'Ask Hermes: "이 회사에 marketer 추가해줘"',
        'Ask Hermes: "이 회사 런치 준비해줘"',
    ]


def format_bootstrap_result(payload: dict) -> str:
    plan = payload.get('plan') or payload.get('bootstrap', {}).get('plan', {})
    company = payload.get('company') or payload.get('bootstrap', {}).get('company', {})
    agents = payload.get('agents') or payload.get('bootstrap', {}).get('agents', [])
    issues = payload.get('issues') or payload.get('bootstrap', {}).get('issues', [])
    interpreted = payload.get('interpreted_request')

    lines: list[str] = []
    lines.append('Paperclip Company Factory Report')
    lines.append('===')
    if interpreted:
        lines.append(f"Prompt: {interpreted.get('prompt', '')}")
        lines.append(f"Template: {interpreted.get('template', '-')}")
        lines.append(f"Visibility: {interpreted.get('visibility', '-')}")
        lines.append(f"Deploy target: {interpreted.get('deploy_target', '-')}")
        lines.append('===')

    company_name = plan.get('company_name', '-')
    template_id = plan.get('template_id', '-')
    lines.append(f"Plan company: {company_name}")
    lines.append(f"Mission: {plan.get('mission', '-')}")
    lines.append(f"Template id: {template_id}")
    lines.append(f"Provider profile: {plan.get('provider_profile', '-')}")
    lines.append('===')
    lines.append(_company_line(company))
    lines.extend(_agent_lines(agents))
    lines.extend(_issue_lines(issues))
    if not company.get('dry_run') and company.get('id'):
        lines.append('Dashboard URL: http://127.0.0.1:3100')
    lines.append('===')
    lines.append('Next actions')
    for command in _next_commands(company_name, template_id, company.get('dry_run', False)):
        lines.append(f'- {command}')
    return '\n'.join(lines)
