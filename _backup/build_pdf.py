#!/usr/bin/env python3
"""Markdown -> LaTeX -> PDF (pdflatex, self-contained thebibliography; no bibtex/pandoc).
ASCII-ifies unicode math so it compiles under pdflatex without font dependencies.
Usage: python build_pdf.py AGENT_FAIRNESS_SURVEY.md  ->  writes paper_pdf.tex (+ paper_pdf.pdf if pdflatex runs)."""
from __future__ import annotations
import re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "AGENT_FAIRNESS_SURVEY.md"
STEM = "paper_pdf"
md = SRC.read_text(encoding="utf-8")

# 1. protect \cite{...}
cited_order = []
cite_store = {}
def stash_cite(m):
    keys = [k.strip() for k in m.group(1).split(",")]
    for k in keys:
        if k not in cited_order: cited_order.append(k)
    tok = f"@@CITE{len(cite_store)}@@"
    cite_store[tok] = "\\cite{" + ",".join(keys) + "}"
    return tok
md = re.sub(r"\\cite[tp]?\{([^}]+)\}", stash_cite, md)

# 2. unicode -> LaTeX (math wrapped in $...$)
UNI = {
    # punctuation / quotes / dashes
    "—": "---", "–": "--", "“": "``", "”": "''", "‘": "`", "’": "'", "…": r"\ldots{}",
    "§": r"\S{}", "†": r"$\dagger$", "′": r"$^{\prime}$",
    # math relations / operators
    "≈": r"$\approx$", "≥": r"$\geq$", "≫": r"$\gg$", "→": r"$\rightarrow$",
    "×": r"$\times$", "·": r"$\cdot$", "∈": r"$\in$", "−": r"$-$",
    # greek
    "Δ": r"$\Delta$", "Π": r"$\Pi$", "Σ": r"$\Sigma$", "π": r"$\pi$", "τ": r"$\tau$",
    "φ": r"$\varphi$",
    # brackets / markers
    "⟨": r"$\langle$", "⟩": r"$\rangle$", "○": r"$\circ$", "●": r"$\bullet$",
    "⪯": r"$\preceq$", "⪰": r"$\succeq$", "≡": r"$\equiv$", "∅": r"$\emptyset$",
    # safety extras (not currently present but cheap)
    "≤": r"$\leq$", "≠": r"$\neq$", "≅": r"$\cong$", "≪": r"$\ll$", "∞": r"$\infty$",
    "±": r"$\pm$", "∑": r"$\sum$", "∏": r"$\prod$", "√": r"$\surd$",
    "δ": r"$\delta$", "θ": r"$\theta$", "α": r"$\alpha$", "β": r"$\beta$",
    "γ": r"$\gamma$", "λ": r"$\lambda$", "μ": r"$\mu$",
}

def esc_text(t: str) -> str:
    # escape LaTeX specials in plain text (after unicode handled, before re-merge)
    t = t.replace("\\", r"\textbackslash{}")
    for ch in "&%#":
        t = t.replace(ch, "\\" + ch)
    t = t.replace("_", r"\_").replace("^", r"\textasciicircum{}").replace("~", r"\textasciitilde{}")
    t = t.replace("{", r"\{").replace("}", r"\}")
    return t

def inline(text: str) -> str:
    # bold/italic/code first, on raw text, then escape pieces
    out = []
    for part in re.split(r"(\*\*.+?\*\*|\*[^*]+?\*|`[^`]+?`)", text):
        if not part: continue
        if part.startswith("**") and part.endswith("**"):
            out.append(r"\textbf{" + esc_text(part[2:-2]) + "}")
        elif part.startswith("`") and part.endswith("`"):
            out.append(r"\texttt{" + esc_text(part[1:-1]) + "}")
        elif part.startswith("*") and part.endswith("*"):
            out.append(r"\emph{" + esc_text(part[1:-1]) + "}")
        else:
            out.append(esc_text(part))
    return "".join(out)

def convert_unicode(s: str) -> str:
    for u, l in UNI.items(): s = s.replace(u, l)
    return s

# ── Figure 1: taxonomy tree (LaTeX / forest) ──────────────────────────────
FIGURE1_LATEX = r"""
\begin{figure}[ht]
\centering
\begin{forest}
for tree={
  grow'=0,
  parent anchor=east, child anchor=west,
  anchor=west,
  l sep=10pt, s sep=3pt,
  font=\small,
  rounded corners, draw, fill=blue!5,
  align=left, inner sep=3pt
}
[Fairness in LLM Agents, fill=gray!18
  [1.\ Tool/API selection -- tool-choice bias; description sensitivity]
  [2.\ Memory \& retrieval -- RAG fairness; multi-turn accumulation]
  [3.\ Multi-agent delegation -- persona/role bias; emergent bias]
  [4.\ Planning / decomposition -- CoT-reasoning bias; task allocation]
  [5.\ User modeling / personalization -- identity inference; dialect bias]
  [6.\ Long-horizon drift -- multi-turn compounding; sycophancy decay]
]
\end{forest}
\caption{Taxonomy of fairness in LLM-based agents, organized by agent component
(Axis~1). Each node names a structural entry locus and its primary harm mechanism.
Unlike QA-level LLM-fairness taxonomies, the unit of analysis is the
\emph{acting} agent.}
\label{fig:taxonomy}
\end{figure}
"""

