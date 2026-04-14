#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SERVICE_NAME="paperclip-company-factory-paperclip"
LOG_FILE="$ROOT_DIR/.paperclip-company-factory.paperclip.log"

print_status() {
  printf '%-24s %s
' "$1" "$2"
}

port_pid() {
  if command -v lsof >/dev/null 2>&1; then
    lsof -t -iTCP:3100 -sTCP:LISTEN 2>/dev/null | head -n 1 || true
  else
    echo "unknown (lsof not installed)"
  fi
}

print_status "root" "$ROOT_DIR"
PID="$(port_pid)"
if curl -fsS http://127.0.0.1:3100/api/companies >/dev/null 2>&1; then
  print_status "paperclip_http" "up"
else
  print_status "paperclip_http" "down"
fi
print_status "port_3100_pid" "${PID:-none}"

if [[ "$(uname -s)" == "Darwin" ]]; then
  if launchctl list | grep -q "$SERVICE_NAME"; then
    print_status "autostart" "launchd enabled"
  else
    print_status "autostart" "launchd not loaded"
  fi
elif [[ "$(uname -s)" == "Linux" ]]; then
  if systemctl --user is-enabled "${SERVICE_NAME}.service" >/dev/null 2>&1; then
    print_status "autostart" "systemd user enabled"
  else
    print_status "autostart" "systemd user disabled"
  fi
fi

print_status "dashboard" "http://127.0.0.1:3100"
print_status "background_log" "$LOG_FILE"
print_status "factory_health" "PYTHONPATH=src python3 -m paperclip_company_factory.cli health"
print_status "restart_command" "./scripts/restart.sh"
print_status "logs_command" "./scripts/logs.sh"
