# Codebook: corpus extension and dual-coded extraction

Version 1.0, 2026-11-09. Applies to three tasks: screening candidate papers (Part A), coding
locus entries for the coverage figures (Part B), and extracting mitigation results for the
papers cited in the mitigation map (Part C). Every rule cites the place in the survey it comes
from. `main` is `submit/main.tex`, `supp` is `submit/supplement.tex`. A rule marked
**[codebook rule]** is not stated in the survey; it was added to make a decision repeatable
from an abstract, and it should be read as this protocol's choice, not the authors' published
method.

All examples are invented. None describes a real paper.

## 0. General rules (all tasks)

0.1 **What you code from.** Title and abstract only, plus year/venue or publication date. For
papers already in the corpus you also receive the authors' locus tags and a one-line summary.
Do not use outside knowledge of a paper, its authors, its citations or its later versions, and
do not search for it. **[codebook rule]**

0.2 **Ignore every other input field.** If a record carries authors, a source, a branch label,
a corpus-membership flag or anything not named in your task prompt, ignore it.
**[codebook rule]**

0.3 **Findings, not framing.** A title phrased as a question ("Does X introduce bias?"), a
motivation sentence, or related work is not a finding. Code what the abstract reports the
paper found or did. **[codebook rule]**

0.4 **Evidence strings.** Every coded field has an `_evidence` companion: a verbatim quote of at
most 25 words from the title or abstract that decides the field. Quote exactly (an ellipsis
`...` may join two pieces of one sentence). Two exceptions: (a) when a field takes its default
value because nothing in the abstract decides it (`unspecified`, `UNCHARACTERIZED`,
`not_reported`, `not_named`, `no`, `false`, empty list), the evidence is `""`; (b) when the
abstract is missing, quote the author summary and prefix the quote with `SUMMARY: `. Never
quote the author summary when an abstract is present. **[codebook rule]**

0.5 **When two rules collide**, the more specific rule in this codebook wins over the general
one, and a numbered precedence list wins over prose.

---

## Part A. Screening

### A1. Criteria

The survey states three inclusion criteria (main §2.3, `sec:scope-coverage-decisions`) and a
fuller criteria table (supp §S6, `tab:inclusion-criteria`). The survey numbers only (i) to
(iii); (iv) and (v) below are this codebook's numbering of the remaining rows of the supplement
table.

| # | Criterion (include if) | Matched exclusion | Source |
|---|---|---|---|
| i | The studied system has an LLM as a primary reasoning component (fine-tuned variants included), **or** the paper supplies a mechanism that transfers to one (transferable-mechanism clause, A4) | Classical NLP models, RL agents without an LLM backbone, symbolic planners, with no transferable mechanism | main §2.3 (i); supp `tab:inclusion-criteria` "System type" |
| ii | It studies bias, fairness, equity or disparate treatment **of people** in outcomes or behavior | Pure capability evaluation; "bias" in a technical sense (position bias, order bias, popularity bias, self-preference, judge inconsistency) with no protected or social group | main §2.3 (ii); supp "Fairness content"; adjudication memo `corpus/_ADJUDICATION_2026-08-24.md` ("a fairness question about people rather than a technical sense of bias") |
| iii | Its findings bear on at least one locus C1 to C5 or the temporal axis T, or on the evaluation or mitigation of disparity there; single-turn work qualifies only through the transferable-mechanism clause | Exclusively single-turn static generation with no agentic framing and no transferable mechanism | main §2.3 (iii); supp "Agent component relevance" |
| iv | First made public (preprint or publication, whichever is earlier) on or before **10 June 2026** | Post-cutoff publications | main §2.3; supp "Temporal scope" and §S6 ("literature cutoff of 10 June 2026") |
| v | English-language, with full text accessible | Non-English; extended abstract only; inaccessible | supp "Language", "Availability" |

Criterion ii is not met by a paper that lists unfairness among several challenges without
studying it, for example a broad survey or system paper with one clause on bias (adjudication
memo, false-positive pattern 2).

### A2. Verdicts

