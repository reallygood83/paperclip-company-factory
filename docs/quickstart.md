# Quickstart

1. Clone the repository
2. Copy `.env.example` to `.env`
3. Install dependencies: `python3 -m pip install -r requirements.txt`
4. Start Paperclip: `npx paperclipai run`
5. Validate environment: `PYTHONPATH=src python3 -m paperclip_company_factory.cli validate-env`
6. Generate a plan:
   `PYTHONPATH=src python3 -m paperclip_company_factory.cli plan-company "Acme Research" --template research-company`
7. Dry-run company creation:
   `PYTHONPATH=src python3 -m paperclip_company_factory.cli create-company "Acme Research" --template research-company --dry-run`
