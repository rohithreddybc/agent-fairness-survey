#!/usr/bin/env python3
"""
build_acm.py  —  Markdown → acmart LaTeX → PDF (pdflatex + BibTeX).

Reads  AGENT_FAIRNESS_SURVEY.md  +  references.bib
Writes latex/main.tex, latex/references.bib, then compiles to latex/main.pdf.

Usage:  python build_acm.py          (from the survey directory)
"""
from __future__ import annotations
import re, subprocess, shutil, sys
from pathlib import Path

HERE  = Path(__file__).resolve().parent
LATEX = HERE / "latex"
LATEX.mkdir(exist_ok=True)

SRC = HERE / "AGENT_FAIRNESS_SURVEY.md"
BIB = HERE / "references.bib"
md  = SRC.read_text(encoding="utf-8")

# ─────────────────────────────────────────────────────────────────────────────
# 1.  Protect  \cite{...}  tokens  (survives all text transforms)
# ─────────────────────────────────────────────────────────────────────────────
cited_order: list[str] = []
cite_store:  dict[str,str] = {}

def stash_cite(m: re.Match) -> str:
    keys = [k.strip() for k in m.group(1).split(",")]
    for k in keys:
        if k not in cited_order:
            cited_order.append(k)
    tok = f"@@CITE{len(cite_store)}@@"
    cite_store[tok] = "\\cite{" + ",".join(keys) + "}"
    return tok

md = re.sub(r"\\cite[tp]?\{([^}]+)\}", stash_cite, md)

# ─────────────────────────────────────────────────────────────────────────────
# 2.  Unicode → LaTeX  (math wrapped in $...$)
# ─────────────────────────────────────────────────────────────────────────────
UNI: dict[str,str] = {
    # punctuation / quotes / dashes
    "—": "---", "–": "--",
    "“": "``",  "”": "''",
    "‘": "`",   "’": "'",
    "…": r"\ldots{}",
    "§": r"\S{}",
    "†": r"$\dagger$",
    "′": r"$^{\prime}$",
    "·": r"$\cdot$",
    # math relations / operators
    "≈": r"$\approx$",
    "≥": r"$\geq$",
    "≫": r"$\gg$",
    "→": r"$\rightarrow$",
    "×": r"$\times$",
    "∈": r"$\in$",
    "−": r"$-$",
    "≤": r"$\leq$",
    "≠": r"$\neq$",
    "≅": r"$\cong$",
    "≪": r"$\ll$",
    "∞": r"$\infty$",
    "±": r"$\pm$",
    "∑": r"$\sum$",
    "∏": r"$\prod$",
    "√": r"$\surd$",
    "≡": r"$\equiv$",
    "∅": r"$\emptyset$",
    # greek
    "Δ": r"$\Delta$",
    "Π": r"$\Pi$",
    "Σ": r"$\Sigma$",
    "π": r"$\pi$",
    "τ": r"$\tau$",
    "φ": r"$\varphi$",
    "δ": r"$\delta$",
    "θ": r"$\theta$",
    "α": r"$\alpha$",
    "β": r"$\beta$",
    "γ": r"$\gamma$",
    "λ": r"$\lambda$",
    "μ": r"$\mu$",
    "ω": r"$\omega$",
    "κ": r"$\kappa$",
    "ε": r"$\epsilon$",
    "η": r"$\eta$",
    "ν": r"$\nu$",
    "ξ": r"$\xi$",
    "ρ": r"$\rho$",
    "σ": r"$\sigma$",
    "ψ": r"$\psi$",
    "ζ": r"$\zeta$",
    # brackets / markers
    "⟨": r"$\langle$",
    "⟩": r"$\rangle$",
    "○": r"$\circ$",
    "●": r"$\bullet$",
    "⪯": r"$\preceq$",
    "⪰": r"$\succeq$",
    # arrows
    "⇒": r"$\Rightarrow$",
    "⇐": r"$\Leftarrow$",
    "⇔": r"$\Leftrightarrow$",
    "←": r"$\leftarrow$",
    "↔": r"$\leftrightarrow$",
    # subscript/superscript digits (unicode)
    "₀": r"$_0$", "₁": r"$_1$", "₂": r"$_2$",
    "₃": r"$_3$", "₄": r"$_4$", "₅": r"$_5$",
    # bullets / special marks
    "•": r"$\bullet$",
    "▶": r"$\triangleright$",
    "✓": r"$\checkmark$",
    "✗": r"$\times$",
    # additional misc
    "é": r"\'{e}",
    "è": r"\`{e}",
    "ê": r"\^{e}",
    "à": r"\`{a}",
    "â": r"\^{a}",
    "ô": r"\^{o}",
    "û": r"\^{u}",
    "ü": r'\"u',
    "ö": r'\"o',
    "ä": r'\"a',
    "ß": r"{\ss}",
    "É": r"\'{E}",
    "ñ": r"\~{n}",
    "ç": r"\c{c}",
    "’": "'",   # right single quote — repeat for clarity (already above)
    "▪": r"$\blacksquare$",
    "—": "---",  # em dash (already above, harmless duplicate)
    # degree / other
    "°": r"${}^\circ$",
    "½": r"$\frac{1}{2}$",
    # circled bullets used in maturity markers ●●●
    "●": r"$\bullet$",   # already above
    "○": r"$\circ$",     # already above
}

