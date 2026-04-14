# Beginner Onboarding UX

## Goal

A first-time user should be able to:

1. install the toolkit
2. start Paperclip
3. keep it alive after reboot
4. create a first company from natural language
5. understand the result without reading raw JSON

within a single onboarding flow.

## Beginner-first UX principles

- hide Paperclip internals at first
- default to local + safe + self-hosted
- show success as a living company, not as config files
- use progressive disclosure for advanced settings
- make recovery obvious: status, restart, logs
- format results as human-readable reports by default in beginner paths

## Recommended first-run flow

1. Run `scripts/one_click_install.sh`
2. Optional: enable autostart
3. Run `python3 scripts/first_run_wizard.py`
4. Review the dry-run report
5. Approve real creation
6. Open the dashboard
7. Continue from Hermes with a phrase like:
   - `리서치 회사 하나 만들어줘`

## Hermes-first onboarding

The best beginner experience after install is:
- Hermes asks what kind of company to create
- Hermes runs `bootstrap-from-prompt --dry-run --format text`
- Hermes shows a short report
- Hermes asks for approval
- Hermes runs the real bootstrap

## Success screen should show

- dashboard URL
- current status
- autostart state
- company created / planned
- agents created / planned
- starter issues created / planned
- the next natural-language command to try
