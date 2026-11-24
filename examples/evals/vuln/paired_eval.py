#!/usr/bin/env python3
"""漏洞检测的配对评测：同一个函数的「漏洞版」和「修复版」成对打分，并给每个指标配一个笨基线。

    python vuln/paired_eval.py --pairs vuln/data/pairs.jsonl \
        --predictions vuln/data/model_predictions.jsonl --cutoff 2026-06-01

做法参考 Right Verdict, Right Reason?（arXiv 2611.28584）：
  - 主指标是 P-C（pair-wise correct）：漏洞版判有漏洞、修复版判没漏洞，两边都对才算；
  - 同时报 P-V（两边都判有漏洞）、P-R（判反了）和 MCC；
  - 每个指标都和笨基线比：「永远判有漏洞」和「看到危险函数名就判有漏洞」的关键词规则；
  - 按模型训练截止日期把样本分成前后两组分别统计，截止日期之后的那组更能说明泛化。
F1 为什么不够：在平衡的配对数据上，「永远判有漏洞」的 F1 是 0.67，P-C 却是 0。
data/ 里的 C 片段和预测都是为演示人工构造的玩具数据，不对应任何真实 CVE。只依赖标准库。
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys

RISKY = re.compile(r"\b(strcpy|strcat|sprintf|gets|memcpy|malloc|atoi)\s*\(")


def keyword_rule(code: str) -> str:
    return "vulnerable" if RISKY.search(code) else "benign"


def always_vulnerable(code: str) -> str:
    return "vulnerable"


def metrics(pairs: list[dict], verdicts: dict[str, tuple[str, str]]) -> dict:
    tp = fp = tn = fn = 0
    pc = pv = pr = pb = 0
    for p in pairs:
        v, f = verdicts[p["id"]]
        tp += v == "vulnerable"; fn += v != "vulnerable"
        fp += f == "vulnerable"; tn += f != "vulnerable"
        if v == "vulnerable" and f != "vulnerable":
            pc += 1
        elif v == "vulnerable" and f == "vulnerable":
            pv += 1
        elif v != "vulnerable" and f == "vulnerable":
            pr += 1
        else:
            pb += 1
    n = len(pairs)
    prec = tp / (tp + fp) if tp + fp else 0.0
    rec = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * prec * rec / (prec + rec) if prec + rec else 0.0
    denom = math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    mcc = (tp * tn - fp * fn) / denom if denom else 0.0
    share_vuln = (tp + fp) / (2 * n)
    return {"pairs": n, "F1": f1, "MCC": mcc, "P-C": pc / n, "P-V": pv / n, "P-R": pr / n, "P-B": pb / n,
            "chance_P-C": share_vuln * (1 - share_vuln)}


def show(name: str, m: dict) -> None:
    print(f"  {name:<22} F1={m['F1']:.3f} MCC={m['MCC']:+.3f} P-C={m['P-C']:.3f} "
          f"(chance {m['chance_P-C']:.3f}) P-V={m['P-V']:.3f} P-R={m['P-R']:.3f}  n={m['pairs']}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pairs", required=True)
    ap.add_argument("--predictions", required=True)
    ap.add_argument("--cutoff", required=True, help="被测模型的训练截止日期，YYYY-MM-DD")
    args = ap.parse_args()

    pairs = [json.loads(l) for l in open(args.pairs, encoding="utf-8") if l.strip()]
    preds = {}
    for l in open(args.predictions, encoding="utf-8"):
        if l.strip():
            d = json.loads(l)
            preds[d["id"]] = (d["vulnerable_verdict"], d["fixed_verdict"])
    detectors = {
        "always_vulnerable": {p["id"]: (always_vulnerable(p["vulnerable"]), always_vulnerable(p["fixed"])) for p in pairs},
        "keyword_rule": {p["id"]: (keyword_rule(p["vulnerable"]), keyword_rule(p["fixed"])) for p in pairs},
        "model": preds,
    }
    groups = {
        "all": pairs,
        f"before {args.cutoff}": [p for p in pairs if p["published"] < args.cutoff],
        f"after {args.cutoff}": [p for p in pairs if p["published"] >= args.cutoff],
    }
    results = {}
    for gname, gpairs in groups.items():
        if not gpairs:
            continue
        print(f"[{gname}]")
        for dname, verdicts in detectors.items():
            m = metrics(gpairs, verdicts)
            results[(gname, dname)] = m
            show(dname, m)
    base = results[("all", "always_vulnerable")]
    assert abs(base["F1"] - 2 / 3) < 1e-9 and base["P-C"] == 0.0, "sanity check: always-vulnerable must give F1=0.667, P-C=0"
    model, kw = results[("all", "model")], results[("all", "keyword_rule")]
    verdict = "beats" if model["P-C"] > max(kw["P-C"], model["chance_P-C"]) else "does NOT beat"
    print(f"\nmodel {verdict} the keyword rule and its chance level on P-C (all pairs)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
