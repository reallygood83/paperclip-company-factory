from __future__ import annotations

import json
import urllib.request
from dataclasses import asdict
from .config import FactoryConfig
from .planner import CompanyPlan
from .provider_profiles import resolve_provider_profile


def _request(url: str, method: str = 'GET', payload: dict | None = None, api_key: str = '') -> dict:
    headers = {'Content-Type': 'application/json'}
    if api_key:
        headers['Authorization'] = f'Bearer {api_key}'
        headers['X-API-Key'] = api_key
    data = None if payload is None else json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = resp.read().decode('utf-8')
        return json.loads(body) if body else {}


def _api_url(config: FactoryConfig, path: str) -> str:
    path = path if path.startswith('/') else '/' + path
    return f'{config.paperclip_base_url}{config.paperclip_api_prefix}{path}'


def healthcheck(config: FactoryConfig) -> dict:
    for candidate in (_api_url(config, '/companies'), f'{config.paperclip_base_url}/api/companies'):
        try:
            return {'ok': True, 'url': candidate, 'response': _request(candidate, api_key=config.paperclip_api_key)}
        except Exception:
            continue
    return {'ok': False, 'error': 'Paperclip API not reachable with known company endpoints'}


def create_company(config: FactoryConfig, plan: CompanyPlan, dry_run: bool = True) -> dict:
    payload = {
        'name': plan.company_name,
        'issuePrefix': plan.company_prefix,
        'description': plan.mission,
        'metadata': {
            'factoryTemplate': plan.template_id,
            'visibility': plan.visibility,
            'deployTarget': plan.deploy_target,
            'providerProfile': plan.provider_profile,
        },
    }
    endpoint = _api_url(config, '/companies')
    if dry_run:
        return {'dry_run': True, 'endpoint': endpoint, 'payload': payload}
    return _request(endpoint, method='POST', payload=payload, api_key=config.paperclip_api_key)


def create_agents(config: FactoryConfig, company_id: str, plan: CompanyPlan, dry_run: bool = True) -> list[dict]:
    profile = resolve_provider_profile(plan.provider_profile, config)
    endpoint = _api_url(config, f'/companies/{company_id}/agents')
    results: list[dict] = []
    ceo_id: str | None = None
    for role in plan.agent_roles:
        payload = {
            'name': role.get('title', role['role'].replace('-', ' ').title()),
            'role': 'ceo' if role['role'] == 'ceo' else 'general',
            'title': role.get('title'),
            'capabilities': role.get('objective'),
            'reportsTo': None if role['role'] == 'ceo' else ceo_id,
            'adapterType': profile['adapterType'],
            'adapterConfig': profile['adapterConfig'],
            'runtimeConfig': {
                'heartbeat': {
                    'enabled': True,
                    'wakeOnDemand': True,
                    'intervalSec': 300,
                    'maxConcurrentRuns': 1,
                }
            },
            'metadata': {
                'factoryRole': role['role'],
                'factoryTemplate': plan.template_id,
            },
        }
        if dry_run:
            results.append({'dry_run': True, 'endpoint': endpoint, 'payload': payload})
            if role['role'] == 'ceo':
                ceo_id = 'dry-run-ceo'
            continue
        created = _request(endpoint, method='POST', payload=payload, api_key=config.paperclip_api_key)
        results.append(created)
        if role['role'] == 'ceo':
            ceo_id = created['id']
    return results


def create_starter_issues(config: FactoryConfig, company_id: str, plan: CompanyPlan, dry_run: bool = True) -> list[dict]:
    endpoint = _api_url(config, f'/companies/{company_id}/issues')
    results: list[dict] = []
    for issue in plan.starter_issues:
        payload = {
            'title': issue['title'],
            'description': f"Factory-generated starter issue for template {plan.template_id}.",
            'priority': issue.get('priority', 'medium'),
        }
        if dry_run:
            results.append({'dry_run': True, 'endpoint': endpoint, 'payload': payload})
            continue
        results.append(_request(endpoint, method='POST', payload=payload, api_key=config.paperclip_api_key))
    return results


def bootstrap_company(config: FactoryConfig, plan: CompanyPlan, dry_run: bool = True) -> dict:
    company_result = create_company(config, plan, dry_run=dry_run)
    company_id = company_result.get('id', 'dry-run-company')
    agents_result = create_agents(config, company_id, plan, dry_run=dry_run)
    issues_result = create_starter_issues(config, company_id, plan, dry_run=dry_run)
    return {
        'plan': plan.to_dict(),
        'company': company_result,
        'agents': agents_result,
        'issues': issues_result,
    }
