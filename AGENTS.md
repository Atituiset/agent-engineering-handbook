# AGENTS.md

TypeScript (Node ≥ 20, ESM) library: `parseDuration("1h30m")` → seconds.
Code in `src/`, tests in `test/`. Package manager: npm (lockfile committed).

## Commands

- Install: `npm ci`
- Test all: `npm test`
- Test one: `npx vitest run test/parse.test.ts -t "<name>"`
- Format: `npm run format`
- Lint: `npm run lint`
- Types: `npm run typecheck`
- **Done means: `bash scripts/verify.sh` prints `verify: OK`.** Paste its last lines in your summary.

## Boundaries

- Always: add or update a test in `test/` for every behaviour change; run `scripts/verify.sh`.
- Ask first: adding a dependency; changing exports in `src/index.ts`.
- Never: edit `.github/`, `scripts/`, `.pre-commit-config.yaml`, `.claude/settings.json`,
  `eslint.config.js`, `tsconfig*.json`, `package.json` or `package-lock.json` (a hook blocks it);
  weaken or delete tests to make them pass; use `any`, `as` casts or `eslint-disable` /
  `@ts-expect-error` to silence a check; commit secrets.

## Non-obvious conventions

- Relative imports end in `.js` (ESM + `nodenext`), e.g. `import { x } from "./parse.js"`.
- Errors are `DurationError`, never a plain `Error`, `null` or `NaN`.
- Units must appear in descending order, each at most once (`1m1h` is invalid).
- `noUncheckedIndexedAccess` is on: array/regex lookups are `T | undefined`, handle it.

## Gotchas

- Use `npx --no-install ...` or the npm scripts, not globally installed tools.
