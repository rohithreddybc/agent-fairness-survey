# CSUR acceptance goal + self-prompt (review→revise→ship)

**GOAL (set 2026-06-11):** Revise "Fairness and Equity in LLM-Based Agents: A
Taxonomic Survey" to maximize probability of acceptance at **ACM Computing Surveys
(CSUR)**. *Honesty: no one can guarantee 100% acceptance; the aim is to remove every
fixable reason a CSUR reviewer would reject, and to be honest about residual risk.*

**Venue change:** target is now **CSUR** (was SIGKDD Explorations). SIGKDD
Explorations remains the faster fallback; revising to CSUR's higher bar also
satisfies Explorations. Consistent with the decision file's "→ ACM CSUR/TMLR for the
archival stamp."

## What CSUR acceptance requires (the bar we revise against)
1. **An original organizing FRAMEWORK**, not an annotated bibliography. The
   agent-component taxonomy must demonstrably *explain/predict* and yield
   propositions — not just categorize. (Addresses the ChatGPT note directly.)
2. **Critical synthesis**, not paper-by-paper summary.
3. **Comprehensive + current** coverage, incl. all relevant **ACM** prior work and
   recent (2025–2026) competing surveys — found via live web + ACM DL, not only
   Consensus.
4. **Explicit differentiation** vs every similar survey; if we are not clearly
   different, *modify our paper* until we are.
5. **Survey-craft completeness:** review methodology/protocol, comparison-to-prior-
   surveys table, trend analysis, challenges→solutions→gaps mapping, glossary,
   threats-to-validity of the survey, ethics/limitations, practitioner/regulator guide.
6. **Every figure/table carries an explicit "Takeaway:"** line.
7. Zero hallucinated/incorrect citations (already machine-verified; re-verify any new).

## Self-prompt / orchestration plan (this pass — running NOW, not scheduled)
- **Phase A (recon+review, parallel):** 6 agents — recent-web-surveys, acm-dl-scan,
  csur-readiness-review (Fable), framework-originality (Fable), figure-table-takeaways,
  completeness-gaps. → `reviews/` + a synthesized revision plan. *(run wf_b74d61df-666)*
- **Phase B (verify new prior-art):** machine-verify any newly found papers (arXiv
  API / DOI) before citing; drop unverifiable ones.
- **Phase C (revise, parallel by section):** strengthen the framework (Phase A spec),
  add differentiation table + new ACM/recent citations, add per-figure/table takeaways,
  fill the survey-craft gaps, tighten prose. Mid models for prose, Fable for the
  framework §3 + intro positioning.
- **Phase D (re-verify):** re-assemble, re-run the cite audit (0 missing), confirm
  differentiation holds.
- **Phase E.5 (humanize):** run the `humanizer` / `myhumanizer` / `undetectable`
  skills over the prose to strip AI-writing tells (em-dash overuse, rule-of-three,
  promotional tone, copula avoidance, negative parallelisms, uniform burstiness)
  while PRESERVING citations, numbers, technical accuracy, and academic register;
  honor the non-native-author false-positive protocol. Re-run the cite audit after
  to confirm no `\cite` keys changed. The humanized text becomes the export source.
- **Phase E (export):** compile `main.tex` → **PDF** (pdflatex/MiKTeX); build **Word**
  (python-docx).
- **Phase F (ship):** commit to a **PRIVATE GitHub repo**, author = Rohith, **no
  Claude co-author / no AI co-author trailer**.

## Coordination with the previously-scheduled run
The one-time task `agent-fairness-survey-audit-and-repo` (fires 2026-06-12 00:50 EDT)
runs the §6 empirical audit + builds the public awesome-list repo. This pass keeps a
clear `Results (to be completed)` placeholder in §6 so that run can still fill real
numbers; it does not conflict.

## Resourcing rule
Use **Fable only when necessary** (framework design, CSUR-level judgment, final
synthesis/citation verification); Sonnet/Haiku for scans, inventories, body prose.
