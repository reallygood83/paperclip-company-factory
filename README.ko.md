# paperclip-company-factory

Hermes + Paperclip으로 자연어만으로 AI 회사를 생성·구성·배포·운영할 수 있게 해주는 공개용 오픈소스 툴킷입니다.

## GitHub 주소만으로 에이전트 설치

사용자가 Hermes나 OpenClaw에 이 GitHub 주소만 던져줘도 설치가 가능하도록 설계합니다.

`bash <(curl -fsSL https://raw.githubusercontent.com/reallygood83/paperclip-company-factory/main/scripts/install_from_github_url.sh) https://github.com/reallygood83/paperclip-company-factory --dry-run`

그 다음 추천 명령
- `./scripts/status.sh`
- `python3 scripts/first_run_wizard.py`
- `PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-from-prompt "공개용 AI 콘텐츠 회사 만들어줘" --dry-run --format text`

## 3분 초보자 경로

1. 저장소 클론
2. 원클릭 설치 실행
   - `./scripts/one_click_install.sh --enable-autostart`
3. 대화형 wizard 실행
   - `python3 scripts/first_run_wizard.py`
4. dry-run 리포트 확인
5. 승인 후 실제 생성
6. 대시보드 열기
   - `http://127.0.0.1:3100`

## 초보자용 스크립트

- `scripts/install_from_github_url.sh`
- `scripts/one_click_install.sh`
- `scripts/enable_autostart.sh`
- `scripts/status.sh`
- `scripts/restart.sh`
- `scripts/logs.sh`
- `scripts/first_run_wizard.py`

## 복구 UX

처음 쓰는 사람도 바로 이해할 수 있게 복구 경로를 분리했습니다.
- 상태 확인: `./scripts/status.sh`
- 재시작: `./scripts/restart.sh`
- 로그 보기: `./scripts/logs.sh`

## 문서

- `AGENTS.md`
- `docs/quickstart.ko.md`
- `docs/onboarding.ko.md`
- `docs/agent-install.ko.md`

## 멀티컴퍼니 지원

Paperclip 은 이제 멀티컴퍼니를 지원합니다. 다음 명령어로 관리하세요:

```bash
# 모든 회사 목록
PYTHONPATH=src python3 -m paperclip_company_factory.cli list-companies --format text

# 접두사로 회사 조회
PYTHONPATH=src python3 -m paperclip_company_factory.cli get-company HER --format text

# 특정 접두사로 회사 생성
PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-company "Hermes Validation Lab 01" --prefix HVL1 --format text
```

## 예시 출력

```
🏢 Hermes Validation Lab 01

📋 미션: Hermes Validation Lab 01 delivers AI-native market intelligence and decision support.
📊 템플릿: research-company
🔖 접두사: HER
👥 에이전트: 4 명 (CEO, Researcher, Analyst, Publisher)
📝 이슈: 3 개 스타터 태스크

✅ Dry-run 완료. --dry-run 없이 실행하면 실제 리소스가 생성됩니다.
```
