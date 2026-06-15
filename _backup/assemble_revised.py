#!/usr/bin/env python3
"""Assemble the CSUR-revised draft from the 6 revision blocks; run the cite audit.
Usage: python assemble_revised.py <revision-workflow-output.json>"""
from __future__ import annotations
import json, re, sys
from pathlib import Path
from collections import Counter

HERE = Path(__file__).resolve().parent
D2 = HERE / "drafts_v2"; D2.mkdir(exist_ok=True)
OUT = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
BLOCKS = {b["key"]: b["md"] for b in OUT["result"]}
ORDER = ["01_front", "02_background", "03_taxonomy", "04_evaluation", "05_mitigation", "06_back"]

def clean(md: str) -> str:
    # If the block already begins with a markdown header, there is no narration
    # preamble to strip (guards against eating the first section — the §6 bug).
    if md.lstrip().startswith("#"):
        return md.strip() + "\n"
    # Otherwise, strip only a short leading narration run before the first header.
    i = md.find("\n## ")
    j = md.find("\n# ")
    cut = min([x for x in (i, j) if x != -1], default=-1)
    if cut != -1:
        head = md[:cut]
        if len(head) < 600 and re.search(
                r"(here is|here'?s|writing|i have|i'?ll|now i|below is|revised block|the revised)",
                head, re.I):
            md = md[cut + 1:]
    return md.strip() + "\n"

for k in ORDER:
    if k in BLOCKS:
        (D2 / f"{k}.md").write_text(clean(BLOCKS[k]), encoding="utf-8")

TITLE = """# Fairness and Equity in LLM-Based Agents: A Taxonomic Survey

**Rohith**  ·  **Wenbin Zhang** (Florida International University)

*Submitted to ACM Computing Surveys.*

---

"""
assembled = TITLE + "\n\n---\n\n".join(clean(BLOCKS[k]) for k in ORDER if k in BLOCKS)
(HERE / "AGENT_FAIRNESS_SURVEY.md").write_text(assembled, encoding="utf-8")

# cite audit
bibkeys = set(re.findall(r"@\w+\{([^,]+),", (HERE / "references.bib").read_text(encoding="utf-8")))
cited = []
for grp in re.findall(r"\\cite[tp]?\{([^}]+)\}", assembled):
    cited += [c.strip() for c in grp.split(",")]
cited_set = set(cited)
missing = sorted(cited_set - bibkeys)
uncited = sorted(bibkeys - cited_set)
freq = Counter(cited)
audit = [f"# Citation audit — CSUR revised draft\n",
         f"- distinct cite keys: **{len(cited_set)}** | occurrences: **{len(cited)}** | bib entries: **{len(bibkeys)}**",
         f"- **MISSING (cited but absent from references.bib): {len(missing)}**  <- must be 0",
         f"- uncited bib entries: {len(uncited)}\n"]
if missing:
    audit.append("## MISSING (fix)\n" + "\n".join(f"- `{m}`" for m in missing) + "\n")
audit.append("## Most-cited\n" + "\n".join(f"- `{k}` x{n}" for k, n in freq.most_common(20)))
audit.append("\n## Uncited bib entries\n" + "\n".join(f"- `{u}`" for u in uncited))
(HERE / "CITE_AUDIT.md").write_text("\n".join(audit), encoding="utf-8")

words = len(re.findall(r"\w+", assembled))
print(f"assembled CSUR draft: {words} words (~{words/650:.0f} double-col pp)")
print(f"distinct cites: {len(cited_set)} | MISSING: {len(missing)} | uncited: {len(uncited)}")
if missing: print("MISSING:", ", ".join(missing[:40]))
