#!/usr/bin/env bash
# The one command an agent (or a human) must pass before saying "done".
# CI runs exactly this script, so "green locally" means "green in CI".
set -euo pipefail
cd "$(dirname "$0")/.."

step() { printf '\n==> %s\n' "$*"; }
# find, not git ls-files: new files the agent has not staged yet are checked too.
SOURCES=$(find include src tests -name '*.c' -o -name '*.h' | sort)

step "format (clang-format --dry-run --Werror)"
# shellcheck disable=SC2086
clang-format --dry-run --Werror $SOURCES

step "configure + build (cmake, C17, -Werror -Wconversion)"
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug > /dev/null
cmake --build build -j

step "static analysis (clang-tidy, warnings are errors)"
# shellcheck disable=SC2086
clang-tidy -p build --quiet $(find src tests -name '*.c' | sort)

step "tests (ctest)"
ctest --test-dir build --output-on-failure

step "skill copies in sync (.agents/skills == .claude/skills)"
diff -r .agents/skills .claude/skills

printf '\nverify: OK\n'