def convert_unicode(s: str) -> str:
    for u, l in UNI.items():
        s = s.replace(u, l)
    return s

# ─────────────────────────────────────────────────────────────────────────────
# 3.  LaTeX special-character escaping  (plain text regions only)
# ─────────────────────────────────────────────────────────────────────────────
def esc_text(t: str) -> str:
    """Escape LaTeX specials in plain-text fragments (after unicode is converted)."""
    t = t.replace("\\", r"\textbackslash{}")
    for ch in "&%#":
        t = t.replace(ch, "\\" + ch)
    t = t.replace("_", r"\_")
    t = t.replace("^", r"\textasciicircum{}")
    t = t.replace("~", r"\textasciitilde{}")
    t = t.replace("{", r"\{").replace("}", r"\}")
    return t

# ─────────────────────────────────────────────────────────────────────────────
# 4.  Inline formatting  (bold / italic / code)
# ─────────────────────────────────────────────────────────────────────────────
def inline(text: str) -> str:
    out = []
    for part in re.split(r"(\*\*.+?\*\*|\*[^*]+?\*|`[^`]+?`)", text, flags=re.S):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            out.append(r"\textbf{" + esc_text(part[2:-2]) + "}")
        elif part.startswith("`") and part.endswith("`"):
            out.append(r"\texttt{" + esc_text(part[1:-1]) + "}")
        elif part.startswith("*") and part.endswith("*") and len(part) >= 3:
            out.append(r"\emph{" + esc_text(part[1:-1]) + "}")
        else:
            out.append(esc_text(part))
    return "".join(out)

