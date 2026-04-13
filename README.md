# paperclip-company-factory

Launch AI-native companies from natural language using Hermes + Paperclip.

`paperclip-company-factory` is an open-source toolkit for bootstrapping, configuring, hosting, and operating reusable agent companies with public-safe templates and a Hermes-friendly natural-language workflow.

## What this repo includes

- Public-safe company templates
- A Python CLI for planning, interpreting prompts, and bootstrapping companies
- Real Paperclip bootstrap flow for company + agents + starter issues
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
6. Interpret a natural-language request
   - `PYTHONPATH=src python3 -m paperclip_company_factory.cli interpret-request "Create a public AI content studio company for newsletters"`
7. Generate a company plan
   - `PYTHONPATH=src python3 -m paperclip_company_factory.cli plan-company "Acme Research" --template research-company`
8. Dry-run the full bootstrap
   - `PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-company "Acme Research" --template research-company --dry-run`
9. Bootstrap directly from a natural-language request
   - `PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-from-prompt "Create a public AI content studio company for newsletters" --dry-run`
10. Execute the real bootstrap
   - `PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-company "Acme Research" --template research-company`

## Example commands

- `pcf validate-env`
- `pcf health`
- `pcf interpret-request "Create a public AI content studio company for newsletters"`
- `pcf plan-company "Atlas Research" --template research-company`
- `pcf bootstrap-company "Atlas Research" --template research-company --dry-run`
- `pcf bootstrap-from-prompt "Create a public AI content studio company for newsletters" --dry-run`

## Implemented bootstrap flow

The CLI now supports a real Paperclip bootstrap sequence:

1. create company
2. create agents from the selected template
3. create starter issues

By default, start with `--dry-run` first.

## Hermes integration concept

Hermes acts as the natural-language orchestrator.
Paperclip acts as the company runtime and issue/agent engine.
This repo provides the reusable factory layer between them.

A practical Hermes flow looks like this:
- user says: “리서치 회사 하나 만들어줘”
- Hermes maps prompt → template, visibility, deploy target
- Hermes runs `bootstrap-company --dry-run`
- Hermes shows the plan and asks for approval for risky steps
- Hermes runs the real bootstrap and reports URLs / IDs / starter issues

## Templates

- `research-company`
- `content-studio`
- `ai-agency`
- `saas-company`
- `personal-ops-company`

## Docs

- `docs/architecture.md`
- `docs/quickstart.md`
- `docs/security.md`
- `docs/troubleshooting.md`
- `docs/launch-playbook.md`

## License

MIT
