# Fairness and Equity in LLM-Based Agents: A Taxonomic Survey

**Canonical authoring home for this paper.** (Strategic command center — decisions,
scoop watch, pipeline — remains at `../research-command-center`, which also holds a
pushed backup snapshot of this paper under `06_paper_pipeline/AGENT_FAIRNESS_SURVEY/`.)

- **Authors:** Rohith (first & corresponding) · Dr. Wenbin Zhang (FIU, senior anchor)
- **Venue:** ACM SIGKDD Explorations Newsletter (survey track)
- **Status:** v1 draft assembled + citation-verified · target arXiv v1 ~Sept 2026

## Map
| File | What |
|---|---|
| `AGENT_FAIRNESS_SURVEY.md` | Assembled full draft (~14.8K words, ~15–16 ACM double-col pp) |
| `main.tex` | ACM `acmart` LaTeX scaffold (port from the markdown) |
| `references.bib` | 127 verified references (0 hallucinated) |
| `drafts/` | Per-section markdown (01–09) |
| `corpus/` | Master corpus, coverage matrix, and the arXiv-API verification results |
| `OUTLINE.md` · `PROTOCOL.md` | Structure + positioning, honesty bar, phase status |
| `FIGURES.md` | Taxonomy tree + coverage-matrix specs + 5 tables |
| `PITCH_FOR_ZHANG.md` | 1-page co-author pitch (+ internal review note, July-15 gate) |
| `ARXIV_CHECKLIST.md` · `CITE_AUDIT.md` | Submission readiness + citation integrity |
| `scripts/auto_commit_push.py` | Local commit/push helper (push is a no-op until a remote is added) |

## Rebuild commands
```
python corpus/build_corpus.py      # dedup corpus -> master + references.bib + coverage matrix
python corpus/verify_citations.py  # re-check every arXiv id against the arXiv API
python build_latex.py              # regenerate main.tex from the assembled markdown
python scripts/auto_commit_push.py # commit + push (add a remote first to enable push)
```

## Remaining path to arXiv
1. **Run the §6 empirical audit** (moderation insurance — scheduled 2026-06-12) so it
   clears arXiv as "survey + original results."
2. Render Figures 1–2; hand-clean the LaTeX port (tables, lists, math).
3. Zhang co-author + arXiv-first by the **2026-07-15** gate.

> To enable backup pushes: `git remote add origin <url>` then
> `python scripts/auto_commit_push.py`.
