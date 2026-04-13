# Beginner Onboarding UX

## Goal

A first-time user should be able to:

1. install the toolkit
2. start Paperclip
3. keep it alive after reboot
4. create a first company from natural language

within a single onboarding flow.

## Beginner-first UX principles

- hide Paperclip internals at first
- default to local + safe + self-hosted
- show success as a living company, not as config files
- use progressive disclosure for advanced settings
- make recovery obvious: status, restart, logs

## Recommended first-run flow

1. Run `scripts/one_click_install.sh`
2. Optional: enable autostart
3. Run a natural-language bootstrap dry-run
4. Approve real creation
5. Open the dashboard
6. Continue from Hermes with a phrase like:
   - `리서치 회사 하나 만들어줘`

## One-click experience

The installer should:
- check prerequisites
- install Python requirements
- start Paperclip in the background if needed
- validate health
- optionally enable autostart
- print the exact next command for first company creation

## Autostart UX copy

Do not say:
- daemon registration
- launchd plist
- systemd unit

Say:
- start automatically when the computer starts
- keep the server running in the background
- restart automatically if it stops

## Success screen should show

- dashboard URL
- current status
- autostart state
- the next natural-language command to try
