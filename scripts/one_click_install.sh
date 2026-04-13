#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

ENABLE_AUTOSTART=false
DRY_RUN=false
BOOTSTRAP_PROMPT=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --enable-autostart)
      ENABLE_AUTOSTART=true
      shift
      ;;
    --dry-run)
      DRY_RUN=true
      shift
      ;;
    --bootstrap-prompt)
      BOOTSTRAP_PROMPT="${2:-}"
      shift 2
      ;;
    *)
      echo "Unknown argument: $1"
      exit 1
      ;;
  esac
done

log() {
  printf '\n== %s ==\n' "$1"
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || {
    echo "Missing required command: $1"
    exit 1
  }
}

healthcheck() {
  curl -fsS http://127.0.0.1:3100/api/companies >/dev/null 2>&1
}

log "Checking prerequisites"
require_cmd python3
require_cmd node
require_cmd npm
require_cmd npx
require_cmd curl

log "Preparing .env"
if [[ ! -f .env ]]; then
  cp .env.example .env
  echo "Created .env from .env.example"
else
  echo ".env already exists"
fi

log "Installing Python dependencies"
python3 -m pip install -q -r requirements.txt

log "Checking Paperclip server"
if healthcheck; then
  echo "Paperclip is already running on http://127.0.0.1:3100"
else
  echo "Starting Paperclip in background..."
  nohup npx paperclipai run > "$ROOT_DIR/.paperclip-company-factory.paperclip.log" 2>&1 &
  PAPERCLIP_PID=$!
  echo "Spawned Paperclip PID: $PAPERCLIP_PID"

  for _ in $(seq 1 30); do
    if healthcheck; then
      break
    fi
    sleep 1
  done
fi

if ! healthcheck; then
  echo "Paperclip health check failed. Inspect logs at: $ROOT_DIR/.paperclip-company-factory.paperclip.log"
  exit 1
fi

echo "Paperclip health check passed"

log "Validating factory config"
PYTHONPATH=src python3 -m paperclip_company_factory.cli validate-env

if [[ "$ENABLE_AUTOSTART" == "true" ]]; then
  log "Enabling autostart"
  "$ROOT_DIR/scripts/enable_autostart.sh"
fi

if [[ -n "$BOOTSTRAP_PROMPT" ]]; then
  log "Bootstrapping from natural-language prompt"
  CMD=(python3 -m paperclip_company_factory.cli bootstrap-from-prompt "$BOOTSTRAP_PROMPT")
  if [[ "$DRY_RUN" == "true" ]]; then
    CMD+=(--dry-run)
  fi
  PYTHONPATH=src "${CMD[@]}"
fi

log "Done"
echo "Dashboard: http://127.0.0.1:3100"
echo "Status script: $ROOT_DIR/scripts/status.sh"
echo "Next step example:"
echo "  PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-from-prompt \"Create a public AI content studio company for newsletters\" --dry-run"
