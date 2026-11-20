# AGENTS.md

C++20 library `durations`: `durations::parse_duration("1h30m")` → seconds.
Header in `include/durations/`, code in `src/`, tests (doctest) in `tests/`. Build: CMake + ctest.
Tools: CMake ≥ 3.20, GCC or Clang with C++20, clang-format 19.1.7, clang-tidy 19.1.

## Commands
- Configure + build: `cmake -S . -B build && cmake --build build -j`
- Test all: `ctest --test-dir build --output-on-failure`
- Test one case: `./build/durations_tests -tc="<test case name>"`
- Format: `find include src tests -name '*.cpp' -o -name '*.hpp' | xargs clang-format -i`
- Static analysis: `clang-tidy -p build src/*.cpp tests/*.cpp`
- **Done means: `bash scripts/verify.sh` prints `verify: OK`.** Paste its last lines in your summary.

## Boundaries
- Always: add or update a `TEST_CASE` in `tests/` for every behaviour change; run `scripts/verify.sh`.
- Ask first: adding a dependency; changing the public header `include/durations/parse.hpp`
  beyond what the task needs.
- Never: edit `.github/`, `scripts/`, `third_party/`, `CMakeLists.txt`, `.clang-format`,
  `.clang-tidy`, `.pre-commit-config.yaml` or `.claude/settings.json` (a hook blocks it);
  add `NOLINT`, `#pragma` warning suppressions or turn off `-Werror`; weaken or delete tests.

## Non-obvious conventions
- Errors are `durations::DurationError` (an `std::invalid_argument`); never return -1 or 0 for errors.
- Units must appear in descending order, each at most once (`1m1h` is invalid).
- Overflow of `std::int64_t` is an error, not wrap-around.

## Gotchas
- clang-tidy prints "N warnings generated" for system headers; that is not a failure.
  Only lines with `error:` fail the build.
