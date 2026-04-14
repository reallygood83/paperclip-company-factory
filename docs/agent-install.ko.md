# 에이전트 친화 설치

이 저장소는 Hermes, OpenClaw, Codex 같은 에이전트가 GitHub 주소만 받아도 설치를 진행할 수 있도록 설계합니다.

## 목표
에이전트는 GitHub URL만 받아도 아래를 수행할 수 있어야 합니다.
- 저장소 clone/update
- one-click installer 실행
- Paperclip health 검증
- wizard 또는 자연어 bootstrap 시작

## 원격 설치 명령

`bash <(curl -fsSL https://raw.githubusercontent.com/reallygood83/paperclip-company-factory/main/scripts/install_from_github_url.sh) https://github.com/reallygood83/paperclip-company-factory --dry-run`

## Hermes/OpenClaw에 줄 수 있는 예시 프롬프트

- 이 GitHub 저장소를 설치해서 첫 실행이 가능하도록 준비해줘: https://github.com/reallygood83/paperclip-company-factory
- 설치 후 상태를 확인하고, 콘텐츠 회사 dry-run 리포트까지 보여줘.

## 설치 후 추천 명령

`./scripts/status.sh`

`python3 scripts/first_run_wizard.py`

`PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-from-prompt "공개용 AI 콘텐츠 회사 만들어줘" --dry-run --format text`
