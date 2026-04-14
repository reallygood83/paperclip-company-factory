# AGENTS.md

This repository is designed to be agent-friendly for Hermes, OpenClaw, Codex, Claude Code, and similar coding agents.

## Primary goal
Given only this GitHub URL, an agent should be able to:
1. clone or update the repo
2. run the one-click installer
3. verify Paperclip health
4. run the first-run wizard or bootstrap from a natural-language prompt

## Fastest path for agents

If the user gives only the GitHub URL, do this:

1. Clone or update the repository
   - `bash <(curl -fsSL https://raw.githubusercontent.com/reallygood83/paperclip-company-factory/main/scripts/install_from_github_url.sh) https://github.com/reallygood83/paperclip-company-factory --dry-run`

2. Verify status
   - `./scripts/status.sh`

3. Create a first company from prompt
   - `PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-from-prompt "Create a public AI content studio company for newsletters" --dry-run --format text`

## Preferred execution pattern
- Start with `--dry-run`
- Show the text report to the user
- Ask for approval before the real bootstrap
- On failure, use `./scripts/status.sh`, `./scripts/restart.sh`, and `./scripts/logs.sh`

## Beginner-friendly commands
- install: `./scripts/one_click_install.sh --enable-autostart`
- wizard: `python3 scripts/first_run_wizard.py`
- status: `./scripts/status.sh`
- restart: `./scripts/restart.sh`
- logs: `./scripts/logs.sh`

## Agent hints
- Prefer `--format text` for user-facing output
- Prefer `bootstrap-from-prompt` over manual JSON planning for first-run UX
- Use the repo's own scripts before inventing custom install steps
