# AGENTS.md

Rust library crate `durations`: `parse_duration("1h30m")` → `Ok(5400)` seconds.
Code in `src/lib.rs`, tests in `tests/parse.rs`. Toolchain pinned in `rust-toolchain.toml` (1.100.0).

## Commands
- Build: `cargo build --locked`
- Test all: `cargo test --locked`
- Test one: `cargo test --locked --test parse parses_valid_durations`
- Format: `cargo fmt --all`
- Lint: `cargo clippy --locked --all-targets -- -D warnings`
- **Done means: `bash scripts/verify.sh` prints `verify: OK`.** Paste its last lines in your summary.

## Boundaries
- Always: add or update a test in `tests/` for every behaviour change; run `scripts/verify.sh`.
- Ask first: adding a dependency; changing the public API (`parse_duration`, `DurationError`).
- Never: edit `.github/`, `scripts/`, `.pre-commit-config.yaml`, `.claude/settings.json`,
  `Cargo.toml`, `Cargo.lock` or `rust-toolchain.toml` (a hook blocks it); add `#[allow(...)]`
  or `#![allow(...)]` to silence a lint; use `unwrap()`/`expect()` in library code; use `unsafe`.

## Non-obvious conventions
- Errors are `DurationError`; never panic on bad input.
- Units must appear in descending order, each at most once (`1m1h` is invalid).
- Overflow is an error (`checked_*` arithmetic), never wrap-around or `as` casts.
- clippy runs the `pedantic` group (see `[lints]` in Cargo.toml); `as` casts that can truncate fail.
