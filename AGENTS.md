# AGENTS.md

Go library `durations`: `ParseDuration("1h30m")` → seconds (`int64`).
Code in `durations.go`, tests in `durations_test.go`. Go ≥ 1.26 (CI uses 1.27.3).

## Commands
- Test all: `go test -race ./...`
- Test one: `go test -race -run 'TestParseDurationValid/1h30m' ./...`
- Format: `gofmt -w . && go tool goimports -w .`
- Vet + lint: `go vet ./... && go tool staticcheck ./...`
- **Done means: `bash scripts/verify.sh` prints `verify: OK`.** Paste its last lines in your summary.

## Boundaries
- Always: add or update a table-test case for every behaviour change; run `scripts/verify.sh`.
- Ask first: adding a dependency; changing the exported API (`ParseDuration`, `ErrInvalid`).
- Never: edit `.github/`, `scripts/`, `.pre-commit-config.yaml`, `.claude/settings.json`,
  `go.mod` or `go.sum` (a hook blocks it); add `//lint:ignore` or `//nolint` to silence a check;
  weaken or delete tests; ignore a returned error with `_`.
- `evals/` holds the eval harness and its hidden tests: never edit it (the hook blocks it)
  and do not read it to solve a task; evals run you in a copy without it.

## Non-obvious conventions
- Every error wraps `ErrInvalid` (`fmt.Errorf("%w: ...", ErrInvalid, ...)`); tests use `errors.Is`.
- Units must appear in descending order, each at most once (`1m1h` is invalid).
- Overflow of `int64` is an error, not wrap-around.

## Gotchas
- staticcheck and goimports are pinned in `go.mod` (`tool` block): run them with `go tool ...`,
  not a globally installed binary.
- `go test -race` needs cgo (a C compiler); without one, the race step fails to build.
