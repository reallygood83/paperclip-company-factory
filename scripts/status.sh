#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SERVICE_NAME="paperclip-company-factory-paperclip"

print_status() {
  printf '%-24s %s\n' "$1" "$2"
}

print_status "root" "$ROOT_DIR"

if curl -fsS http://127.0.0.1:3100/api/companies >/dev/null 2>&1; then
  print_status "paperclip_http" "up"
else
  print_status "paperclip_http" "down"
fi

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

echo "dashboard               http://127.0.0.1:3100"
echo "factory_health_command  PYTHONPATH=src python3 -m paperclip_company_factory.cli health"
