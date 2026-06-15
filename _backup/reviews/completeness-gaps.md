Now I have a thorough picture of the draft. Let me produce the gap analysis.

---

The draft is a strong 70%-complete arXiv preprint targeting SIGKDD Explorations. Upgrading to ACM Computing Surveys (CSUR) demands a fundamentally different register: CSUR referees treat a survey as a *research contribution in its own right*, not a well-organized reading list. Below is a ranked list of what the draft is missing or thin on, with CSUR-specific justification and concrete prescriptions.

---

## Ranked Gap Analysis: What CSUR Expects That the Draft Lacks

---

### 1. EXPLICIT REVIEW METHODOLOGY / SYSTEMATIC PROTOCOL (Critical — CSUR baseline requirement)

**Why CSUR expects it.** CSUR's author guidelines explicitly require a reproducible search protocol. Reviewers flag the absence as grounds for desk rejection. This is non-negotiable: without it, the paper is categorized as a position piece or annotated bibliography, not a survey.

**What the draft has.** Section 2.4 contains four paragraphs that name sources (arXiv, ACL Anthology, ACM DL, NeurIPS/ICML/ICLR, FAccT), describe keyword families per component, and state corpus size (127 papers, 61% from 2024+). This is the raw material for a methodology but is not a methodology in the CSUR sense.

**What is missing.**
- No PRISMA-style or equivalent flow diagram showing: records identified → duplicates removed → screened by title/abstract → full-text reviewed → included. CSUR referees look for this figure first.
- No exact search strings (quoted, reproducible). "Variant terms for each component" is too vague.
- No inter-rater agreement or inter-author reconciliation protocol. Did both authors screen independently? What was the kappa?
- No inclusion/exclusion criteria in tabular form with operationalized definitions. The four sentences in 2.4 gesture at criteria but do not operationalize them (e.g., "agentic framing" is not defined with a bright line).
- No documentation of how the 127 were reached: what was the initial pool size, how many were removed at each stage, what fraction were excluded for being single-turn QA only vs. non-LLM vs. other.
- No cut-off date stated explicitly (the "mid-2026" language appears only in passing).

**Where to add.** A dedicated subsection 2.5 titled "Systematic Search and Corpus Construction" plus a PRISMA-flow figure (Figure 0 or an appendix figure). The subsection should occupy roughly half a page in the final paper. Include a table: Branch | Search String | Database | Records Found | After Dedup | After Screening | Included.

**Effort.** Moderate — the data exists in corpus_master.md and corpus/ files; it needs to be surfaced, audited, and formatted.

---

### 2. COMPARISON TABLE VS. PRIOR SURVEYS (High — differentiator for CSUR reviewers)

**Why CSUR expects it.** CSUR is a venue that publishes surveys on topics with prior survey coverage. Reviewers explicitly ask: "How does this survey differ from prior surveys in scope, method, and coverage?" A prose paragraph (§1.4, §2.4 positioning) is necessary but not sufficient. CSUR tradition expects a structured comparison table.

**What the draft has.** The prose differentiation in §1.4 and §2.4 is good, and Table 0 is mentioned ("Differentiation vs. the 3 competitor surveys + Zhang 2024") in FIGURES.md and OUTLINE.md but is NOT in the assembled draft. It is specced but absent.

**What is missing.**
- Table 0 needs to actually appear in the paper. Columns should include: Survey | Year | Venue | Organizing Axis | Agent Coverage? | Fairness-Dedicated? | Component-Level? | Corpus Size | Original Results? | Action-Level Metrics?
- The table should cover at minimum: Gallegos et al. 2024, Chu et al. (Zhang 2024), Mohammadi et al. 2025, Vatsal et al. 2026, Mayilvaghanan et al. 2026, and 2–3 other adjacent fairness-in-AI surveys (e.g., Mehrabi et al. 2021 as the classical ML baseline).
- The table is the single visual that prevents a reviewer from asking "why not just read Gallegos?"

**Where to add.** End of §1.4 or as a standalone display at the start of §2. It should be referenced from both §1.4 and §7.4.

