# Review — lens: BCF formal core (§3.0, §3.7, §4, §6, §7 notation)

**Overall:** The recent rigor edits (interaction residual in P1, signed-vs-magnitude hedge in §3.0.4, P5 tiers, the §3.0.6 mapping table, GENERATE-as-entry in D3) are real improvements, and several pieces are now sound (noted at the end). But the edits were applied unevenly: §3.7, §1.3, and §5.0 still carry the pre-revision strong forms, the signed disparity required by the conduction equation is never actually defined or estimated anywhere, and `R` is used for two different things across §3.0 and §4. Findings:

---

## Must-fix

**1. §3.7 still states P3 as an "if and only if," contradicting the weakened §3.0.5.**
- §3.0.5 P3: *"Δ_τ can exceed the naive sum Σ_c |Δ_c| when at least one AMPLIFY or GENERATE edge lies on a conduction path. This is a sufficient condition under the linearized model…"*
- §3.7 opening: *"trajectory disparity is super-additive (Δ_τ > Σ_c Δ_c) **if and only if** an AMPLIFY or GENERATE edge lies on a conduction path"* and later *"super-additivity is present **precisely** where some φ_e > 1…"*
- §3.7 also drops the absolute values (Σ_c Δ_c, not Σ_c |Δ_c|) — with signed Δ_c, `Δ_τ > Σ_c Δ_c` is trivially satisfiable by cancellation, so the unsigned form is the only meaningful one.
- Fix: rewrite the §3.7 lead to the weakened modal form with |Δ_c|, and delete "precisely." Also align §3.7's "Conversely… if every edge is PRESERVE or ATTENUATE, component audits compose into a conservative bound," which silently drops §3.0.5's required qualifier "and no interaction term."

**2. P3's "sufficient condition" label points the wrong direction mathematically.**
§3.0.5: *"This is a sufficient condition under the linearized model: an AMPLIFY/GENERATE edge can be offset by a downstream ATTENUATE edge…"* The explanatory clause itself proves **non**-sufficiency (an offset AMPLIFY edge yields no super-additivity). Under the linearized magnitude model the correct statement is: if all φ_e ≤ 1 and there is no interaction term, |Δ_τ| ≤ Σ_c |Δ_c|, so an AMPLIFY/GENERATE edge is **necessary** for super-additivity (within linearization) and not sufficient; outside linearization even necessity fails. Fix: restate P3 as "necessary under the linearized model, not sufficient (downstream offset), and not necessary once nonlinear interactions are admitted." As written, the proposition's label and its own justification contradict each other.

**3. The signed disparity the conduction equation requires is never defined, and none of the paper's estimators can measure it.**
- D2 (§3.0.2) defines Δ_c via *"a task-appropriate distance d (a flip indicator… an absolute score difference…)"* — nonnegative by construction.
- §3.0.4 then takes *"Δ_c and Δ_τ here as signed (directional) disparities so that oppositely directed component contributions can cancel."*
- Every operational quantity in §4.2–4.3 (CFR, MASD, TID via total variation, ESD, PAD via weighted ℓ1) is a magnitude. So P2's "sign-opposed entries" and the cancellation mechanism have no measurable counterpart in the survey's own instrument set, and D2 (the "canonical estimator") estimates only |Δ_c|.
- Fix: add one definition to §3.0.2 or §4.2 — a signed component disparity for ordered emission spaces (e.g., mean *signed* score difference, MSD_c = E[s_c(τ(x′)) − s_c(τ(x))], with a stated favorable-direction convention), note that flip-type emissions carry no sign without an orientation convention, and state explicitly which §4 metrics estimate |Δ_c| (all of them) versus signed Δ_c (currently none). One sentence in §4.2 acknowledging that cancellation diagnosis requires the signed variant would close the loop with P2.

**4. P4's direction is stated oppositely in §3.0.5 and §5.0.**
- §3.0.5 P4: mitigation *"must match the entry locus and **sit downstream of it**"* (and §3.8 step 4: "Intervene at the entry locus or on the amplifying edge").
- §5.0 (line 752): *"an intervention reduces Δ_τ only if it acts **at or upstream of** the entry locus producing Δ_c."*
These are contradictory, and §5.1's own analysis (prompting fails *because* it sits upstream of the GENERATE edge; cf. hu2024free in P4's justification) supports the §3.0.5 version. Fix §5.0 to "at the entry locus or downstream on its conduction path."

**5. `R` is overloaded: feedback channel in D1, role-assigner in §4.**
- D1/§3.0.6: R = *"the feedback channel"*; role assignment = π_ctrl (mapping table row C3).
- §4.1.1: *"which roles **R** assigns"*; §4.2: *"the role assignments for **R**"*; §4.3 closing remark: *"meeting P5 for the T, **R**, and planning surfaces of D1"* (where the metric in question, ESD, is an escalation/routing emission, not a feedback-channel quantity).
This breaks exactly the C1–C5 ↔ {π, T, M, R, π_ctrl} mapping the revision added. Fix: replace with π_ctrl in §4.1.1/§4.2; in §4.3, say "the T, routing, and planning surfaces" or key the claim to loci (C1, escalation, C4).