# ─────────────────────────────────────────────────────────────────────────────
# 5.  Figure 1: taxonomy tree (forest)
# ─────────────────────────────────────────────────────────────────────────────
FIGURE1_LATEX = r"""
\begin{figure}[ht]
\centering
\begin{forest}
for tree={
  grow'=0,
  parent anchor=east, child anchor=west,
  anchor=west,
  l sep=8pt, s sep=2pt,
  font=\small,
  rounded corners, draw, fill=blue!5,
  align=left, inner sep=2pt
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

# ─────────────────────────────────────────────────────────────────────────────
# 6.  Table conversion:  markdown  |col|col|  →  LaTeX tabular + booktabs
# ─────────────────────────────────────────────────────────────────────────────

def make_tabular(rows: list[list[str]], caption_text: str = "", label: str = "") -> list[str]:
    """Convert a list-of-rows (strings already inline-converted) to a
    table* float with booktabs.  Wide tables use \\small + resizebox."""
    n = len(rows[0]) if rows else 1
    # column spec: equal-width p{} columns
    col_frac = 0.90 / max(n, 1)
    col_spec = "|" + "|".join([f"p{{{col_frac:.3f}\\textwidth}}"]*n) + "|"

    out = []
    # Use table* for wide tables (>=4 cols), table for narrow
    float_env = "table*" if n >= 4 else "table"
    out.append(f"\\begin{{{float_env}}}[htbp]")
    out.append(r"\centering\small")
    if caption_text:
        # caption_text is already latex-processed (inline+convert_unicode applied)
        out.append(f"\\caption{{{caption_text}}}")
    if label:
        out.append(f"\\label{{{label}}}")
    out.append(f"\\resizebox{{\\columnwidth}}{{!}}{{%")
    out.append(f"\\begin{{tabular}}{{{col_spec}}}")
    out.append(r"\toprule")

    header = rows[0]
    out.append(" & ".join(r"\textbf{" + h + "}" for h in header) + r" \\")
    out.append(r"\midrule")

    for row in rows[1:]:
        cells = (row + [""] * n)[:n]
        out.append(" & ".join(cells) + r" \\")

    out.append(r"\bottomrule")
    out.append(r"\end{tabular}%")
    out.append(r"}")   # close resizebox
    out.append(f"\\end{{{float_env}}}")
    return out

# caption heuristic: look for a trailing *bold caption line* just above the table
def extract_caption(lines: list[str], table_start_idx: int) -> str:
    """Scan backwards from table_start_idx for a caption-like line."""
    for j in range(table_start_idx - 1, max(table_start_idx - 5, -1), -1):
        s = lines[j].strip()
        if not s:
            continue
        # bold marker or "Table N:" prefix
        if re.match(r"(\*\*Table\s+\w+.*\*\*|Table\s+\w+:)", s, re.I):
            return re.sub(r"\*\*", "", s)
        # italicized takeaway line — skip
        if s.startswith("*Takeaway") or s.startswith("_"):
            continue
        # paragraph caption ending with a period
        if s.endswith(".") and len(s) < 250:
            return re.sub(r"\*", "", s)
        break
    return ""

# ─────────────────────────────────────────────────────────────────────────────
# 7.  Abstract extraction
# ─────────────────────────────────────────────────────────────────────────────
abstract_lines: list[str] = []
body_start_idx = 0
in_abstract = False
lines = md.splitlines()

for idx, line in enumerate(lines):
    st = line.strip()
    if st == "## Abstract":
        in_abstract = True
        continue
    if in_abstract:
        if st.startswith("## "):
            # first section after abstract → body starts here
            body_start_idx = idx
            in_abstract = False
            break
        if st == "---":
            # separator ends abstract
            in_abstract = False
            body_start_idx = idx + 1
            break
        abstract_lines.append(line)

# clean up leading/trailing blank lines from abstract
while abstract_lines and not abstract_lines[0].strip():
    abstract_lines.pop(0)
while abstract_lines and not abstract_lines[-1].strip():
    abstract_lines.pop()

abstract_md = "\n".join(abstract_lines)

def process_abstract(text: str) -> str:
    """Convert markdown inline to LaTeX for the abstract.
    Order: inline() first (escapes specials, handles **bold**/etc.),
    then convert_unicode() (replaces unicode chars with LaTeX macros)."""
    result = []
    for para in re.split(r"\n{2,}", text):
        para = para.strip()
        if not para:
            continue
        result.append(convert_unicode(inline(para)))
    return "\n\n".join(result)

abstract_tex = process_abstract(abstract_md)

# ─────────────────────────────────────────────────────────────────────────────
# 8.  Body conversion: line-by-line
# ─────────────────────────────────────────────────────────────────────────────

def latex_header(level: int, txt: str) -> str:
    # level 1 = ## (section), 2 = ### (subsection), 3 = #### (subsubsection), 4+ = paragraph
    cmd = {1: "section", 2: "subsection", 3: "subsubsection", 4: "paragraph"}.get(
        min(level, 4), "paragraph"
    )
    # strip leading numbering like "1.", "1.1", "1.1.1"
    clean = re.sub(r"^\d+(\.\d+)*\.?\s+", "", txt).strip()
    return f"\\{cmd}{{{convert_unicode(inline(clean))}}}"

body_lines = lines[body_start_idx:]

def is_table_sep(s: str) -> bool:
    return bool(re.match(r"^\|[\s:|-]+\|?$", s))

out_body: list[str] = []
i = 0
table_count = 0

while i < len(body_lines):
    s = body_lines[i].rstrip()
    st = s.strip()

    # ── blank line ─────────────────────────────────────────────────────────
    if not st:
        out_body.append("")
        i += 1
        continue

    # ── horizontal rule ────────────────────────────────────────────────────
    if st == "---":
        i += 1
        continue

    # ── FIGURE1 marker ─────────────────────────────────────────────────────
    if st == "<!--FIGURE1-->":
        out_body.append(FIGURE1_LATEX)
        i += 1
        continue

    # ── HTML comments ──────────────────────────────────────────────────────
    if st.startswith("<!--") and st.endswith("-->"):
        i += 1
        continue

    # ── Fenced math blocks  $$ ... $$ (standalone) ─────────────────────────
    if st == "$$":
        math_lines = []
        i += 1
        while i < len(body_lines) and body_lines[i].strip() != "$$":
            math_lines.append(body_lines[i])
            i += 1
        i += 1  # skip closing $$
        out_body.append("\\begin{equation*}")
        out_body.extend(math_lines)
        out_body.append("\\end{equation*}")
        continue

    # ── Inline $...$ math lines starting with $$ (display) ─────────────────
    if st.startswith("$$") and st.endswith("$$") and len(st) > 4:
        inner = st[2:-2].strip()
        out_body.append("\\begin{equation*}")
        out_body.append(inner)
        out_body.append("\\end{equation*}")
        i += 1
        continue

    # ── Markdown table ─────────────────────────────────────────────────────
    if st.startswith("|") and i + 1 < len(body_lines) and is_table_sep(body_lines[i+1].strip()):
        # collect all table rows
        raw_rows: list[list[str]] = []
        while i < len(body_lines) and body_lines[i].strip().startswith("|"):
            r = body_lines[i].strip()
            if is_table_sep(r):
                i += 1
                continue
            cells_raw = [c.strip() for c in r.strip("|").split("|")]
            # apply inline + unicode to each cell
            cells = [convert_unicode(inline(c)) for c in cells_raw]
            raw_rows.append(cells)
            i += 1

        if not raw_rows:
            continue

        table_count += 1
        cap_raw = extract_caption(body_lines, i - len(raw_rows) - 2)
        # apply unicode conversion + inline markup to caption
        cap = convert_unicode(inline(cap_raw)) if cap_raw else ""
        label = f"tab:{table_count}"
        out_body.extend(make_tabular(raw_rows, cap, label))
        continue

    # ── Section headers  ## / ### / #### ────────────────────────────────────
    m = re.match(r"^(#{1,6})\s+(.*)$", st)
    if m:
        level = len(m.group(1))
        out_body.append(latex_header(level, m.group(2)))
        i += 1
        continue

    # ── Bullet / unordered list ─────────────────────────────────────────────
    if re.match(r"^[-*]\s+", st):
        items = []
        while i < len(body_lines) and re.match(r"^[-*]\s+", body_lines[i].strip()):
            item_text = re.sub(r"^[-*]\s+", "", body_lines[i].strip())
            items.append(convert_unicode(inline(item_text)))
            i += 1
        out_body.append("\\begin{itemize}")
        for it in items:
            out_body.append("\\item " + it)
        out_body.append("\\end{itemize}")
        continue

    # ── Numbered list  1. 2. ... ─────────────────────────────────────────────
    if re.match(r"^\d+\.\s+", st):
        items = []
        while i < len(body_lines) and re.match(r"^\d+\.\s+", body_lines[i].strip()):
            item_text = re.sub(r"^\d+\.\s+", "", body_lines[i].strip())
            items.append(convert_unicode(inline(item_text)))
            i += 1
        out_body.append("\\begin{enumerate}")
        for it in items:
            out_body.append("\\item " + it)
        out_body.append("\\end{enumerate}")
        continue

    # ── Block quote ─────────────────────────────────────────────────────────
    if st.startswith(">"):
        content = convert_unicode(inline(st.lstrip("> ").strip()))
        out_body.append("\\begin{quote}" + content + "\\end{quote}")
        i += 1
        continue

    # ── Regular paragraph line ─────────────────────────────────────────────
    out_body.append(convert_unicode(inline(s)))
    i += 1

tex_body = "\n".join(out_body)

# ─────────────────────────────────────────────────────────────────────────────
# 9.  Restore  \cite{...}  tokens
# ─────────────────────────────────────────────────────────────────────────────
for tok, val in cite_store.items():
    # the token may have been escaped by esc_text; restore both forms
    tex_body    = tex_body.replace(esc_text(tok), val).replace(tok, val)
    abstract_tex = abstract_tex.replace(esc_text(tok), val).replace(tok, val)

# ─────────────────────────────────────────────────────────────────────────────
# 10.  Build  main.tex  (acmart / CSUR format)
# ─────────────────────────────────────────────────────────────────────────────

PREAMBLE = r"""\documentclass[acmsmall]{acmart}

