I have enough to deliver a complete holistic judgment. I noticed one concrete internal-consistency issue worth verifying — the Figure 3 cell counts vs. the "59 papers / 68 entries" tagging claim. The Figure 3 table sums far above 68. Let me confirm.

The Figure 3 table rows sum: Tool (1+3+1+1+6=12), Memory (2+2+3+1+4=12), Multi-agent (3+1+4+3+1=12), Planning (2+2+2+0+4=10), User (1+4+3+1+3=12), Long-horizon (2+1+4+1+2=10) = **68 operator-tags**, but these are tag instances (a paper "can carry multiple tags"), so this is internally consistent with 68 component-branch entries only by coincidence of number, not by construction. This is a genuine ambiguity a referee could probe. I have what I need.

---

# Holistic CSUR Acceptance Review — *Fairness and Equity in LLM-Based Agents: A Taxonomic Survey*

## (1) Overall lean: **MINOR REVISION (accept-oriented)**

Core reason: This is a genuinely publishable CSUR survey. It does the three things CSUR most rewards — comprehensive, transparently-constructed corpus (PRISMA, 202 papers, search tables); a clear novel organizing contribution (the BCF: agent-component × conduction-operator); and an actionable agenda — and it does them with unusual intellectual honesty about the boundary between what is evidenced and what is conjectured (Conjecture 1, the P3 hedging, the §6.5 caveats, §9.1 positionality). The prose has already been de-AI'd and reads as a coherent authored argument. The remaining issues are presentational and calibration-level, not structural. I do not see a must-reject or major-revision trigger.

The honest caveat to that lean: the *empirical* contribution is thin (a 10-profile, single-name-pair, single-model pilot). But the paper has been carefully re-architected so that **nothing load-bearing rests on the pilot** — it is framed as a survey whose contribution is the framework + protocol + coverage analysis, with the pilot as an explicitly-bounded "directional" illustration. Given that framing, the thin pilot is a should-fix calibration matter, not an acceptance blocker. A CSUR survey is not required to carry confirmatory experiments.

---

## (2) Is the central contribution novel, useful, well-supported enough for CSUR?

**Yes, with a real but survivable soft spot.**

**Where it is strongest.** The two-axis organization (entry locus × conduction operator) is the right abstraction and is, as far as the Table 0 comparison establishes, genuinely first-of-kind. The strongest single move in the paper is converting "agents make bias worse" into a *checkable* property: the conduction equation Δ_τ ≈ Σ_c Δ_c·Π φ_e plus the four operators turn a rhetorical worry into an audit specification (§3.8 four-step recipe; §4.2 the φ̂_e disparity-ratio estimator). P2 (Masking) and P4 (Mitigation-matching) are the propositions that earn their keep: P2 is well-supported (li2025actions, xu2025quantifying, turpin2023language) and P4 is operationally validated by the hu2024free-vs-kim2025mitigating contrast (prompt upstream of the GENERATE edge fails; embedder-level intervention succeeds). That contrast is the paper's best worked piece of evidence and it recurs correctly across §3.2, §3.8, §5.6.

**Where it is weakest.**
- **The conduction equation's status.** The paper is admirably explicit that it is "a bookkeeping identity under linearization and not a validated dynamical model" (§3.0.4). Good. But the equation still does a lot of *rhetorical* work throughout (§4, §6, §8) as if it were a quantitative tool, while not a single Δ_c, φ_e, or φ_fb is ever numerically estimated anywhere in the paper. The pilot reports endpoint MASD only. So the framework's central quantitative apparatus is, end to end, **never instantiated with a real number**. A sharp referee will note that the "five propositions / testable formal theory" framing (abstract, Contribution 1) writes a check the paper cashes only qualitatively. This is survivable because the paper repeatedly flags it ("these paired/interior estimates await the full study" appears ~6 times) — but the *frequency* of that disclaimer is itself a tell (see §5 below).
- **P3 (Super-additivity)** is the proposition with the weakest grounding: it is corpus-evidenced only *within* one locus (C3 multi-agent), and the cross-component version is openly labeled Conjecture 1. That honesty is the right call, but it means the headline "agentic multiplier" — which the abstract and intro lean on — is, strictly, a single-locus finding plus a conjecture. This is fine *if* the framing stays disciplined (it mostly does).

Net: the contribution clears the CSUR bar on novelty and usefulness. It is "a new lens + agenda" survey, not "a new validated theory" — and it should be sold unambiguously as the former.

---

## (3) Single highest-leverage change + runner-ups

