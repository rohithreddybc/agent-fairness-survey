# Re-executed screen, August 2026 — working notes

NOT YET REPORTED IN THE MANUSCRIPT. Nothing here has been written into main.tex.

## What this is

The original screen ran to saturation and its per-record decisions were not logged, so the
PRISMA figure reports no screening or full-text count. This is an attempt to supply real
counts by re-executing the screen against a defined, bounded pool with every decision logged.

## Pool construction

Top relevance-ranked records per branch from the ten executed arXiv branch queries of
SEARCH_LOG_2026-08-17.md. Queries verbatim in _branch_queries.json; fetch script
_fetch_screen_pools.py. Pools: _pool_grp{B1,B4,B7,B10}.tsv, 580 records total.

## Screening

Blind: each screener saw only branch, arXiv id, title and abstract. No access to the corpus,
the bibliography or the manuscript. Same six reason codes throughout
(IN_SCOPE / NO_FAIRNESS / NON_LLM / NOT_AGENT_RELEVANT / SINGLE_TURN_NO_TRANSFER / POST_CUTOFF).
Results: _screen_grp{B1,B4,B7,B10}_results.tsv.

## Status at last checkpoint

280 of 580 screened (groups B1 and B7). Groups B4 and B10 were interrupted by a session limit
and relaunched.

Interim: 111 unique INCLUDE, of which 20 are in the corpus and 91 are not.
B3 returned 48 of 60 includable against a corpus holding 9 multi-agent papers.

## The unresolved question, which blocks reporting any of this

These numbers cannot be dropped into the PRISMA figure. The corpus was not built from this
pool, so labelling them as the original screening stage would be false, and they contradict
the 202 anyway.

More fundamentally, they do not distinguish two explanations, exactly as the earlier
kappa = 0.28 result did not:

  (a) the LLM screener applies the criteria more liberally than the original human screen, or
  (b) the corpus genuinely under-collects.

The earlier second screen gives direct evidence that (a) is at least partly true: that screener
rejected mayilvaghanan2026counterfactual, a key near-neighbour that belongs in the corpus. Its
INCLUDE set is therefore a candidate list, not ground truth, and the same caution applies here.

## What would resolve it

Human adjudication of a random sample of the not-in-corpus INCLUDEs against the S2.4 criteria,
yielding a false-positive rate for the screener. With that rate, either:
  - most are genuinely in scope, and the corpus needs extending before submission; or
  - most are screener noise, and kappa = 0.28 can be reported as a quantified and defended
    limitation rather than an open one.

Until that adjudication exists, the honest options are to report this as a completeness audit
with the ambiguity stated, or not to report it. Fabricating screening counts for the figure is
not among them.

---

## Outcome: this exercise does NOT supply the PRISMA counts. Abandoned as a source of figures.

All 580 records are screened, but the result is not usable, for two independent reasons.

### 1. The four groups did not apply the same criteria (my error)

| group | include rate | SINGLE_TURN_NO_TRANSFER | prompt |
|---|---|---|---|
| B1/B2/B3 | 89/160 = 56% | 0 | earlier session |
| B7/B8 | 51/120 = 42% | 6 | earlier session |
| B4/B5/B6 | 27/180 = 15% | 33 | added explicit strictness instruction |
| B10/B11 | 9/120 = 8% | 33 | added strictness + branch-specific notes |

The second batch was written with "be strict and consistent, over-inclusion destroys the
measurement, when uncertain choose EXCLUDE" and, for B10/B11, extra branch-specific guidance.
The first batch had neither. A three-to-sevenfold difference in include rate, and the
lopsided use of one exclusion code, track the prompt rather than the branches. Pooling these
would measure the instruction wording, not the literature.

Fixing this would mean re-screening all 580 under one identical prompt. That is doable, but it
would not fix reason 2.

### 2. Even a consistent re-run could not fill the figure's blanks

The corpus was not assembled from this pool. Labelling any count from it as the original
screening stage would be false, and the totals contradict the 202 regardless. The exercise can
measure what a defined query pool yields today; it cannot recover what was screened in the
past and never recorded.

### Conclusion

"Count not logged" stays in the PRISMA figure, because it is true. The alternative on offer was
a fabricated number, and fabricated counts are the specific defect this manuscript has already
had to remove twice: the venue distribution fitted to sum to 202, and the original search funnel
whose stages were asserted rather than executed.

The pools, queries, fetch script and all four result sets remain committed as a record of the
attempt and of why it was not used.

### What is still worth doing with this data

The 300 records screened under the strict prompt (groups B4 and B10) are internally consistent
with each other. They are not a PRISMA count, but they are a usable completeness probe if
someone adjudicates a sample by hand: of their 36 includes, the ones absent from the corpus are
the candidate misses worth a human decision.
