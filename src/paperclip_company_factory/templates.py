from __future__ import annotations

from pathlib import Path
import yaml


def load_template(path: str | Path) -> dict:
    data = yaml.safe_load(Path(path).read_text())
    if not isinstance(data, dict):
        raise ValueError(f"Template at {path} did not parse to a mapping")
    return data


def resolve_template_path(template_name: str, root: str | Path | None = None) -> Path:
    base = Path(root) if root else Path(__file__).resolve().parents[2]
    path = base / 'templates' / f'{template_name}.yaml'
    if not path.exists():
        raise FileNotFoundError(f'Template not found: {path}')
    return path
