#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'src'
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from paperclip_company_factory.bridge import interpret_prompt
from paperclip_company_factory.config import FactoryConfig
from paperclip_company_factory.formatter import format_bootstrap_result
from paperclip_company_factory.planner import build_company_plan
from paperclip_company_factory.paperclip_api import bootstrap_company, healthcheck


def ask(question: str, default: str = '') -> str:
    suffix = f' [{default}]' if default else ''
    value = input(f'{question}{suffix}: ').strip()
    return value or default


def ask_yes_no(question: str, default: bool = True) -> bool:
    label = 'Y/n' if default else 'y/N'
    value = input(f'{question} [{label}]: ').strip().lower()
    if not value:
        return default
    return value in {'y', 'yes'}


def suggested_prompt(mode: str) -> str:
    if mode == 'advanced':
        return 'Create a public AI SaaS company for internal knowledge search deployed to docker compose'
    return 'Create a public AI content studio company for newsletters'


def main() -> int:
    cfg = FactoryConfig()
    print('Paperclip Company Factory Wizard')
    print('===')
    health = healthcheck(cfg)
    if not health.get('ok'):
        print('Paperclip is not reachable at the configured URL.')
        print('Run ./scripts/one_click_install.sh first, then come back.')
        return 1

    print('Paperclip is reachable.')
    print('===')
    mode = ask('Choose mode: beginner or advanced', 'beginner').strip().lower()
    prompt = ask('What kind of company do you want to create?', suggested_prompt(mode))
    inferred = interpret_prompt(prompt)
    print(f"Suggested template: {inferred['template']}")
    print(f"Suggested visibility: {inferred['visibility']}")
    print(f"Suggested deploy target: {inferred['deploy_target']}")
    company_name = ask('Suggested company name', inferred['company_name'])
    provider_profile = ask('Provider profile', cfg.default_provider_profile)
    dry_run = ask_yes_no('Start with a dry-run?', True)

    plan = build_company_plan(
        company_name=company_name,
        template_name=inferred['template'],
        visibility=inferred['visibility'],
        deploy_target=inferred['deploy_target'],
        provider_profile=provider_profile,
    )
    payload = {
        'interpreted_request': inferred,
        'bootstrap': bootstrap_company(cfg, plan, dry_run=dry_run),
    }
    print()
    print(format_bootstrap_result(payload))
    print()

    if dry_run and ask_yes_no('Create the company for real now?', False):
        payload = {
            'interpreted_request': inferred,
            'bootstrap': bootstrap_company(cfg, plan, dry_run=False),
        }
        print()
        print(format_bootstrap_result(payload))
    print()
    print('Try next in Hermes:')
    print('- 리서치 회사 하나 만들어줘')
    print('- 이 회사에 marketer 추가해줘')
    print('- 이 회사 런치 준비해줘')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
