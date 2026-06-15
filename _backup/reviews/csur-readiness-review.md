# CSUR Review: "Fairness and Equity in LLM-Based Agents: A Taxonomic Survey"

**Recommendation: Major Revision (borderline Reject-and-Resubmit in current form).** The organizing idea is publishable and the coverage matrix (§7) is genuinely good, but the draft has one fatal internal contradiction, several honesty/positioning problems, a taxonomy with unresolved category errors, and substantial stretches of annotated-bibliography prose. It also still wears its SIGKDD Explorations clothing — at ~15–20pp with 127 corpus papers, it is roughly half the length and depth CSUR expects.

---

## 1. Originality of the framework & quality of synthesis

**The framework is original in combination, not in parts — and the paper never confronts this.** The six "components" are the standard agent anatomy from Wang/Xi/Sumers (planning, memory, tool use, action, persona), crossed with fairness. That cross is a legitimate contribution, but a hostile reviewer will say: "you took the agent-survey decomposition and ran a fairness literature search per box." The defense must be that the *mechanisms of harm* differ per component in ways that demand different metrics and mitigations — the paper asserts this repeatedly but demonstrates it unevenly (strong for tools/multi-agent, weak for planning).

**The taxonomy has category errors a CSUR reviewer will not forgive:**

- **§3.6 "Long-horizon drift" is not a component; it is a temporal property of the other five.** You have five architectural loci plus one dynamics axis presented as a sixth sibling. FairMT-Bench is the "anchor result" in §3.2 *and* "again anchors" §3.6; `ma2026implicit` carries both §3.2 and §3.6. Either make horizon an explicit second axis (component × time) or defend the asymmetry head-on.
- **Tool vs. retrieval boundary is admitted to be porous in the text itself**: §3.1 says "When the 'tool' is a retriever, the bias becomes informational" and then "\cite{wu2024rag} again applies here" in §3.2. If your flagship contribution is the partition, papers cannot float between cells without stated assignment rules. Give explicit decision criteria for tagging a paper to a component.
- **§3.4 Planning is mostly non-agentic CoT work relabeled.** `wu2025reasoning` and `zhou2025veracity` study reasoning bias in QA-style settings; only `parziale2026once` is genuinely about agentic task allocation. This directly contradicts your own inclusion criterion ("Papers exclusively studying static generation tasks without an agentic framing were excluded" — §2.4). Same problem in §3.5: `kantharuban2024stereotype`, `weissburg2024llms`, `lin2024assessing` are single-turn chatbot/recommender studies. Either soften the inclusion criteria to "evidence transferred from adjacent settings, marked as such," or the corpus violates its own methodology. Right now a reviewer can falsify §2.4 with §3.

**Synthesis vs. listing:** §3.7 and §7 are real synthesis — the "formalization tracks decision explicitness, not harm severity" finding (§7.4) is exactly what CSUR wants. But large stretches are citation-chained enumeration:

- §3.2: "Mitigation exists but is partial: \cite{kim2025mitigating} controls the embedder." — a dangling one-clause sentence; `kim2025mitigating` was already cited two sentences earlier in the same paragraph.
- §3.6: "\cite{liu2025truth} and \cite{hong2025measuring} together establish that drift is measurable per-turn" — both already cited in the same paragraph; this sentence adds nothing.
- §4.4 is pure annotated bibliography: "X (FairMedQA) benchmarks… Y provides… Z introduces… W extends…" — five consecutive paragraphs of the pattern CSUR explicitly rejects. The Table should carry the inventory; the prose should carry *analysis* (e.g., why clinical benchmarks all stop at vignettes — incentives? data access? liability?).
- §5.1–5.2 likewise: one-paper-per-sentence summaries, and worse, they re-survey token-level LLM debiasing that §2.4 declared out of scope ("addressed in the parent survey"). §5 should be restructured around the component-mapping claim (Table 3) with token-level families compressed to a paragraph each.

**§3.7's "agentic multiplier" is overclaimed.** The only *evidence* of compounding is intra-multi-agent amplification (`nguyen2025social`, `madigan2025emergent`). The cross-component cascade paragraph ("an attribute inferred by user modeling becomes a retrieved fact… conditions tool selection… delegates along role lines") is a hypothesis dressed as a finding — no cited paper traces a bias across two or more *different* components. Mark it explicitly as conjecture, or it becomes the reviewer's example of the paper believing its own framing.

## 2. Comprehensiveness & currency

Currency is good (61% post-2024, cites into 2026). Comprehensiveness is not CSUR-grade:

