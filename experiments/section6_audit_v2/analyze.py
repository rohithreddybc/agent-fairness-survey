#!/usr/bin/env python3
"""Analyze §6 audit v2: per-config CFR/MASD/advance-rate + 2x2 race/gender score
effects with bootstrap 95% CIs. Deterministic bootstrap (fixed seed)."""
import json, random
from pathlib import Path
from statistics import mean
H = Path(__file__).resolve().parent
raw = json.loads((H / "audit_v2_raw.json").read_text(encoding="utf-8"))["result"]["raw"]
random.seed(42)
CONDS = ["WM", "WF", "BM", "BF"]
configs = ["C0", "C2", "C3"]
pids = sorted({r["pid"] for r in raw})

def cell(cfg, pid, cond):
    for r in raw:
        if r["cfg"] == cfg and r["pid"] == pid and r["cond"] == cond:
            return r
    return None

def stats_for(cfg, sample_pids):
    advs = {c: [] for c in CONDS}; scores = {c: [] for c in CONDS}
    flips = 0; ranges = []
    for pid in sample_pids:
        cs = {c: cell(cfg, pid, c) for c in CONDS}
        if any(cs[c] is None or cs[c]["advance"] is None for c in CONDS):
            continue
        decs = [cs[c]["advance"] for c in CONDS]
        if len(set(decs)) > 1:
            flips += 1
        sc = [cs[c]["score"] for c in CONDS]
        ranges.append(max(sc) - min(sc))
        for c in CONDS:
            advs[c].append(1 if cs[c]["advance"] else 0)
            scores[c].append(cs[c]["score"])
    n = len(ranges)
    adv_rate = {c: mean(advs[c]) for c in CONDS}
    sc_mean = {c: mean(scores[c]) for c in CONDS}
    cfr = flips / n if n else 0
    masd = mean(ranges) if ranges else 0
    # 2x2 effects on score (positive = advantage to first group)
    race_gap = (sc_mean["WM"] + sc_mean["WF"]) / 2 - (sc_mean["BM"] + sc_mean["BF"]) / 2
    gender_gap = (sc_mean["WM"] + sc_mean["BM"]) / 2 - (sc_mean["WF"] + sc_mean["BF"]) / 2
    # advance-rate disparity (max-min across conds)
    adv_disp = max(adv_rate.values()) - min(adv_rate.values())
    return dict(n=n, cfr=cfr, masd=masd, adv_rate=adv_rate, sc_mean=sc_mean,
                race_gap=race_gap, gender_gap=gender_gap, adv_disp=adv_disp)

def boot_ci(cfg, key, B=3000):
    vals = []
    for _ in range(B):
        s = [random.choice(pids) for _ in pids]
        vals.append(stats_for(cfg, s)[key])
    vals.sort()
    return vals[int(0.025 * B)], vals[int(0.975 * B)]

print("config | n | CFR | MASD | adv-disp | race_gap(score) | gender_gap(score)")
out = {}
for cfg in configs:
    s = stats_for(cfg, pids)
    rci = boot_ci(cfg, "race_gap"); gci = boot_ci(cfg, "gender_gap"); mci = boot_ci(cfg, "masd")
    out[cfg] = dict(s=s, masd_ci=mci, race_ci=rci, gender_ci=gci)
    print(f"{cfg} | {s['n']} | {s['cfr']:.2f} | {s['masd']:.2f} [{mci[0]:.1f},{mci[1]:.1f}] | {s['adv_disp']:.2f} | "
          f"{s['race_gap']:+.2f} [{rci[0]:+.1f},{rci[1]:+.1f}] | {s['gender_gap']:+.2f} [{gci[0]:+.1f},{gci[1]:+.1f}]")
print()
for cfg in configs:
    s = out[cfg]["s"]
    print(f"{cfg} adv_rate:", {k: round(v, 2) for k, v in s['adv_rate'].items()},
          "score_mean:", {k: round(v, 1) for k, v in s['sc_mean'].items()})
# tier split: borderline only (where decisions can vary)
print("\nBorderline-only advance rates by config/cond:")
bpids = [p for p in pids if p.startswith("b")]
for cfg in configs:
    s = stats_for(cfg, bpids)
    print(f"  {cfg}: CFR={s['cfr']:.2f} adv={ {k:round(v,2) for k,v in s['adv_rate'].items()} } adv_disp={s['adv_disp']:.2f}")
(H / "analysis_summary.json").write_text(json.dumps({c: {"masd": out[c]["s"]["masd"], "masd_ci": out[c]["masd_ci"],
    "cfr": out[c]["s"]["cfr"], "adv_disp": out[c]["s"]["adv_disp"], "race_gap": out[c]["s"]["race_gap"],
    "race_ci": out[c]["race_ci"], "gender_gap": out[c]["s"]["gender_gap"], "gender_ci": out[c]["gender_ci"],
    "adv_rate": out[c]["s"]["adv_rate"]} for c in configs}, indent=2), encoding="utf-8")
print("\nwrote analysis_summary.json")
