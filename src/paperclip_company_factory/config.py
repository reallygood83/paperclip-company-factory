from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass
class FactoryConfig:
    paperclip_base_url: str = os.getenv("PAPERCLIP_BASE_URL", "http://127.0.0.1:3100")
    paperclip_api_prefix: str = os.getenv("PAPERCLIP_API_PREFIX", "/api")
    paperclip_api_key: str = os.getenv("PAPERCLIP_API_KEY", "")
    paperclip_mode: str = os.getenv("PAPERCLIP_MODE", "local_trusted")
    hermes_enabled: str = os.getenv("HERMES_ENABLED", "true")
    hermes_platform: str = os.getenv("HERMES_PLATFORM", "telegram")
    hermes_bridge_mode: str = os.getenv("HERMES_BRIDGE_MODE", "manual")
    default_template: str = os.getenv("DEFAULT_TEMPLATE", "research-company")
    default_deploy_target: str = os.getenv("DEFAULT_DEPLOY_TARGET", "local")
    default_visibility: str = os.getenv("DEFAULT_VISIBILITY", "private")
    default_provider_profile: str = os.getenv("DEFAULT_PROVIDER_PROFILE", "openai-codex")

    def missing_required(self) -> list[str]:
        missing: list[str] = []
        if not self.paperclip_base_url:
            missing.append("PAPERCLIP_BASE_URL")
        if not self.paperclip_api_prefix:
            missing.append("PAPERCLIP_API_PREFIX")
        return missing