**Effort.** Low — the comparisons are already written in prose; the table is a formatting task.

---

### 3. TEMPORAL / TREND ANALYSIS OF THE FIELD (High — CSUR hallmark)

**Why CSUR expects it.** CSUR surveys are expected to characterize the field's *trajectory*, not just its current state. Reviewers ask: is this a mature field being consolidated, or an emerging one? Are the publication rates accelerating? Which components are receiving increasing vs. decreasing attention?

**What the draft has.** One data point: "61% published in 2024 or later." That is it.

**What is missing.**
- A publication-volume-by-year chart for the 127-paper corpus, broken down by component. This would make visually immediate the field's explosive growth in 2024–2026 and the relative maturity of QA-fairness vs. agentic-fairness subfields.
- A narrative analysis: which components received papers earliest (likely multi-agent delegation, user modeling — older NLP traditions), which are newest (long-horizon drift, tool-selection bias — genuinely 2025–2026 phenomena).
- Identification of "inflection events" — specific papers or systems (ReAct 2023, AutoGen 2023, GPT-4 function calling 2023) that triggered the agentic-fairness literature.
- A note on venue distribution: where is this work published (FAccT, NeurIPS, ICLR, arXiv-only)? This tells CSUR reviewers the maturity and interdisciplinarity of the subfield.

**Where to add.** A subsection 2.5 (or 2.6 after methodology), approximately one-third of a page, with one figure (bar chart by year, stacked by component). Alternatively, fold into §7 as a temporal subsection alongside the coverage matrix.

**Effort.** Moderate — requires building a year-by-year breakdown of the corpus, which requires reading publication dates in corpus_master.md.

---

### 4. CHALLENGES → SOLUTIONS → OPEN GAPS MAPPING (High — structural synthesis requirement)

**Why CSUR expects it.** CSUR defines a survey as providing "a synthesis that identifies challenges, solutions, and remaining gaps." The draft does the taxonomy (§3), evaluation (§4), mitigation (§5), and open problems (§8) in separate sections but never presents a unified mapping that closes the loop: for each challenge identified in §3, what solutions from §5 exist, what do they miss, and what does §8 then target?

**What the draft has.** Table 3 (mitigation × component × stage × evidence) is specced in FIGURES.md and referenced in §5.5 but its actual content is only described in prose within §5, never rendered as a machine-readable table in the assembled draft. More fundamentally, there is no table or figure that reads: Component → Known Harms → Existing Mitigations → Remaining Gap.

