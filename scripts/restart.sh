#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SERVICE_NAME="paperclip-company-factory-paperclip"
LOG_FILE="$ROOT_DIR/.paperclip-company-factory.paperclip.log"

healthcheck() {
  curl -fsS http://127.0.0.1:3100/api/companies >/dev/null 2>&1
}

if [[ "$(uname -s)" == "Darwin" ]] && launchctl list | grep -q "$SERVICE_NAME"; then
  launchctl kickstart -k "gui/$(id -u)/$SERVICE_NAME" || {
    PLIST="$HOME/Library/LaunchAgents/${SERVICE_NAME}.plist"
    launchctl unload "$PLIST" >/dev/null 2>&1 || true
    launchctl load "$PLIST"
  }
elif [[ "$(uname -s)" == "Linux" ]] && systemctl --user is-enabled "${SERVICE_NAME}.service" >/dev/null 2>&1; then
  systemctl --user restart "${SERVICE_NAME}.service"
else
  pkill -f "paperclipai run" >/dev/null 2>&1 || true
  nohup npx paperclipai run > "$LOG_FILE" 2>&1 &
fi

for _ in $(seq 1 20); do
  if healthcheck; then
    echo "Paperclip restarted successfully"
    exit 0
  fi
  sleep 1
done

echo "Paperclip restart attempted, but health check is still failing"
exit 1
