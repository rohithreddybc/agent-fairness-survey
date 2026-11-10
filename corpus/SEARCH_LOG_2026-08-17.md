# Executed search log — 2026-08-17

Every number in this file was produced by an executed query on the date shown, not
estimated or reconstructed. Queries are reproducible verbatim.

- **arXiv**: queried via the public arXiv API (`http://export.arxiv.org/api/query`),
  counts read from `<opensearch:totalResults>`.
- **Scopus**: queried via Scopus Advanced Search (authenticated institutional session),
  counts read from the "N documents found" result header.
- Scopus queries are bounded `AND PUBYEAR BEF 2027`. arXiv queries are unbounded in date
  (the API has no clean date bound); the corpus cutoff is applied at screening.

---

## 1. Branch queries — identification counts

| Branch | arXiv query (`search_query=`) | arXiv hits | Scopus query (`TITLE-ABS-KEY(...) AND PUBYEAR BEF 2027`) | Scopus hits |
|---|---|---|---|---|
| B1 Tool / API selection | `(abs:"tool selection" OR abs:"tool use" OR abs:"function calling" OR abs:"API selection") AND (abs:bias OR abs:fairness) AND (abs:"language model" OR abs:LLM)` | 38 | `("large language model" OR LLM) AND agent* AND (bias OR fairness OR unfair*) AND ("tool selection" OR "tool use" OR "tool-calling" OR "function calling" OR "API selection")` | 9 |
| B2 Memory & retrieval | `(abs:"retrieval-augmented" OR abs:RAG OR abs:memory) AND (abs:bias OR abs:fairness) AND (abs:"language model" OR abs:LLM)` | 447 | `("large language model" OR LLM) AND ("retrieval-augmented generation" OR RAG OR retrieval OR memory) AND (bias OR fairness OR unfair*)` | 1054 |
| B3 Multi-agent delegation | `(abs:"multi-agent" OR abs:persona OR abs:"role assignment") AND (abs:bias OR abs:fairness) AND (abs:"language model" OR abs:LLM)` | 348 | `("large language model" OR LLM) AND ("multi-agent" OR multiagent OR delegation OR "role assignment" OR persona) AND (bias OR fairness OR unfair*)` | 480 |
| B4 Planning / decomposition | `(abs:planning OR abs:reasoning OR abs:"chain-of-thought") AND (abs:bias OR abs:fairness) AND abs:agent AND (abs:"language model" OR abs:LLM)` | 298 | `(planning OR reasoning OR "chain-of-thought") AND (bias OR fairness) AND agent* AND ("large language model" OR LLM)` | 300 |
| B5 User modeling / personalization | `(abs:personalization OR abs:"user modeling" OR abs:dialect) AND (abs:bias OR abs:fairness) AND (abs:"language model" OR abs:LLM)` | 360 | `(personalization OR "user modeling" OR dialect) AND (bias OR fairness) AND ("large language model" OR LLM)` | 250 |
| B6 Long-horizon drift | `(abs:"long-term fairness" OR abs:"feedback loop" OR abs:sycophancy OR abs:"multi-turn") AND (abs:bias OR abs:fairness) AND (abs:"language model" OR abs:LLM)` | 163 | `("long-term fairness" OR "feedback loop" OR sycophancy OR "multi-turn") AND (bias OR fairness) AND ("large language model" OR LLM)` | 107 |
| B7 Evaluation & benchmarks | `(abs:benchmark OR abs:evaluation OR abs:audit) AND (abs:fairness OR abs:bias) AND abs:agent AND (abs:"language model" OR abs:LLM)` | 523 | `(benchmark OR evaluation OR audit) AND (fairness OR bias) AND agent* AND ("large language model" OR LLM)` | 401 |
| B8 Mitigation | `(abs:debiasing OR abs:mitigation) AND (abs:fairness OR abs:bias) AND abs:agent AND (abs:"language model" OR abs:LLM)` | 158 | `(debiasing OR mitigation) AND (fairness OR bias) AND agent* AND ("large language model" OR LLM)` | 82 |
| B10 High-stakes domains | `(abs:hiring OR abs:clinical OR abs:lending OR abs:judicial) AND (abs:bias OR abs:fairness) AND (abs:"language model" OR abs:LLM)` | 332 | `(hiring OR clinical OR lending OR judicial) AND (bias OR fairness) AND ("large language model" OR LLM)` | 1423 |
| B11 Prior-art / neighbour surveys | `(abs:survey OR abs:review) AND (abs:fairness OR abs:bias) AND abs:agent AND (abs:"language model" OR abs:LLM)` | 84 | `(survey OR review) AND (fairness OR bias) AND agent* AND ("large language model" OR LLM)` | 231 |
| **Total** | | **2751** | | **4337** |

