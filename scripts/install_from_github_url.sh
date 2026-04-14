#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <github_repo_url> [target_dir] [installer args...]"
  echo "Example: $0 https://github.com/reallygood83/paperclip-company-factory --enable-autostart"
  exit 1
fi

REPO_URL="$1"
shift
TARGET_DIR=""
EXTRA_ARGS=()

if [[ $# -gt 0 && ! "$1" =~ ^-- ]]; then
  TARGET_DIR="$1"
  shift
fi

while [[ $# -gt 0 ]]; do
  EXTRA_ARGS+=("$1")
  shift
done

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || {
    echo "Missing required command: $1"
    exit 1
  }
}

repo_basename() {
  local url="$1"
  url="${url%.git}"
  basename "$url"
}

require_cmd git
require_cmd bash
require_cmd curl

if [[ -z "$TARGET_DIR" ]]; then
  TARGET_DIR="$(pwd)/$(repo_basename "$REPO_URL")"
fi

if [[ -d "$TARGET_DIR/.git" ]]; then
  echo "Updating existing repository in $TARGET_DIR"
  git -C "$TARGET_DIR" pull --ff-only
else
  echo "Cloning $REPO_URL into $TARGET_DIR"
  git clone "$REPO_URL" "$TARGET_DIR"
fi

cd "$TARGET_DIR"

echo "Running one-click installer..."
./scripts/one_click_install.sh "${EXTRA_ARGS[@]}"

echo "Done. Next useful commands:"
echo "  cd $TARGET_DIR"
echo "  ./scripts/status.sh"
echo "  python3 scripts/first_run_wizard.py"
echo "  PYTHONPATH=src python3 -m paperclip_company_factory.cli bootstrap-from-prompt "Create a public AI content studio company for newsletters" --dry-run --format text"
