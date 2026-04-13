---
name: paperclip-company-factory
description: Launch reusable AI-native companies from natural language using Hermes + Paperclip.
version: 0.2.0
author: Hermes Agent
license: MIT
---

# Paperclip Company Factory

## Purpose
Use this skill to bootstrap, configure, and operate a Paperclip company from natural language while keeping the project public-safe and reproducible.

## Trigger phrases
- create a company
- launch an AI company
- bootstrap a Paperclip company
- set up Hermes + Paperclip
- deploy this company
- prepare launch
- 회사 만들어줘
- 리서치 회사 만들어줘
- 콘텐츠 회사 세팅해줘

## Core workflow
1. Interpret the user prompt into template / visibility / deploy target
2. Generate a structured company plan
3. Run a full bootstrap dry-run
4. Confirm risky steps
5. Create company and seed starter issues
6. Optionally deploy with Docker Compose or VPS

## Recommended commands
- `PYTHONPATH=src python3 -m paperclip_company_factory.cli interpret-request "Create a public AI content studio company"`
- `PYTHONPATH=src python3 -m paperclip_company_factory.cli plan-company "Acme Research" --template research-company`
- `PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-company "Acme Research" --template research-company --dry-run`
- `PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-company "Acme Research" --template research-company`

## Safe defaults
- default to dry-run before POST requests
- default to local/self-hosted deployment
- keep credentials in `.env`, never inline
- require explicit confirmation for destructive or paid actions

## Output style
Return:
- chosen template
- mission
- role lineup
- launch checklist
- deployment recommendation
- created company / agent / issue IDs when execution is real

## Public OSS principles
- no personal IDs or machine-specific paths
- provider-agnostic defaults where possible
- public-friendly onboarding docs
