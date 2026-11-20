#!/usr/bin/env bash
# The one command an agent (or a human) must pass before saying "done".
# CI runs exactly this script, so "green locally" means "green in CI".
set -euo pipefail
cd "$(dirname "$0")/.."

step() { printf '\n==> %s\n' "$*"; }

if [[ ! -d node_modules ]]; then
  step "install deps (npm ci)"
  npm ci --no-audit --no-fund
fi

step "format (prettier --check)"
npx --no-install prettier --check .

step "lint (eslint)"
npx --no-install eslint --max-warnings=0 .

step "types (tsc --noEmit)"
npx --no-install tsc --noEmit

step "tests (vitest run)"
npx --no-install vitest run

step "build (tsc -p tsconfig.build.json)"
npx --no-install tsc -p tsconfig.build.json

step "skill copies in sync (.agents/skills == .claude/skills)"
diff -r .agents/skills .claude/skills

printf '\nverify: OK\n'