**6. §8.3 contradicts the Figure 3 grid and §7.4's own text.**
§8.3: *"Figure 3 shows the GENERATE column is the **least populated** in the multi-agent delegation row."* The grid (§7.4) gives delegation GENERATE = 3 — the largest GENERATE cell of any row, and not the smallest cell within the delegation row (PRESERVE = 1, Uncharacterized = 1). §7.4 itself says delegation provides "the clearest evidence of generation." Fix: the true claim is something like "GENERATE is thinly populated everywhere, and delegation is the only locus with more than one entry."

---

## Should-fix

**7. §1.3 Contribution 1 still carries the pre-weakening proposition forms.**
- P5: *"a fairness metric is adequate for an agent **iff** it surfaces Δ_c for every component with non-negligible φ"* — §3.0.5's P5 deliberately replaced the iff with adequacy tiers (and §4.3/§8.1 correctly use "only if").
- P3: *"trajectory disparity **exceeds** the sum of component disparities under amplifying operators"* — missing the "can."
Fix: align both one-line summaries with §3.0.5; reviewers will read §1.3 first and §3.0.5 second.

**8. The φ̂_e estimator (§4.2) is not sound as stated.**
φ̂_e = Δ_{c′}/Δ_c divides expectations of *different* distances (d_c vs d_{c′}) on *different* emission spaces (e.g., TV over tool distributions vs absolute score difference), so the classification φ̂ < 1 vs > 1 depends on the arbitrary scale of each d_c. Also, Δ_{c′} from trace-replay includes c′'s own entry disparity, so φ̂_e systematically overestimates conduction whenever c′ also GENERATEs — D3 defines φ_e as Δ_out/Δ_in *at one edge*, which is not what this ratio measures. Fix: (i) require d_c normalized to a common scale (e.g., each d_c ∈ [0,1]) as a stated condition for operator classification; (ii) add a sentence that φ̂_e is an upper bound on conduction absent a separate entry-disparity control (e.g., a second replay with the cue nulled at c's input). This matters because §3.8 step 3 and §6 are built on this estimator.

**9. §7.4 reclassifies ma2026implicit's operator against §3.2/§3.6/Table 3.**
§7.4: *"for memory, \cite{ma2026implicit} documents **generation** in the accumulation process."* §3.2 and §3.6 classify accumulation as the AMPLIFY edge (C2 × t), reserving memory-locus GENERATE for retrieval injection (hu2024free, wu2024rag); Table 3 tags ma2026implicit "AMPLIFY → ATTENUATE (memory audit)." Since Figure 3's cell counts depend on this tagging, harmonize (and §9.1.4's tagging caveat does not excuse an intra-paper inconsistency on the same citation).

**10. H2 is labeled "Super-additivity" but tests amplification, and the pilot's "interior" wording stretches P2.**
- §6.3 H2: *"P3 Super-additivity is observable. Total trajectory disparity is non-decreasing along C0 ⪯ C1 ⪯ C2 ⪯ C3."* Monotone endpoint disparity across configurations never compares Δ_τ to Σ_c |Δ_c| (no component decomposition is measured), so it is an amplification/monotonicity test, not a super-additivity test. The pilot text and §9.1.4 are otherwise admirably hedged; the residual problem is the H2 label. Fix: rename H2 ("amplification ordering") or add one sentence stating it is a proxy because the pilot does not estimate the component sum.
- §6.5: *"an endpoint near parity over a disparity that survives in the **interior**."* CFR and MASD are both computed at the output node (§6.2 says so); the masking is coarse-emission (thresholded decision) vs fine-emission (score) at the *same* node — a quantizer acting as a degenerate ATTENUATE edge — not the conduction-equation interior. One clause fixes it, and it would actually strengthen the P2 reading rather than weaken it.

**11. The pilot's C2 is not the protocol's C2.**
§6.1 defines C2 as *"ReAct reasoning-and-acting… φ cumulative over reasoning **+ retrieval**"*; §6.5's C2 is "reason-then-decide" with no tools or retrieval (the text says tool metrics "require a tool-using deployment"). A reader comparing the config table to the results table will conclude the wrong edge was exercised. Fix: state in §6.5 that the pilot C2 instantiates only the reasoning edge of the protocol's C2, or rename the pilot conditions. Also: §6.5 cites "the 10 synthetic profiles of §6.1," but §6.1 never states a profile count.

**12. Stale "(results pending)" in four places.**
§3.7 ("the audit protocol of §6 is designed to produce exactly such paired estimates (results pending)"), §3.8 (×2), §4.2, §4.3 — all written before §6.5 existed. For φ_e pairs and TID/ESD the pending status is still substantively true, but the phrasing now reads as an internal contradiction with §6.5. Fix: "(pilot in §6.5; the paired/action-level estimates await the full study)."

