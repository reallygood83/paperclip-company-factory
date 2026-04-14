#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
LINES="${1:-80}"
LOG_FILE="$ROOT_DIR/.paperclip-company-factory.paperclip.log"
SERVICE_LOG_DIR="$ROOT_DIR/.service-logs"

echo '=== paperclip-company-factory logs ==='
if [[ -f "$LOG_FILE" ]]; then
  echo "-- background log: $LOG_FILE --"
  tail -n "$LINES" "$LOG_FILE"
else
  echo "No background log file found at $LOG_FILE"
fi

if [[ -d "$SERVICE_LOG_DIR" ]]; then
  for file in "$SERVICE_LOG_DIR"/*.log; do
    [[ -e "$file" ]] || continue
    echo "-- service log: $file --"
    tail -n "$LINES" "$file"
  done
fi
