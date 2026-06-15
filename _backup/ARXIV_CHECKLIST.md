# arXiv-readiness checklist — Agent-Fairness Survey

Target: arXiv v1 by ~Sept 2026 (first beats best; v1 at ~70%, v2 expands).

## Moderation insurance (the binding constraint)
- [ ] **Original empirical section present and run** (§6 cross-framework audit) —
      arXiv now declines pure surveys. v1 MUST contain real (even if small) results,
      not just a protocol. *Status: §6 drafted as protocol; the audit run is the
      gating to-do before submission.*
- [ ] Abstract + intro explicitly frame it as "survey **with** an original audit."
- [ ] Backup if held: Zhang submits/endorses from his account; else TechRxiv/SSRN.
- [ ] Primary category `cs.CL` or `cs.CY`; cross-list `cs.AI`, `cs.LG`.

## Content completeness
- [ ] All 9 sections assembled (`AGENT_FAIRNESS_SURVEY.md`).
- [ ] Figure 1 (taxonomy tree) + Figure 2 (coverage matrix) rendered.
- [ ] Tables 0–3 populated from the corpus.
- [ ] Contributions list (5) in the intro; thesis = organize by agent component.
- [ ] Positioned vs. chu2024fairness, mohammadi2025evaluation, vatsal2026agentic,
      mayilvaghanan2026counterfactual.

## Citation integrity (ZERO hallucinations — the survey-killer)
- [x] All 122 arXiv IDs resolve against the arXiv API (`corpus/VERIFY_RESULTS.md`:
      0 NOT_FOUND). DOI-only entries (5) are well-known real papers.
- [ ] Final pass: every `\cite{key}` in the assembled draft exists in
      `references.bib` (run a key-diff before submit).
- [ ] Spot-check that each cited claim matches the cited paper's actual finding.
- [ ] Author/year/venue fields correct (esp. the 14 recent-2026 entries in
      `corpus/VERIFY_QUEUE.md`).

## ACM / formatting
- [ ] Port markdown → `acmart` (double-column, `sigconf` or Explorations style).
- [ ] `references.bib` compiles with BibTeX; no missing fields warnings that break.
- [ ] Authors + affiliations + corresponding author (Rohith) + Zhang (FIU).
- [ ] ~15–20pp double-column; trim or move to appendix if over.
- [ ] ACM CCS concepts + keywords.

## Companion artifacts (citation multipliers — do in week 1)
- [ ] "Awesome-Agent-Fairness" GitHub repo under Rohith's org (living paper list).
- [ ] Project page; dataset/repo names registered.
- [ ] Link the repo from the abstract footnote.

## Process / governance
- [ ] Zhang co-author + arXiv-first confirmed (gate: 2026-07-15).
- [ ] DECISIONS.md updated; auto-commit clean.
- [ ] Scoop watch active ("fairness/bias/equity + agent").

## Known v1→v2 deferrals (state honestly in the draft)
- Empirical audit may ship as a pilot in v1, expanded in v2.
- Figures may be text/table form in v1 if TikZ time-constrained.
- Intersectional + non-English coverage to deepen in v2.
