import re
from pathlib import Path
H = Path(__file__).resolve().parent
A = H / "arxiv_submission"; A.mkdir(exist_ok=True)
md = (H / "AGENT_FAIRNESS_SURVEY.md").read_text(encoding="utf-8")
m = re.search(r"## Abstract\s+(.*?)\n## ", md, re.S)
abs = re.sub(r"\s+", " ", m.group(1)).strip() if m else "(see paper)"
abs = re.sub(r"\\cite[tp]?\{[^}]*\}", "", abs).replace("**", "").replace("*", "")
meta = f"""# arXiv submission metadata

**Title:** Fairness and Equity in LLM-Based Agents: A Taxonomic Survey
**Authors:** Rohith; Wenbin Zhang (Florida International University)
**Primary category:** cs.CY   **Cross-list:** cs.AI, cs.CL, cs.LG
**Comments:** ~35,000 words; 63 pp; 202 references; includes a small original pilot bias audit. Survey + original framework (Bias Conduction Framework) + pilot study.
**License:** CC BY 4.0 (recommended)
**Submit via:** Dr. Zhang's endorsed arXiv account (positions as survey + original results) once co-authorship + arXiv-first is confirmed.

## Source notes
- `main.tex` is self-contained: inline thebibliography (no .bib/.bbl needed), TikZ/forest Figure 1 (available in arXiv TeX Live). Compiles with pdflatex (two passes for refs).

## Abstract (paste into the arXiv form)

{abs}
"""
(A / "00_ARXIV_METADATA.md").write_text(meta, encoding="utf-8")
print(f"wrote arxiv metadata ({len(abs)} char abstract)")
