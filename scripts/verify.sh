#!/usr/bin/env bash
# The one command an agent (or a human) must pass before saying "done".
# CI runs exactly this script, so "green locally" means "green in CI".
# The toolchain version comes from rust-toolchain.toml.
set -euo pipefail
cd "$(dirname "$0")/.."

step() { printf '\n==> %s\n' "$*"; }

step "format (cargo fmt --check)"
cargo fmt --all --check

step "lint + types (cargo clippy -D warnings)"
cargo clippy --locked --all-targets -- -D warnings

step "tests (cargo test)"
cargo test --locked --quiet

step "skill copies in sync (.agents/skills == .claude/skills)"
diff -r .agents/skills .claude/skills

printf '\nverify: OK\n'
