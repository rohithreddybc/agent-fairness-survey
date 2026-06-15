# Review — new-content lens (§3.1–3.6 synthesis, §6.5 pilot, §3.7/§3.8)

Manuscript: `C:\Users\rohit\Documents\Research Papers\research-command-center\06_paper_pipeline\AGENT_FAIRNESS_SURVEY\AGENT_FAIRNESS_SURVEY.md`

## A. Pilot-claim consistency (§6.5 vs Abstract / Contribution 4 / §6 intro / §9.1.4)

**A1. MUST-FIX — Four stale "(results pending)" markers contradict the reported pilot.**
- §3.7 (Conjecture 1, ~line 560): "the audit protocol of §6 is designed to produce exactly such paired estimates (results pending)"
- §3.8 (recipe intro, ~line 576): "which the §6 protocol instantiates on a hiring-style task (results pending)"
- §4.2 (~line 660): "it is the estimator the audit protocol of §6 is designed to compute (results pending)"
- §4.3 (~line 695): "instantiates exactly these estimators for a hiring task across agent configurations C0 to C3 (results pending)"

Problem: the Abstract, Contribution 4, the §6 banner, and §9.1.4 all (correctly and consistently) say a pilot *ran* with directional results. "Results pending" is the forbidden third state and reads as a pre-pilot draft remnant. Note the right fix is not a blanket find-replace: the pilot computed only endpoint CFR/MASD and decision disparity, so the φ̂_e estimator (§4.2), the paired cross-interface estimates (§3.7), and TID/ESD/PAD (§4.3) genuinely were *not* run. Fix each to e.g. "(the §6.5 pilot reports endpoint metrics only; these paired/interior estimates are left to the full study)".

**A2. Fine — the four anchor texts are mutually consistent.** Abstract ("results illustrate P2 … and the P3 amplification trend … full confirmatory study left to future work"), Contribution 4 ("directional only"), the bolded §6 banner ("no claim outside §6.5 rests on its results"), and §9.1.4 (same 1.2/3.4/6.4 numbers, "well-motivated hypotheses … not empirically confirmed") all match each other and the table in §6.5. The §6.5 caveat paragraph is exemplary; no sentence claims significance from N=10.

**A3. SHOULD-FIX — §6.5 "survives in the interior" mischaracterizes what was measured.** Snippet: "an endpoint near parity over a disparity that survives in the interior." The pilot's MASD is computed on the *final score* — an endpoint emission, not an interior Δ_c. P2 (§3.0.5) is defined as endpoint ≈ 0 while *internal component* disparities are large; the pilot shows a coarse endpoint statistic (decision) masking a finer endpoint statistic (score). The Abstract's own gloss ("decision-level parity masking a score-level disparity") is the honest version. Fix: align §6.5 to the Abstract's phrasing, e.g. "an endpoint-level analogue of P2: the decision statistic masks a score-level disparity; the interior Δ_c demonstration awaits the full study."

**A4. SHOULD-FIX — "pre-registered as H2" (§6.5, line 922).** No registration artifact, URL, or timestamp is cited anywhere; §6.3 just states hypotheses in-text. A CSUR reviewer will ask. Fix: either cite the registration or soften to "stated in advance in §6.3."

**A5. SHOULD-FIX — pilot C3 deviates from protocol C3 without flagging it.** §6.1 defines C3 as "Two-agent delegation/debate \cite{wu2023autogen}" (φ at the delegation edge, π_ctrl active); §6.5 runs "a two-role recruiter-reviewer deliberation *within one context*." A single-context role-play has no delegation edge in D1 terms, so attributing the C3 MASD rise to the C3 *locus* is weaker than the table implies. Fix: add one caveat sentence ("the pilot's C3 is a single-context proxy for delegation; a true two-agent π_ctrl configuration is part of the full study").

