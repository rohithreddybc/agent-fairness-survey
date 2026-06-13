# LaTeX source — canonical working copy

`main.tex` is the **single source of truth** for the paper (ACM `acmart`,
`acmsmall` / CSUR journal format). Edit it directly; the markdown is retired.

## Files
- `main.tex` — the complete, self-contained manuscript. It contains five
  native-LaTeX figures (Figure 1: PRISMA flow diagram; Figure 2: temporal
  distribution bar chart; Figure 3: taxonomy tree; Figure 4: coverage-matrix
  heatmap; Figure 5: operator-grid heatmap), all tables (including four
  multi-page `longtable`s), inline math, and the bibliography inlined as a
  `thebibliography` environment.
- `references.bib` — bibliography source (202 entries; 168 cited). Kept for
  provenance; not needed to compile.
- `main.bbl` — the pre-built ACM-Reference-Format bibliography (168 bibitems)
  that was inlined into `main.tex`. Kept for reference; not read at compile time.
- `main.pdf` — current output (≈71 pp).

## Compile
The bibliography is inlined, so **`pdflatex` alone** compiles the paper — no
BibTeX. Run two or three passes so cross-references and the table of contents
settle:
```
pdflatex -interaction=nonstopmode main
pdflatex -interaction=nonstopmode main
pdflatex -interaction=nonstopmode main
```
There are no figure includes or external assets: every figure is drawn in
TikZ/pgfplots inside `main.tex`, so the file is fully self-contained.

If you add/remove/change a `\cite`, edit the inlined `thebibliography` block in
`main.tex` directly (or regenerate from `references.bib` with BibTeX and
re-inline the resulting `main.bbl`).

## Provenance / archive
The retired markdown pipeline (the old `AGENT_FAIRNESS_SURVEY.md`, the md→LaTeX/Word
converters, drafts, review notes, the article-class arXiv bundle) is in `../_backup/`.
The verified corpus and the §6 pilot data remain alongside (`../corpus/`, `../experiments/`).
