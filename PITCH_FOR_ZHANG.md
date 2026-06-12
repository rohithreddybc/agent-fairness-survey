# One-page pitch — Dr. Wenbin Zhang

**To:** Dr. Wenbin Zhang (FIU)  **From:** Rohith  **Date:** June 2026
**Re:** A direct successor to your SIGKDD Explorations fairness survey — co-authored, arXiv-first

---

## The paper
**"Fairness and Equity in LLM-Based Agents: A Taxonomic Survey"** — the first
*dedicated*, comprehensively-organized taxonomy of fairness and bias in LLM
**agent** systems. Target venue: **ACM SIGKDD Explorations Newsletter** (your home
turf, and fast). I lead and write; you anchor as senior author.

## Why this, why now
Your *Fairness in Large Language Models: A Taxonomic Survey* (SIGKDD Explorations
2024) is the canonical reference for fairness in LLMs that **answer**. LLMs now
**act** — they select tools, accumulate memory across turns, delegate across
multi-agent roles, plan, and run over long horizons — in hiring, lending,
healthcare, and public benefits. **Fairness research has not followed the field
from answering to acting.** This survey is the agentic successor to yours, and the
window to own it is closing: fairness is already being folded as a *sub-topic* into
broad 2026 agent-evaluation surveys. No dedicated, agent-component-organized
fairness-of-agents survey exists yet. We can be it — if we move now.

## What makes it defensible (not a rehash)
- **Organized by agent component, not by metric** — tool/API selection, memory &
  retrieval, multi-agent delegation, planning/decomposition, user
  modeling/personalization, long-horizon drift. This is the structural novelty.
- **A measurement gap, quantified.** I've already built the corpus (127 verified
  papers) and a coverage matrix: across all six agent components, formal
  *counterfactual* fairness — the natural test for "would the agent have *acted*
  differently for another demographic?" — is measured in **essentially one** paper.
  Today's benchmarks score *answers*, not *actions*.
- **Precisely positioned** against the three near-neighbors (broad agent-eval
  survey; the 7-dimensional healthcare taxonomy where fairness is 1 of 7; the
  single-domain contact-center counterfactual paper) and rooted in your 2024 lineage.

## Status (already done, this is not vapor)
- ✅ 127 real papers gathered and **machine-verified against the arXiv API** (0 not
  found; zero-hallucination discipline) → `references.bib`.
- ✅ Taxonomy, full outline, two signature figures (taxonomy tree + coverage matrix)
  and five tables specced.
- 🔄 Full section drafts in progress; assembled v1 imminent.
- ⏭ One small original cross-framework bias audit (synthetic profiles, ~$100–300,
  no IRB) so it clears arXiv moderation as **survey + original results**.

## What I need from you
1. **A nod to co-author + arXiv-first** (preprint now; venue trails). One ask:
   please confirm by **~July 15** so the territory claim isn't lost to a scoop.
2. Senior-author review of the taxonomy and open-problems framing.
3. (If easy) endorse/submit the arXiv listing from your account as backup, given
   arXiv's tightened stance on review articles.

## Why it's worth your name
Front-loaded citation accrual on your proven engine (first credible fairness
taxonomy of a just-hot subfield), in a venue you already publish in. It also seeds
a companion benchmark I'm building separately (fairness for *acting* clinical
agents) — the survey defines the gap, the benchmark fills it.

---
*Honest projection: 150–450 citations / 24 months (plannable band), higher tail if
it becomes the default reference. This is a plannable bet, not a moonshot.*

---

## Internal review note (not for Zhang)
- **Dilution-risk mitigation:** I am first + corresponding; I present it; the repo/
  project page lives under my GitHub. Zhang is confined to senior anchor. (Per the
  EB-1A independence architecture in `reports/NEXT_PAPER_DECISION_2026-06.md`.)
- **Gate:** no committed engagement by 2026-07-15 → shrink to a health-specific SoK
  or proceed solo with the benchmark; the survey must not block on Zhang.
- **Scoop watch:** weekly on "fairness/bias/equity + agent"; if scooped before
  2026-08-31, pivot framing to the SoK and let FairMedAgent carry the portfolio.
