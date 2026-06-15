import re
from pathlib import Path
H = Path(__file__).resolve().parent
md = (H / "AGENT_FAIRNESS_SURVEY.md").read_text(encoding="utf-8")
bib = set(re.findall(r"@\w+\{([^,]+),", (H / "references.bib").read_text(encoding="utf-8")))
cited = set()
for g in re.findall(r"\\cite[tp]?\{([^}]+)\}", md):
    for k in g.split(","):
        cited.add(k.strip())
print("distinct cites:", len(cited), "| missing:", sorted(cited - bib))
print("em/en dashes:", md.count("—") + md.count("–"))
print("words:", len(re.findall(r"\w+", md)))
