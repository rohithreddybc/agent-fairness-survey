#!/usr/bin/env python3
"""Reassemble the humanized manuscript from the 5 chunk outputs.
Chunks partition the file at known section headers; we trim each chunk to its
exact [from,to) boundary, concatenate in order, and GUARD (abort if any required
header is missing/duplicated or citations drop). Usage:
  python splice_humanized.py <workflow-output.json>"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

H = Path(__file__).resolve().parent
F = H / "AGENT_FAIRNESS_SURVEY.md"
orig = F.read_text(encoding="utf-8")
out = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
chunks = {c["key"]: c for c in out["result"]}
ORDER = ["A_front", "B_sec3", "C_sec45", "D_sec67", "E_sec89"]
TITLE = "# Fairness and Equity"

def trim(md, frm, to):
    start_key = TITLE if frm == "<<START>>" else frm
    i = md.find(start_key)
    if i != -1:
        md = md[i:]
    if to != "<<END>>":
        j = md.find(to)
        if j != -1:
            md = md[:j]
    return md.strip()

pieces = []
for k in ORDER:
    c = chunks[k]
    pieces.append(trim(c["md"], c["from"], c["to"]))
new = "\n\n".join(pieces) + "\n"

# ---- GUARDS ----
def count(pat, s):
    return len(re.findall(pat, s, re.M))
required = [r"^# Fairness and Equity", r"^## 1\. Introduction", r"^## 2\. Background",
           r"^## 3\. The Bias Conduction", r"^## 4\. How to Evaluate", r"^## 5\. How to Mitigate",
           r"^## 6\. Empirical Study", r"^## 7\. Coverage", r"^## 8\. Open Problems",
           r"^## 9\. Conclusion", r"^## 9\.1"]
problems = []
for r in required:
    n = count(r, new)
    if n != 1:
        problems.append(f"header {r!r} appears {n}x (want 1)")

bib = set(re.findall(r"@\w+\{([^,]+),", (H / "references.bib").read_text(encoding="utf-8")))
def cites(s):
    return set(x.strip() for g in re.findall(r"\\cite[tp]?\{([^}]+)\}", s) for x in g.split(","))
orig_c, new_c = cites(orig), cites(new)
dropped = sorted(orig_c - new_c)
missing = sorted(new_c - bib)
ow, nw = len(re.findall(r"\w+", orig)), len(re.findall(r"\w+", new))
emn = new.count("—") + new.count("–")
if dropped: problems.append(f"DROPPED {len(dropped)} cite keys: {dropped[:12]}")
if missing: problems.append(f"MISSING-from-bib cites: {missing[:12]}")
if nw < ow * 0.85: problems.append(f"word count dropped {ow}->{nw} (>15%)")
if emn: problems.append(f"{emn} em/en dashes reintroduced")

if problems:
    print("ABORT — not written. Problems:")
    for p in problems: print("  -", p)
    sys.exit(1)
F.write_text(new, encoding="utf-8")
print(f"OK: humanized draft written. words {ow}->{nw}, cites {len(new_c)} (0 dropped, 0 missing), em/en dashes {emn}")
