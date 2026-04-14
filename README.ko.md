# paperclip-company-factory

Hermes + Paperclip으로 자연어만으로 AI 회사를 생성·구성·배포·운영할 수 있게 해주는 공개용 오픈소스 툴킷입니다.

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

## Hermes 연동 개념

예시 흐름
- 사용자: “리서치 회사 하나 만들어줘”
- Hermes: `bootstrap-from-prompt --dry-run --format text` 실행
- 사람이 읽기 쉬운 보고서 출력
- 승인 후 실제 회사/에이전트/이슈 생성
- 이후 “이 회사에 marketer 추가해줘”, “이 회사 런치 준비해줘”처럼 이어감
