# Quickstart

## 1. Install

```bash
python3 -m pip install -r requirements.txt
```

## 2. Run Paperclip

```bash
npx paperclipai run
```

## 3. Validate config

```bash
PYTHONPATH=src python3 -m paperclip_company_factory.cli validate-env
```

## 4. Interpret a request

```bash
PYTHONPATH=src python3 -m paperclip_company_factory.cli interpret-request "Create a public AI content studio company for newsletters"
```

## 5. Dry-run a full bootstrap

```bash
PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-company "Atlas Research" --template research-company --dry-run
```

## 6. Execute the bootstrap

```bash
PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-company "Atlas Research" --template research-company
```

## 7. Expected outputs

- created company object
- created agents from template roles
- created starter issues

## 8. Bootstrap straight from a prompt

```bash
PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-from-prompt "Create a public AI content studio company for newsletters" --dry-run
```