**What is missing.**
- A synthesis table (Table 4 or a restructured Table 3) with columns: Component | Primary Harm Mechanism | Mitigation Evidence | Mitigation Coverage (full/partial/none) | Critical Open Gap. This would let a practitioner or regulator look up any component and immediately see the state of play.
- Explicit closure sentences at the end of each §3.x subsection linking the "open edge" to a specific §8.x agenda item and to whatever §5 mitigation exists. Currently the open edges in §3 are self-contained and do not systematically reference §5 or §8 by number.
- A "challenges-to-agenda" mapping in §8 or a bridging paragraph at the end of §7 that reads across: the coverage matrix (§7) shows the empty cells; those cells map to specific open problems (§8.1–8.6) and to the absence of mitigation (§5's summary assessment). This triangulation exists conceptually in the authors' heads but is not explicit on the page.

**Where to add.** A synthesis display after §5 or in §7, plus cross-referencing edits to §3 subsection endings.

**Effort.** Moderate to high — requires genuine synthesis, not just reformatting.

---

### 5. EXPLICIT ETHICS, SOCIETAL IMPACT, AND LIMITATIONS OF THIS SURVEY (High — ACM mandatory + CSUR expectation)

**Why CSUR expects it.** ACM's publication policy (since 2020) requires an explicit consideration of ethical and societal implications in submissions. For a fairness survey, the bar is higher: reviewers will find it conspicuous if the paper does not reflect on (a) the survey's own positionality, (b) potential harms from the survey's framing choices, and (c) the societal stakes of the field it reviews. Beyond ACM policy, CSUR referees expect this for a paper whose subject is itself equity and harm.

**What the draft has.** Scattered motivational sentences in §1.1 (consequential domains, national importance) and in §8.4 (intersectional harms). There is no dedicated section.

**What is missing.**
- A short dedicated section (or a clearly headed subsection, e.g., §9.1 "Ethical Considerations and Societal Impact") covering: (i) the harms of misusing survey findings (e.g., using the taxonomy to appear to comply without addressing root causes; using mitigation checklists as liability shields); (ii) the gap between academic fairness metrics and legal/regulatory standards (disparate impact doctrine, EU AI Act requirements) and what the survey can and cannot certify; (iii) the authors' own positionality and the limits of their coverage (language, geography, domain — the 127-paper corpus is overwhelmingly English-language and US/EU centric, which is a limitation); (iv) the dual-use risk that the same taxonomy can be used by practitioners to audit systems or by bad actors to evade audits.
- A "Limitations of This Survey" subsection (distinct from societal impact) addressing: scope decisions that may have excluded relevant work, the risk that the corpus skews toward English-language and well-resourced deployment contexts, the rapidly moving literature (papers published after the cut-off date), and the unexecuted empirical audit (§6 results are pending).

**Where to add.** A subsection before or after the Conclusion (§9), or appended to §8 as §8.7. Approximately half a page.

**Effort.** Low to moderate — mostly prose; no new analysis required but requires genuine reflection.

---

### 6. GLOSSARY / CONSISTENT TERMINOLOGY (Medium-High — CSUR polish standard)

**Why CSUR expects it.** CSUR publishes surveys that become the field's reference document. Reviewers expect the paper to be the authoritative source for terminology in its area. The draft introduces several terms without formal definitions: "agentic multiplier" (coined in §3.7), "action-level disparity" (coined in §4.3), "tool-selection bias" (sourced from Blankenstein et al.), "long-horizon fairness drift" (coined in §3.6), "fairness at the component level." These are valuable contributions but they need to be formally defined and collected.

**What the draft has.** Definitions embedded in §3 subsection openings (under "Definition." in bold) — these are good and should be collected. The §2.1 fairness definitions are solid. But there is no consolidated glossary.

**What is missing.**
- A consolidated Glossary section or Table (can be an appendix or an online supplement) that lists all novel terms coined in this survey with their formal definitions, plus a set of adopted terms (CFR, MASD, RAG, etc.) for readers unfamiliar with subfields.
- Consistency audit: "agentic multiplier" is defined in §3.7 but used in several places; "action-level disparity" appears in §4.3, §6, §8.1, and the Abstract but its formal definition appears only in §4.3. A glossary entry with a page reference would make this cross-referencing explicit.
- Notation table: CFR and MASD are given natural-language descriptions but not formal mathematical notation. For a CSUR audience that includes ML theorists, a brief notation block (even just the formulas from Mayilvaghanan et al., adapted) is expected.

**Where to add.** A glossary box at the end of §2 or as an appendix. A notation block in §4.2.

**Effort.** Low — primarily reorganization of content already in the draft.

---

### 7. THREATS TO VALIDITY OF THE SURVEY ITSELF (Medium-High — rarely done, always noticed by top reviewers)

**Why CSUR expects it.** CSUR surveys are treated as empirical research. Just as an empirical paper reports threats to validity (internal, external, construct, conclusion), a survey must report analogous threats: selection bias in the corpus (what papers might be missing?), confirmation bias in interpretation (does the taxonomy's organizing axis pre-select certain findings?), publication bias (does the corpus over-represent positive/significant results?), and recency bias (61% from 2024+ means the older theoretical foundations may be under-represented).

**What the draft has.** Nothing explicit. The "explicit out-of-scope" in §2.4 is close but is not framed as a validity threat.

**What is missing.**
- A "Threats to Validity" subsection (short, ~0.25 page) or paragraph at the end of §2.4 or in the limitations section. Cover: (1) corpus completeness — the search was systematic but not exhaustive; grey literature and non-English work are excluded; (2) construct validity — the six-component taxonomy is an analytical choice, not a ground truth; other taxonomies are possible and may yield different coverage patterns; (3) publication bias — papers demonstrating bias exist; papers showing no agentic disparity may be in the file drawer; (4) recency — the field is moving fast enough that coverage from before 2026-06-11 may already be stale by publication.

**Where to add.** End of §2.4 or as part of a §8.7 or §9.1 Limitations block.

**Effort.** Low.

---

### 8. EVALUATION REPRODUCIBILITY DISCUSSION (Medium — increasingly required by CSUR)

**Why CSUR expects it.** CSUR increasingly expects surveys to comment on the reproducibility of the empirical work they survey — not just their own empirical study but the corpus. This matters especially here because the draft argues that agentic fairness evaluation lacks standardization (§8.5), making reproducibility of existing results a direct corollary of the survey's central claim.

**What the draft has.** Section 6 (the audit) correctly commits to releasing synthetic profiles, prompts, pinned model identifiers, and analysis code. This is excellent for the survey's own study. But the draft says nothing about whether the 127 surveyed papers are reproducible.

**What is missing.**
- A brief analysis (can be a column in Table 2 or a paragraph in §4.4 or §8.5): for the empirical papers in the corpus, what fraction release code, data, or evaluation prompts? What fraction use pinned model versions? This speaks directly to the draft's measurement-gap thesis: not only do benchmarks score the wrong thing, but many existing audits are not rerunnable.
- A note in §8.5 (standardization and governance) that reproducibility is a prerequisite for auditability: if a fairness audit of a deployed agent cannot be reproduced by a regulator, it provides no accountability.

**Where to add.** Column in Table 2 ("Code/Data Released?") and a paragraph in §4.4 or §8.5.

**Effort.** Low to moderate — requires scanning corpus papers for artifact availability, but can be done at a high level.

---

### 9. "HOW TO USE THIS SURVEY" GUIDE FOR PRACTITIONERS AND REGULATORS (Medium — CSUR impact value)

**Why CSUR expects it.** CSUR's stated mission includes serving practitioners and policymakers, not only researchers. For a survey on fairness in high-stakes agent deployments, a brief navigation guide substantially increases the paper's impact and is specifically mentioned in CSUR editorial guidelines as a best practice for applied topics.

**What the draft has.** None. The paper is organized purely for a research reader.

**What is missing.**
- A short (quarter-page) box or sidebar: "How to Use This Survey." Four reader paths: (a) AI practitioner deploying an agent in a consequential domain → start at §3 for your component, go to §5 for mitigations, check Table 3; (b) auditor or regulator evaluating an agent for fairness compliance → start at §4.2–4.3 for metrics, §8.5 for governance gaps; (c) researcher entering the field → read §2–3 for foundations, §7 for the coverage map showing where to contribute; (d) benchmark builder → §4.4 for the measurement gap, §8.1 for what FairMedAgent needs to cover.
- In the absence of a box, at minimum a paragraph at the end of §1 (after contributions and positioning) that directs different reader types to the relevant sections.

**Where to add.** End of §1 or a callout box in §2.

**Effort.** Very low — purely additive prose.

---

### 10. FUTURE-WORK CONCRETENESS AND ACTIONABILITY (Medium — distinguishes CSUR from workshop papers)

**Why CSUR expects it.** Section 8 exists and is substantive, but CSUR reviewers distinguish between open problems that are "directions" (vague) and open problems that are "research specifications" (actionable). The current §8 mostly describes *what* is missing; it does not consistently specify *what a solution would look like* in operational terms — the protocol, dataset structure, metric formula, or system design that would close the gap.

**What the draft has.** §8.1 is the strongest: it specifies FairMedAgent at a reasonable level of detail. §8.2–8.6 are thinner — they state the problem and say "what a solution needs" but at a level of generality that does not give a researcher a concrete starting point.

**What is missing.**
- For each §8.x open problem, one concrete "first step" — a specific research question, a proposed dataset structure, a proposed metric formula, or a named system design. Example for §8.2: "A long-horizon fairness benchmark would need at minimum M simulated multi-turn sessions per demographic group, covering at least K decision points per session, and would report equal long-term benefit rate [Xu et al.] as the primary metric alongside CFR computed over the full trajectory." Example for §8.3: "A multi-agent amplification metric would quantify the ratio of system-level disparity to the maximum per-agent disparity, with a value > 1 indicating emergence."
- For §8.5 (governance), a concrete mapping to existing regulatory frameworks: EU AI Act Article 10/13 data and transparency requirements, US EEOC guidance on automated hiring tools, NIST AI RMF. This grounds the governance gap in existing instruments that practitioners and regulators actually use, and substantially strengthens the national-importance argument.

**Where to add.** One to three sentences added to each §8.x "What a solution needs" block.

**Effort.** Moderate — requires domain knowledge of regulatory frameworks and careful operationalization, but no new literature review.

---

### 11. PRIOR SURVEY COMPARISON ON CORPUS COVERAGE (Lower priority but noticed)

**Why CSUR expects it.** CSUR reviewers sometimes ask: does this survey cover papers the prior surveys missed? A brief note (or column in Table 0) showing that the 127-paper corpus includes a set of papers not in Gallegos et al. 2024 or Chu et al. 2024 would demonstrate that the survey has not simply re-organized the same literature but has genuinely found new material by targeting the agentic subfield.

**What the draft has.** None of this comparison.

**What is missing.** In Table 0, add a column "Unique papers not in prior surveys (approx.)" or a footnote. Even a rough count is useful. Alternatively, a sentence in §2.4: "Of the 127 papers in our corpus, approximately N appear in neither Gallegos et al. nor Chu et al., reflecting the post-2023 agentic literature that those surveys predate."

**Where to add.** §2.4 or Table 0 footnote.

**Effort.** Very low.

---

## Summary Ranking Table

| Rank | Gap | Severity for CSUR | Effort | Where to Add |
|---|---|---|---|---|
| 1 | Systematic review methodology / PRISMA flow | Critical / desk-rejection risk | Moderate | New §2.5, new Figure 0 |
| 2 | Survey comparison table (Table 0) | High / differentiator | Low | End of §1.4 or §2 |
| 3 | Temporal / trend analysis | High / CSUR hallmark | Moderate | New §2.6 or §7 subsection |
| 4 | Challenges→solutions→gaps mapping table | High / synthesis | Moderate-High | After §5 or §7, plus §3 edits |
| 5 | Ethics, societal impact, limitations section | High / ACM mandatory | Low-Moderate | New §9.1 or §8.7 |
| 6 | Glossary and notation table | Medium-High / reference standard | Low | End of §2, §4.2 notation block |
| 7 | Threats to validity of the survey | Medium-High / top reviewers | Low | End of §2.4 or §9.1 |
| 8 | Reproducibility of surveyed empirical work | Medium / increasingly required | Low-Moderate | Table 2 column, §4.4 para |
| 9 | "How to use this survey" reader guide | Medium / impact and CSUR guidelines | Very Low | End of §1 or callout box |
| 10 | Future-work operationalization + regulatory mapping | Medium / workshop-vs-CSUR distinction | Moderate | §8.x "solution" blocks |
| 11 | Coverage comparison to prior surveys | Lower / nice-to-have | Very Low | §2.4 or Table 0 footnote |

---

## Critical Observation on Target Venue

The OUTLINE.md and PROTOCOL.md both target **ACM SIGKDD Explorations Newsletter**, not CSUR. SIGKDD Explorations has a substantially lower bar: it accepts 15–20pp survey/overview pieces, does not require PRISMA-style methodology, and is oriented toward the KDD community rather than the computing-as-a-whole CSUR audience. If the actual target is CSUR, the paper requires approximately 10,000–15,000 additional words (CSUR surveys typically run 30–60 pages in double-column), a far more comprehensive corpus (CSUR expects 200–400+ papers for a mature topic), and the full set of gaps identified above as mandatory rather than recommended. If the target remains SIGKDD Explorations, gaps 1–5 are still strongly recommended but the scope is achievable at the current draft length. The decision of which venue to target should be made explicitly and the paper tuned accordingly — the current draft is appropriately sized for SIGKDD Explorations but would need substantial expansion for CSUR.