# Fairness and Equity in LLM-Based Agents: A Taxonomic Survey

Target venue: **ACM Computing Surveys (CSUR)**.
Authors: Rohith (first & corresponding) · Wenbin Zhang (Florida International University).

## Canonical source: LaTeX
The paper is maintained in **LaTeX** (ACM `acmart`). The single source of truth is:

- **`latex/main.tex`** — the manuscript (self-contained: TikZ Figure 1, tables for
  Figures 2-3 and Tables 0-4, the Bias Conduction Framework, §6 pilot).
- `latex/references.bib` — 202 entries (168 cited).
- `latex/main.bbl` — pre-built (ACM-Reference-Format, patched), so it compiles without BibTeX.
- `latex/main.pdf` — current output (~67 pp).

Compile (prose edits): `pdflatex main` twice. See `latex/README.md` for the full
instructions and the BibTeX path when citations change.

## Other contents
- `corpus/` — the verified 202-paper corpus (`corpus_master.md`) and the arXiv
  citation-verification log (`VERIFY_RESULTS.md`).
- `experiments/section6_audit/` — the §6 pilot bias-audit harness + raw results.
- `CAMERA_READY_TODO.md` — remaining items before final submission.
- `_backup/` — retired artifacts (the old markdown source, Word export, the
  article-class arXiv bundle, intermediate files). Not part of the live paper.

## Status
Complete, reviewed (minor-revision / accept-oriented), citation-clean (168 cited, 0
missing). Proceeding at Dr. Zhang's pace; nothing posted unilaterally.
