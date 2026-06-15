# REVISION_PLAN — CSUR acceptance pass (synthesis of 4 reviews + 2 prior-art scans)

Source reviews in `reviews/`. This plan is authoritative for the revision workflow.
Verdict across reviewers: organizing idea + §7 coverage matrix are CSUR-worthy, but the
draft is right-sized for SIGKDD Explorations, claims results it doesn't have, and
under-delivers a formal framework. **Decision: commit to the CSUR expansion** (~30–40pp,
≥180–200 refs, named framework, full survey-craft). SIGKDD Explorations stays as fallback.

## Novelty status (honest): NOT scooped, but must cite + differentiate new neighbors
No paper scoops the dedicated agent-component fairness survey. New near-neighbors found
that MUST be cited + differentiated (and folded into Table 0):
- **Ranjan et al. 2025, "Fairness in Agentic AI: A Unified Framework…" (arXiv 2502.07254)**
  — most title-similar; 12pp position paper, classical MAS not LLM-agents, no component
  taxonomy. Differentiate as short/non-LLM/no-component-axis.
- **Ebrahimi & Asudeh 2025, RTAF survey of LLM-MAS** (ResearchGate; fairness = 1 of 4 pillars).
- **Binkyte 2025, "Interactional Fairness in LLM Multi-Agent Systems" (AIES'25, 2505.12001)**
  — narrow (interactional fairness, negotiation).
- **Yu et al. 2025, "Trustworthy LLM Agents" (2503.09648)** — already in corpus; fairness = 1 dim.
Plus adjacent ACM CSUR trustworthy-AI / fairness-ML surveys to engage (Mehrabi 2021, Caton
2024, Pessach 2022, etc.). If after differentiation we are not clearly distinct → sharpen
scope (the BCF framework below is the decisive differentiator).

## ★ CENTERPIECE: adopt the Bias Conduction Framework (BCF) — converts taxonomy → framework
(Full spec: `reviews/framework-originality.md`.) Two axes: **entry locus** (the 6 components,
unchanged) × **conduction operator** (how disparity transforms across each pipeline edge):
ATTENUATE (φ<1) / PRESERVE (φ≈1) / AMPLIFY (φ>1) / GENERATE (φ on zero input). Formal core
(new §3.0): D1 agent-loop tuple ⟨π,T,M,R⟩; D2 component counterfactual disparity Δ_c via
trace-replay; D3 operators; conduction equation Δ_τ ≈ Σ_c Δ_c · Π φ_e with feedback recurrence
Δ^(t+1)=φ_fb·Δ^(t)+Δ_entry. Five propositions P1 Locality, P2 Masking (= the measurement gap,
as a theorem), P3 Super-additivity (= the agentic multiplier, derived; = §6 H2), P4 Mitigation
matching, P5 Measurement adequacy. New §3.8 worked example (hiring agent C0→C3 ladder) + a
4-step auditor recipe. This single upgrade: (a) answers the "is it a real framework?" note,
(b) supplies the §4.3 formulas, (c) formalizes the agentic multiplier, (d) reuses ~90% of text.

## MUST-FIX (acceptance-blocking) — every one required
1. **HONESTY — resolve the §6 contradiction.** Abstract/§6/Conclusion currently say the audit
   "corroborates/confirmed/exposes" results, but §6.5 says it is unrun. Rewrite ALL of Abstract,
   §6, §9 to **protocol-only language** (no corroborate/confirm/expose). (The real run is
   scheduled separately for 2026-06-12 00:50; keep a clean `Results (pending)` placeholder so
   that run fills it.) NON-NEGOTIABLE.
2. **Delete in-manuscript meta-commentary**: the arXiv-moderation strategy talk (§6.4
   "positioned to clear arXiv moderation as survey with original results"), ALL "national
   importance"/NIW language (§1.1, §8.5), the venue/header scaffolding, and "Rohith (first &
   corresponding)" with no surname. These are disqualifying.
3. **Reconcile ALL numbers + publish tagging rules**: 127 papers; "eight branches" vs the ten
   listed; §7 "57 component-tagged / 51 unspecified" vs Figure 2 summing to 68/52. State the
   multi-tag convention precisely (a paper may map to several loci) and make every count agree.
4. **Fix definitions**: Dwork et al. 2012 is **individual** fairness (currently mis-placed under
   group in §2.1) — ground group fairness in demographic-parity / equalized-odds lineage; tighten
   the counterfactual-fairness definition (descendants of A under intervention, not "appears in
   any causal path").
5. **Deliver Contribution 2 with EQUATIONS**: formally define trajectory-level CFR/MASD and the
   action-level metrics (tool-invocation disparity, escalation disparity, plan-allocation
   disparity) as instances of D2's Δ_c. Replace §4.3's "no canonical formula" with the formulas.
6. **Repair taxonomy category structure**: justify long-horizon drift as a **temporal axis**, not
   a 6th sibling component (or make component×time explicit); give explicit **component-assignment
   rules** (resolve the tool↔retrieval overlap; stop papers floating between cells).
7. **Align inclusion criteria with the corpus**: §2.4 says non-agentic single-turn work is
   excluded, but §3.4/§3.5 rely on CoT/chatbot studies. Either mark transferred adjacent evidence
   explicitly per component, or restrict the claims. Remove "verified for existence" (reads as
   LLM-assembled); describe a real PRISMA-style pipeline.
8. **Rewrite annotated-bibliography prose → comparative synthesis** in §4.4 and §5.1–5.2; move
   inventories into Tables 1–2 (which must actually be BUILT — Table 1 absent, Table 2 is a
   placeholder). Compress token-level debiasing (out-of-scope per §2.4) to a paragraph.
9. **Reposition for CSUR**: expand to ~30–40pp, corpus toward ≥180–200 refs, CSUR structure
   (subsubsections, full tables).

## SHOULD-FIX
10. Add missing literatures: **fair ranking/IR** (Singh & Joachims, Zehlike, Ekstrand, TREC Fair
    Ranking) to §3.2; **fair RL/sequential** expanded in §3.6; **impossibility results**
    (Kleinberg, Chouldechova) + metric tensions over trajectories in §4.1; **Gender Shades**
    (Buolamwini & Gebru), **WEAT** (Caliskan) in foundations.
11. Confront **WebArena/τ-bench/AgentBench/Mind2Web/SWE-agent** when claiming no trajectory-level
    fairness benchmark exists (why they can't be demographically instrumented yet).
12. Downgrade §3.7 cross-component cascade to explicit **conjecture** (P3 covers the evidenced
    multi-agent case); no cited paper traces bias across two different components.
13. Cut **FairMedAgent** self-promotion to ≤1 neutral sentence (no vaporware advertising).
14. **Deduplicate positioning** (say "first dedicated" once, with Table 0); merge §2.2↔§4.4
    overlap; remove conclusion-only citations (benkirane2024diagnose, yang2025prompt,
    bommasani2021opportunities, bender2021dangers) or discuss them in body.
15. Add **legal/governance anchoring**: EU AI Act (Art. 10/13), US EEOC automated-hiring guidance,
    NYC Local Law 144, NIST AI RMF — in §8.5 + future-work operationalization.

## SURVEY-CRAFT GAPS to ADD (from completeness-gaps.md, ranked)
- G1 **Systematic methodology / PRISMA** subsection §2.5 + a PRISMA flow figure + a
  Branch|SearchString|DB|Found|AfterDedup|AfterScreen|Included table. (Critical/desk-reject risk.)
- G2 **Table 0** survey-comparison (build + place at end of §1.4). Columns: Survey|Year|Venue|
  Organizing axis|Agent coverage|Fairness-dedicated|Component-level|Corpus size|Original results|
  Action-level metrics. Add an "≈N papers not in Gallegos/Chu" note.
- G3 **Temporal/trend analysis** §2.6: papers-per-year-by-component chart + inflection events
  (ReAct/AutoGen/GPT-4 function-calling 2023) + venue distribution.
- G4 **Challenges→solutions→gaps** synthesis Table 4: Component|Harm|Mitigation evidence|Coverage
  (full/partial/none)|Open gap; cross-reference each §3.x open-edge to a §5 mitigation + §8.x item.
- G5 **Ethics / societal impact / limitations** §9.1: dual-use of the taxonomy (audit vs evade),
  academic-vs-legal fairness gap, positionality (English/US-EU-centric corpus), survey limitations.
- G6 **Glossary + notation** (end of §2): coined terms (agentic multiplier→now P3, action-level
  disparity, long-horizon drift) + CFR/MASD notation block.
- G7 **Threats to validity of the survey** (selection/construct/publication/recency bias).
- G8 **Reproducibility** of surveyed empirical work: Table 2 "Code/Data released?" column + §8.5 note.
- G9 **"How to use this survey"** reader-paths box (practitioner / auditor-regulator / researcher /
  benchmark-builder) at end of §1.
- G10 Future-work operationalization: each §8.x gets one concrete first-step (metric formula /
  dataset structure / system design).

## FIGURE/TABLE TAKEAWAYS (from figure-table-takeaways.md) — add a one-line "Takeaway:" to EACH
- Fig 1 (taxonomy tree): six structurally distinct entry points; one model-level score can't capture all.
- Fig 2 (coverage matrix): counterfactual fairness applied in exactly 1 of 57 component-tagged papers.
- Fig 3 (NEW, locus×operator): GENERATE/AMPLIFY edges — the agentic ones — are least instrumented.
- Fig 0 (NEW, PRISMA flow): corpus construction is reproducible.
- Fig (NEW, trend): the subfield's explosive 2024–26 growth.
- Table 0 (differentiation): only work pairing agent-component organization + whole-survey fairness
  + executable audit. (Rename "Executable?" → "Audit/executable metric?" + footnote.)
- Table 1 (component×harm×evidence+maturity): half the pipeline is ●○○ despite real-world harm.
- Table 2 (benchmarks): the "Agentic?" column has no "yes" — structured proof of the gap.
- Table 3 (mitigation, re-keyed locus×operator×stage): (amplify,generate) rows are empty.
- Table 4 (NEW, challenges→solutions→gaps): closes the §3→§5→§8 loop.
Each takeaway goes at caption-end AND as an in-text sentence at the cited line.

## EXECUTION (workflow, parallel by workstream; Fable only on framework + final synthesis)
- WS-A (Fable): write **§3.0 BCF framework** + **§3.8 worked example** + re-key §3.7 to P3.
- WS-B (Fable): **§4 equations** (trajectory CFR/MASD + action-level metrics as Δ_c) + §4.1 tensions.
- WS-C (Sonnet): rewrite §4.4 + §5 from listing → synthesis; build Tables 1–4.
- WS-D (Sonnet): add §2.5 methodology+PRISMA, §2.6 trend, glossary/notation, threats-to-validity.
- WS-E (Sonnet): §9.1 ethics/limitations, "how to use" box, governance/legal anchoring in §8.5+§8.x.
- WS-F (Sonnet): §3.1–3.6 conduction-signature lines + component-assignment rules + mark transferred
  evidence; integrate fair-ranking/IR, fair-RL, impossibility, Gender Shades/WEAT, agent benchmarks.
- WS-G (Sonnet): Abstract/§1/§9 honesty rewrite (protocol-only §6 language; delete NIW/meta/venue;
  dedupe positioning; Table 0; fix Dwork; cut FairMedAgent promo).
- Then: merge verified NEW papers into references.bib; reconcile all numbers; re-assemble; re-audit
  cites (0 missing); humanize; export PDF+Word; push to private repo (no Claude co-author).

## Honesty caveat to the user
This is a major expansion, not a polish. No one can guarantee 100% CSUR acceptance; the plan
removes every fixable reviewer objection found. The §6 audit must be RUN (scheduled) before the
honesty rewrite can become "results reported" rather than "protocol."
