---
name: paperclip-company-factory
description: Launch reusable AI-native companies from natural language using Hermes + Paperclip.
version: 0.1.0
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

## Core workflow
1. Clarify business type and select a template
2. Generate a structured company plan
3. Dry-run creation payload
4. Confirm risky steps
5. Create company and seed starter issues
6. Optionally deploy with Docker Compose or VPS

## Safe defaults
- Default to dry-run before POST requests
- Default to local/self-hosted deployment
- Keep credentials in `.env`, never inline
- Require explicit confirmation for destructive or paid actions

## Recommended commands
- `PYTHONPATH=src python3 -m paperclip_company_factory.cli validate-env`
- `PYTHONPATH=src python3 -m paperclip_company_factory.cli health`
- `PYTHONPATH=src python3 -m paperclip_company_factory.cli plan-company "Acme Research" --template research-company`
- `PYTHONPATH=src python3 -m paperclip_company_factory.cli create-company "Acme Research" --template research-company --dry-run`

## Output style
Return:
- chosen template
- mission
- role lineup
- launch checklist
- deployment recommendation

## Public OSS principles
- no personal IDs or machine-specific paths
- provider-agnostic defaults
- public-friendly onboarding docs
