# Beginner Onboarding UX

## Goal

A first-time user should be able to:

1. install the toolkit
2. start Paperclip
3. keep it alive after reboot
4. create a first company from natural language
5. understand the result without reading raw JSON
6. recover quickly if the server stops

within a single onboarding flow.

## Recommended first-run flow

1. Run `scripts/one_click_install.sh`
2. Optional: enable autostart
3. Run `python3 scripts/first_run_wizard.py`
4. Review the dry-run report
5. Approve real creation
6. Open the dashboard
7. If something breaks, use:
   - `./scripts/status.sh`
   - `./scripts/restart.sh`
   - `./scripts/logs.sh`

## Hermes-first onboarding

The best beginner experience after install is:
- Hermes asks what kind of company to create
- Hermes runs `bootstrap-from-prompt --dry-run --format text`
- Hermes shows a short report
- Hermes asks for approval
- Hermes runs the real bootstrap
- Hermes suggests the next 2-3 commands to try
