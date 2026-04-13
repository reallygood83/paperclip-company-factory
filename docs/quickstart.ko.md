# 빠른 시작

1. 저장소를 클론합니다
2. `.env.example`를 `.env`로 복사합니다
3. 의존성을 설치합니다
   `python3 -m pip install -r requirements.txt`
4. Paperclip을 실행합니다
   `npx paperclipai run`
5. 환경을 검증합니다
   `PYTHONPATH=src python3 -m paperclip_company_factory.cli validate-env`
6. 회사 생성 계획을 만듭니다
   `PYTHONPATH=src python3 -m paperclip_company_factory.cli plan-company "Acme Research" --template research-company`
7. 생성 dry-run을 실행합니다
   `PYTHONPATH=src python3 -m paperclip_company_factory.cli create-company "Acme Research" --template research-company --dry-run`
