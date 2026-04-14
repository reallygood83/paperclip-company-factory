# 초보자용 온보딩 UX

## 목표

처음 쓰는 사용자가 한 번의 흐름 안에서 아래를 끝내야 합니다.

1. 설치
2. Paperclip 실행
3. 재부팅 후에도 계속 살아있게 설정
4. 자연어로 첫 회사 생성
5. raw JSON을 읽지 않고도 결과 이해
6. 서버가 멈춰도 빠르게 복구

## 추천 첫 실행 흐름

1. `scripts/one_click_install.sh` 실행
2. 원하면 자동 시작 켜기
3. `python3 scripts/first_run_wizard.py` 실행
4. dry-run 보고서 확인
5. 승인 후 실제 생성
6. 대시보드 열기
7. 문제가 생기면 아래 사용
   - `./scripts/status.sh`
   - `./scripts/restart.sh`
   - `./scripts/logs.sh`

## Hermes-first 온보딩

설치가 끝난 뒤 가장 좋은 경험은 아래입니다.
- Hermes가 어떤 회사를 만들지 질문
- `bootstrap-from-prompt --dry-run --format text` 실행
- 짧고 읽기 쉬운 보고서 출력
- 승인 질문
- 실제 bootstrap 실행
- 다음에 해볼 Hermes 명령 2~3개 제안
