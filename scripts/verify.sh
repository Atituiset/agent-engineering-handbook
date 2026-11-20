#!/usr/bin/env bash
# The one command an agent (or a human) must pass before saying "done".
# CI runs exactly this script, so "green locally" means "green in CI".
# Maven is pinned by the wrapper (.mvn/wrapper/maven-wrapper.properties);
# every plugin and tool version is pinned in pom.xml.
set -euo pipefail
cd "$(dirname "$0")/.."

step() { printf '\n==> %s\n' "$*"; }
# Run a Maven goal through the wrapper. Quiet on success; on failure print
# everything the wrapper and Maven wrote, unfiltered. A filter would also hide
# errors that do not look like Maven's "[ERROR]" lines, e.g. the wrapper's
# "wget: Failed to fetch ..." when downloading Maven itself fails.
mvn_step() {
  local log rc=0
  log=$(mktemp)
  ./mvnw -B -ntp "$@" >"$log" 2>&1 || rc=$?
  if ((rc != 0)); then
    cat "$log"
    printf '\nverify: ./mvnw %s failed (exit %d); full output above\n' "$*" "$rc"
  fi
  rm -f "$log"
  return "$rc"
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
