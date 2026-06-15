# LaTeX source — canonical working copy

`main.tex` is the manuscript (ACM `acmart`, `acmsmall` / CSUR journal format).
The bibliography is in a separate `references.bib` (standard BibTeX workflow).

## Files (upload BOTH to Overleaf)
- `main.tex` — the complete manuscript. Five native-LaTeX figures (Figure 1 PRISMA
  flow, Figure 2 temporal bar chart, Figure 3 taxonomy tree, Figure 4 coverage-matrix
  heatmap, Figure 5 operator-grid heatmap), all tables (four multi-page `longtable`s),
  inline math. No external image files: every figure is drawn in TikZ/pgfplots inside
  `main.tex`. Uses `\bibliographystyle{ACM-Reference-Format}` + `\bibliography{references}`.
- `references.bib` — 210 entries (176 cited). Required to compile.

## Overleaf
Upload `main.tex` and `references.bib`. Compiler: **pdfLaTeX** (Overleaf runs BibTeX
automatically). `acmart`, `forest`, `pgfplots`, `tikz`, `longtable`, `booktabs` are all
in Overleaf's TeX distribution. Recompile → ~75-page PDF.

## Local compile
```
pdflatex -interaction=nonstopmode main
bibtex main
pdflatex -interaction=nonstopmode main
pdflatex -interaction=nonstopmode main
```

## Notes
- `main.bbl` (if present) is the generated bibliography; Overleaf/BibTeX regenerates it.
  Not required for upload.
- Author fields in `references.bib` use the proper BibTeX `... and others` form (renders
  as "et al."); do not revert to a literal "et al." string (it breaks the ACM `.bst`).
- Retired artifacts (old markdown pipeline, converters, drafts, Word/arXiv bundles) are
  in `../_backup/`; verified corpus and §6 audit data in `../corpus/`, `../experiments/`.
