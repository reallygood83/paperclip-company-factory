# paperclip-company-factory

Hermes + Paperclip으로 자연어만으로 AI 회사를 생성·구성·배포·운영할 수 있게 해주는 공개용 오픈소스 툴킷입니다.

## 포함 내용

- 공개용 범용 회사 템플릿
- 회사 생성 계획과 dry-run을 위한 Python CLI
- Hermes 자연어 연동용 스킬 초안
- Docker Compose 배포 스타터
- launch / troubleshooting 문서

## 빠른 시작

1. 저장소 클론
2. `.env.example`를 `.env`로 복사
3. 의존성 설치
   - `python3 -m pip install -r requirements.txt`
4. Paperclip 실행
   - `npx paperclipai run`
5. 설정 검증
   - `PYTHONPATH=src python3 -m paperclip_company_factory.cli validate-env`
6. 회사 생성 계획 작성
   - `PYTHONPATH=src python3 -m paperclip_company_factory.cli plan-company "Acme Research" --template research-company`
7. 회사 생성 dry-run
   - `PYTHONPATH=src python3 -m paperclip_company_factory.cli create-company "Acme Research" --template research-company --dry-run`

## 템플릿

- research-company
- content-studio
- ai-agency
- saas-company
- personal-ops-company

## 핵심 방향

- Hermes = 자연어 오케스트레이터
- Paperclip = 회사/에이전트/이슈 실행 엔진
- paperclip-company-factory = 템플릿 + bootstrap + deploy 레이어

## 현재 상태

v0.1 스타터이며, 범용 공개 배포를 위한 기본 구조와 문서, 계획 CLI, 템플릿, Hermes 스킬 초안을 포함합니다.
