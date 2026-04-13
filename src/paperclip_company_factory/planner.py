from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from .templates import load_template, resolve_template_path


def slugify(value: str) -> str:
    return ''.join(ch.lower() if ch.isalnum() else '-' for ch in value).strip('-')


@dataclass
class CompanyPlan:
    company_name: str
    company_prefix: str
    mission: str
    template_id: str
    visibility: str
    deploy_target: str
    provider_profile: str
    agent_roles: list[dict]
    starter_issues: list[dict]
    launch_checklist: list[str]

    def to_dict(self) -> dict:
        return asdict(self)


def build_company_plan(company_name: str, template_name: str, prefix: str | None = None, visibility: str = 'private', deploy_target: str = 'local', provider_profile: str = 'openai-codex', template_root: str | Path | None = None) -> CompanyPlan:
    path = resolve_template_path(template_name, template_root)
    template = load_template(path)
    company_prefix = (prefix or ''.join([part[0] for part in company_name.split() if part])[:4] or slugify(company_name)[:4]).upper()
    return CompanyPlan(
        company_name=company_name,
        company_prefix=company_prefix,
        mission=template.get('mission_template', 'Launch an AI-native company').replace('{company_name}', company_name),
        template_id=template['template_id'],
        visibility=visibility,
        deploy_target=deploy_target,
        provider_profile=provider_profile,
        agent_roles=template.get('agent_roles', []),
        starter_issues=template.get('starter_issues', []),
        launch_checklist=template.get('launch_checklist', []),
    )