- **127 papers is thin.** CSUR taxonomic surveys typically synthesize 200–400. Your own OUTLINE targets 150–200 references but the corpus is 127.
- **Fair ranking / fair IR is nearly absent** despite memory/retrieval being a core component: no Singh & Joachims, Zehlike et al., Ekstrand et al., TREC Fair Ranking. §3.2 rests on a handful of 2024–25 RAG papers while ignoring a decade of directly applicable retrieval-fairness theory.
- **Missing literatures**: fairness impossibility results (Kleinberg et al., Chouldechova) — essential when you propose multiple metric families; LLM-as-judge bias (directly relevant to agent self-evaluation and critic agents in C3); fair RL/bandits beyond two cites (your §3.6 formal grounding is exactly this literature); web/computer-use agent benchmarks (WebArena, τ-bench, AgentBench) — your claim that "no benchmark… presents a fairness evaluation problem at the level of a full agent trajectory" must confront why these can't be demographically instrumented; algorithmic recourse and contestability (invoked in §8.5 without citation); regulation (EU AI Act, NYC LL144 for hiring audits — you discuss hiring audits and governance with zero legal anchoring); social-choice/game-theoretic fairness for multi-agent allocation.
- **§2.4 methodology is under-specified for a "systematic" search**: no counts of hits screened/excluded, no date cutoffs, no screening procedure. The sentence "Candidate papers were verified for existence, accurate metadata, and relevance" is a red flag — verifying that papers *exist* implies the candidate list came from a generative model. Reviewers will infer an LLM-assembled corpus. Reword and describe a PRISMA-style pipeline.

## 3. Structure, flow, balance

