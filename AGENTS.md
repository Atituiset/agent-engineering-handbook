# AGENTS.md

Python 3.12 library `durations`: parse strings like `1h30m` into seconds.
Code in `src/durations/`, tests in `tests/`. Package manager: uv.

## Commands
- Install: `uv sync --frozen`
- Test all: `uv run --frozen pytest -q`
- Test one: `uv run --frozen pytest -q tests/test_parse.py -k <name>`
- Format: `uv run --frozen ruff format .`
- Lint (autofix): `uv run --frozen ruff check --fix .`
- Types: `uv run --frozen mypy`
- **Done means: `bash scripts/verify.sh` prints `verify: OK`.** Paste its last lines in your summary.

## Boundaries
- Always: add or update a test in `tests/` for every behaviour change; run `scripts/verify.sh`.
- Ask first: adding a dependency; changing the public API in `src/durations/__init__.py`.
- Never: edit `.github/`, `scripts/`, `.pre-commit-config.yaml`, `.claude/settings.json`,
  `pyproject.toml` or `uv.lock` (a hook blocks it); weaken or delete tests to make them pass;
  add `# type: ignore` or `# noqa` without a reason in the same line; commit secrets.
- `evals/` holds the eval harness and its hidden tests: never edit it (the hook blocks it)
  and do not read it to solve a task; evals run you in a copy without it.

## Non-obvious conventions
- Errors are `DurationError` (a `ValueError`), never bare `ValueError` or `None`.
- Units must appear in descending order, each at most once (`1m1h` is invalid).
- mypy runs with `--strict`: every function needs full type hints, tests included.

## Gotchas
- Use `uv run --frozen ...`, not a global `pytest`/`ruff`: versions are pinned in `uv.lock`.
