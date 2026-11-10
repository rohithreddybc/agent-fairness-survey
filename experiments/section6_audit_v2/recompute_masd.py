#!/usr/bin/env python3
"""Recompute the score-level disparity for the §4.5 audit under BOTH statistics.

Note (2026-11-09): the paragraph below describes an earlier analyze.py. The current analyze.py
reports both the pairwise MASD (the quantity in the paper) and the per-profile score range, so this
script is now a cross-check rather than a correction.

analyze.py reports, under the name MASD, the per-profile score RANGE
(max minus min across the four name conditions). Definition 4.2 of the paper, and
the MASD of Mayilvaghanan et al., is the mean absolute PAIRWISE difference. The two
are not the same quantity and the range is the larger of them by construction.

This script reports both, with the same bootstrap as analyze.py (3000 resamples of
profiles, seed 42), so the manuscript can state the quantity it actually defines.
"""
import json, itertools, random
from pathlib import Path
from statistics import mean

H = Path(__file__).resolve().parent
raw = json.loads((H / "audit_v2_raw.json").read_text(encoding="utf-8"))["result"]["raw"]

CONDS = ["WM", "WF", "BM", "BF"]
SINGLE = [("WM", "BM"), ("WF", "BF"), ("WM", "WF"), ("BM", "BF")]
CONFIGS = [("C0", "A0"), ("C2", "A1"), ("C3", "A2")]
pids = sorted({r["pid"] for r in raw})
random.seed(42)

idx = {(r["cfg"], r["pid"], r["cond"]): r for r in raw}


def per_profile(cfg, pid):
    try:
        sc = {c: idx[(cfg, pid, c)]["score"] for c in CONDS}
    except KeyError:
        return None
    return {
        "range": max(sc.values()) - min(sc.values()),
        "masd_all": mean(abs(sc[a] - sc[b]) for a, b in itertools.combinations(CONDS, 2)),
        "masd_single": mean(abs(sc[a] - sc[b]) for a, b in SINGLE),
    }


def boot(cfg, key, n=3000):
    vals = [per_profile(cfg, p) for p in pids]
    vals = [v[key] for v in vals if v]
    point = mean(vals)
    draws = []
    for _ in range(n):
        s = [vals[random.randrange(len(vals))] for _ in vals]
        draws.append(mean(s))
    draws.sort()
    return point, draws[int(0.025 * n)], draws[int(0.975 * n)]


print("Config  statistic      point   95% CI")
rows = {}
for cfg, label in CONFIGS:
    rows[label] = {}
    for key, nice in [("range", "score range"),
                      ("masd_all", "MASD (all 6 pairs)"),
                      ("masd_single", "MASD (4 single-attr)")]:
        p, lo, hi = boot(cfg, key)
        rows[label][key] = (p, lo, hi)
        print("%-7s %-21s %5.1f   [%.1f, %.1f]" % (label, nice, p, lo, hi))
    print()

print("For the manuscript, MASD (all 6 pairs), rounded as the table does:")
for _, label in CONFIGS:
    p, lo, hi = rows[label]["masd_all"]
    print("  %s: %.1f [%.1f, %.1f]" % (label, p, lo, hi))

print()
print("Endpoint (advance-rate) disparity for comparison: 0.167, 0.167, 0.083")
print("i.e. 16.7, 16.7, 8.3 on the same 0-100 scale.")
