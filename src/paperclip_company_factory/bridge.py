from __future__ import annotations

import re


def infer_template_from_prompt(prompt: str) -> str:
    lowered = prompt.lower()
    if any(word in lowered for word in ['research', '리서치', 'analysis', 'analyst', 'intel']):
        return 'research-company'
    if any(word in lowered for word in ['content', 'writer', 'newsletter', '뉴스레터', '콘텐츠', 'media']):
        return 'content-studio'
    if any(word in lowered for word in ['agency', 'client', '에이전시', 'marketing', 'marketer']):
        return 'ai-agency'
    if any(word in lowered for word in ['saas', 'software', 'app', 'product', '제품']):
        return 'saas-company'
    if any(word in lowered for word in ['personal', 'ops', 'assistant', '비서', '개인 운영']):
        return 'personal-ops-company'
    return 'research-company'


def infer_deploy_target_from_prompt(prompt: str) -> str:
    lowered = prompt.lower()
    if any(word in lowered for word in ['vps', 'coolify', 'server', '서버', 'self-host']):
        return 'vps'
    if any(word in lowered for word in ['docker', 'compose']):
        return 'docker-compose'
    return 'local'


def infer_visibility_from_prompt(prompt: str) -> str:
    lowered = prompt.lower()
    if any(word in lowered for word in ['public', '공개']):
        return 'public'
    return 'private'


def infer_company_name(prompt: str) -> str:
    # Best effort heuristic: quoted string > cleaned prompt > fallback
    matches = re.findall(r'"([^"]+)"|\'([^\']+)\'', prompt)
    flattened = [item for pair in matches for item in pair if item]
    if flattened:
        return flattened[0]
    cleaned = re.sub(r'(?i)create|make|launch|bootstrap|build|company|startup|set up|please', ' ', prompt)
    cleaned = re.sub(r'(회사|만들어줘|세팅해줘|런치해줘|부트스트랩)', ' ', cleaned)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip(' .,!')
    if cleaned:
        return cleaned[:60].strip().title()
    return 'New Company'


def interpret_prompt(prompt: str) -> dict:
    return {
        'prompt': prompt,
        'company_name': infer_company_name(prompt),
        'template': infer_template_from_prompt(prompt),
        'deploy_target': infer_deploy_target_from_prompt(prompt),
        'visibility': infer_visibility_from_prompt(prompt),
    }
