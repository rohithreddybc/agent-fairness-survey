# Adjudication of screener candidates not present in the corpus

Run 2026-08-24. Inputs: `_adjudicate_input.tsv` (32 records: branch, arXiv id, title, abstract).

## What this is

The retrospective second screen (§2.5) disagreed with the corpus almost entirely in one
direction: it admitted records the corpus lacks, and rarely rejected records the corpus holds.
That shape has two readings — a lenient screener, or a corpus that under-collects — and the
kappa alone cannot separate them. This exercise separates them.

## Method

From the 300 records screened under one identical strict prompt (branch groups B4/B5/B6 and
B10/B11 — the only groups that used the same instruction and are therefore comparable), the
screener admitted 36. Of those, 32 are absent from the corpus. Each of the 32 was adjudicated
individually against the §2.4 inclusion criteria: an LLM as primary reasoning component; a
fairness question about people rather than a technical sense of "bias"; and findings bearing on
one of the six loci, or reaching them through the transferable-mechanism clause.

Each verdict records the deciding criterion, the locus if any, and the phrase from the abstract
that settles it.

## Result

| Verdict | Count |
|---|---|
| GENUINE_MISS — in scope by our criteria, should have been found | 20 |
| FALSE_POSITIVE — screener over-read | 7 |
| BORDERLINE — abstract does not settle it | 5 |
| **Total** | **32** |

Screener false-positive rate on this set: **7/32, roughly one in five.**

So the leniency reading is real but partial. It explains about a fifth of the disagreement and
cannot explain the remainder. **The corpus under-collects**, and the rate is now measured rather
than inferred.

## Where the misses fall

Concentrated in two loci:

- **C3, multi-agent delegation** — 7 records. Code-generation bias under role-scoped multi-agent
  frameworks, dialect-stereotype mitigation via generate-critique-revise architectures,
  redistricting agents representing opposing interests, cross-cultural negotiation between
  regional agents, role-based feedback agents with a dedicated equity monitor.
- **C5, user modeling and personalisation** — 7 records, plus 2 shared with C2. Recommendation
  fairness across demographic attributes, digital twins of survey respondents, personalised
  advice varying by national language, persona-conditioned preference work.
- **C2, memory and retrieval** — 2 records plus the 2 shared. Retrieval-stage disparity in resume
  ranking; case-retrieval prompting in clinical prediction.
- **C4** and the **temporal axis** — 1 each.

The corpus holds twelve papers in each of C3, C5 and C2, so these are large relative gaps.

## The pattern behind them

The recurring miss is a study whose fairness object is a persona, a recommendation, or a role
assignment rather than a tool call. Such work satisfies criterion (iii) through the
transferable-mechanism clause, but a recall-oriented query built around agentic vocabulary
("tool", "agent", "trajectory") does not surface it. The failure is in the search strings, not
in the screening judgement.

## The false positives, for contrast

The 7 confirmed over-reads fall into two narrow patterns the criteria explicitly warn about:

- **Technical "bias" mistaken for demographic fairness** — self-consistency metrics for
  LLM-as-judge verification; neuron-pruning work bundling "fairness" with inconsistency drift and
  naming no protected attribute.
- **Keyword matches with no substantive finding** — broad recommender-system surveys listing
  "unfairness and bias" among challenges; generic chatbot audits with no mechanism connecting
  them to any locus.

Both are failure modes of speed, not of criteria, which is consistent with a screener working
fast rather than one applying a different standard.

## Consequences for the manuscript

Reported in §2.5. Two claims are scoped as a result: per-locus counts for C3 and C5 are floors
with a wider gap to the true literature than the untested loci; and row counts must not be read
as a census of what exists, only as a statement about what this corpus contains. Column-level
claims are *not* unaffected, and an earlier version of this memo said they were. An
uncollected paper is exactly what would put an entry in a column the survey reports as empty,
so the column counts are the claims most exposed to under-collection. What under-collection
cannot do is inflate a cell, so every count is a floor.

## Caveat on this exercise

**Correction (2026-11-09, first author).** The first sentence of the paragraph below is wrong: the
adjudication of the 32 candidates was carried out by human review against the §2.4 criteria, not by
an LLM. The paragraph is kept as originally written so the record of the error stays visible; the
remaining caveat about per-record verdicts still applies.

The adjudication is a second LLM pass, not human review. It is more reliable than the fast screen
that produced the candidates — close reading of disputed cases, one at a time, with reasoning
written out — but it is the same class of instrument. The per-record verdicts were not retained in a
publishable form, so the split above is this memo's summary and not a table a reader can
audit record by record; that is a limitation of the exercise, not a property of it. A human adjudication of the same 32 would supersede it.
