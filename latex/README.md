# LaTeX source — canonical working copy

`main.tex` is now the **single source of truth** for the paper (ACM `acmart`,
`acmsmall` / CSUR journal format). Edit it directly; the markdown is retired.

## Files
- `main.tex` — the manuscript (self-contained: TikZ Figure 1, tables for Figures 2-3 and Tables 0-4, inline math).
- `references.bib` — bibliography (202 entries; 168 cited).
- `main.bbl` — pre-built, ACM-Reference-Format, already patched (168 bibitems). Lets you compile without re-running BibTeX.
- `main.pdf` — current output (≈67-68 pp).

## Compile
Prose-only edits (citations unchanged) — two passes, no BibTeX needed:
```
pdflatex -interaction=nonstopmode main
pdflatex -interaction=nonstopmode main
```
If you add/remove/change a `\cite`, regenerate the bibliography:
```
pdflatex main && bibtex main && pdflatex main && pdflatex main
```
Note: ACM-Reference-Format can emit a few `\natexlab{}` artifacts in `main.bbl`
for preprint entries; the patch that cleans them lives in
`../_backup/build_acm.py` (run it, or fix the `.bbl` by hand) only if you re-run BibTeX.

## Provenance / archive
The retired markdown pipeline (the old `AGENT_FAIRNESS_SURVEY.md`, the md→LaTeX/Word
converters, drafts, review notes, the article-class arXiv bundle) is in `../_backup/`.
The verified corpus and the §6 pilot data remain alongside (`../corpus/`, `../experiments/`).