| Verdict | Meaning | Source |
|---|---|---|
| `INCLUDE_TOPICAL` | Meets i to v and is a **primary study**: it reports a measurement, benchmark, audit, method or mitigation evaluated on a system | main Table 2 (`tab:corpus-accounting`), "topical studies"; supp §S5 |
| `INCLUDE_PRIOR_ART` | Meets i to v and is a **secondary work** on bias or fairness in LLM-based agents or one of their components: a survey, review, taxonomy, position or conceptual-framework paper that reports no new measurement of its own | main Table 2, "prior-art works, mostly neighbor surveys"; supp §S5; supp §S6 `tab:search-protocol`, prior-art branch query `(survey OR review) AND (fairness OR bias) AND agent AND LLM` |
| `EXCLUDE` | Fails at least one of i to v | supp `tab:inclusion-criteria` |
| `BORDERLINE` | The abstract does not settle one criterion, and the two readings lead to different verdicts | adjudication memo, "BORDERLINE: abstract does not settle it" |

There is no CONTEXTUAL verdict. Contextual works (definitions, impossibility results,
architectures, standards) entered the corpus only by backward citation chase under a separate
rule (main Table 2; supp §S5). A screened record that would only qualify as contextual is
`EXCLUDE` on criterion iii.

A framework paper that also reports an empirical study on an LLM system is `INCLUDE_TOPICAL`.
A framework paper whose abstract reports no measurement is `INCLUDE_PRIOR_ART`.
**[codebook rule]** Example: "We propose a taxonomy of fairness risks in tool-using agents and
illustrate it with three case vignettes" is prior-art; "...and audit two agents on 500 tasks,
finding approval gaps of 8 points" is topical.

A general LLM-fairness survey with no agent component in scope is `EXCLUDE` (iii), not
prior-art: prior-art works were screened under the topical criteria, including iii (main
Table 2; supp §S5).

### A3. Decision procedure

1. Compute `post_cutoff` from the date field (A6). Record it for every record.
2. If the abstract is missing or empty, verdict `BORDERLINE`, `deciding_criterion` = `v`.
   **[codebook rule]**
3. Check i, ii, iii, iv, v in that order. The **lowest-numbered** criterion that fails is the
   `deciding_criterion` and the verdict is `EXCLUDE`. If a criterion cannot be settled from the
   abstract and no lower-numbered criterion fails, the verdict is `BORDERLINE` and that
   criterion is the `deciding_criterion`. **[codebook rule]**
4. If all pass, `deciding_criterion` = `all_met`; choose `INCLUDE_TOPICAL` or
   `INCLUDE_PRIOR_ART` (A2).
5. `transfer_clause_used` is `true` when i or iii is met only through the transferable-mechanism
   clause (A4).
6. For `INCLUDE_TOPICAL`, assign `primary_branch`, `locus_tags` and `secondary_branches` (A7).
   For `BORDERLINE`, fill them as they would be if the paper were included topical. For
   `EXCLUDE` and `INCLUDE_PRIOR_ART`, `primary_branch` = `null` and both lists are empty.
   Prior-art works carry no locus tag and enter neither coverage figure (main §6.2: a prior-art
   record lies "outside both figures"; released `corpus/corpus_master.json`: no prior-art paper
   carries a locus branch).

Use `BORDERLINE` sparingly. "I am unsure" is not enough; name the clause of the abstract that
admits two readings. The typical case in the survey's own adjudication was an abstract that
leaves unclear whether a system is a real multi-agent architecture or one relabeled prompt
(supp §S6, adjudication paragraph).

### A4. The transferable-mechanism clause

