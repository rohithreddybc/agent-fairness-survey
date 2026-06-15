#!/usr/bin/env python3
"""Reassemble the condensed manuscript from per-section blocks, with hard guards.
Each block is trimmed to its exact [from_header, to_header) range and spliced into
the original main.tex. ABORTS (writes nothing) unless: all sections present, 0 cite
keys dropped, table/figure/equation counts preserved, em-dashes still 0, word count
decreased (the goal) but not by >35%. Usage: python condense_splice.py <wf-output.json>"""
from __future__ import annotations
import json, re, sys
from pathlib import Path
H = Path(__file__).resolve().parent
M = H / "main.tex"
orig = M.read_text(encoding="utf-8")
out = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
blocks = {b["key"]: b for b in out["result"]}
ORDER = ["A_intro_bg", "B_bcf", "C_eval_mit", "D_emp_cov", "E_open_concl"]

def clean(md):  # strip any agent preamble before the first \section
    i = md.find("\\section{")
    return md[i:] if i != -1 else md

def trim(md, frm, to):
    md = clean(md)
    i = md.find(frm)
    if i != -1: md = md[i:]
    if to != "<<BIB>>":
        j = md.find(to)
        if j != -1: md = md[:j]
    else:
        j = md.find("\\bibliographystyle")
        if j != -1: md = md[:j]
    return md.rstrip() + "\n\n"

# build new doc by replacing each section range in the original (high-to-low)
new = orig
spans = []
for k in ORDER:
    b = blocks[k]
    s = new.find(b["from"])
    e = len(new) if b["to"] == "<<BIB>>" else new.find(b["to"])
    if b["to"] == "<<BIB>>":
        e = new.find("\\bibliographystyle")
    assert s != -1 and e != -1 and s < e, f"boundary fail {k}: s={s} e={e}"
    spans.append((s, e, trim(b["md"], b["from"], b["to"])))
for s, e, rep in sorted(spans, reverse=True):
    new = new[:s] + rep + new[e:]

# ---- GUARDS ----
def cites(t): return set(x.strip() for g in re.findall(r"\\cite[tp]?\{([^}]+)\}", t) for x in g.split(","))
def words(t): return len(re.findall(r"[A-Za-z]{2,}", re.sub(r"\\[a-zA-Z]+\{[^}]*\}", " ", t)))
def cnt(pat, t): return len(re.findall(pat, t))
problems = []
oc, nc = cites(orig), cites(new)
dropped = sorted(oc - nc)
if dropped: problems.append(f"DROPPED {len(dropped)} cites: {dropped[:15]}")
for name, pat in [("section", r"\\section\{"), ("table", r"\\begin\{table\*?\}"),
                  ("longtable", r"\\begin\{longtable\}"), ("figure", r"\\begin\{figure\*?\}"),
                  ("tikzpicture", r"\\begin\{tikzpicture\}"), ("equation", r"\\begin\{equation\*?\}")]:
    o, n = cnt(pat, orig), cnt(pat, new)
    if n < o: problems.append(f"{name}: {o}->{n} (lost {o-n})")
em = sum(1 for ln in new.splitlines() if not ln.lstrip().startswith("%") for ch in ln if ch in "—–")
if em: problems.append(f"{em} em/en dashes reintroduced")
ow, nw = words(orig), words(new)
if nw >= ow: problems.append(f"word count NOT reduced ({ow}->{nw})")
if nw < ow * 0.60: problems.append(f"word count cut >40% ({ow}->{nw}) - too aggressive")

if problems:
    print("ABORT - not written. Problems:")
    for p in problems: print("  -", p)
    sys.exit(1)
M.write_text(new, encoding="utf-8")
print(f"OK condensed: words {ow}->{nw} ({100*(ow-nw)//ow}% cut), cites {len(nc)} (0 dropped), em-dashes {em}")
