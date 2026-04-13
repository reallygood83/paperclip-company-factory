# 아키텍처

paperclip-company-factory는 4개 계층으로 구성됩니다.

1. Hermes: 자연어 오케스트레이터
2. Factory CLI + 템플릿: 재현 가능한 회사 생성 레이어
3. Paperclip: 회사/에이전트/이슈 실행 엔진
4. 선택형 배포 레이어: Docker Compose / VPS / Coolify

핵심 목표는 특정 개인 환경이 아니라 공개용 재현성입니다.
