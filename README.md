# paperclip-company-factory

Launch AI-native companies from natural language using Hermes + Paperclip.

`paperclip-company-factory` is an open-source toolkit for bootstrapping, configuring, hosting, and operating reusable agent companies with public-safe templates and a Hermes-friendly natural-language workflow.

## GitHub-URL-only agent install

If a user gives Hermes or OpenClaw only this GitHub URL, the repo should still be installable:

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/reallygood83/paperclip-company-factory/main/scripts/install_from_github_url.sh) https://github.com/reallygood83/paperclip-company-factory --dry-run
```

Then continue with:
- `./scripts/status.sh`
- `python3 scripts/first_run_wizard.py`
- `PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-from-prompt "Create a public AI content studio company for newsletters" --dry-run --format text`

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

- `scripts/install_from_github_url.sh`
- `scripts/one_click_install.sh`
- `scripts/enable_autostart.sh`
- `scripts/status.sh`
- `scripts/restart.sh`
- `scripts/logs.sh`
- `scripts/first_run_wizard.py`

## Recovery UX

For first-time users, recovery should be obvious:
- check status: `./scripts/status.sh`
- restart service: `./scripts/restart.sh`
- inspect logs: `./scripts/logs.sh`

## Example commands

- `pcf validate-env`
- `pcf health`
- `pcf interpret-request "Create a public AI content studio company for newsletters"`
- `pcf bootstrap-company "Atlas Research" --template research-company --dry-run --format text`
- `pcf bootstrap-from-prompt "Create a public AI content studio company for newsletters" --dry-run --format text`

## Hermes integration concept

A practical Hermes flow looks like this:
- user says: "리서치 회사 하나 만들어줘"
- Hermes runs `bootstrap-from-prompt --dry-run --format text`
- Hermes shows a readable report and asks for approval
- Hermes runs the real bootstrap and reports company, agent, and issue IDs
- Hermes can continue with commands like "이 회사에 marketer 추가해줘"

## Multi-company support

Paperclip now supports multiple companies. Use these commands to manage them:

```bash
# List all companies
PYTHONPATH=src python3 -m paperclip_company_factory.cli list-companies --format text

# Get company by prefix
PYTHONPATH=src python3 -m paperclip_company_factory.cli get-company HER --format text

# Create company with specific prefix
PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-company "Hermes Validation Lab 01" --prefix HVL1 --format text
```

## Example output

```
🏢 Hermes Validation Lab 01

📋 Mission: Hermes Validation Lab 01 delivers AI-native market intelligence and decision support.
📊 Template: research-company
🔖 Prefix: HER
👥 Agents: 4 (CEO, Researcher, Analyst, Publisher)
📝 Issues: 3 starter tasks

✅ Dry-run complete. Run without --dry-run to create real resources.
```

## Docs

- `AGENTS.md`
- `docs/architecture.md`
- `docs/quickstart.md`
- `docs/onboarding.md`
- `docs/agent-install.md`
- `docs/security.md`
- `docs/troubleshooting.md`
- `docs/launch-playbook.md`

## License

MIT