Branch B9 (Foundations) is populated by backward citation chasing from named anchor
papers, not by a database query, and so has no row here.

Additional whole-field reference query, Scopus:
`TITLE-ABS-KEY(("large language model" OR LLM) AND agent* AND (fairness OR bias OR unfair*)) AND PUBYEAR BEF 2027`
→ **983 documents**.

These counts are recall-oriented and heavily off-target; they are the identification
pool, not a screened set. The two databases overlap substantially, so the totals are
not additive.

---

## 2. Scopus coverage of the final corpus — measured, not assumed

**Method.** Systematic 1-in-7 sample of `corpus/corpus_master.md` (rows 1, 8, 15, …,
197), N = 29. Each sampled paper was queried in Scopus by a distinctive title phrase
using `TITLE("…")`. A paper counts as indexed if the query returns ≥ 1 document.

**Result: 22 / 29 indexed = 75.9%.**

| # | Title phrase queried | Scopus hits | Indexed |
|---|---|---|---|
| 01 | Bias and Fairness in Large Language Models | 3 | yes |
| 02 | The Rise and Potential of Large Language Model Based Agents | 1 | yes |
| 03 | Holistic Descriptor Dataset | 1 | yes |
| 04 | Toolformer | 3 | yes |
| 05 | BiasBusters | 0 | **no** |
| 06 | Bias-Aware Agent | 1 | yes |
| 07 | Unmasking Conversational Bias | 0 | **no** |
| 08 | Effect of Retrieval Augmentation on Social Biases | 1 | yes |
| 09 | Persona-Induced Bias | 1 | yes |
| 10 | Does Reasoning Introduce Bias | 1 | yes |
| 11 | Assessing Dialect Fairness and Robustness | 1 | yes |
| 12 | Achieving Long-Term Fairness in Sequential Decision Making | 1 | yes |
| 13 | Adapting Static Fairness to Sequential Decision-Making | 1 | yes |
| 14 | Evaluating Biases in LLMs with Counterfactual Reasoning | 0 | **no** |
| 15 | FairMedQA | 0 | **no** |
| 16 | Causal-Guided Active Learning for Debiasing | 1 | yes |
| 17 | Multi-Objective Approach within a Multi-Agent Framework | 1 | yes |
| 18 | Fairness of ChatGPT | 1 | yes |
| 19 | Coding Inequity | 0 | **no** |
| 20 | Optimization of Large Language Model-based Agents | 1 | yes |
| 21 | Limitations of Large Language Models | 48 | yes (generic phrase) |
| 22 | Responsible Agentic Reasoning | 0 | **no** |
| 23 | Fairness in Ranking | 19 | yes (generic phrase) |
| 24 | Stereotyping Norwegian Salmon | 1 | yes |
| 25 | Surveying the Horizons of Multimodal Interaction | 0 | **no** |
| 26 | TrustLLM | 2 | yes |
| 27 | Preferred Reporting Items for Systematic Reviews | 53 | yes (generic phrase) |
| 28 | Mitigating Bias in Algorithmic Hiring | 1 | yes |
| 29 | Always Say What They Think | 1 | yes |

**Sensitivity.** Rows 21, 23 and 27 matched on a generic phrase, so the specific corpus
paper cannot be confirmed to be among the hits. Treating all three as misses gives a
conservative lower bound of **19 / 29 = 65.5%**. Reported coverage is therefore
**66–76%**.

**Structure of the misses.** All 7 confirmed misses are 2025–2026 arXiv-only preprints
(BiasBusters, Unmasking Conversational Bias, MEDEQUALQA, FairMedQA, Coding Inequity,
Responsible Agentic Reasoning, Agent AI). The gap is not random: it is concentrated in
exactly the recent agentic-fairness frontier the survey is about. A Scopus-only
identification protocol would have systematically missed the newest primary evidence.

---

## 3. Corpus metadata verification (pre-existing, `corpus/VERIFY_RESULTS.md`)

Automated resolution against the arXiv API:

- arXiv-identified papers checked: **177**
- Resolved with matching title: **175**
- Title mismatch (both manually confirmed correct, differing published vs. preprint title): **2**
- Not found: **0**
- DOI-only / no-identifier papers requiring manual check: **24**

