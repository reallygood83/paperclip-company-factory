Example
===

Prompt
- Create an AI-native semiconductor research company

CLI flow
- `PYTHONPATH=src python3 -m paperclip_company_factory.cli interpret-request "Create an AI-native semiconductor research company"`
- `PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-company "Semiconductor Alpha Research" --template research-company --dry-run`
- `PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-company "Semiconductor Alpha Research" --template research-company`

Expected result
- Research company created in Paperclip
- CEO / Researcher / Analyst / Publisher created
- Starter issues seeded
