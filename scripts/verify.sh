#!/usr/bin/env bash
# The one command an agent (or a human) must pass before saying "done".
# CI runs exactly this script, so "green locally" means "green in CI".
set -euo pipefail
cd "$(dirname "$0")/.."

step() { printf '\n==> %s\n' "$*"; }

step "format (gofmt -l, go tool goimports -l)"
unformatted=$( { gofmt -l .; go tool goimports -l .; } | sort -u)
if [[ -n "$unformatted" ]]; then
  echo "not formatted (run: gofmt -w . && go tool goimports -w .):"
  echo "$unformatted"
  exit 1
fi

step "vet (go vet)"
go vet ./...

step "lint (go tool staticcheck)"
go tool staticcheck ./...

step "tests (go test -race)"
go test -race -count=1 ./...

step "skill copies in sync (.agents/skills == .claude/skills)"
diff -r .agents/skills .claude/skills

printf '\nverify: OK\n'