---

## 3b. Corpus composition figures (recomputed from `corpus_master.md`, 2026-08-17)

All computed directly from the 202 rows of `corpus/corpus_master.md`.

**Publication year** (from the `Yr` column):

| Bucket | Count | Share |
|---|---|---|
| pre-2020 | 18 | 9% |
| 2020–2022 | 24 | 12% |
| 2023 | 29 | 14% |
| 2024 | 57 | 28% |
| 2025–2026 | 74 | 37% |
| **Total** | **202** | |

Combined 2024–2026 = 131 = 65%. Corpus year range is **2009–2026** (the earliest record is
the PRISMA statement, `moher2009preferred`).

**Peer-review status.** Two different rules give two different (both defensible) figures.
They must not be conflated:

- **Bare arXiv venue category — 62 (31%).** Venue field is exactly `arXiv preprint`,
  `ArXiv preprint`, or `arXiv` (48 + 7 + 7).
- **No peer-reviewed venue named — 70 (35%).** The above, plus arXiv postings whose venue
  string carries an appended arXiv ID (5), a TechRxiv/IEEE preprint (1), a
  ResearchGate/unpublished posting (1), and one ICLR submission not reported as accepted
  (1). Excludes the two `arXiv preprint (ICLR 20XX workshop)` records and the
  `EMNLP 2024 (arXiv preprint 2023)` record, all of which name an accepted venue.

The paper reports 31% in §2.6 (venue category) and 35% in §2.5 (evidentiary weight), and
says explicitly that these are different measurements.

**ACM Computing Surveys papers in corpus: 16** (exact venue-string match). The paper
previously said 10; corrected.

**FAccT papers in corpus: 8** (venue matches `FAccT` or `Fairness, Accountability`). The
paper previously said 9; corrected.

**Venue distribution.** The previously reported distribution (arXiv 62, ACL-family 41,
NeurIPS/ICML/ICLR 28, ACM 24, domain 19, remaining 28) summed to 202 but did not survive
recomputation: only the bare-arXiv figure was correct. The categories below are disjoint,
computed by priority-ordered matching on the venue field, and sum to 202:

| Category | Count | Share |
|---|---|---|
| No peer-reviewed venue named | 70 | 35% |
| ACM venues (incl. Computing Surveys 16, FAccT 8, KDD, SIGIR, CIKM, WWW, UIST) | 39 | 19% |
| ML conferences (NeurIPS, ICML, ICLR, TMLR) | 31 | 15% |
| ACL-family (ACL, EMNLP, NAACL, EACL, Findings, *Computational Linguistics*) | 30 | 15% |
| Science / medical / IEEE (*Science*, *Nature Medicine*, *Lancet Digital Health*, PNAS Nexus, *PLoS Medicine*, *Annals NYAS*, IEEE Access, IEEE ICSE) | 10 | 5% |
| Other (AAAI, IJCAI, AIES, ITCS, *Frontiers of Computer Science*, *JASA*, *Big Data*; books, standards, regulatory sources) | 22 | 11% |
| **Total** | **202** | |

Percentages are rounded independently and therefore sum to 100 only by coincidence; check
counts, not shares.

Note: an earlier draft of this table put the science/medical bucket at 13 and Other at 19.
That split was produced by a regex that captured "Theoretical Computer Science" (ITCS) and
*Frontiers of Computer Science* as science venues. Corrected above; the two buckets are
complementary so the total is unaffected.

**Verification accounting.** 177 arXiv-resolved + 24 manual DOI checks = 201. The 202nd
record is `moher2009preferred`, the PRISMA methodology citation. It carries a valid DOI
(10.1371/journal.pmed.1000097); it sits outside both verification groups by editorial
choice, because it is a methods reference rather than surveyed fairness evidence, not
because it lacks a resolvable identifier.

---

## 3c. Retrospective second screen (2026-08-17)

**Purpose.** The corpus was built without a formally independent dual-rater screen. This
exercise retrospectively measures the resulting risk instead of only acknowledging it.

**Method.** The 35 relevance-ranked records returned by the evaluation-and-benchmarks
branch query (B7) were taken as the candidate set, in `_screen_pool.tsv` (columns: branch,
arXiv id, title, abstract). All indication of corpus membership was withheld. An
independent LLM-based screener (Claude Sonnet, no access to the corpus, bibliography or
manuscript) applied the §2.4 inclusion criteria to each title and abstract and returned
INCLUDE/EXCLUDE per record. Per-record results in `_screen_round2_results.tsv`.