%% ACM journal metadata
\acmJournal{CSUR}
\acmYear{2026}
\settopmatter{printacmref=true}

%% Extra packages (acmart loads hyperref and amsmath automatically)
%% Do NOT load amsmath/amssymb here — acmart already loads them,
%% and a second load causes \Bbbk conflict with MiKTeX's amssymb.
\usepackage{booktabs}
\usepackage{forest}
\usepackage{tikz}
\usepackage{graphicx}

%% suppress ACM copyright / price blocks for preprint builds
\setcopyright{none}
\acmDOI{}
\acmISBN{}
\acmConference{}{}{}{}

"""

AUTHORS = r"""
\title{Fairness and Equity in LLM-Based Agents: A Taxonomic Survey}

\author{Rohith Reddy Bheemreddy}
\authornote{Corresponding author.}
\email{rbhee001@fiu.edu}
\affiliation{%
  \institution{Florida International University}
  \city{Miami}
  \state{FL}
  \country{USA}
}

\author{Wenbin Zhang}
\email{wzhang@fiu.edu}
\affiliation{%
  \institution{Florida International University}
  \city{Miami}
  \state{FL}
  \country{USA}
}

"""

CCS_KEYWORDS = r"""
\begin{CCSXML}
<ccs2012>
  <concept>
    <concept_id>10010147.10010178.10010187</concept_id>
    <concept_desc>Computing methodologies~Natural language processing</concept_desc>
    <concept_significance>500</concept_significance>
  </concept>
  <concept>
    <concept_id>10003456.10003457.10003527</concept_id>
    <concept_desc>Social and professional topics~Socio-technical systems</concept_desc>
    <concept_significance>500</concept_significance>
  </concept>
  <concept>
    <concept_id>10010147.10010178.10010179</concept_id>
    <concept_desc>Computing methodologies~Artificial intelligence</concept_desc>
    <concept_significance>300</concept_significance>
  </concept>
