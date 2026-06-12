# Fairness and Equity in LLM-Based Agents: A Taxonomic Survey

Manuscript and supporting materials. Target venue: **ACM Computing Surveys (CSUR)**.

**Authors:** Rohith (first & corresponding) · Wenbin Zhang (Florida International University)

## Contents
- `AGENT_FAIRNESS_SURVEY.md` — the manuscript (source).
- `AGENT_FAIRNESS_SURVEY.pdf` — compiled PDF (56 pp).
- `AGENT_FAIRNESS_SURVEY.docx` — Word version.
- `references.bib` — 201-entry bibliography; every arXiv ID machine-verified against the arXiv API (see `corpus/VERIFY_RESULTS.md`).
- `main.tex` — ACM `acmart` submission scaffold.
- `paper_pdf.tex` — self-contained LaTeX used to compile the PDF.
- `FIGURES.md` — figure/table specifications (taxonomy tree, coverage matrices, tables).
- `OUTLINE.md` — section outline.
- `corpus/` — verified paper corpus, citation-verification results, and coverage matrix.

## Summary
The first dedicated survey of fairness in LLM-based **agents**, organized by the
**Bias Conduction Framework (BCF)**: a two-axis model (entry locus × conduction
operator) with formal definitions, a conduction equation, and five propositions
characterizing where bias enters an agent pipeline, how it transforms across pipeline
edges, and why answer-level fairness measurement misses action-level disparity.

> Note: the §6 cross-framework bias audit is specified as a protocol; numerical
> results are pending execution and will be added in the camera-ready version.
