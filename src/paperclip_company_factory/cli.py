from __future__ import annotations

import argparse
import json
from .config import FactoryConfig
from .planner import build_company_plan
from .paperclip_api import healthcheck, create_company


def cmd_validate_env(_: argparse.Namespace) -> int:
    cfg = FactoryConfig()
    print(json.dumps({
        'missing': cfg.missing_required(),
        'config': cfg.__dict__,
    }, indent=2, ensure_ascii=False))
    return 0


def cmd_health(_: argparse.Namespace) -> int:
    cfg = FactoryConfig()
    print(json.dumps(healthcheck(cfg), indent=2, ensure_ascii=False))
    return 0


def cmd_plan(args: argparse.Namespace) -> int:
    cfg = FactoryConfig()
    plan = build_company_plan(
        company_name=args.company_name,
        template_name=args.template or cfg.default_template,
        prefix=args.prefix,
        visibility=args.visibility or cfg.default_visibility,
        deploy_target=args.deploy_target or cfg.default_deploy_target,
        provider_profile=args.provider_profile or cfg.default_provider_profile,
    )
    print(json.dumps(plan.to_dict(), indent=2, ensure_ascii=False))
    return 0


def cmd_create(args: argparse.Namespace) -> int:
    cfg = FactoryConfig()
    plan = build_company_plan(
        company_name=args.company_name,
        template_name=args.template or cfg.default_template,
        prefix=args.prefix,
        visibility=args.visibility or cfg.default_visibility,
        deploy_target=args.deploy_target or cfg.default_deploy_target,
        provider_profile=args.provider_profile or cfg.default_provider_profile,
    )
    print(json.dumps(create_company(cfg, plan, dry_run=args.dry_run), indent=2, ensure_ascii=False))
    return 0


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog='pcf', description='Paperclip Company Factory CLI')
    sub = p.add_subparsers(dest='command', required=True)

    sub.add_parser('validate-env')
    sub.add_parser('health')

    plan = sub.add_parser('plan-company')
    plan.add_argument('company_name')
    plan.add_argument('--template')
    plan.add_argument('--prefix')
    plan.add_argument('--visibility')
    plan.add_argument('--deploy-target')
    plan.add_argument('--provider-profile')

    create = sub.add_parser('create-company')
    create.add_argument('company_name')
    create.add_argument('--template')
    create.add_argument('--prefix')
    create.add_argument('--visibility')
    create.add_argument('--deploy-target')
    create.add_argument('--provider-profile')
    create.add_argument('--dry-run', action='store_true')

    return p


def main() -> int:
    p = parser()
    args = p.parse_args()
    if args.command == 'validate-env':
        return cmd_validate_env(args)
    if args.command == 'health':
        return cmd_health(args)
    if args.command == 'plan-company':
        return cmd_plan(args)
    if args.command == 'create-company':
        return cmd_create(args)
    p.error(f'unknown command: {args.command}')
    return 2


if __name__ == '__main__':
    raise SystemExit(main())
