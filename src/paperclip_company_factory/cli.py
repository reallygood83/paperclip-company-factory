from __future__ import annotations

import argparse
import json
from .bridge import interpret_prompt
from .config import FactoryConfig
from .formatter import format_bootstrap_result
from .planner import build_company_plan
from .paperclip_api import healthcheck, create_company, bootstrap_company


def _emit(data: dict, output_format: str = 'json') -> None:
    if output_format == 'text':
        print(format_bootstrap_result(data))
    else:
        print(json.dumps(data, indent=2, ensure_ascii=False))


def _build_plan_from_args(args: argparse.Namespace, cfg: FactoryConfig):
    return build_company_plan(
        company_name=args.company_name,
        template_name=args.template or cfg.default_template,
        prefix=getattr(args, 'prefix', None),
        visibility=getattr(args, 'visibility', None) or cfg.default_visibility,
        deploy_target=getattr(args, 'deploy_target', None) or cfg.default_deploy_target,
        provider_profile=getattr(args, 'provider_profile', None) or cfg.default_provider_profile,
    )


def cmd_validate_env(_: argparse.Namespace) -> int:
    cfg = FactoryConfig()
    print(json.dumps({'missing': cfg.missing_required(), 'config': cfg.__dict__}, indent=2, ensure_ascii=False))
    return 0


def cmd_health(_: argparse.Namespace) -> int:
    cfg = FactoryConfig()
    print(json.dumps(healthcheck(cfg), indent=2, ensure_ascii=False))
    return 0


def cmd_plan(args: argparse.Namespace) -> int:
    cfg = FactoryConfig()
    print(json.dumps(_build_plan_from_args(args, cfg).to_dict(), indent=2, ensure_ascii=False))
    return 0


def cmd_create(args: argparse.Namespace) -> int:
    cfg = FactoryConfig()
    plan = _build_plan_from_args(args, cfg)
    print(json.dumps(create_company(cfg, plan, dry_run=args.dry_run), indent=2, ensure_ascii=False))
    return 0


def cmd_bootstrap(args: argparse.Namespace) -> int:
    cfg = FactoryConfig()
    plan = _build_plan_from_args(args, cfg)
    _emit(bootstrap_company(cfg, plan, dry_run=args.dry_run), args.format)
    return 0


def cmd_interpret(args: argparse.Namespace) -> int:
    print(json.dumps(interpret_prompt(args.prompt), indent=2, ensure_ascii=False))
    return 0


def cmd_bootstrap_from_prompt(args: argparse.Namespace) -> int:
    cfg = FactoryConfig()
    inferred = interpret_prompt(args.prompt)
    plan = build_company_plan(
        company_name=args.company_name or inferred['company_name'],
        template_name=inferred['template'],
        prefix=args.prefix,
        visibility=inferred['visibility'],
        deploy_target=inferred['deploy_target'],
        provider_profile=args.provider_profile or cfg.default_provider_profile,
    )
    payload = {
        'interpreted_request': inferred,
        'bootstrap': bootstrap_company(cfg, plan, dry_run=args.dry_run),
    }
    _emit(payload, args.format)
    return 0


def cmd_list_companies(args: argparse.Namespace) -> int:
    cfg = FactoryConfig()
    from .paperclip_api import _request
    endpoint = f"{cfg.paperclip_base_url}/api/companies"
    companies = _request(endpoint, api_key=cfg.paperclip_api_key)
    if args.format == 'text':
        print("Companies:")
        for c in companies:
            print(f"  {c['issuePrefix']}: {c['name']}")
    else:
        print(json.dumps(companies, indent=2, ensure_ascii=False))
    return 0


def cmd_get_company(args: argparse.Namespace) -> int:
    cfg = FactoryConfig()
    from .paperclip_api import _request
    endpoint = f"{cfg.paperclip_base_url}/api/companies"
    companies = _request(endpoint, api_key=cfg.paperclip_api_key)
    for c in companies:
        if c['issuePrefix'].upper() == args.prefix.upper():
            if args.format == 'text':
                print(f"Company: {c['name']}")
                print(f"Prefix: {c['issuePrefix']}")
                print(f"ID: {c['id']}")
            else:
                print(json.dumps(c, indent=2, ensure_ascii=False))
            return 0
    print(f"Company with prefix '{args.prefix}' not found", file=sys.stderr)
    return 1


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

    bootstrap = sub.add_parser('bootstrap-company')
    bootstrap.add_argument('company_name')
    bootstrap.add_argument('--template')
    bootstrap.add_argument('--prefix')
    bootstrap.add_argument('--visibility')
    bootstrap.add_argument('--deploy-target')
    bootstrap.add_argument('--provider-profile')
    bootstrap.add_argument('--dry-run', action='store_true')
    bootstrap.add_argument('--format', choices=['json', 'text'], default='json')

    interpret = sub.add_parser('interpret-request')
    interpret.add_argument('prompt')

    from_prompt = sub.add_parser('bootstrap-from-prompt')
    from_prompt.add_argument('prompt')
    from_prompt.add_argument('--company-name')
    from_prompt.add_argument('--prefix')
    from_prompt.add_argument('--provider-profile')
    from_prompt.add_argument('--dry-run', action='store_true')
    from_prompt.add_argument('--format', choices=['json', 'text'], default='json')

    # List companies
    list_companies = sub.add_parser('list-companies')
    list_companies.add_argument('--format', choices=['json', 'text'], default='json')

    # Get company by prefix
    get_company = sub.add_parser('get-company')
    get_company.add_argument('prefix')
    get_company.add_argument('--format', choices=['json', 'text'], default='json')

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
    if args.command == 'bootstrap-company':
        return cmd_bootstrap(args)
    if args.command == 'interpret-request':
        return cmd_interpret(args)
    if args.command == 'bootstrap-from-prompt':
        return cmd_bootstrap_from_prompt(args)
    if args.command == 'list-companies':
        return cmd_list_companies(args)
    if args.command == 'get-company':
        return cmd_get_company(args)
    p.error(f'unknown command: {args.command}')
    return 2


if __name__ == '__main__':
    raise SystemExit(main())