**13. C1-locus operator labels drift in §5.**
§5.1: *"the **AMPLIFY** operator introduced when a tool registry presents demographically unequal options (§3.1)"* — §3.1 classifies intrinsic registry/selection skew on clean input as GENERATE. Table 4, tool row: *"**PRESERVE or AMPLIFY on zero user-level input** \cite{blankenstein2025biasbusters…}"* — incoherent under D3 (on zero input the only available mode is GENERATE; φ is undefined), and it contradicts §3.1's explicit "reproducible GENERATE-operator signature" for the same citation. Harmonize both with §3.1.

---

## Nice

**14. Feedback recurrence edge case (§3.0.4):** "for φ_fb ≥ 1 it grows without bound" — at φ_fb = 1 growth is linear and requires Δ_entry > 0 (constant if Δ_entry = 0). One parenthetical.

**15. Glossary vs D3 on GENERATE:** glossary (§2.7) and §9 say "φ acting on zero input = GENERATE," while D3 says φ is *undefined* on zero input and GENERATE is a new entry. Align the shorthand with D3's (good) resolution.

**16. Δ_c index drift:** D2 indexes c ∈ {π, T, M, R, π_ctrl}; the conduction equation, §4.2 ("each component c of the taxonomy"), and §6 index by locus. The §3.0.6 table makes this resolvable, but picking C1–C5 (+ T-axis) as the canonical index and saying D1 objects are where each Δ_c is *measured* would remove the ambiguity (and dissolve the residual awkwardness of C4/C5 both mapping to π).

**17. P1 wording:** "folds into the nearest downstream GENERATE edge" presupposes such an edge exists; say the residual is *bookkept as a synthetic GENERATE entry* at the point of composition.

**18. P2 wording:** a downstream ATTENUATE edge with φ < 1 *reduces*; it "cancels" only as φ → 0. "Whenever a downstream ATTENUATE edge… cancels" should be "a sufficiently strong ATTENUATE edge (φ ≈ 0) or sign-opposed entries."

**19. §8.4 intersectional first step:** Δ_c^{A×B} = joint minus sum-of-marginals over nonnegative magnitudes can be negative and re-imports the sign/magnitude ambiguity of finding 3; state the convention.

**20. C0–C3 overloading:** capability rungs (§3.8), audit configs (§6), and loci (C1–C5) share the "C" namespace. §3.8 flags it, but §6.1's configs coincide with same-numbered loci only partially (config C2 ≠ locus C2, see finding 11). Renaming configs A0–A3 would cost one find-and-replace.

---

## What is fine (checked, no action)

- **D1** is internally consistent and matches §2.3 and the glossary exactly.
- **D3's GENERATE-as-entry resolution** ("we treat a GENERATE edge as contributing its own Δ_c term") is coherent and used consistently in P1 and the conduction equation.
- **The feedback recurrence math** is correct (steady state Δ_entry/(1−φ_fb) for φ_fb < 1), and Δ^(t) notation is consistent across §3.0.4, §2.7, §3.6, §4.1.5, §5.4, §8.2.
- **P5's tier scheme** is consistent with its restatements in §4.3 ("only if") and §8.1 — only §1.3's "iff" is stale (finding 7).
- **The §3.0.6 mapping table and rules R1–R5** are internally consistent and genuinely load-bearing in §3.1–§3.6 (R1 correctly separates singh2025biasb→C1 from wu2024rag→C2; R2 correctly places parziale2026once in C4; R4's drift-as-axis argument is coherent with P1 double-counting).
- **The §6 pilot does not overclaim**: the abstract, §6.4, §6.5 caveats, and §9.1.4 are mutually consistent in calling it directional, the ceiling-effect explanation for CFR = 0 is honest, and the only residual issues are the H2 label and "interior" wording (finding 10).
- **Figure 3 arithmetic reconciles**: row sums total 68, matching §7's 68 component-branch entries.

**Out-of-lens, one line:** the corpus count oscillates between 201 (Table 0, §2.4, §2.5 table, Stage 4 header) and 202 (abstract, §2.4 "covers 202", Stage 4 prose, §7), and the span is "2017 to 2026" in the abstract but "2015 to 2026" in §2.5.2 — same-paragraph contradictions a CSUR reviewer will catch immediately.

File: `C:\Users\rohit\Documents\Research Papers\research-command-center\06_paper_pipeline\AGENT_FAIRNESS_SURVEY\AGENT_FAIRNESS_SURVEY.md` (key lines: P1–P5 at 405–413, conduction eq. 391–399, §3.7 at 552, §5.0 at 752, §4 R-misuse at 600/630/695, §6.5 at 910–924, Figure 3 grid at 960–971, §8.3 at 1015).