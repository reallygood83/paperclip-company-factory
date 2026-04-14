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
    prompt = ask('What kind of company do you want to create?', 'Create a public AI content studio company for newsletters')
    inferred = interpret_prompt(prompt)
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
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
