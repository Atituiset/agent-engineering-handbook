#!/usr/bin/env bash
# Stop hook: before the agent may say "done", scripts/verify.sh must pass.
# Exit code 2 sends the failure back to the agent so it keeps working.
# stop_hook_active=true means we already blocked once in this turn: let it
# stop to avoid an endless loop (the failure is still visible to the human).
set -uo pipefail
cd "$(dirname "$0")/.."

input=$(cat)
if printf '%s' "$input" | grep -q '"stop_hook_active"[[:space:]]*:[[:space:]]*true'; then
  exit 0
fi

if ! out=$(bash scripts/verify.sh 2>&1); then
  printf '%s\n' "$out" | tail -n 40 >&2
  echo "scripts/verify.sh failed: fix the problems above before finishing." >&2
  exit 2
fi
exit 0
