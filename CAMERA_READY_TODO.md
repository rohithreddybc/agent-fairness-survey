# Status & remaining items

## Ready now (arXiv-postable)
- Manuscript complete: BCF framework, §3 critical synthesis, §4 action-level metric
  equations, §5 mitigation map, **§6 pilot bias-audit results** (decision-level parity
  with score-level MASD rising 1.2→3.4→6.4 across C0/C2/C3; directional, heavily
  caveated), §7 coverage matrices, §8 governance-anchored agenda, §9 + §9.1 ethics.
- **202 verified references** (0 arXiv not-found). 168 cited, 0 missing. Em-dash-free.
- **Figure 1 (taxonomy tree) now rendered** in the PDF (TikZ/forest). Figures 2 and 3
  render as tables in §7. Tables 0–4 in text.
- **arXiv bundle ready**: `experiments/`… and the submission source under
  `arxiv_submission/` (`main.tex` self-contained, compiles with pdflatex; metadata in
  `00_ARXIV_METADATA.md`: primary cs.CY, cross-list cs.AI/cs.CL/cs.LG).
- PDF (63 pp) + DOCX exported.

## Gating step (not a production item)
- **Zhang co-author + arXiv-first sign-off.** Package drafted (`ZHANG_SIGNOFF_EMAIL.md`
  in the working repo). Target post date June 26; solo-proceed gate 2026-07-15. The
  manuscript byline carries Zhang, so posting needs his consent — this is the only true
  blocker. Awesome-list flips public on post day.

## Deferred to v2 / CSUR camera-ready (intentionally not done now)
- Larger **confirmatory audit** (bigger N; name pairs decoupling race/gender; borderline
  profiles to break the decision ceiling; tool-using configs for tool-invocation and
  escalation disparity; CIs and significance tests). v2 material; do not delay v1 for it.
- **ACM `acmart` port** with CCS concepts/keywords — required for CSUR submission, not
  for arXiv. `arxiv_submission/main.tex` is article-class for the preprint.
- Figures 2/3 as TikZ heatmaps (currently clean tables); appendix relocation of long
  tables for CSUR readability.