# 3. line-by-line
lines = md.splitlines()
body, i = [], 0
def latex_header(level, txt):
    cmd = {1: "section", 2: "subsection", 3: "subsubsection", 4: "paragraph"}.get(level, "paragraph")
    return f"\\{cmd}*{{{inline(txt)}}}"

while i < len(lines):
    s = lines[i].rstrip()
    st = s.strip()
    if st.startswith("|") and i+1 < len(lines) and re.match(r"^\|[\s:|-]+\|?$", lines[i+1].strip()):
        rows = []
        while i < len(lines) and lines[i].strip().startswith("|"):
            rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
        header = rows[0]; data = rows[2:]; n = len(header)
        body.append("\\begin{center}\\footnotesize")
        body.append("\\begin{longtable}{|" + "p{%.2f\\textwidth}|" % (0.92/max(n,1)) * n + "}")
        body.append("\\hline " + " & ".join(r"\textbf{"+inline(c)+"}" for c in header) + r" \\ \hline\endhead")
        for r in data:
            cells = (r + [""]*n)[:n]
            body.append(" & ".join(inline(c) for c in cells) + r" \\ \hline")
        body.append("\\end{longtable}\\end{center}")
        continue
    if st == "<!--FIGURE1-->":
        body.append(FIGURE1_LATEX); i += 1; continue
    if not st:
        body.append(""); i += 1; continue
    if st == "---":
        i += 1; continue
    m = re.match(r"^(#{1,6})\s+(.*)$", st)
    if m:
        body.append(latex_header(len(m.group(1)), m.group(2))); i += 1; continue
    if re.match(r"^[-*]\s+", st):
        items = []
        while i < len(lines) and re.match(r"^[-*]\s+", lines[i].strip()):
            items.append(re.sub(r"^[-*]\s+", "", lines[i].strip())); i += 1
        body.append("\\begin{itemize}")
        for it in items: body.append("\\item " + inline(it))
        body.append("\\end{itemize}")
        continue
    if st.startswith(">"):
        body.append("\\begin{quote}" + inline(st.lstrip("> ")) + "\\end{quote}"); i += 1; continue
    body.append(inline(st)); i += 1

tex_body = "\n".join(body)
tex_body = convert_unicode(tex_body)
# restore cites
for tok, val in cite_store.items():
    tex_body = tex_body.replace(esc_text(tok), val).replace(tok, val)

# 4. thebibliography from references.bib (only cited keys)
bib = (HERE / "references.bib").read_text(encoding="utf-8")
ent = {}
for m in re.finditer(r"@\w+\{([^,]+),(.*?)\n\}", bib, re.S):
    k = m.group(1).strip(); b = m.group(2)
    def f(name):
        mm = re.search(rf"{name}\s*=\s*\{{(.*?)\}}", b, re.S)
        return re.sub(r"\s+", " ", mm.group(1)).strip() if mm else ""
    ent[k] = (f("author"), f("year"), f("title"), f("journal") or f("booktitle"), f("eprint"), f("doi"))
bibitems = []
for k in cited_order:
    if k not in ent: continue
    au, yr, ti, ve, ep, doi = ent[k]
    parts = [p for p in [au, f"({yr})" if yr else "", ti, ve, ("arXiv:"+ep) if ep else "", ("doi:"+doi) if doi else ""] if p]
    bibitems.append(f"\\bibitem{{{k}}} " + esc_text(". ".join(parts)))

doc = r"""\documentclass[10pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{longtable,array,amsmath,amssymb,hyperref}
\usepackage[T1]{fontenc}\usepackage{lmodern}
\usepackage{tikz}
\usepackage{forest}
\setlength{\parskip}{4pt}\setlength{\parindent}{0pt}
\title{Fairness and Equity in LLM-Based Agents: A Taxonomic Survey}
\author{Rohith \and Wenbin Zhang (Florida International University)}
\date{Submitted to ACM Computing Surveys}
\begin{document}\maketitle
""" + tex_body + r"""

\begin{thebibliography}{999}
""" + "\n".join(bibitems) + r"""
\end{thebibliography}
\end{document}
"""
(HERE / f"{STEM}.tex").write_text(doc, encoding="utf-8")
print(f"wrote {STEM}.tex ({len(cited_order)} cited)")

# 5. compile
try:
    for _ in range(2):
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", f"{STEM}.tex"],
                           cwd=HERE, capture_output=True, text=True, timeout=300)
    pdf = HERE / f"{STEM}.pdf"
    if pdf.exists():
        print(f"PDF OK: {pdf.name} ({pdf.stat().st_size//1024} KB)")
    else:
        tail = "\n".join(r.stdout.splitlines()[-15:])
        print("PDF FAILED; last log:\n" + tail)
except Exception as e:
    print(f"pdflatex error: {e}")
