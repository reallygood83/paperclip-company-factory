# paperclip-company-factory

Launch AI-native companies from natural language using Hermes + Paperclip.

`paperclip-company-factory` is an open-source toolkit for bootstrapping, configuring, hosting, and operating reusable agent companies with public-safe templates and a Hermes-friendly natural-language workflow.

## 3-minute beginner path

1. Clone this repository
2. Run one command:
   - `./scripts/one_click_install.sh --enable-autostart`
3. Open the interactive wizard:
   - `python3 scripts/first_run_wizard.py`
4. Review the dry-run report
5. Approve the real bootstrap
6. Open the Paperclip dashboard at `http://127.0.0.1:3100`

## Beginner-friendly scripts

- `scripts/one_click_install.sh`
- `scripts/enable_autostart.sh`
- `scripts/status.sh`
- `scripts/first_run_wizard.py`

## What this repo includes

- Public-safe company templates
- A Python CLI for planning, interpreting prompts, and bootstrapping companies
- Real Paperclip bootstrap flow for company + agents + starter issues
- Text report formatting for beginner-friendly results
- Beginner-first onboarding docs and scripts
- Hermes skill scaffolding for natural-language orchestration
- Docker Compose deployment starter
- Launch and troubleshooting docs

## Quickstart

See `docs/quickstart.md` for the step-by-step flow.

## Example commands

- `pcf validate-env`
- `pcf health`
- `pcf interpret-request "Create a public AI content studio company for newsletters"`
- `pcf bootstrap-company "Atlas Research" --template research-company --dry-run --format text`
- `pcf bootstrap-from-prompt "Create a public AI content studio company for newsletters" --dry-run --format text`

## Implemented bootstrap flow

The CLI now supports a real Paperclip bootstrap sequence:

1. create company
2. create agents from the selected template
3. create starter issues
4. summarize the result in a human-friendly report

By default, start with `--dry-run` first.

## Hermes integration concept

Hermes acts as the natural-language orchestrator.
Paperclip acts as the company runtime and issue/agent engine.
This repo provides the reusable factory layer between them.

A practical Hermes flow looks like this:
- user says: “리서치 회사 하나 만들어줘”
- Hermes runs `bootstrap-from-prompt --dry-run --format text`
- Hermes shows a readable report and asks for approval
- Hermes runs the real bootstrap and reports company, agent, and issue IDs
- Hermes can continue with commands like “이 회사에 marketer 추가해줘”

## Templates

- `research-company`
- `content-studio`
- `ai-agency`
- `saas-company`
- `personal-ops-company`

## Docs

- `docs/architecture.md`
- `docs/quickstart.md`
- `docs/onboarding.md`
- `docs/security.md`
- `docs/troubleshooting.md`
- `docs/launch-playbook.md`

## License

MIT
