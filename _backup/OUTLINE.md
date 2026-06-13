# OUTLINE — Fairness and Equity in LLM-Based Agents: A Taxonomic Survey

*ACM SIGKDD Explorations, double-column, target ~15–20pp. Section page budgets are
guidance for arXiv v1 (~70%). Strong-model sections marked ★; mid-model body ☆.*

## Abstract (★)
LLM agents now *act* — selecting tools, accumulating memory, delegating across
roles, planning over long horizons — in hiring, lending, healthcare, and public
benefits. Fairness research, however, still mostly measures single-turn QA. We
present the first dedicated taxonomy of fairness and equity in LLM-based agents,
organized **by agent component** (where bias enters), paired with an evaluation
axis (group/individual/counterfactual; CFR/MASD; action-level disparity) and a
mitigation axis. We surface a measurement gap — today's benchmarks score answers,
not actions — and lay out a research agenda. We include a small original
cross-framework bias audit demonstrating component-level disparity. (~150 words)

## 1. Introduction (★) — ~1.5pp
- The shift from answering to **acting**; why agentic deployment raises the stakes
  (autonomy, compounding, opacity) in consequential domains (NIW framing: hiring,
  lending, healthcare, public benefits).
- Thesis: fairness must be analyzed **per agent component**, not as one metric.
- Contributions (numbered): (1) the agent-component taxonomy; (2) an evaluation
  framework incl. action-level disparity + CFR/MASD generalization; (3) a
  mitigation map; (4) an original cross-framework audit exposing the measurement
  gap; (5) an open-problems agenda + the case for an acting-agent benchmark.
- Explicit positioning vs. 2507.21504, 2602.04813, 2602.14970, and Zhang 2024.

## 2. Background & Scope (☆) — ~2pp
- 2.1 Fairness definitions: group, individual, counterfactual (Dwork, Hardt,
  Kusner) — concise, for a KDD audience.
- 2.2 LLM bias in brief (Gallegos, Zhang 2024 taxonomy; BBQ/BOLD/StereoSet) and
  why QA-level fairness ≠ agentic fairness.
- 2.3 What is an LLM agent? Component anatomy (perception/tool-use, memory/RAG,
  planning, multi-agent orchestration, long-horizon execution) — defines the
  taxonomy's organizing axis. (ReAct, Reflexion, AutoGen, Toolformer, RAG.)
- 2.4 Scope & methodology of this survey (inclusion criteria, corpus size, search
  process); explicit out-of-scope (pure single-turn QA fairness, non-LLM agents).

## 3. Taxonomy: Where Bias Enters the Agent Pipeline (★) — ~4–5pp (CORE)
Per subsection: definition → mechanism of harm → evidence (cite) → open edge.
- 3.1 Tool / API selection bias
- 3.2 Memory & retrieval — bias accumulation across turns
- 3.3 Multi-agent delegation & role assignment
- 3.4 Planning / decomposition disparities
- 3.5 User modeling & personalization harms
- 3.6 Long-horizon fairness drift over trajectories
- 3.7 Cross-cutting: how component harms **compound** (the agentic multiplier).
- Anchored by **Figure 1 (taxonomy tree)** and **Table 1 (component × harm
  mechanism × representative evidence)**.

## 4. How to Evaluate Agent Fairness (☆/★) — ~2.5pp
- 4.1 Metric families: group / individual / counterfactual mapped onto agents.
- 4.2 Counterfactual methods for agents: CFR & MASD (gen. from 2602.14970);
  counterfactual demographic swaps over trajectories.
- 4.3 Action-level disparity metrics (decision/tool/escalation disparity) — what's
  missing today.
- 4.4 Datasets & benchmarks: inventory (incl. clinical FairMedQA/mFARM/MedEqualQA/
  EquityMedQA, hiring/lending sets) — **Table 2 (benchmarks × level × domain ×
  agentic?)**; the punchline: almost all are QA-level → measurement gap.

## 5. How to Mitigate (☆) — ~2pp
- 5.1 Prompting / in-context debiasing.
- 5.2 Fine-tuning / alignment (RLHF/DPO/constitutional).
- 5.3 Guardrails & filters.
- 5.4 Multi-agent debiasing (debate, critic, role rotation).
- 5.5 Process-level / architectural interventions (memory hygiene, tool-selection
  constraints, planning audits). **Table 3 (mitigation × component × stage ×
  evidence)**.

## 6. Original Empirical Study: Cross-Framework Bias Audit (★) — ~1.5–2pp
- 6.1 Setup: 3–4 agent configurations on a consequential-decision task with
  counterfactual demographic swaps (synthetic profiles).
- 6.2 Metrics: CFR, MASD, action-level disparity.
- 6.3 Results: component-level disparity that QA-level scoring misses.
- 6.4 Takeaway: the measurement gap is empirically real → motivates §8.
- (Moderation insurance per PROTOCOL §3 + §6. Compute-light.)

## 7. Coverage Map & Cross-Analysis (★) — ~1pp
- **Figure 2 (coverage matrix): papers × components × fairness dimension** — shows
  where the field is dense (QA-level group fairness) vs. empty (action-level
  counterfactual fairness over long horizons). The visual that sells the gap.

## 8. Open Problems & Research Agenda (★) — ~2pp
- 8.1 The measurement gap: benchmarks for **acting** agents (sets up FairMedAgent;
  cite as companion/forthcoming).
- 8.2 Long-horizon & compounding fairness (longitudinal eval).
- 8.3 Multi-agent fairness dynamics.
- 8.4 Intersectional & sociotechnical harms in deployment.
- 8.5 Standardization, auditing, governance (ties to NIW national-importance).
- 8.6 Mitigation that operates at the agent (not token) level.

## 9. Conclusion (☆) — ~0.5pp

## References (★ verify) — target 150–200 entries, ALL verified real.

---

### Figures & tables (see FIGURES.md)
- **Fig 1** Taxonomy tree (agent components × bias entry points).
- **Fig 2** Coverage matrix (papers × components × fairness dimension).
- **Table 1** Component × harm mechanism × representative evidence.
- **Table 2** Benchmarks × fairness level × domain × agentic?
- **Table 3** Mitigation × component × pipeline stage × evidence.
- (opt.) **Table 0** Differentiation vs. the 3 competitor surveys + Zhang 2024.

### Draft assignment (Phase 3)
| Section | Model | Notes |
|---|---|---|
| Abstract, §1, §3, §6, §7, §8 | strong (Fable) | citation-driving + taxonomy + empirical |
| §2, §4, §5, §9 | mid (Sonnet) | body prose from corpus extractions |
