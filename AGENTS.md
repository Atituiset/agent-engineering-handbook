# AGENTS.md

Java 21 library: `example.durations.Durations.parse("1h30m")` → `5400L` seconds.
Code in `src/main/java/`, tests (JUnit 5) in `src/test/java/`. Build: Maven via the wrapper `./mvnw`.

## Commands
- Build + test: `./mvnw -B verify`
- Test one: `./mvnw -B test -Dtest='DurationsTest#parsesValidDurations'`
- Format: `./mvnw -B spotless:apply`   (google-java-format)
- Compile only (javac -Xlint:all -Werror + Error Prone): `./mvnw -B test-compile`
- **Done means: `bash scripts/verify.sh` prints `verify: OK`.** Paste its last lines in your summary.

## Boundaries
- Always: add or update a case in `DurationsTest` for every behaviour change; run `scripts/verify.sh`.
- Ask first: adding a dependency; changing public signatures in `Durations` or `DurationException`.
- Never: edit `.github/`, `scripts/`, `.mvn/`, `mvnw*`, `pom.xml`, `.pre-commit-config.yaml` or
  `.claude/settings.json` (a hook blocks it); add `@SuppressWarnings` to silence a check;
  weaken, `@Disabled` or delete tests.
- `evals/` holds the eval harness and its hidden tests: never edit it (the hook blocks it)
  and do not read it to solve a task; evals run you in a copy without it.

## Non-obvious conventions
- Errors are `DurationException` (an `IllegalArgumentException`); never return -1 or null.
- Units must appear in descending order, each at most once (`1m1h` is invalid).
- Overflow is an error: use `Math.addExact` / `Math.multiplyExact`, not plain `+` / `*` or casts.

## Gotchas
- Use `./mvnw`, not a system `mvn`: the wrapper pins Maven 3.9.16.
- Error Prone needs the `--add-exports` lines in `.mvn/jvm.config` and JDK 21+.
