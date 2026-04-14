# Agent-Friendly Install

This repository is intentionally friendly to Hermes, OpenClaw, and other coding agents.

## Goal
An agent should be able to install this project from only the GitHub URL.

## Remote bootstrap command

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/reallygood83/paperclip-company-factory/main/scripts/install_from_github_url.sh) https://github.com/reallygood83/paperclip-company-factory --dry-run
```

## What this does
- clone or update the repo
- run the one-click installer
- validate the Paperclip health path
- print the next wizard/bootstrap commands

## Suggested Hermes/OpenClaw prompt

- Install this GitHub repo and get it ready for first-run onboarding: https://github.com/reallygood83/paperclip-company-factory
- Then run the status check and show me the dry-run report for a content company.

## Suggested post-install commands

```bash
./scripts/status.sh
python3 scripts/first_run_wizard.py
PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-from-prompt "Create a public AI content studio company for newsletters" --dry-run --format text
```
