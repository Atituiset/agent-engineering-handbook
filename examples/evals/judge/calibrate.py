#!/usr/bin/env python3
"""LLM 裁判校准：拿裁判的判定和人工标签比，算一致性指标；比较两个裁判版本；检查位置偏差。

    python judge/calibrate.py --labels judge/data/labels.csv --judge judge_v1 \
        --compare judge_v2 --pairwise judge/data/pairwise.csv --min-kappa 0.6 --min-fail-recall 0.7

为什么不只看「一致率」：如果只有 5% 的样本是失败，一个永远判「通过」的裁判也有 95% 一致率，
却一个失败都抓不到。所以同时报 Cohen's kappa（扣掉碰巧一致）、失败类的召回率与精确率。
阈值是示例值，按你们能接受的漏报/误报来定。只依赖标准库。
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter

POS = "fail"  # 我们关心的是裁判能不能抓到失败，所以把 fail 当正类


def confusion(human: list[str], judge: list[str]) -> Counter:
    return Counter((h, j) for h, j in zip(human, judge))


def cohen_kappa(human: list[str], judge: list[str]) -> float:
    n = len(human)
    labels = sorted(set(human) | set(judge))
    po = sum(h == j for h, j in zip(human, judge)) / n
    hc, jc = Counter(human), Counter(judge)
    pe = sum(hc[l] * jc[l] for l in labels) / (n * n)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def report(name: str, human: list[str], judge: list[str]) -> dict:
    cm = confusion(human, judge)
    tp, fn = cm[(POS, POS)], cm[(POS, "pass")]
    fp, tn = cm[("pass", POS)], cm[("pass", "pass")]
    res = {
        "judge": name,
        "agreement": (tp + tn) / len(human),
        "kappa": cohen_kappa(human, judge),
        "fail_recall": tp / (tp + fn) if tp + fn else float("nan"),
        "fail_precision": tp / (tp + fp) if tp + fp else float("nan"),
        "pass_recall": tn / (tn + fp) if tn + fp else float("nan"),
        "confusion": {"tp": tp, "fn": fn, "fp": fp, "tn": tn},
    }
    print(f"[{name}] agreement={res['agreement']:.3f} kappa={res['kappa']:.3f} "
          f"fail_recall={res['fail_recall']:.3f} fail_precision={res['fail_precision']:.3f} "
          f"pass_recall={res['pass_recall']:.3f} confusion={res['confusion']}")
    return res


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--labels", required=True)
    ap.add_argument("--judge", required=True, help="要上线/在用的裁判列名")
    ap.add_argument("--compare", help="另一个裁判版本的列名（例如升级后的模型）")
    ap.add_argument("--pairwise", help="两两比较的换位结果 CSV")
    ap.add_argument("--min-kappa", type=float, default=0.6)
    ap.add_argument("--min-fail-recall", type=float, default=0.7)
    args = ap.parse_args()

    rows = list(csv.DictReader(open(args.labels, encoding="utf-8")))
    human = [r["human"] for r in rows]
    print(f"{len(rows)} labelled cases, {human.count(POS)} human-labelled failures")
    report("always_pass (dumb baseline)", human, ["pass"] * len(human))
    main_res = report(args.judge, human, [r[args.judge] for r in rows])

    failed = []
    if main_res["kappa"] < args.min_kappa:
        failed.append(f"{args.judge} kappa {main_res['kappa']:.3f} < {args.min_kappa}")
    if main_res["fail_recall"] < args.min_fail_recall:
        failed.append(f"{args.judge} fail_recall {main_res['fail_recall']:.3f} < {args.min_fail_recall}")

    if args.compare:
        new_res = report(args.compare, human, [r[args.compare] for r in rows])
        flips = sum(r[args.judge] != r[args.compare] for r in rows)
        print(f"[drift] {args.judge} -> {args.compare}: verdict flips {flips}/{len(rows)} "
              f"({flips / len(rows):.1%}); kappa {main_res['kappa']:.3f} -> {new_res['kappa']:.3f}")
        if new_res["kappa"] < args.min_kappa or new_res["fail_recall"] < args.min_fail_recall:
            print(f"[drift] {args.compare} would NOT pass calibration; keep {args.judge} pinned or re-label")

    if args.pairwise:
        prs = list(csv.DictReader(open(args.pairwise, encoding="utf-8")))
        inconsistent = [p for p in prs if p["winner_order_ab"] != p["winner_order_ba"]]
        first_slot = sum(1 for p in inconsistent if p["winner_order_ab"] == "A" and p["winner_order_ba"] == "B")
        print(f"[position] consistent after swap: {len(prs) - len(inconsistent)}/{len(prs)}; "
              f"inconsistent pairs favouring whichever answer came first: {first_slot}/{len(inconsistent)} "
              "-> count a win only if it holds in both orders")

    if failed:
        print("CALIBRATION GATE FAILED: " + "; ".join(failed))
        return 1
    print("calibration gate passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
