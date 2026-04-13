# paperclip-company-factory

Hermes + Paperclip으로 자연어만으로 AI 회사를 생성·구성·배포·운영할 수 있게 해주는 공개용 오픈소스 툴킷입니다.

## 3분 초보자 경로

1. 저장소 클론
2. 원클릭 설치 실행
   - `./scripts/one_click_install.sh --enable-autostart`
3. 자연어로 첫 회사 dry-run 생성
   - `PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-from-prompt "공개용 AI 콘텐츠 회사 만들어줘" --dry-run`
4. 승인 후 실제 생성
5. 대시보드 열기
   - `http://127.0.0.1:3100`

## 초보자용 스크립트

- `scripts/one_click_install.sh`
- `scripts/enable_autostart.sh`
- `scripts/status.sh`

## 이번 버전에서 되는 것

- 공개용 범용 회사 템플릿
- 자연어 요청 해석 CLI
- 실제 Paperclip 회사 + 에이전트 + starter issue 생성 흐름
- 초보자용 온보딩 문서와 원클릭 스크립트
- Hermes 자연어 오케스트레이션용 스킬 초안
- Docker Compose 배포 스타터

## Quickstart

자세한 흐름은 `docs/quickstart.ko.md` 참고.

## Hermes 연동 개념

- Hermes = 자연어 오케스트레이터
- Paperclip = 회사/에이전트/이슈 실행 엔진
- paperclip-company-factory = 템플릿 + bootstrap + deploy 레이어

예시 흐름
- 사용자: “리서치 회사 하나 만들어줘”
- Hermes: 요청 해석 → 템플릿 추천 → dry-run 실행
- 승인 후 실제 회사/에이전트/이슈 생성
- 결과를 대시보드/ID/초기 이슈와 함께 보고
