from __future__ import annotations

import json
import urllib.request
import urllib.error
from dataclasses import asdict
from .config import FactoryConfig
from .planner import CompanyPlan


def _request(url: str, method: str = 'GET', payload: dict | None = None, api_key: str = '') -> dict:
    headers = {'Content-Type': 'application/json'}
    if api_key:
        headers['Authorization'] = f'Bearer {api_key}'
        headers['X-API-Key'] = api_key
    data = None if payload is None else json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=10) as resp:
        body = resp.read().decode('utf-8')
        return json.loads(body) if body else {}


def healthcheck(config: FactoryConfig) -> dict:
    for candidate in (f'{config.paperclip_base_url}/api/companies', f'{config.paperclip_base_url}{config.paperclip_api_prefix}/companies'):
        try:
            return {'ok': True, 'url': candidate, 'response': _request(candidate, api_key=config.paperclip_api_key)}
        except Exception:
            continue
    return {'ok': False, 'error': 'Paperclip API not reachable with known company endpoints'}


def create_company(config: FactoryConfig, plan: CompanyPlan, dry_run: bool = True) -> dict:
    payload = {
        'name': plan.company_name,
        'prefix': plan.company_prefix,
        'description': plan.mission,
        'metadata': {
            'factoryTemplate': plan.template_id,
            'visibility': plan.visibility,
            'deployTarget': plan.deploy_target,
            'providerProfile': plan.provider_profile,
        },
    }
    if dry_run:
        return {'dry_run': True, 'endpoint': f'{config.paperclip_base_url}{config.paperclip_api_prefix}/companies', 'payload': payload}
    return _request(f'{config.paperclip_base_url}{config.paperclip_api_prefix}/companies', method='POST', payload=payload, api_key=config.paperclip_api_key)
