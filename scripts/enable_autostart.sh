#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SERVICE_NAME="paperclip-company-factory-paperclip"
LOG_DIR="$ROOT_DIR/.service-logs"
mkdir -p "$LOG_DIR"

if [[ "$(uname -s)" == "Darwin" ]]; then
  PLIST="$HOME/Library/LaunchAgents/${SERVICE_NAME}.plist"
  cat > "$PLIST" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>Label</key>
    <string>${SERVICE_NAME}</string>
    <key>ProgramArguments</key>
    <array>
      <string>/bin/bash</string>
      <string>-lc</string>
      <string>cd \"${ROOT_DIR}\" && exec npx paperclipai run</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>WorkingDirectory</key>
    <string>${ROOT_DIR}</string>
    <key>StandardOutPath</key>
    <string>${LOG_DIR}/paperclip.out.log</string>
    <key>StandardErrorPath</key>
    <string>${LOG_DIR}/paperclip.err.log</string>
  </dict>
</plist>
PLIST
  launchctl unload "$PLIST" >/dev/null 2>&1 || true
  launchctl load "$PLIST"
  echo "Autostart enabled via launchd: $PLIST"
elif [[ "$(uname -s)" == "Linux" ]]; then
  UNIT_DIR="$HOME/.config/systemd/user"
  UNIT_FILE="$UNIT_DIR/${SERVICE_NAME}.service"
  mkdir -p "$UNIT_DIR"
  cat > "$UNIT_FILE" <<UNIT
[Unit]
Description=Paperclip Company Factory Paperclip Service
After=network.target

[Service]
Type=simple
WorkingDirectory=${ROOT_DIR}
ExecStart=/bin/bash -lc 'cd "${ROOT_DIR}" && exec npx paperclipai run'
Restart=always
RestartSec=5
StandardOutput=append:${LOG_DIR}/paperclip.out.log
StandardError=append:${LOG_DIR}/paperclip.err.log

[Install]
WantedBy=default.target
UNIT
  systemctl --user daemon-reload
  systemctl --user enable --now "${SERVICE_NAME}.service"
  echo "Autostart enabled via systemd user service: $UNIT_FILE"
else
  echo "Unsupported OS for autostart: $(uname -s)"
  exit 1
fi
