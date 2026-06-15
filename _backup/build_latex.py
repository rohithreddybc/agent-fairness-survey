#!/usr/bin/env python3
"""
build_latex.py — Phase 5: emit an ACM-acmart-ready LaTeX scaffold from the
assembled markdown. The body's \\cite{...} are already LaTeX; we convert headers,
emphasis, and escape stray specials, then wrap in a main.tex with the author block
and \\bibliography. Pragmatic v1 port — expect light hand-cleanup before camera-ready.
"""
from __future__ import annotations
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
md = (HERE / "AGENT_FAIRNESS_SURVEY.md").read_text(encoding="utf-8")

# drop the markdown title block (everything above the first '## ')
i = md.find("\n## ")
body_md = md[i+1:] if i != -1 else md

def convert(s: str) -> str:
    out = []
    for line in s.splitlines():
        if line.startswith("## "):
            t = re.sub(r"^##\s+\d+\.?\s*", "", line[3:]).strip()
            # abstract handled specially in main.tex; skip a lone "Abstract" header
            if t.lower() == "abstract":
                out.append("%%__ABSTRACT_MARKER__"); continue
            out.append(f"\\section{{{t}}}")
        elif line.startswith("### "):
            t = re.sub(r"^###\s+\d+(\.\d+)*\.?\s*", "", line[4:]).strip()
            out.append(f"\\subsection{{{t}}}")
        elif line.strip() == "---":
            continue
        else:
            out.append(line)
    text = "\n".join(out)
    # emphasis: **bold** and *italic* (order matters)
    text = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", text, flags=re.S)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"\\emph{\1}", text, flags=re.S)
    # inline code `x` -> \texttt{x}
    text = re.sub(r"`([^`]+)`", r"\\texttt{\1}", text)
    # markdown bullets "- " -> itemize lines (light touch: convert leading "- ")
    text = re.sub(r"(?m)^\s*-\s+", r"\\item ", text)
    return text

body = convert(body_md)

# split abstract (text after the abstract marker up to first \section) into \begin{abstract}
abstract_tex = ""
if "%%__ABSTRACT_MARKER__" in body:
    after = body.split("%%__ABSTRACT_MARKER__", 1)[1]
    m = re.search(r"\\section\{", after)
    abstract_tex = after[:m.start()].strip() if m else ""
    body = body.replace("%%__ABSTRACT_MARKER__" + (abstract_tex if False else ""), "")
    # remove the abstract prose from the body (keep from first \section onward)
    ms = re.search(r"\\section\{", body)
    body = body[ms.start():] if ms else body

main = r"""\documentclass[sigconf,nonacm]{acmart}
%% ACM SIGKDD Explorations target. Swap to the Explorations house style for camera-ready.
\usepackage{booktabs}
\usepackage{forest}
\usepackage{graphicx}

\begin{document}

\title{Fairness and Equity in LLM-Based Agents: A Taxonomic Survey}

\author{Rohith}
\authornote{Corresponding author.}
\affiliation{\institution{}\country{}}
\email{rohithreddybc98@gmail.com}

\author{Wenbin Zhang}
\affiliation{\institution{Florida International University}\country{USA}}

\begin{abstract}
%(ABSTRACT)
\end{abstract}

\keywords{fairness, equity, large language models, LLM agents, bias, counterfactual
fairness, multi-agent systems, trustworthy AI}

\maketitle

%(BODY)

\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\end{document}
"""
main = main.replace("%(ABSTRACT)", abstract_tex or "%% paste abstract")
main = main.replace("%(BODY)", body)
(HERE / "main.tex").write_text(main, encoding="utf-8")
print(f"wrote main.tex ({len(main)} chars); abstract={'yes' if abstract_tex else 'no'}")
print("NOTE: pragmatic port — verify \\item/itemize blocks, tables (build from FIGURES.md), "
      "and $...$ math/dollar signs before camera-ready.")
