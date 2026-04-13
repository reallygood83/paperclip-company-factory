# Quickstart

## Fastest path

```bash
./scripts/one_click_install.sh --enable-autostart
PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-from-prompt "Create a public AI content studio company for newsletters" --dry-run
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

### 5. Dry-run a full bootstrap from prompt

```bash
PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-from-prompt "Create a public AI content studio company for newsletters" --dry-run
```

### 6. Execute the bootstrap

```bash
PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-from-prompt "Create a public AI content studio company for newsletters"
```
