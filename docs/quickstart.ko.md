# 빠른 시작

## 1. 설치

`python3 -m pip install -r requirements.txt`

## 2. Paperclip 실행

`npx paperclipai run`

## 3. 설정 검증

`PYTHONPATH=src python3 -m paperclip_company_factory.cli validate-env`

## 4. 자연어 요청 해석

`PYTHONPATH=src python3 -m paperclip_company_factory.cli interpret-request "공개용 AI 콘텐츠 회사 만들어줘"`

## 5. 전체 생성 dry-run

`PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-company "Atlas Research" --template research-company --dry-run`

## 6. 실제 생성 실행

`PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-company "Atlas Research" --template research-company`

## 7. 결과

- 회사 생성
- 템플릿 기반 에이전트 생성
- starter issue 생성

## 8. 자연어에서 바로 bootstrap

`PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-from-prompt "공개용 AI 콘텐츠 회사 만들어줘" --dry-run`
