# PROTOCOL — Fairness and Equity in LLM-Based Agents: A Taxonomic Survey

*Owner: Rohith (first + corresponding). Senior anchor: Dr. Wenbin Zhang (FIU).
Venue: ACM SIGKDD Explorations Newsletter (survey track). Target: arXiv v1 ~Sept 2026.
Full rationale: `reports/NEXT_PAPER_DECISION_2026-06.md`.*

## 1. One-line thesis
The first **dedicated, agent-component-organized** taxonomy of where unfairness
enters, how to measure it, and how to mitigate it in **LLM-based agent** systems —
distinct from QA-level LLM fairness and from broader agent-evaluation surveys that
treat fairness as a single dimension.

## 2. Positioning (what makes it defensible, honestly)
- **Parent lineage:** Zhang, Chu, Wang, "Fairness in Large Language Models: A
  Taxonomic Survey," ACM SIGKDD Explorations 2024 (DOI 10.1145/3682112.3682117).
  This survey is the *agentic successor*: LLMs that **act** (tools, memory,
  delegation, planning, long horizons), not LLMs that answer.
- **Differentiate against three near-neighbors (cite, position, surpass):**
  1. *Evaluation and Benchmarking of LLM Agents: A Survey* (arXiv 2507.21504) —
     broad agent-eval; fairness is one sub-topic, not the organizing axis.
  2. *Agentic AI in Healthcare: A Seven-Dimensional Taxonomy* (arXiv 2602.04813) —
     conceptual, single-domain, fairness = 1 of 7 dimensions; not executable.
  3. *Counterfactual Fairness Evaluation of LLM-Based Contact-Center Agents*
     (arXiv 2602.14970) — single-domain (customer service); we generalize its
     CFR/MASD method across all agent components.
- **Honesty bar:** no dedicated agent-component-organized fairness-of-agents survey
  exists as of 2026-06-11, but the window is narrowing (fairness is being folded
  into broader 2026 agent surveys; an AAAI'26 workshop paper is the canary).
  Claim: *first dedicated taxonomy*, NOT *first to mention fairness in agents*.

## 3. Hard constraint — arXiv moderation
arXiv now declines pure survey/review articles without original research. **The
survey MUST include an original empirical section** (small cross-model/cross-
framework agent bias audit) so it clears moderation as "survey + original results."
See §6. Backups: Zhang submits from his endorsed account; TechRxiv/SSRN last resort.

## 4. Taxonomy (organize BY AGENT COMPONENT, not by metric)
**Axis 1 — where bias ENTERS the agent pipeline:**
- (a) Tool / API selection
- (b) Memory & retrieval (bias accumulation across turns)
- (c) Multi-agent delegation & role assignment
- (d) Planning / decomposition disparities
- (e) User modeling & personalization harms
- (f) Long-horizon fairness drift over trajectories

**Axis 2 — how to EVALUATE:** group / individual / counterfactual fairness;
CFR (counterfactual flip rate) & MASD (mean absolute score difference);
agentic-action disparity metrics; datasets/benchmarks (note: today's are mostly
QA-level — the measurement gap).

**Axis 3 — how to MITIGATE:** prompting, fine-tuning, guardrails, multi-agent
debiasing, process-level interventions.

**Axis 4 — OPEN PROBLEMS + agenda:** culminating in a measurement-gap subsection
that motivates a fairness benchmark for *acting* agents (sets up the companion
FairMedAgent benchmark, built separately).

## 5. Phase plan (orchestration)
| Phase | What | Model tier | Status |
|---|---|---|---|
| 1 CORPUS | 11 parallel agents, one per branch → verified real papers | cheap (Sonnet) | ✅ **127 unique papers** (wf_26f7f904-733) |
| 2 ARCHITECT | dedupe + map to taxonomy; outline; taxonomy tree + coverage matrix + tables | strong (Fable) | ✅ corpus_master, references.bib, FIGURES.md |
| 3 DRAFT | parallel by section; mid for body, strong for intro/taxonomy/open-problems | mixed | ✅ 9 sections (wf_6b7d0afa-ee5) |
| 4 VERIFY | citation check (ZERO hallucinations); coverage; differentiation | strong/deterministic | ✅ arXiv API 0 not-found; cite-audit 0 missing |
| 5 ASSEMBLE | full draft (md + ACM-LaTeX), references.bib, FIGURES.md, PITCH, checklist | strong | ✅ AGENT_FAIRNESS_SURVEY.md + main.tex |

**v1 draft assembled (2026-06-11): ~14.8K words (~15–16 ACM double-col pp), 119 distinct
verified citations (344 occurrences), 0 hallucinated/missing.** Remaining gating items
before arXiv submit: (1) **run the §6 audit** (moderation insurance — currently a
results-pending protocol); (2) hand-clean the LaTeX port (tables from FIGURES.md, lists,
dollar/math); (3) render Figures 1–2; (4) Zhang co-author + arXiv-first by 2026-07-15.

## 6. Original empirical section (moderation insurance) — design
A compact, compute-light **cross-framework agent bias audit**:
- 3–4 agent setups (e.g., single-LLM tool-use vs. ReAct vs. a 2-agent
  delegation/debate setup) on a consequential-decision task (hiring screen or
  loan triage) with counterfactual demographic swaps.
- Metrics: CFR + MASD (reused from 2602.14970), plus an action-level disparity
  metric (e.g., disparity in tool invoked / decision taken / escalation rate).
- ~$100–300 API budget, pinned model versions, synthetic counterfactual profiles
  (no IRB). Goal: a real but modest result demonstrating component-level disparity
  the QA-level benchmarks miss — proof the measurement gap is real.
- This is *insurance + a teaser* for FairMedAgent, not the survey's main weight.

## 7. Deliverables (this folder)
`PROTOCOL.md` · `OUTLINE.md` · `corpus/` (raw + deduped corpus JSON/MD) ·
`drafts/` (per-section md) · `references.bib` · `FIGURES.md` ·
`PITCH_FOR_ZHANG.md` · `ARXIV_CHECKLIST.md` · `AGENT_FAIRNESS_SURVEY.md` (assembled).

## 8. Standing rules
- Commit + push every turn: `python scripts/auto_commit_push.py`.
- Log project decisions in `DECISIONS.md`.
- Honesty bar: extract genuine contributions; no padding; no hallucinated cites;
  position precisely against the 3 competitors; first beats best (ship v1 at ~70%).

## 9. Gates / risks (from the decision file)
- **Zhang commitment gate — 2026-07-15:** get arXiv-first agreement in writing.
  No commitment → survey shrinks to a health-specific SoK (#7) or waits.
- **Scoop watch** weekly on "fairness/bias/equity + agent." If scooped before
  2026-08-31 → pivot to the SoK framing; the FairMedAgent benchmark is unaffected.
- **First beats best:** arXiv v1 at ~70%; v2/v3 expand. Don't let venue
  perfectionism delay the preprint.
