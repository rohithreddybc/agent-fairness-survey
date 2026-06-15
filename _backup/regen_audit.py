import re
from pathlib import Path
H = Path(__file__).resolve().parent
md = (H / "AGENT_FAIRNESS_SURVEY.md").read_text(encoding="utf-8")
bib = set(re.findall(r"@\w+\{([^,]+),", (H / "references.bib").read_text(encoding="utf-8")))
cited = [k.strip() for g in re.findall(r"\\cite[tp]?\{([^}]+)\}", md) for k in g.split(",")]
cs = set(cited)
(H / "CITE_AUDIT.md").write_text(
    "# Citation audit (current)\n\n"
    f"- distinct cite keys: **{len(cs)}**\n"
    f"- total occurrences: **{len(cited)}**\n"
    f"- bib entries: **{len(bib)}**\n"
    f"- MISSING (cited but absent from references.bib): **{len(cs - bib)}**\n"
    f"- uncited bib entries: **{len(bib - cs)}**\n", encoding="utf-8")
print(f"CITE_AUDIT.md: {len(cs)} cited / {len(bib)} bib / {len(cs - bib)} missing")
