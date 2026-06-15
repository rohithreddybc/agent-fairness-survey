#!/usr/bin/env python3
"""
assemble.py — Phase 5: stitch the 9 section drafts into AGENT_FAIRNESS_SURVEY.md
and run the Phase-4 citation-integrity diff (every \\cite key must exist in
references.bib). Reads the drafting-workflow output JSON, strips any agent
preamble before the first markdown header, writes per-section files to drafts/,
the assembled draft, and CITE_AUDIT.md.
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DRAFTS = HERE / "drafts"; DRAFTS.mkdir(exist_ok=True)
OUT = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
SECTIONS = OUT["result"]

def clean(md: str) -> str:
    # drop any preamble before the first '##' header (agents sometimes narrate)
    i = md.find("\n## ")
    if i == -1 and md.lstrip().startswith("## "):
        return md.strip() + "\n"
    if i != -1:
        head = md[:i]
        # keep if the preamble itself is content (rare); else cut narration lines
        if re.search(r"(writing the section|i have (everything|the context)|here is|let me|i'?ll write|now i have)", head, re.I):
            md = md[i+1:]
    return md.strip() + "\n"

order = ["01_abstract_intro","02_background","03_taxonomy","04_evaluation",
         "05_mitigation","06_empirical","07_coverage","08_openproblems","09_conclusion"]
by_key = {s["key"]: clean(s["md"]) for s in SECTIONS}

for k in order:
    (DRAFTS / f"{k}.md").write_text(by_key[k], encoding="utf-8")

TITLE = """# Fairness and Equity in LLM-Based Agents: A Taxonomic Survey

*Rohith (first & corresponding) · Wenbin Zhang (FIU, senior author)*
*Target venue: ACM SIGKDD Explorations Newsletter · Draft v1 (assembled) · June 2026*

> Working draft assembled from per-section drafts in `drafts/`. Citations are LaTeX
> cite-commands keyed to `references.bib` (all keys audited — see `CITE_AUDIT.md`).
> Figures/tables specced in `FIGURES.md`. This is an arXiv-v1 (~70%) draft; the §6
> audit run and ACM-LaTeX port are the remaining gating items (`ARXIV_CHECKLIST.md`).

---

"""
assembled = TITLE + "\n\n---\n\n".join(by_key[k] for k in order)
(HERE / "AGENT_FAIRNESS_SURVEY.md").write_text(assembled, encoding="utf-8")

# ---- citation integrity ----
bibkeys = set(re.findall(r"@\w+\{([^,]+),", (HERE / "references.bib").read_text(encoding="utf-8")))
cited = re.findall(r"\\cite\{([^}]+)\}", assembled)
cited_keys = []
for grp in cited:
    cited_keys += [c.strip() for c in grp.split(",")]
cited_set = set(cited_keys)
missing = sorted(cited_set - bibkeys)          # cited but not in bib (PROBLEM)
uncited = sorted(bibkeys - cited_set)          # in bib but never cited (OK, just info)

from collections import Counter
freq = Counter(cited_keys)
audit = [f"# Citation audit — assembled draft\n",
         f"- distinct \\cite keys used: **{len(cited_set)}**",
         f"- total \\cite occurrences: **{len(cited_keys)}**",
         f"- bib entries: **{len(bibkeys)}**",
         f"- **MISSING (cited but not in references.bib): {len(missing)}**  <-- must be 0",
         f"- uncited bib entries (informational): {len(uncited)}\n"]
if missing:
    audit.append("## ⚠ MISSING KEYS (fix before submit)\n")
    for m in missing: audit.append(f"- `{m}`")
    audit.append("")
audit.append("## Uncited corpus entries (candidates to weave in or drop)\n")
for u in uncited: audit.append(f"- `{u}`")
audit.append("\n## Most-cited (sanity check)\n")
for k, n in freq.most_common(15):
    audit.append(f"- `{k}` ×{n}")
(HERE / "CITE_AUDIT.md").write_text("\n".join(audit), encoding="utf-8")

words = len(re.findall(r"\w+", assembled))
print(f"assembled: {words} words (~{words/550:.1f} double-col pages)")
print(f"distinct cites: {len(cited_set)} | MISSING: {len(missing)} | uncited bib: {len(uncited)}")
if missing:
    print("MISSING KEYS:", ", ".join(missing))