**A6. SHOULD-FIX — release claim with no artifact.** "The harness, synthetic profiles, and raw decisions are released for exact reproduction" (§6.5) and Contribution 4's "released for independent reproduction" have no URL/DOI/footnote anywhere in the manuscript. Add the link or change "are released" to "will be released with the camera-ready."

**A7. SHOULD-FIX — N=10 appears only retroactively.** §6.5 says "the 10 synthetic profiles of §6.1," but §6.1's "Profiles and perturbation" paragraph never states a count. Add the number where the profiles are defined.

**A8. NICE — "the direction predicted by P3 (Super-additivity)" (§6.5).** The pilot measures no component disparities, so it cannot speak to super-additivity (Δ_τ vs Σ_c Δ_c), only to a rising-with-scaffolding trend. The Abstract's "P3 amplification trend" is the right register; reuse it here.

## B. §3.1–3.6: synthesis quality

Overall verdict: this is genuine critical synthesis, not a relapse into listing. Each locus makes comparative claims, names unresolved tensions with their mitigation implications (§3.2's truncation-vs-reordering-vs-filtering trichotomy is a model of the genre), and ends with a falsifiable measurement target. §3.2 and §3.6 are the strongest; §3.5 and §3.1 have specific defects below; none is an annotated bibliography.

**B1. MUST-FIX — §3.4 contradicts Figure 3 and Table 4 on the C4 operator.** §3.4: "the GENERATE operator at C4 is not a boundary case but the dominant mode"; conduction signature: "*Dominant outbound operator:* GENERATE." But the Figure 3 table (§7.4) shows Planning/decomposition GENERATE = **0** papers, §7.4's takeaway calls that column "nearly uncharacterized," and Table 4's planning row labels the harm "PRESERVE or AMPLIFY within chain-of-thought." Three parts of the paper assign three different operators to the same locus. Fix: if \cite{wu2025reasoning} and \cite{parziale2026once} are GENERATE evidence (as §3.4 argues), tag them so in Figure 3 and Table 4; otherwise soften §3.4 to "GENERATE-consistent, pending the revealer-vs-generator adjudication §3.4 itself describes."

**B2. SHOULD-FIX — Table 4 tool row mislabels the operator.** "PRESERVE or AMPLIFY on zero user-level input \cite{blankenstein2025biasbusters}" — disparity on zero input is the *definition* of GENERATE (D3), and §3.1 explicitly calls Blankenstein "a reproducible GENERATE-operator signature." Fix the label.

**B3. SHOULD-FIX — §3.1 misstates the theory to manufacture a conflict.** Snippet: "the theoretical expectation under P3 is that early-locus disparities should amplify when downstream operators are non-attenuating." Under the linearized BCF, non-attenuating includes PRESERVE (φ≈1), which conducts *unchanged*; amplification is expected only when some φ_e > 1. So \cite{xu2026ducx}'s PRESERVE finding does not conflict with P3 at all. Rephrase: the open question is whether clinical pipelines lack AMPLIFY edges or whether the measurement missed them — not a theory–data tension.

**B4. SHOULD-FIX — §3.5 says the same thing twice.** "What is unmeasured" (line 526) and "Open edge" (line 528) both cover: persistent user model, cue-channel fragility per \cite{tonneau2026different}, and the \cite{staab2023memorization} counterfactual-definability problem. Merge; the duplication makes §3.5 the locus most visibly bearing refactor scars.

**B5. SHOULD-FIX — thread-heading inconsistency across loci.** §3.1/3.2 use bold "What is known / What conflicts or is contested / What transfers only by analogy / What is unmeasured"; §3.3 uses "Evidence: what is known…" and replaces "What is unmeasured" with "Open edge"; §3.4 nests italic threads under "Evidence and synthesis"; §3.5 has both labels (B4). The four threads are *delivered in substance* at all six loci, but the inconsistent scaffolding undercuts the claim that this is a uniform analytical template. Normalize to one heading set.

**B6. SHOULD-FIX — malformed bib key.** `\cite{u2018algorithms}` (twice in §3.1) is almost certainly a mangled key for Noble 2018, *Algorithms of Oppression* (the "u2018" looks like a Unicode-quote artifact in key generation). Verify the .bib entry resolves.

**B7. NICE — §3.5 "What is known" second paragraph drifts toward listing.** "In education… In recommendation settings… Socioeconomic bias…" is the one stretch in §3.1–3.6 that enumerates domains without comparing them. One sentence on whether the education and recommender disparities share the stereotype-over-preference mechanism would restore the synthesis register.

## C. §3.7 and §3.8 coherence

**C1. MUST-FIX — §3.7 upgrades P3 to a biconditional that §3.0.5 explicitly denies.** §3.7 opening: "trajectory disparity is super-additive … **if and only if** an AMPLIFY or GENERATE edge lies on a conduction path" and "super-additivity is present **precisely** where some φ_e > 1." But P3 as stated in §3.0.5 says the condition is "**a sufficient condition** under the linearized model: an AMPLIFY/GENERATE edge can be offset by a downstream ATTENUATE edge, and nonlinear cross-component interactions can produce super-additivity even without one." Both directions of §3.7's biconditional are denied by the proposition's own statement. The converse claim in §3.7 ("if every edge … is PRESERVE or ATTENUATE, component-level audits compose into a conservative system-level bound") also drops §3.0.5's "no interaction term" qualifier. Fix: restate §3.7's opening as one-directional and restore the interaction caveat; otherwise a careful reviewer will quote the two paragraphs against each other.

**C2. MUST-FIX — three colliding C-numbering schemes, centered on §3.8.** Loci are C1–C5; §3.8's capability rungs are C0–C3 where the "C1 rung" adds retrieval (locus **C2**) and the "C2 rung" adds tools (locus **C1**); §6's configurations C0–C3 differ from both (§6 C1 = tool use, C2 = ReAct, vs §3.8 C2 = tools + persistent memory). The parenthetical "(The rungs are capability levels … the loci remain C1 to C5)" acknowledges but does not cure this, and the headline pilot numbers are reported against "C0/C2/C3" in the Abstract and §9.1.4 — a reader who cross-references §3.8 will attach them to the wrong architectures. Fix: rename §3.8's rungs (R0–R3 or L0–L3) and add one sentence in §6.1 mapping configs to §3.8 rungs.

**C3. Fine — §3.7's honesty machinery survives the pilot.** "no paper in the corpus traces a single disparity across two or more *different* components of one agent" remains true after §6.5 (the pilot is endpoint-only), and Conjecture 1's status is unchanged by the pilot. The §3.8 worked example's per-rung evidence citations (an2025measuring, wilson2024gender, hu2024free, blankenstein2025biasbusters, nguyen2025social) support the claims made at each rung; the four-step recipe is consistent with §6.2's metrics modulo A1.

**C4. NICE — dangling forward pointer.** §3.8: "The per-rung re-audit obligation this implies is taken up in §8.5" — §8.5 specifies a minimum audit spec but never discusses re-auditing after architecture upgrades. Add a clause to §8.5(iv) or drop the pointer.

## D. One out-of-lens item too load-bearing to omit

**D1. MUST-FIX — 201 vs 202 corpus count, and 2015 vs 2017 span.** Abstract: "202 papers spanning 2017 to 2026"; §2.4 and Table 0: "201"; Table 2.1 total: "201 (unique)"; §2.5.2 Stage 4 header "(n = 201)" followed in the same paragraph by "202 unique papers spanning **2015** to 2026"; §7: "202 unique papers." Pick one count and one span and propagate.

**Bottom line.** The pilot framing in the four anchor texts is honest and internally consistent — the discipline asked for is achieved there. The failures are seams: four pre-pilot "(results pending)" remnants (A1), §3.7's biconditional overstating its own proposition (C1), the §3.4-vs-Figure-3/Table-4 operator contradiction (B1), and the rung/locus/config numbering collision (C2). All four are mechanical to fix and all four are the kind of thing a CSUR referee quotes verbatim.