Rater 1 = the original screening decision, operationalised as corpus membership.
Rater 2 = the LLM screener.

**Temporal-scope caveat.** The candidate file carried no publication dates, so the screener
could not apply criterion (v). Four records are outside the June 10 2026 cutoff (2607.08681,
2608.06949, 2608.02827, and 2606.14474). The primary analysis excludes them; both are reported.

**Results.**

| | | All 35 | In-scope 31 |
|---|---|---|---|
| Both INCLUDE | | 6 | 6 |
| Rater 1 INCLUDE, Rater 2 EXCLUDE | | 1 | 1 |
| Rater 1 EXCLUDE, Rater 2 INCLUDE | | 14 | 11 |
| Both EXCLUDE | | 14 | 13 |
| Observed agreement $P_o$ | | 0.571 | 0.613 |
| Expected agreement $P_e$ | | 0.457 | 0.473 |
| **Cohen's $\kappa$** | | **0.21** | **0.26** |

Both values fall in the "fair" band (Landis & Koch 0.21–0.40) and below what a dual-human
protocol would be expected to yield.

**Interpretation.** Disagreement is nearly one-directional: 11 records the second screener
would admit against 1 it would reject. This is the signature of screening to saturation
(the original screen stopped early) rather than of differing judgement. Note also that the
single rejection is `mayilvaghanan2026counterfactual`, a genuine agentic-fairness study and
one of the survey's key near-neighbours — i.e. rater 2 produces false negatives too, and
its INCLUDE set should not be treated as ground truth.

**11 in-scope candidate additions** (not currently in the corpus; 8 of the 11 are
multi-agent/C3, a branch currently holding only 9 papers):

| arXiv | Title |
|---|---|
| 2603.17179 | Ablation Study of a Fairness Auditing Agentic System … Early-Onset Colorectal Cancer Detection |
| 2605.00382 | Social Bias in LLM-Generated Code: Benchmark and Mitigation |
| 2601.12091 | Mitigating Cultural Bias in LLMs via Multi-Agent Cultural Debate |
| 2501.05396 | FairCoder: Probing LLM Bias in High-Stakes Decision Making via Coding Tasks |
| 2605.28098 | Examining Agents' Bias Amplification versus Suppression in Multi-Agent Systems |
| 2411.07656 | Mitigating Bias in Queer Representation within LLMs: A Collaborative Agent Approach |
| 2503.00355 | Structured Reasoning for Fairness: A Multi-Agent Approach to Bias Detection in Textual Data |
| 2603.16215 | CoMAI: A Collaborative Multi-Agent Framework for Robust and Equitable Interview Evaluation |
| 2506.13245 | A Game-Theoretic Negotiation Framework for Cross-Cultural Consensus in LLMs |
| 2605.28114 | Language model agents show in-group trust bias invisible to standard behavioural audits |
| 2606.01584 | Identifying High-Confidence Social Biases in LLMs for Trustworthy Conversational Tutoring Agents |

`2605.28114` is notable: demographic bias in agent *behaviour* that output-level audits
miss is the survey's own P2 masking claim, arriving as evidence the corpus had not collected.

**Scope of this exercise.** One branch, 35 records, one LLM screener. It is a measurement
of the limitation, not a repair of it, and it does not license removing the
single-screener caveat from the manuscript.

---

## 4. Known limitations of this protocol

1. **No independent dual-rater screen at build time.** Title/abstract screening and
   full-text inclusion were performed without a second independent rater. The
   retrospective second screen of §3c measures the consequence rather than removing it:
   Cohen's kappa = 0.26 on the in-scope sample, with disagreement almost entirely in the
   direction of records the corpus omits. Treat the affected branches, C3 above all, as a
   lower bound on available evidence.
2. **Screening was relevance-ranked to saturation**, not exhaustive over all 7,088
   identification hits. Per branch, relevance-ranked results were screened until
   successive results stopped yielding admissible papers. The number of records
   individually assessed at title/abstract level was not logged contemporaneously and
   is therefore not reported as a PRISMA stage count.
3. **English-language only.**
4. **Preprint-heavy corpus.** 177 / 202 papers carry arXiv identifiers; many are not
   peer-reviewed at time of writing. This is a property of the field, not a choice, but
   it weakens the evidentiary floor and is disclosed in the threats-to-validity section.
