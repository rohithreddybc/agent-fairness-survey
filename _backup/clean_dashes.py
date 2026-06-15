#!/usr/bin/env python3
"""Final dash cleanup on the assembled draft: en-dash ranges -> hyphen; em-dash in
labels/headers -> colon; table empty-cells -> n/a; dual-em-dash parentheticals -> ();
remaining prose em-dash -> comma. Never touches \\cite or math minus (U+2212)."""
import re
from pathlib import Path
P = Path(__file__).resolve().parent / "AGENT_FAIRNESS_SURVEY.md"
lines = P.read_text(encoding="utf-8").splitlines()
out = []
LABEL = re.compile(r"(Contribution\s+\d|Locus\s+C\d|Table\s+\d|Figure\s+\d|Axis)\b", re.I)
for ln in lines:
    s = ln
    # en-dash -> hyphen everywhere (ranges like C1-C5, 2017-2026, sec ranges)
    s = s.replace("–", "-")
    if "—" not in s:
        out.append(s); continue
    is_table = s.lstrip().startswith("|")
    is_header = s.lstrip().startswith("#")
    if is_table:
        # empty-marker cells "| — |" -> "| n/a |"
        s = re.sub(r"(?<=\|)(\s*)—(\s*)(?=\|)", r"\1n/a\2", s)
        # label separators inside cells -> colon
        s = s.replace(" — ", ": ")
        out.append(s); continue
    # dual em-dash parenthetical: — X — -> (X)
    s = re.sub(r"—\s+(.+?)\s+—", r"(\1)", s)
    if "—" not in s:
        out.append(s); continue
    # header or bold-label or named label -> colon; else comma
    if is_header or LABEL.search(s) or re.search(r"\*\*[^*]+\*\*\s*—", s):
        s = s.replace(" — ", ": ").replace("—", ":")
    else:
        s = s.replace(" — ", ", ").replace("—", ", ")
    out.append(s)
P.write_text("\n".join(out) + "\n", encoding="utf-8")
rem = sum(l.count("—") + l.count("–") for l in out)
print(f"cleanup done; residual em/en dashes: {rem}")
