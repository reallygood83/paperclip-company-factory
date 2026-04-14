# 빠른 시작

## 가장 빠른 경로

`./scripts/one_click_install.sh --enable-autostart`

`python3 scripts/first_run_wizard.py`

## 단계별 흐름

### 1. 설치

`python3 -m pip install -r requirements.txt`

### 2. Paperclip 실행

`npx paperclipai run`

### 3. 상태 확인

`./scripts/status.sh`

### 4. 자연어 요청 해석

`PYTHONPATH=src python3 -m paperclip_company_factory.cli interpret-request "공개용 AI 콘텐츠 회사 만들어줘"`

### 5. 자연어에서 바로 전체 dry-run + 읽기 쉬운 리포트

`PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-from-prompt "공개용 AI 콘텐츠 회사 만들어줘" --dry-run --format text`

### 6. 실제 생성 실행

`PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-from-prompt "공개용 AI 콘텐츠 회사 만들어줘" --format text`

### 7. Wizard 모드

`python3 scripts/first_run_wizard.py`
