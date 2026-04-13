from __future__ import annotations

from .config import FactoryConfig


def resolve_provider_profile(profile_name: str, config: FactoryConfig) -> dict:
    profiles = {
        'openai-codex': {
            'adapterType': 'hermes_local',
            'adapterConfig': {
                'model': 'gpt-5.4',
                'timeoutSec': 300,
                'maxIterations': 50,
            },
        },
        'claude-sonnet': {
            'adapterType': 'claude_local',
            'adapterConfig': {
                'model': 'claude-sonnet-4-6',
                'timeoutSec': 300,
                'maxTurnsPerRun': 50,
            },
        },
        'local-hermes': {
            'adapterType': config.default_agent_adapter_type,
            'adapterConfig': {
                'model': config.default_agent_model,
                'timeoutSec': 300,
            },
        },
    }
    return profiles.get(
        profile_name,
        {
            'adapterType': config.default_agent_adapter_type,
            'adapterConfig': {'model': config.default_agent_model, 'timeoutSec': 300},
        },
    )