Source: main §2.3 ("enters only where a mechanism transfers to agents", "fair sequential
decision-making and recommender fairness are drawn on where the dynamics parallel agentic
deployment"); supp `tab:inclusion-criteria` ("included only if mechanism transfers to agentic
settings"); supp §S6 adjudication ("a study whose fairness object is a persona, a
recommendation, or a role assignment rather than a tool call ... meets criterion (iii) through
the transferable-mechanism clause").

**Operational test.** The clause is met when you can name the component emission that the
paper's mechanism produces, using the consumes-to-emits column of supp `tab:locus-mapping`:

| Locus | The paper's disparity lives in ... |
|---|---|
| C1 | a choice among tools, APIs, retrievers, sources or search results |
| C2 | retrieved content, ranked passages, stored memory, or conversation history that conditions later output |
| C3 | a persona, role or identity attached to an agent, or interaction among two or more agents |
| C4 | a plan, decomposition, ordering, reasoning trace or resource allocation over subjects |
| C5 | a model of the interacting user (stated or inferred identity, preferences) that changes personalized output or recommendations |
| T | outputs fed back over turns, sessions or deployment cycles (feedback loops, sycophancy over turns, long-term drift) |

If no row applies (a single prompt, a single response, a bias score on that response), the
clause is not met and the paper fails iii. A non-LLM study (recommender, ranking, search
engine, sequential decision-making, RL feedback loop) meets i through the clause only if one
row applies; otherwise it fails i.

Example (meets): "An LLM recommends jobs to users whose stated gender varies; recommended
salaries differ by gender." Row C5 applies; `transfer_clause_used` = true.
Example (fails): "We measure stereotype completions of 12 LLMs on sentence templates." No row
applies; `EXCLUDE`, iii.

### A5. Fairness about people (criterion ii)

Two false-positive patterns from the survey's adjudication are excluded (adjudication memo):
technical "bias" (position, order, length, self-preference, consistency of an LLM judge), and
keyword matches with no substantive finding (fairness listed as a challenge). A study of bias
against a social group defined by a protected attribute, culture, language variety or national
origin meets ii. Political or ideological lean of outputs, with no group of people as the
object, does not meet ii. **[codebook rule for the political case]**

### A6. Post-cutoff check (criterion iv)

`post_cutoff` = `true` if the record's date is later than 2026-06-10. The date is the first
public version (arXiv v1 `published` field, not `updated`); a later journal version does not
move it. If the date has only year and month and the month is June 2026, the date cannot settle
iv: verdict `BORDERLINE`, criterion iv. Year only, with year 2026: `BORDERLINE`, iv. The
evidence for `post_cutoff` is the date string as given. Source: main §2.3; supp §S6; main §4 (Datasets and
Benchmarks, "Concurrent work") treats a benchmark first posted five days after the cutoff as
outside the corpus.

### A7. Primary branch, locus tags, secondary branches

Branch vocabulary: `C1`, `C2`, `C3`, `C4`, `C5`, `T`, `evaluation`, `mitigation`,
`high-stakes` (supp `tab:search-protocol`, the ten queried branches minus prior-art).

**Locus tags.** List every locus (C1 to C5, T) that a reported finding bears on, applying R1
to R5 (supp §S11, `supp:s3-locus-d1-mapping`):

- **R1 selection vs content (C1/C2).** Disparity in *which* resource is invoked is C1; disparity
  in *what* the invoked resource returns, and how that content conditions generation or
  persists, is C2. A paper that evidences both is tagged both.
  Example: "the agent queries the premium credit database less often for applicants from ZIP
  codes with majority-minority populations" is C1; "retrieved case notes for female patients
  omit pain history" is C2.
- **R2 role vs plan (C3/C4).** Disparity caused by *who is assigned* (persona, role or identity
  cue attached to an agent) is C3, including a demographic persona given to a single LLM.
  Disparity in *how the task is cut up*, ordered or resourced, independent of identity
  assignment, is C4, including allocation over external subjects by a team of agents.
  Example: "giving the reviewer agent a Muslim identity changes which loan files it approves" is
  C3; "the orchestrator allocates fewer verification steps to loan files of older applicants"
  is C4.
- **R3 subject vs user (C5).** Disparity keyed to the *decision subject* (applicant, patient,
  defendant) goes to C1 to C4 by where it is measured; disparity keyed to the *interacting
  user*, especially an attribute the system infers, is C5.
- **R4 temporal indexing (T).** A finding measured as a function of turn, session or cycle is
  the same locus indexed by time: tag that locus **and** T. Tag T alone only when the paper
  measures change over time without locating it at any component. **[the "T alone" clause is a
  codebook rule; supp §S11 does not state when T is primary, but nine corpus papers carry T as
  primary branch]**
- **R5 multi-tagging.** A paper is counted at every locus it evidences but has exactly one
  primary locus: the component whose input or output the paper directly measures.

A finding on a single final decision about a subject whose demographic cue is placed directly
in the prompt, with no component emission measured, carries **no** locus tag. **[codebook
rule]**

**Primary branch.** Precedence, first match wins:

1. If `locus_tags` is non-empty, `primary_branch` is the R5 primary locus. Source: every
   multi-branch topical paper in the released `corpus/corpus_master.json` lists its locus
   branch first, ahead of evaluation, mitigation or high-stakes. **[codebook rule derived from
   the released file; the survey states no precedence]**
2. Else `mitigation` if the main contribution is an intervention that reduces bias.
3. Else `evaluation` if the main contribution is a benchmark, dataset, metric or audit method.
4. Else `high-stakes` if the paper audits LLM decisions about people in a consequential domain
   (the branch query names hiring, clinical, lending and judicial; education, housing,
   insurance and welfare decisions also count). **[the added domains are a codebook rule]**

If 2 and 3 both fit, the contribution named first in the title decides. **[codebook rule]**

`secondary_branches`: any of `evaluation`, `mitigation`, `high-stakes` that also apply and are
not the primary branch (branch tags are non-exclusive; supp §S5).

### A8. Screening examples (invented)

| Abstract gist | Verdict | Criterion | Note |
|---|---|---|---|
| LLM-as-judge prefers the first-listed answer; we calibrate it | EXCLUDE | ii | technical bias, no group of people |
| Survey of LLM recommender systems; challenges include cold start and unfairness | EXCLUDE | ii | fairness listed, not studied |
| Survey of fairness risks in tool-using and multi-agent LLM systems | INCLUDE_PRIOR_ART | all_met | secondary work, agent scope |
| An LLM agent drafts discharge plans; plans for patients described as uninsured contain fewer follow-up steps | INCLUDE_TOPICAL | all_met | primary C4 (allocation over subjects, R2) |
| Debiasing a 2019 BERT classifier for toxicity | EXCLUDE | i | no LLM, no transferable mechanism |
| arXiv v1 dated 2026-06-15 | EXCLUDE | iv | post-cutoff, whatever else holds |

---

## Part B. Entry coding (feeds Figures 8 and 9)

### B1. Unit of analysis

The unit is the **entry**: one (paper, locus) pair. A paper with three locus tags yields three
entries. Source: main §6.1 and Table 2 ("59 locus-tagged papers yield 68 entries"). For papers
already in the corpus the locus tags are **given** (`author_locus_tags`, with `primary_locus`)
and are not re-decided. For newly admitted papers the tags are the adjudicated output of Part A
and are equally given at this stage.

Code each entry from the finding that concerns that locus's emission. When the abstract reports
one undifferentiated finding, every entry of the paper receives the same codes.
**[codebook rule]**

### B2. `fairness_dimension` and `fairness_basis`

Values: `group`, `individual`, `counterfactual`, `unspecified`. Companion field
`fairness_basis`: `named`, `instantiated`, `none`.

Definitions (main §2.1, `sec:fairness-definitions`; supp §S19):

- **group**: a decision or score should fall equally often on each group; demographic parity,
  equalized odds, equality of opportunity, disparate impact, four-fifths rule.
- **individual**: similar people treated similarly, a Lipschitz condition over *all* pairs
  under a task-relevant similarity metric, not only demographic pairs.
- **counterfactual**: the outcome should be unchanged had the person's protected attribute been
  different. The survey treats a demographic swap "as a criterion in its own right" as
  belonging to this family, and as "a special case of the similar-individual pair, not its
  general form" (supp §S19, individual-fairness paragraph).
- **unspecified**: a harm documented without a fairness family (main Figure 8 caption; main
  §6.3 "harms documented without a named fairness family"; §6.4 "name no fairness
  dimension").

**Rule: the family the paper's own measure names or instantiates.** Precedence, first match
wins:

1. **Named.** The abstract names a family, or a criterion formally belonging to one (listed
   above), *for its own measurement*. Code that family, `fairness_basis` = `named`. A family
   mentioned only in motivation or related work does not count. If two families are named for
   the paper's own measures, code the one attached to the first quantitative result.
2. **Instantiated.** No family is named, but the abstract describes the measure:
   - an outcome rate, score, accuracy, error rate, ranking or recommendation **aggregated per
     group** and compared across groups: `group`;
   - a **within-pair** comparison of inputs identical except for a protected-attribute cue
     (name, pronoun, dialect, demographic persona, stated attribute), reported as the share of
     pairs whose output changes, a paired score difference, or a consistency or invariance
     rate: `counterfactual`;
   - consistency across pairs judged similar on task-relevant features, with that similarity
     stated and not restricted to demographic pairs: `individual`.
   `fairness_basis` = `instantiated`. The compared quantity must be named (a rate, score,
   accuracy, ranking, recommendation, decision); "disparities across demographic attributes"
   or "bias across groups" with no quantity named does not instantiate a family.
   **[codebook rule]**
3. Otherwise `unspecified`, `fairness_basis` = `none`. This covers abstracts that describe no
   measure, stereotype or toxicity rates scored by a classifier or judge, association tests,
   bias-benchmark scores that do not compare an outcome across groups, and qualitative
   analysis.

**Swap and name-substitution designs, stated once.** The swap is how inputs are built; the
family is decided by what the reported number compares.
- Swapped inputs whose results are **aggregated into per-group rates** and compared across
  groups are `group` (instantiated): the comparison is between groups (main §2.1).
- Swapped inputs whose result is a **per-pair change** (flip rate, paired difference,
  invariance) are `counterfactual` (instantiated): the swap as a criterion in its own right
  (supp §S19).
- A demographic swap is **never** coded `individual` on instantiation (supp §S19: a special
  case, not the general form). It is coded `individual` only if the paper names individual
  fairness (step 1).

Examples (invented):
- "Replacing applicant names with names typical of four race-gender groups, interview
  recommendations differ by up to 12 points across groups." `group`, instantiated.
- "Changing only the patient's stated race flips the triage level in 9% of cases." 
  `counterfactual`, instantiated.
- "We evaluate counterfactual fairness by comparing approval rates of original and
  race-swapped profiles." `counterfactual`, named (step 1 wins over step 2).
- "Classifier-scored hostility toward named religious groups rises over 20 sessions."
  `unspecified`, none.

Note for analysis, not for coders: Figure 8 can be reproduced under the strict reading of
§6.2/§6.4 ("named framing", "name no fairness dimension") by recoding every entry with
`fairness_basis` other than `named` as `unspecified`. **[codebook rule; see Part E]**

### B3. `operator` and `operator_secondary`

Values: `ATTENUATE`, `PRESERVE`, `AMPLIFY`, `GENERATE`, `UNCHARACTERIZED`.

Source: main D3 and Table 3 (`tab:conduction-operators`): labels are "ordinal codes read from
the direction a paper reports"; main §6.3: GENERATE is counted "only where one design measures
none upstream and disparity downstream"; Figure 9 (`fig:operator`) caption: "each entry counted
under one operator", with an uncharacterized coding residual column.

| Operator | Licensed when the abstract reports ... |
|---|---|
| `GENERATE` | disparity at a point where the same design shows **none** upstream: no disparity, a non-significant or negligible one, or a demographically clean condition (base model without the component, closed-book answer, no persona, query with no demographic cue) |
| `AMPLIFY` | disparity present upstream and **larger** downstream, across a component, hand-off, agent interaction, turn or cycle; also a disparity reported as accumulating, escalating or compounding over turns, rounds or cycles |
| `PRESERVE` | disparity present upstream and **carried through** about unchanged: inherited, reproduced, carried over, or explicitly reported as not reduced by a downstream step |
| `ATTENUATE` | disparity present upstream and **smaller** downstream, including after an intervention (debiasing, anonymization or redaction of the cue, reranking, guardrail) |
| `UNCHARACTERIZED` | anything else: disparity at one point only, a benchmark or audit with no two-point comparison, a survey-like result, or no direction stated |

**Decision procedure.**

1. Find the entry's finding(s) in the abstract (B1).
2. Ask whether the finding compares disparity at **two points**: before and after a component or
   hand-off; without and with the component, cue, persona or role; single-turn and multi-turn;
   earlier and later turn, round or cycle; one agent and after interaction; before and after an
   intervention. If not, `UNCHARACTERIZED`.
3. Map the comparison with the table above. An intervention that leaves disparity unchanged is
   `PRESERVE`; one that increases it is `AMPLIFY`.
4. **GENERATE needs the upstream measurement.** A disparity found at the output with no upstream
   or baseline condition reported is `UNCHARACTERIZED`, not `GENERATE`. A cue present upstream
   is not disparity upstream: "attribute information ... can be present upstream with zero
   disparity" (main D3).
5. "Higher", "more frequent" or "worse" downstream than a reference condition, where the abstract
   does not say the reference shows none, is `AMPLIFY`, not `GENERATE`. **[codebook rule]**
6. Co-presence is not conduction. Disparity reported at two stages with no stated relation
   between them ("bias appears in both retrieval and generation") is `UNCHARACTERIZED`.
   **[codebook rule]**

**Two operators.** `operator_secondary` is filled only when the abstract reports **two distinct
findings** that take different operators. Distinct means a different comparison (a different
pair of points, or an intervention as opposed to the system as built); the same comparison on
another model or dataset, or a restatement, is not distinct. **[codebook rule; the survey does
not state a two-operator rule]**
- `operator` (the one Figure 9 counts) is the first **directional descriptive** finding about
  the system as built (one that maps to an operator other than UNCHARACTERIZED); an
  intervention result then goes to `operator_secondary`. If no descriptive finding has a
  direction, the intervention result is `operator`. `UNCHARACTERIZED` is used only when no
  finding has a direction, and then `operator_secondary` is `null`. **[codebook rule]**
- Same operator twice: no secondary. At most two operators are recorded.
  `operator_secondary` is never `UNCHARACTERIZED`.
- Otherwise `operator_secondary` = `null`.

Examples (invented):
- "When the agent may call a credit-scoring API, approval gaps by race reach 7 points; without
  the tool, no significant gap." `GENERATE`.
- "Age gaps in triage priority widen at each of five hand-offs between agents; redacting age
  before the second hand-off narrows them." `operator` = `AMPLIFY`, `operator_secondary` =
  `ATTENUATE`.
- "Our benchmark finds that all eight agents favor tenants with Anglo names." Only one point:
  `UNCHARACTERIZED`.
- "The summarizer agent passes the screener's gender gap in scores to the final shortlist
  unchanged." `PRESERVE`.

### B4. `evidence_type`

Values: `direct_llm_agent`, `llm_non_agentic_transferred`, `non_llm_transferred`.

Source: main §2.3 (scope: "LLM-based agents that perform multi-step, tool-augmented, or
multi-agent reasoning toward a goal"); main §3.1 and Table 3 caption ([dagger] marks "evidence
that transfers by analogy from a non-agentic, non-LLM or non-demographic setting, without an
agentic, demographic measurement"); Figure 8 caption (non-LLM studies "admitted as
transferable mechanisms").

- `direct_llm_agent`: the measurement is taken on an LLM-based system **while it operates as
  an agent component**: a tool, API or source choice; retrieval-augmented or memory-conditioned
  generation, including multi-turn conversation history; two or more interacting LLM agents,
  or a role or persona inside a multi-step or multi-agent task; an explicit plan,
  decomposition or allocation in a goal-directed task; personalization driven by a stored or
  inferred user model; outputs fed back over turns or cycles.
- `llm_non_agentic_transferred`: an LLM, but the measurement is on a single prompt and single
  response (including a persona prompt answered in one turn, or one hiring decision), and the
  mechanism is carried to agents by analogy.
- `non_llm_transferred`: no LLM in the studied system (recommender, ranker, search engine,
  classical ML, RL or simulation).

The boundary between a single-turn persona or user-identity prompt and an agentic one is a
**[codebook rule]**: single turn, no tool, no retrieval, no second agent, no carried state means
`llm_non_agentic_transferred`.

**Derived, not coded:** an entry carries the [dagger] marker if `evidence_type` is not
`direct_llm_agent` **or** `demographic` = `no`. Source: the three settings named in the Table 3
caption.

### B5. `demographic`

`yes` if the finding concerns a protected attribute of people: race, ethnicity, gender, sex,
age, religion, disability, sexual orientation, nationality or national origin,
socioeconomic status, or a proxy used for one of these in the paper (names, dialect or
language variety, region of origin). `no` otherwise (tool or brand preference, source or
popularity bias, political lean, task-difficulty bias). Source: main §3 opening and §3.1
(the survey's object is "demographic disparity"); Table 3 caption ("non-demographic setting").
The list of attributes is a **[codebook rule]**.

---

## Part C. Mitigation extraction (papers cited in Table 6)

Input: each distinct key cited in the mitigation map (main Table 6, `tab:mitigation-map`;
`table6_papers.json`). Coders receive key, title, year, venue and abstract only, never the
Table 6 row, its operator column or its [dagger] marks. One output object per paper.

| Field | Values | Rule |
|---|---|---|
| `setting` | `agentic_multistep`, `single_decision`, `qa_generation`, `other` | Where the intervention is **evaluated**, not where it could apply. `agentic_multistep`: tool use, retrieval or RAG, memory, two or more interacting LLMs (debate, ensemble, critique loop), multi-turn interaction, or multi-step planning. `single_decision`: one model call that decides, scores, ranks or recommends about a person (hiring, lending, clinical, legal). `qa_generation`: bias benchmarks in question answering or multiple choice, open-ended generation, completion, single-response dialogue. `other`: anything else (preference or reward-model evaluation, a system description with no fairness evaluation). If several apply, take the first in the order listed. **[codebook rule]** |
| `metric_named` | free text, or `not_named` | The fairness or bias metric the abstract names for the intervention's effect, verbatim, `; `-separated. If only a benchmark is named, give it with the suffix ` (benchmark)`. Generic words ("bias", "fairness") alone are `not_named`. |
| `effect_direction` | `reduces`, `mixed`, `none`, `increases`, `not_reported` | Effect of the intervention on the fairness or bias measure as the abstract reports it. `mixed`: reduces in some reported settings and not in others, or trades one group against another. `none`: reported as no meaningful change. `not_reported`: no fairness effect stated. |
| `utility_cost_reported` | `yes`, `no` | `yes` if the abstract reports the intervention's effect on task performance, accuracy, helpfulness or capability, including "without degrading performance". |
| `demographic` | `yes`, `no` | As B5, applied to the bias the intervention targets. |

Each field has an `_evidence` string (rule 0.4).

Examples (invented):
- "Three LLM agents critique each other's answers; bias on a QA bias benchmark falls 40% with
  accuracy unchanged." `setting` = `agentic_multistep` (interacting LLMs come first in the
  order), `effect_direction` = `reduces`, `utility_cost_reported` = `yes`.
- "Fine-tuning lowers gender bias on two QA bias benchmarks but raises it on a third." No
  performance figure is given. `setting` = `qa_generation`, `effect_direction` = `mixed`,
  `utility_cost_reported` = `no`.

---

## Part D. Field defaults when the abstract is silent

| Field | Default |
|---|---|
| `fairness_dimension` / `fairness_basis` | `unspecified` / `none` |
| `operator` | `UNCHARACTERIZED` |
| `operator_secondary` | `null` |
| `demographic` | `no` only if the abstract names no group of people; if it names a protected group, `yes` |
| `metric_named` | `not_named` |
| `effect_direction` | `not_reported` |
| `utility_cost_reported` | `no` |

`evidence_type` has no default: it is always decidable from what system was studied.

---

## Part E. Rules this codebook adds to the survey

Listed so that a reader can separate the protocol's choices from the survey's published method.

1. Criteria iv and v are this codebook's numbering; the survey numbers only (i) to (iii) and
   gives the rest as rows of supp `tab:inclusion-criteria`.
2. Deciding criterion = lowest-numbered failing criterion; missing abstract is BORDERLINE (v).
3. Framework vs prior-art split (A2) and the political-lean exclusion (A5).
4. Primary-branch precedence (A7.1) is inferred from the released corpus file, not stated in
   the survey; "T alone" (R4) and the added high-stakes domains likewise.
5. "No locus for a single final decision with the cue in the prompt" (A7).
6. Fairness dimension: the survey's wording supports two readings. §6.2 and §6.4 describe the
   coding as the *named* family ("named framing", "name no fairness dimension"), while §6.2 also
   says a stage-attribution study "is coded under its attribution method", which implies coding
   by the measure used. This codebook codes named-or-instantiated, as instructed, and records
   `fairness_basis` so that either reading can be reproduced.
7. Two operators per entry: Figure 9 counts one operator per entry. This codebook keeps that
   count on `operator` and holds a second distinct finding in `operator_secondary`, which no
   figure counts; the descriptive-before-intervention precedence is a codebook choice.
8. Co-presence at two stages is UNCHARACTERIZED, not PRESERVE; "more than the reference" with
   the reference level unstated is AMPLIFY (B3 steps 5 and 6). A family is instantiated only
   when the compared quantity is named (B2).
9. Single-turn persona or user-identity prompts are `llm_non_agentic_transferred` (B4).
10. The protected-attribute list (B5) and the `setting` precedence (Part C).
