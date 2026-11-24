#!/usr/bin/env bash
# PreToolUse hook: block edits to files the agent must not change.
# Claude Code passes the tool call as JSON on stdin; exit code 2 blocks the
# call and the stderr text is shown to the agent.
# Test it by hand:
#   echo '{"tool_input":{"file_path":"scripts/verify.sh"}}' | scripts/guard-protected.sh
set -euo pipefail

PROTECTED_REGEX='(^|/)(\.github/|scripts/|evals/|third_party/|\.pre-commit-config\.yaml$|\.claude/settings\.json$|\.clang-(format|tidy)$|CMakeLists\.txt$)'

input=$(cat)
path=$(printf '%s' "$input" | sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -n 1)

if [[ -n "$path" ]] && [[ "$path" =~ $PROTECTED_REGEX ]]; then
  echo "blocked: $path is protected (CI, checks, dependency and tool config). Ask a human to change it." >&2
  exit 2
fi
exit 0