</ccs2012>
\end{CCSXML}

\ccsdesc[500]{Computing methodologies~Natural language processing}
\ccsdesc[500]{Social and professional topics~Socio-technical systems}
\ccsdesc[300]{Computing methodologies~Artificial intelligence}

\keywords{fairness, equity, large language models, LLM agents, bias,
          counterfactual fairness, trustworthy AI}

"""

doc_parts = [
    PREAMBLE,
    AUTHORS,
    r"\begin{document}",
    "",
    r"\begin{abstract}",
    abstract_tex,
    r"\end{abstract}",
    "",
    CCS_KEYWORDS,
    "",
    r"\maketitle",
    "",
    tex_body,
    "",
    r"\bibliographystyle{ACM-Reference-Format}",
    r"\bibliography{references}",
    "",
    r"\end{document}",
]

main_tex = "\n".join(doc_parts)

out_tex = LATEX / "main.tex"
out_tex.write_text(main_tex, encoding="utf-8")
print(f"Wrote {out_tex}  ({len(main_tex):,} chars, {len(cited_order)} cited keys)")

# ─────────────────────────────────────────────────────────────────────────────
# 11.  Copy  references.bib
# ─────────────────────────────────────────────────────────────────────────────
shutil.copy2(BIB, LATEX / "references.bib")
print(f"Copied references.bib -> {LATEX / 'references.bib'}")

# ─────────────────────────────────────────────────────────────────────────────
# 11b.  Fix references.bib  (in-place, latex/ copy only)
# ─────────────────────────────────────────────────────────────────────────────
def fix_bib(bib_path: Path) -> None:
    """
    1. Convert comma-separated author lists to BibTeX 'and'-separated lists.
       BibTeX expects  "Last, First and Last, First"  or  "First Last and First Last".
       Entries like  "A Smith, B Jones, C Doe"  cause "Too many commas" errors.
    2. Ensure every @article entry has at least a journal field (use booktitle
       value when journal is missing, so ACM-Reference-Format doesn't warn).
    """
    text = bib_path.read_text(encoding="utf-8")

    def fix_author_field(m: re.Match) -> str:
        raw = m.group(0)           # e.g.  author = {A, B, C, D}
        content = m.group(1)       # e.g.  A, B, C, D
        # Only fix if there is no " and " already (simple heuristic)
        if " and " in content:
            return raw
        # Split on ", " — but individual names may have ", " too (Last, First)
        # Heuristic: if every comma-separated chunk has at least one space,
        # treat it as "First Last" format → join with " and ".
        # If chunks have internal commas that look like "Last, First" pairs,
        # that's a BibTeX-valid format already (one author, no second) — skip.
        parts = [p.strip() for p in content.split(",")]
        # Merge pairs that look like "Last" "First" → but better heuristic:
        # if the number of comma-separated tokens is >= 2 and none of the parts
        # looks like "Last, First" (i.e., none is a single word), join with and.
        if len(parts) >= 2:
            # Check if any part is a bare single-word (likely a last name only fragment)
            # If chunks all have spaces → they are "First Last" names → join with and
            if all(" " in p or "." in p for p in parts):
                return f"  author = {{{' and '.join(parts)}}}"
        return raw

    # Match  author = {...}  (possibly multi-line via single-line assumption)
    text = re.sub(
        r"  author = \{([^}]+)\}",
        fix_author_field,
        text,
    )

    bib_path.write_text(text, encoding="utf-8")
    print("Fixed references.bib (author and-separation)")

fix_bib(LATEX / "references.bib")

# ─────────────────────────────────────────────────────────────────────────────
# 12.  Compile:  pdflatex → bibtex → pdflatex → pdflatex
# ─────────────────────────────────────────────────────────────────────────────
def run(cmd: list[str], cwd: Path, label: str) -> tuple[int,str]:
    r = subprocess.run(
        cmd, cwd=cwd,
        capture_output=True,   # raw bytes
        timeout=600,
    )
    # decode with errors='replace' so Windows codepage bytes don't crash
    stdout = r.stdout.decode("utf-8", errors="replace") if r.stdout else ""
    stderr = r.stderr.decode("utf-8", errors="replace") if r.stderr else ""
    combined = stdout + stderr
    if r.returncode != 0:
        tail = "\n".join(combined.splitlines()[-30:])
        print(f"[{label}] exit {r.returncode}; last output:\n{tail}")
    else:
        print(f"[{label}] OK (exit 0)")
    return r.returncode, combined

PDFLATEX = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"]

print("\n── Pass 1 (pdflatex) ──────────────────────────────────────────────")
rc1, log1 = run(PDFLATEX, LATEX, "pdflatex-1")

print("\n── BibTeX ─────────────────────────────────────────────────────────")
rc_bib, log_bib = run(["bibtex", "main"], LATEX, "bibtex")

# ── Fix .bbl: remove double blank lines inside bibliography items ──────────
bbl_path = LATEX / "main.bbl"
if bbl_path.exists():
    bbl_text = bbl_path.read_text(encoding="utf-8", errors="replace")
    # 1. Replace 2+ consecutive blank lines → single blank line
    #    (double blank lines inside a \bibitem cause "Paragraph ended" fatal error)
    bbl_text = re.sub(r"\n{3,}", "\n\n", bbl_text)
    # 2. Fix \natexlab with TeX-special disambiguation characters.
    #    ACM BST overflows a-z and emits { | ~ etc. as disambiguation labels.
    #    \natexlab{{}  is fatal (unmatched { in TeX argument)
    #    \natexlab{~}  is problematic (~ = non-breaking space in LaTeX)
    #    Use literal string.replace() — regex backslash escaping is unreliable here
    bbl_text = bbl_text.replace("\\natexlab{{}", "\\natexlab{}")
    bbl_text = bbl_text.replace("\\natexlab{~}", "\\natexlab{}")
    # Extra stray } after \natexlab{}}: remove duplicated close-brace
    bbl_text = bbl_text.replace("\\natexlab{}}", "\\natexlab{}")
    # 3. Fix \bibitem optional arg with TeX-special chars in year position:
    #    [et~al.(2024{)]  or  [et~al.(2024})]  → [et~al.(2024)]
    bbl_text = re.sub(r"\((\d{4})[{}~|]([^)]*)\)\]", r"(\1\2)]", bbl_text)
    bbl_path.write_text(bbl_text, encoding="utf-8")
    print("Fixed .bbl (removed double blank lines, fixed natexlab braces)")

print("\n── Pass 2 (pdflatex) ──────────────────────────────────────────────")
rc2, _ = run(PDFLATEX, LATEX, "pdflatex-2")

print("\n── Pass 3 (pdflatex) ──────────────────────────────────────────────")
rc3, log3 = run(PDFLATEX, LATEX, "pdflatex-3")

# ─────────────────────────────────────────────────────────────────────────────
# 13.  Verify PDF + citation audit
# ─────────────────────────────────────────────────────────────────────────────
pdf = LATEX / "main.pdf"
if pdf.exists():
    kb = pdf.stat().st_size // 1024
    print(f"\nPDF produced: {pdf}  ({kb} KB)")
    try:
        import pypdf
        reader = pypdf.PdfReader(str(pdf))
        print(f"  Page count: {len(reader.pages)}")
    except Exception as e:
        print(f"  pypdf check skipped: {e}")
else:
    print("\nERROR: main.pdf NOT produced")
    # print last 40 lines of pdflatex log
    logf = LATEX / "main.log"
    if logf.exists():
        tail = logf.read_text(encoding="utf-8", errors="replace").splitlines()
        print("Last 40 lines of main.log:")
        print("\n".join(tail[-40:]))

# Check BibTeX log for undefined citations
blg = LATEX / "main.blg"
undefined_cites: list[str] = []
if blg.exists():
    blg_text = blg.read_text(encoding="utf-8", errors="replace")
    undefined_cites = re.findall(r"I didn't find a database entry for \"([^\"]+)\"", blg_text)
    warning_count = blg_text.count("Warning--")
    print(f"\nBibTeX: {warning_count} warnings, {len(undefined_cites)} undefined citations")
    if undefined_cites:
        print("  Undefined:", undefined_cites[:20])
else:
    print("\nNo .blg file found")

# Check main log for undefined references
undef_refs: list[str] = []
if (LATEX / "main.log").exists():
    logtext = (LATEX / "main.log").read_text(encoding="utf-8", errors="replace")
    undef_refs = list(set(re.findall(r"Citation `([^']+)' on page", logtext)))
    print(f"LaTeX log: {len(set(undef_refs))} citation-on-page entries found")

# ─────────────────────────────────────────────────────────────────────────────
# 14.  Clean aux files  (keep .tex, .bib, .pdf, .bbl for ACM submission)
# ─────────────────────────────────────────────────────────────────────────────
for ext in (".aux", ".out", ".log", ".blg", ".toc", ".lof", ".lot",
            ".fls", ".fdb_latexmk", ".synctex.gz", "-blx.bib", ".run.xml"):
    f = LATEX / ("main" + ext)
    if f.exists():
        f.unlink()
        print(f"Removed {f.name}")

print("\nDone.")
print(f"  main.tex : {LATEX / 'main.tex'}")
print(f"  main.pdf : {LATEX / 'main.pdf'}")
