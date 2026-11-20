---
name: verify
description: Run the project's full verification (format, lint, type check, tests) and fix failures. Use after any code change and before reporting a task as done.
---

# Verify

1. Run `bash scripts/verify.sh` from the repository root.
2. If it prints `verify: OK`, report the last lines of its output and stop.
3. If a step fails, read the first error, fix the code (not the checks), and run it again.
   - Format: run the formatter named in the failing step, then re-run verify.
   - Lint or types: fix the reported line; do not add ignore comments to silence it.
   - Tests: decide whether the code or the test is wrong. Never delete or weaken a test
     just to make it pass; if the test is wrong, say why in your summary.
4. Do not edit `scripts/`, CI workflows or tool configuration to make verify pass.
   If you believe a check is wrong, stop and ask a human.
