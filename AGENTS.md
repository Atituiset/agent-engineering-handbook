# AGENTS.md

C17 library `durations`: `durations_parse("1h30m", &secs)` → `DURATIONS_OK`, secs = 5400.
Header in `include/durations/`, code in `src/`, tests (Unity) in `tests/`. Build: CMake + ctest.
Tools: CMake ≥ 3.20, GCC or Clang, clang-format 19.1.7, clang-tidy 19.1.

## Commands
- Configure + build: `cmake -S . -B build && cmake --build build -j`
- Test all: `ctest --test-dir build --output-on-failure`
- Format: `find include src tests -name '*.c' -o -name '*.h' | xargs clang-format -i`
- Static analysis: `clang-tidy -p build src/*.c tests/*.c`
- **Done means: `bash scripts/verify.sh` prints `verify: OK`.** Paste its last lines in your summary.

## Boundaries
- Always: add or update a check in `tests/test_parse.c` for every behaviour change; run `scripts/verify.sh`.
- Ask first: adding a dependency; changing `include/durations/parse.h` beyond what the task needs.
- Never: edit `.github/`, `scripts/`, `third_party/`, `CMakeLists.txt`, `.clang-format`, any
  `.clang-tidy`, `.pre-commit-config.yaml` or `.claude/settings.json` (a hook blocks it);
  add `NOLINT` or `#pragma` warning suppressions; cast to silence `-Wconversion`; weaken tests.

## Non-obvious conventions
- Functions report errors via `durations_status`; `*out_seconds` is written only on success.
- `durations_parse` is `warn_unused_result`: always check the status.
- Units must appear in descending order, each at most once (`1m1h` is invalid).
- No magic numbers in `src/`: name constants in the `enum` at the top of `parse.c`
  (clang-tidy `readability-magic-numbers`; tests are exempt via `tests/.clang-tidy`).

## Gotchas
- clang-tidy prints "N warnings generated" for system headers; that is not a failure.