**HIGHEST LEVERAGE (should-fix): Add one fully-worked numerical micro-example of the conduction machinery — even synthetic/illustrative — so the framework is instantiated once with actual numbers.**
Right now the entire formal apparatus (Δ_c, φ_e, the conduction equation, the disparity-ratio estimator φ̂_e = Δ_{c'}/Δ_c) is defined but never *run*. The biggest credibility lift available is a small box in §3.8 or §4.2: take the hiring ladder, put illustrative Δ_c values on C0→C1→C2→C3 edges, compute the φ̂_e's, show one ATTENUATE edge masking an upstream entry (P2) and one AMPLIFY edge producing super-additivity (P3) numerically. Label it explicitly "illustrative, not measured." This costs half a page, converts the framework from "vocabulary" to "calculus the reader can see operate," and directly answers the referee objection in (2). It is far higher-leverage than anything you could do to the pilot.

**Runner-up A (should-fix): Reduce the repetition of the "§6.5 pilot reports endpoint metrics only; these paired/interior estimates await the full study" disclaimer.** It appears verbatim or near-verbatim in §3.7, §3.8 (twice), §4.2, §4.3, and §6. One instance reads as scrupulous; six reads as defensive and, paradoxically, *amplifies* a referee's sense that the empirical gap is the paper's soft underbelly. Keep it once at the §6 anchor and once in §4 (where the metrics are defined); cut the rest to a short cross-reference.

**Runner-up B (should-fix): Render or stub the four figures.** Figure 0 (PRISMA), Figure 1 (annotated agent loop), Figure 2 (coverage matrix), Figure 3 (locus×operator grid) are referenced constantly and are central to §7's argument, but the manuscript carries only `<!--FIGURE1-->` and prose takeaways. Figure 2 in particular is invoked as "the headline of Figure 2 is a near-vacant column" — a CSUR referee will want to *see* it. At minimum, Figure 3's table is present inline (good); Figure 2 needs an actual rendered matrix, not just narrative counts. Submitting with figures as comments is the most concrete "not finished" signal in the document.

**Runner-up C (nice): Tighten Contribution 1's "testable formal theory" language** to match the cashed-out reality ("a formal organizing framework yielding five falsifiable propositions, four of which are grounded in existing corpus evidence and one stated as a falsifiable conjecture"). Pre-empts the "overclaimed theory" objection cheaply.

---

## (4) Narrative coherence end-to-end

**Strong and genuinely end-to-end coherent.** The spine §3 (framework) → §4 (metrics as Δ_c instances) → §5 (mitigation as engineered ATTENUATE edges keyed to P4) → §6 (protocol instantiating the §3.8 recipe) → §7 (corpus projected onto the same locus×operator grid) → §8 (open problems = the empty cells) is one argument, and each section explicitly re-uses the prior section's apparatus rather than restarting. Specific things that work:
- The five propositions are *threaded*: P2 reappears as Tension T3 in §4.1.5 and as the §6 H1 hypothesis; P4 is the literal organizing key of §5 and Table 3; P5 is the engine of the §4.4 "no row says yes" conclusion. This is the kind of cross-section load-bearing structure that distinguishes a real framework from a decorative one.
- §4.4's "two halves of the benchmark exist in literatures that do not cite each other" (capability harnesses have execution-without-measurement; fairness sets have measurement-without-execution) is the paper's most quotable synthesis and it falls directly out of P5. Excellent.
- §8's six problems each open with a "BCF coordinate" — the agenda is not a generic wishlist, it is the framework's empty cells. This is exactly what a CSUR agenda should look like.

**Does the abstract promise what the body delivers?** Mostly yes, and the abstract has clearly been disciplined: it already says the pilot "illustrate[s] P2" and "is directionally consistent with the P3 amplification trend... with a full confirmatory study left to future work." That is honest. **One residual mismatch (should-fix):** the abstract calls BCF "a testable formal theory: five propositions, stated under the linearized BCF model" — same overclaim as Contribution 1. Align both.

**One real seam (should-fix):** §2.3 introduces six components and calls long-horizon execution "Component 6," then §3.6/R4 reclassifies it as a *temporal axis*, not a sixth component. The paper *argues* this transition well (§3.6 "Why a temporal axis, not a sixth sibling"), but §2.3's "We identify six components" and the abstract's "six agent components" still seed the reader with the wrong count before the correction lands ~15 pages later. A referee skimming will hit "six components" then "five architectural loci + one temporal axis" and register an inconsistency. Fix: in §2.3 flag prospectively ("the sixth, long-horizon execution, we will argue in §3.6 is more precisely a temporal axis"). The abstract's "six agent components: ...and long-horizon trajectory execution" should similarly say "five architectural components plus a temporal axis."

---

## (5) Remaining credibility risks a CSUR referee would seize on

**RISK 1 (must-fix — internal consistency): The "59 papers → 68 component-branch entries" claim vs. the Figure 3 table.**
§7 tagging convention: "59 unique component-tagged papers generate 68 component-branch entries" (Figure 2). But Figure 3's table cells sum to **exactly 68 as well** (12+12+12+10+12+10), *despite* Figure 3 explicitly allowing each paper "multiple [operator] tags." If both Figure 2 entries and Figure 3 operator-tags total 68, that is either (a) a genuine coincidence that looks like a copy-paste artifact, or (b) an error. It cannot be that 59 papers yield 68 component-entries AND those same papers yield 68 operator-tags-with-multiplicity unless every component-entry carries exactly one operator tag — which contradicts "a paper can carry multiple tags." A referee who adds the columns will flag this. **Fix:** state the Figure 3 total explicitly and reconcile it with the 68 (e.g., "68 component-branch entries receive 68 operator classifications — one dominant operator per entry; multi-operator papers are noted in the text"), or correct the cell counts. This is the one place where the numbers, which the prior cycles tightened, still don't visibly tie out.

**RISK 2 (should-fix — the pilot's monotone trend is the most attackable empirical claim).** §6.5: MASD 1.2 → 3.4 → 6.4 across C0/C2/C3 is presented as "directionally consistent with P3." The caveats are thorough and honest. But note the *structural* weakness a referee will name: with CFR = 0 and advance-rate disparity = 0 everywhere (ceiling effect), the **only** moving quantity is MASD, and MASD rising with scaffold complexity is *also* the trivially-expected consequence of longer/more-elaborated reasoning chains producing more score variance generally — i.e., the trend may be a scaffolding-verbosity artifact, not demographic amplification, because there is no non-counterfactual control showing the score *spread* doesn't also grow. The paper says the trend "could reflect score-scale noise" — good — but doesn't name the more specific confound (scaffold complexity inflates score variance independent of demographics). Add one sentence acknowledging that a same-profile (no-swap) variance baseline across C0/C2/C3 is needed to attribute the MASD growth to the swap rather than to scaffolding. Cheap, and it inoculates against the sharpest pilot critique.

**RISK 3 (should-fix — FairMedAgent / FairMedQA-adjacent forward references).** §6.4 and §8.1 cite "FairMedAgent, a forthcoming companion benchmark... its development is independent of this survey's claims." Forward-referencing an unpublished authors' artifact twice can read as self-promotional and, worse, as leaning on vapor. Since it is explicitly future and "independent of this survey's claims," consider demoting both mentions to a single neutral "(e.g., a clinical acting-agent benchmark, in development)" without a name, or drop entirely. CSUR referees are allergic to surveys that advertise the authors' pipeline.

**RISK 4 (nice — claim "first dedicated survey").** The "first" claim is stated repeatedly (abstract, §1.2, §1.4, §3) and is defended well via Table 0. The defense is solid (the closest competitors — ranjan2025, ebrahimi2025, mohammadi2025, vatsal2026 — are correctly characterized). I would keep the claim but ensure it always carries the precise qualifier used in §1.4 ("first to simultaneously: (a) dedicate the entire axis to fairness, (b) structure by agent component, (c) introduce a named formal framework, (d) deliver action-level metrics"). The bare "first dedicated survey" in the abstract is slightly more exposed than the carefully-conjoined version; make the abstract match §1.4's conjunctive phrasing.

**RISK 5 (nice — figures-as-comments, already noted in (3)).** Restating only because a referee's *first* impression of "is this finished?" is figure presence. It is the lowest-effort, highest-signal fix.

**Things that are FINE and should not be touched:**
- The §6 pilot honesty is calibrated correctly — it is not an overclaim. Do not water it down further; it is already at the right level (the only addition needed is RISK 2's variance-baseline sentence).
- The transferred-evidence [†] convention is excellent and is exactly the rigor CSUR wants; it is consistently applied (§3.1–§3.6).
- The corpus numbers (202 unique; 548→415→234→202 funnel; primary-branch partition summing to 202; 65% post-2024) tie out internally and the partition is explicitly reconciled with the multi-tag convention. This is clean.
- The impossibility-results treatment (§2.1.4, §4.1.5 T1–T3) is correct and appropriately attributed (kleinberg2017, chouldechova2017, and crucially *not* attributing group fairness to dwork2012 — §2.1.2 explicitly flags that dwork is individual fairness). This is the kind of definitional precision that earns referee trust.
- Governance anchoring (§8, §9.1.2 academic-vs-legal gap) is well-judged and not overclaimed.

---

## Bottom line for the authors

This is an accept-leaning minor-revision survey. The framework is real, the corpus work is rigorous, the narrative is one coherent argument, and the honesty is a feature not a liability. To convert "minor revision" into "clear accept," do four things in priority order: **(1)** reconcile the Figure 3 / 68-entry counting (must-fix); **(2)** instantiate the conduction machinery once with illustrative numbers (highest-leverage); **(3)** render Figures 0–3; **(4)** trim the repeated pilot disclaimer and add the one missing pilot confound sentence (variance baseline). None of these requires new research — they are calibration, presentation, and one synthetic worked example. The empirical thinness is real but correctly walled off, and a CSUR survey is judged on its synthesis and framework, both of which are strong here.

Relevant file: `C:\Users\rohit\Documents\Research Papers\research-command-center\06_paper_pipeline\AGENT_FAIRNESS_SURVEY\AGENT_FAIRNESS_SURVEY.md` (Figure 3 table at lines 975–982; "59 papers → 68 entries" at line 947; pilot results at lines 929–939; abstract/Contribution-1 overclaim at lines 13 and 35; "six components" seam at lines 174–186 vs. §3.6 lines 545–549).