# Camera-ready TODO (known items before final CSUR submission)

The manuscript is review-ready in content. These are the remaining production items,
stated honestly so a reviewer/coauthor knows what is pending:

1. **§6 empirical results.** The cross-framework bias audit is specified as a protocol;
   numerical results are pending execution and will be added. All abstract/intro/§6/§9
   language is deliberately protocol-only ("we specify", "designed to surface",
   "Results: pending") — no results are claimed.

2. **Figure instantiation.** Figure 2 (coverage matrix) and Figure 3 (locus × operator
   grid) appear as rendered tables in §7. **Figure 1 (the taxonomy tree)** is specified
   in `FIGURES.md` (a LaTeX `forest` diagram + text fallback) and must be instantiated
   as a float for the typeset version. Tables 0–4 are already rendered in the text.

3. **ACM `acmart` port.** `paper_pdf.tex` is a self-contained article-class LaTeX that
   compiles to the included PDF (used for review). The final submission should be ported
   to the ACM `acmart` class with CCS concepts and keywords.

4. **Citation attribution spot-check (done; keep current).** arXiv IDs are
   machine-verified (`corpus/VERIFY_RESULTS.md`). External review (Codex) flagged a few
   attribution nuances that have been addressed: `blankenstein2025biasbusters` is now
   cited only for tool/provider-selection bias (not protected-attribute disparity);
   `dwork2012fairness` is explicitly placed under individual fairness; the Chu et al.
   venue is named as SIGKDD Explorations (not CSUR); deployment claims are hedged to
   "deployed, piloted, and evaluated".
