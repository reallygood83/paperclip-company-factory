#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

echo "[1/4] Checking prerequisites"
command -v node >/dev/null || { echo "node is required"; exit 1; }
command -v curl >/dev/null || { echo "curl is required"; exit 1; }

if ! command -v npx >/dev/null; then
  echo "npx is required"
  exit 1
fi

echo "[2/4] Installing Python dependencies"
python3 -m pip install -r "$ROOT_DIR/requirements.txt"

echo "[3/4] Starting Paperclip (manual step may be required depending on environment)"
echo "Run this in another terminal if Paperclip is not already running:"
echo "  npx paperclipai run"

echo "[4/4] Health check"
python3 -m paperclip_company_factory.cli health || true
