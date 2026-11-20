#!/usr/bin/env bash
# The one command an agent (or a human) must pass before saying "done".
# CI runs exactly this script, so "green locally" means "green in CI".
# Maven is pinned by the wrapper (.mvn/wrapper/maven-wrapper.properties);
# every plugin and tool version is pinned in pom.xml.
set -euo pipefail
cd "$(dirname "$0")/.."

step() { printf '\n==> %s\n' "$*"; }
# Run a Maven goal; on failure show only its WARNING/ERROR lines (with -q,
# Maven would hide the compiler warnings that -Werror turned into errors).
mvn_step() {
  local out
  if ! out=$(./mvnw -B -ntp "$@" 2>&1); then
    printf '%s\n' "$out" | grep -E '^\[(WARNING|ERROR)\]' | grep -vE 'Re-run Maven|For more information|Help 1|full stack trace|^\[ERROR\] *$'
    return 1
  fi
}

step "format (spotless:check, google-java-format)"
mvn_step spotless:check

step "compile (javac -Xlint:all -Werror + Error Prone)"
mvn_step test-compile

step "tests (JUnit 5 via surefire)"
mvn_step verify
total=0
for n in $(grep -ho ' tests="[0-9]*"' target/surefire-reports/TEST-*.xml | grep -o '[0-9]*'); do total=$((total + n)); done
echo "tests passed: $total"

step "skill copies in sync (.agents/skills == .claude/skills)"
diff -r .agents/skills .claude/skills

printf '\nverify: OK\n'
