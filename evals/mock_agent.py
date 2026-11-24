#!/usr/bin/env python3
"""Offline stand-in for a coding agent, so the eval harness runs in CI without a model key.

It runs inside the workspace copy (cwd) and applies one of the prepared edit sets
in evals/bank/<task>/: "good" with probability p_good from evals/profiles.json,
otherwise "bad" (a plausible wrong change) or nothing if there is no bad.json.
The draw is seeded by (seed, task, trial), so a run is reproducible. Profiles
with "cheat": true also edit scripts/verify.sh when they fail, which the
harness must report as a process violation. The probabilities are made up for
the demo and say nothing about any real model.

Prints {"tokens": N} as its last line; a real agent wrapper can do the same.
"""

from __future__ import annotations

import json
import os
import random
from pathlib import Path

EVALS = Path(__file__).resolve().parent


def apply(edits: list[dict]) -> None:
    for e in edits:
        path = Path(e["file"])
        text = path.read_text(encoding="utf-8")
        if e["find"] not in text:
            raise SystemExit(f"mock agent: {e['find']!r} not found in {path}")
        path.write_text(text.replace(e["find"], e["replace"], 1), encoding="utf-8")


def main() -> int:
    task, trial = os.environ["EVAL_TASK_ID"], os.environ["EVAL_TRIAL"]
    seed, name = os.environ.get("EVAL_SEED", "0"), os.environ.get("EVAL_PROFILE", "honest")
    profile = json.loads((EVALS / "profiles.json").read_text(encoding="utf-8"))[name]
    rng = random.Random(f"{seed}:{task}:{trial}")
    good = rng.random() < profile["p_good"][task]
    bank = EVALS / "bank" / task
    variant = "good" if good else ("bad" if (bank / "bad.json").exists() else None)
    if variant:
        apply(json.loads((bank / f"{variant}.json").read_text(encoding="utf-8")))
    if not good and profile.get("cheat"):
        verify = Path("scripts/verify.sh")
        verify.write_text(
            verify.read_text(encoding="utf-8").replace(
                "step() {", 'printf "verify: OK\\n"; exit 0\nstep() {', 1
            ),
            encoding="utf-8",
        )
    tokens = int(profile["tokens_base"] * (0.8 + 0.4 * rng.random()))
    print(json.dumps({"variant": variant or "none", "tokens": tokens}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
