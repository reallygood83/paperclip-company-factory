# paperclip-company-factory

Hermes + Paperclip으로 자연어만으로 AI 회사를 생성·구성·배포·운영할 수 있게 해주는 공개용 오픈소스 툴킷입니다.

## 이번 버전에서 되는 것

- 공개용 범용 회사 템플릿
- 자연어 요청 해석 CLI
- 회사 생성 계획 작성 CLI
- 실제 Paperclip 회사 + 에이전트 + starter issue 생성 흐름
- Hermes 자연어 오케스트레이션용 스킬 초안
- Docker Compose 배포 스타터

## 빠른 시작

1. 저장소 클론
2. `.env.example`를 `.env`로 복사
3. 의존성 설치
   - `python3 -m pip install -r requirements.txt`
4. Paperclip 실행
   - `npx paperclipai run`
5. 설정 검증
   - `PYTHONPATH=src python3 -m paperclip_company_factory.cli validate-env`
6. 자연어 요청 해석
   - `PYTHONPATH=src python3 -m paperclip_company_factory.cli interpret-request "공개용 AI 콘텐츠 회사 만들어줘"`
7. 회사 생성 계획 작성
   - `PYTHONPATH=src python3 -m paperclip_company_factory.cli plan-company "Acme Research" --template research-company`
8. 전체 생성 dry-run
   - `PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-company "Acme Research" --template research-company --dry-run`
9. 자연어에서 바로 생성 흐름 만들기
   - `PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-from-prompt "공개용 AI 콘텐츠 회사 만들어줘" --dry-run`
10. 실제 생성 실행
   - `PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-company "Acme Research" --template research-company`

## Hermes 연동 개념

- Hermes = 자연어 오케스트레이터
- Paperclip = 회사/에이전트/이슈 실행 엔진
- paperclip-company-factory = 템플릿 + bootstrap + deploy 레이어

예시 흐름
- 사용자: “리서치 회사 하나 만들어줘”
- Hermes: 요청 해석 → 템플릿 추천 → dry-run 실행
- 승인 후 실제 회사/에이전트/이슈 생성
- 결과를 대시보드/ID/초기 이슈와 함께 보고
