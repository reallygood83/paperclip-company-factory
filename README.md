# paperclip-company-factory

Launch AI-native companies from natural language using Hermes + Paperclip.

`paperclip-company-factory` is an open-source toolkit for bootstrapping, configuring, hosting, and operating reusable agent companies with public-safe templates and a Hermes-friendly natural-language workflow.

## What this repo includes

- Public-safe company templates
- A small Python CLI for planning and dry-running company creation
- Hermes skill scaffolding for natural-language orchestration
- Docker Compose deployment starter
- Launch and troubleshooting docs

## Quickstart

1. Clone this repository
2. Copy `.env.example` to `.env`
3. Install dependencies
   - `python3 -m pip install -r requirements.txt`
4. Start Paperclip
   - `npx paperclipai run`
5. Validate configuration
   - `PYTHONPATH=src python3 -m paperclip_company_factory.cli validate-env`
6. Generate a company plan
   - `PYTHONPATH=src python3 -m paperclip_company_factory.cli plan-company "Acme Research" --template research-company`
7. Dry-run create-company payload
   - `PYTHONPATH=src python3 -m paperclip_company_factory.cli create-company "Acme Research" --template research-company --dry-run`

## Example commands

- `pcf validate-env`
- `pcf health`
- `pcf plan-company "Atlas Research" --template research-company`
- `pcf create-company "Atlas Research" --template research-company --dry-run`

## Templates

- `research-company`
- `content-studio`
- `ai-agency`
- `saas-company`
- `personal-ops-company`

## Hermes integration concept

Hermes acts as the natural-language orchestrator.
Paperclip acts as the company runtime and issue/agent engine.
This repo provides the reusable factory layer between them.

## Current status

This is a public OSS starter focused on:
- reproducible bootstrap
- structured planning
- dry-run safety
- local/self-host first workflows

## Docs

- `docs/architecture.md`
- `docs/quickstart.md`
- `docs/security.md`
- `docs/troubleshooting.md`
- `docs/launch-playbook.md`

## License

MIT