- **The draft is formatted for the wrong venue.** Header says "Target venue: ACM SIGKDD Explorations Newsletter." Abstract is one bold-laden paragraph; section budgets are 15–20pp. CSUR needs ~30–40pp, restructured §3 with subsubsections, and full tables (Table 1 doesn't exist in the draft at all; Table 2 is a prose placeholder).
- **§1.4 and §2.4 "Positioning" are near-duplicates** — the same three-neighbor differentiation appears in §1.4, §2.4, §3 opening, §3.7, and §7.4. The "first dedicated survey" claim is made at least five times. Say it once, carefully, with Table 0.
- **§2.2 substantially overlaps §4.4** (both inventory QA benchmarks and state the measurement gap). Merge or differentiate.
- **§6 does not belong in a CSUR survey in its current state** (see §5 below); if retained, it must be complete and compressed.
- §3 components are single wall-of-text "mechanism" paragraphs (§3.2's runs ~300 words with ~10 citations). Break into the promised definition/mechanism/evidence/open-edge sub-headings.
- **Conclusion cites papers never discussed in the body** (`benkirane2024diagnose`, `yang2025prompt`, `bommasani2021opportunities`, `bender2021dangers`) — citation dumping; a reviewer checks this.

## 4. Critical depth & the agenda

§7 and §8 are the strongest sections; §8's problem/why/solution-needs structure is right. Weaknesses:

- **§8.1 and §4.4 advertise "FairMedAgent," your own forthcoming, uncited, unavailable benchmark, as "the empirical instrument the gap demands."** CSUR reviewers treat vaporware self-promotion harshly. Either cite a released artifact or cut to one neutral sentence.
- **Contribution 2 promises an "evaluation framework" with "generalized" CFR/MASD and "articulated" action-level metrics — §4 delivers zero equations.** §4.3 even complains that the three metrics have "no canonical formula" — *you are the survey; supply the formulas.* Define tool-invocation disparity, escalation disparity, and trajectory-level CFR formally. This is the single highest-leverage fix for the originality question.
- No treatment of metric *tensions* in agentic settings (can trajectory-level individual fairness and group parity coexist? what do the impossibility theorems become over trajectories?). A taxonomic survey that maps three metric families without their incompatibilities reads shallow.
- The "NIW framing" leaks: "a matter of national importance" (§1.1), "domains of clear national importance" (§8.5). This is US-immigration-petition language, US-centric, and instrumentally motivated. Remove; CSUR is international.

## 5. Scholarly rigor, honesty, consistency

These are the items that get a paper desk-killed:

1. **FATAL CONTRADICTION:** §6.5 states "The audit has been fully specified but not yet executed… No results are claimed at this stage." The Conclusion states "The original cross-framework audit (§6) **confirmed empirically** what the coverage matrix shows structurally: action-level disparity… is real, measurable, and invisible to today's QA-level scoring." The Abstract states "We **corroborate** it with a small original cross-framework bias audit **exposing** component-level disparity." Claiming results from an unrun experiment is, to a reviewer, scientific dishonesty. Run the audit before submission or rewrite Abstract/§6/Conclusion in protocol-only language everywhere.
2. **Meta-commentary must go:** §6.4 — "We also note its publication role candidly: …the work is positioned to clear arXiv moderation as a *survey with original results*." Strategy talk about gaming moderation inside the manuscript is disqualifying.
3. **Numerical inconsistencies:** §2.4 says "eight branches" then lists **ten**. §7 claims 57 component-tagged papers and "51 of the 57… unspecified," but Figure 2's matrix sums to **68** cells with **52** unspecified. Either papers are multi-tagged (say so and reconcile) or the counts are wrong.
4. **Dwork et al. (2012) is presented under the "Group fairness" heading** (§2.1) — it is the canonical *individual*-fairness paper, and your §2.1 then re-cites it correctly under individual fairness. Any FAccT-adjacent reviewer flags this in the first five minutes. Ground group fairness in demographic parity/equalized-odds lineage instead.
5. **"Exactly one paper" counterfactual claim (§7.1) is fragile:** `mayilvaghanan2026counterfactual` *is* a counterfactual evaluation of a deployed agent; `basu2026names` is counterfactual flip auditing in clinical/judicial decisions. The claim survives only via an undisclosed tagging convention ("named formal framing" within "component-tagged" subset). State the convention precisely or the headline finding looks engineered.
6. Counterfactual-fairness gloss is technically off: "deemed biased only if protected attributes appear in any causal path" — the criterion concerns descendants of the protected attribute under intervention; tighten.
7. Author line "Rohith (first & corresponding)" lacks a surname; draft scaffolding notes (header block) must be stripped.

## 6. Required revisions

### Must-fix (acceptance-blocking)
1. **Resolve the §6 contradiction**: execute the audit and report results, or rewrite Abstract, §6, and Conclusion as protocol-only — no "corroborate/confirmed/exposing" language anywhere. (Abstract, §6, §9)
2. **Delete the arXiv-moderation meta-commentary** and all pipeline scaffolding (header notes, "NIW framing," venue line). (§6.4, header, §1.1, §8.5)
3. **Reconcile all corpus numbers**: 127 papers, 8-vs-10 branches, 57-vs-68 tagged entries, 51-vs-52 unspecified; publish the tagging rules. (§2.4, §7, Fig 2)
4. **Fix the Dwork misattribution** and the counterfactual-fairness definition. (§2.1)
5. **Formally define the action-level metrics and the CFR/MASD trajectory generalization with equations** — deliver Contribution 2. (§4.2–4.3)
6. **Repair the taxonomy's category structure**: justify long-horizon drift as component-vs-axis; give explicit component-assignment rules; resolve the tool/retrieval overlap. (§3)
7. **Align inclusion criteria with actual corpus**: either admit transferred non-agentic evidence explicitly per component or restrict claims. (§2.4 vs §3.4/§3.5)
8. **Rewrite §4.4, §5.1–5.2 from annotated-bibliography prose into comparative synthesis**; move inventories into the (currently non-existent) Tables 1–2, which must be built. (§4.4, §5)
9. **Reposition for CSUR**: ~30–40pp, expanded corpus toward ≥180–200 references, CSUR-style structure; the draft is currently a KDD Explorations paper. (global)

### Should-fix
10. Add fair-ranking/IR foundations to §3.2; fair-RL/sequential foundations expanded in §3.6; impossibility theorems and their trajectory-level analogues in §4.1. (§3.2, §3.6, §4.1)
11. Confront WebArena/τ-bench/AgentBench-class agent benchmarks when claiming no trajectory-level fairness benchmark exists. (§4.4)
12. Downgrade §3.7's cross-component cascade to explicit conjecture; keep the multi-agent amplification as the only evidenced case. (§3.7)
13. Cut FairMedAgent promotion to one neutral sentence or cite a released artifact. (§4.4, §8.1, §8 synthesis)
14. Deduplicate positioning (keep §1.4 + Table 0; cut repeats in §2.4, §3, §3.7, §7.4); state "first dedicated taxonomy" once. (§1–§3, §7)
15. Merge or differentiate §2.2 and §4.4; remove conclusion-only citations or discuss them in the body. (§2.2, §9)
16. Describe the systematic search properly (queries, screening counts, dates); remove "verified for existence." (§2.4)
17. Add legal/governance anchoring (EU AI Act, NYC LL144, model audit regimes) to §8.5. (§8.5)

### Nice-to-have
18. A worked end-to-end example (one hiring scenario traced through all six components) early in §3 to make the taxonomy concrete. (§3 intro)
19. Maturity ratings (per FIGURES.md Table 1 spec) surfaced in the §3 prose so each component's evidence strength is graded. (§3, Table 1)
20. Discussion of fairness–utility and fairness–privacy tensions in user modeling (you cite `vijjini2024exploring` and `staab2023memorization` but never synthesize the tension). (§3.5)
21. Colorblind-safe heatmap and a "partial" category criterion for Table 2's Agentic? column (mFARM is "partial" with no stated rule). (Fig 2, Table 2)

**Bottom line:** the component-×-dimension coverage matrix and the measurement-gap thesis are a credible CSUR backbone. But the paper currently claims results it does not have, contradicts its own scope and counts, under-delivers its promised formal framework, and lists where it should synthesize. Fix items 1–9 and this becomes a serious candidate; submit as-is and it is rejected on item 1 alone.

Files reviewed: `C:\Users\rohit\Documents\Research Papers\research-command-center\06_paper_pipeline\AGENT_FAIRNESS_SURVEY\AGENT_FAIRNESS_SURVEY.md`, `...\OUTLINE.md`, `...\FIGURES.md`.