# Quickstart

## Fastest path

```bash
./scripts/one_click_install.sh --enable-autostart
python3 scripts/first_run_wizard.py
```

## Step-by-step

### 1. Install

```bash
python3 -m pip install -r requirements.txt
```

### 2. Run Paperclip

```bash
npx paperclipai run
```

### 3. Check status

```bash
./scripts/status.sh
```

### 4. Interpret a request

```bash
PYTHONPATH=src python3 -m paperclip_company_factory.cli interpret-request "Create a public AI content studio company for newsletters"
```

### 5. Dry-run a full bootstrap from prompt with a readable report

```bash
PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-from-prompt "Create a public AI content studio company for newsletters" --dry-run --format text
```

### 6. Execute the bootstrap

```bash
PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-from-prompt "Create a public AI content studio company for newsletters" --format text
```

### 7. Wizard mode

```bash
python3 scripts/first_run_wizard.py
```
