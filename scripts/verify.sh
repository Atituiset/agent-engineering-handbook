#!/usr/bin/env bash
# The one command an agent (or a human) must pass before saying "done".
# CI runs exactly this script, so "green locally" means "green in CI".
set -euo pipefail
cd "$(dirname "$0")/.."

step() { printf '\n==> %s\n' "$*"; }

step "sync deps (uv sync --frozen)"
uv sync --frozen --quiet

step "format (ruff format --check)"
uv run --frozen ruff format --check .

step "lint (ruff check)"
uv run --frozen ruff check .

step "types (mypy --strict)"
uv run --frozen mypy

step "tests (pytest)"
uv run --frozen pytest -q

step "skill copies in sync (.agents/skills == .claude/skills)"
diff -r .agents/skills .claude/skills

printf '\nverify: OK\n'
