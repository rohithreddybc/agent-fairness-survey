Now I have enough to do the full internal consistency audit. Let me compile all findings systematically.

**AUDIT FINDINGS — LENS: INTERNAL CONSISTENCY ONLY**

---

**ISSUE 1 — MUST-FIX**
**Location:** Abstract (line 13), §2.4 (line 198), §2.5.2 (line 239/241), §7 (line 930/932), §9 (line 1055), Table 0 footnote (line 85), §1.3 corpus note (line 63), and Table 0 (line 81)

**Problem — Corpus size vacillates between 201 and 202 throughout the paper with no explanation:**

- Abstract: "Grounded in a verified corpus of **202** papers" (line 13)
- §1.3 Corpus note: "This survey covers **202** verified papers" (line 63)
- Table 0 footnote: "approximately 140 of the **202** papers" (line 85)
- Table 0, this survey row: corpus size listed as "**201**" (line 81)
- §2.4 multi-tagging note: "the total of unique papers is **201**" (line 198)
- §2.5.1 PRISMA table total: "**201** (unique)" (line 225)
- §2.5.2 Stage 4 text: "The final corpus comprises **202** unique papers spanning 2015 to 2026" (line 239)
- §2.5.2 PRISMA takeaway (line 241): "the **202** included papers"
- §7 tagging convention: "The corpus comprises **202** unique papers. Of these, **59** papers are tagged" (line 932)
- §9.1.1 line 1077: "The 202-paper corpus was assembled from..."

The PRISMA table (§2.5.1, the most authoritative count) produces 201 unique papers, and the multi-tagging note in §2.4 (line 198) also says 201. But the Abstract, §1.3, §2.5.2 Stage 4, the PRISMA takeaway, and §7 all say 202. Table 0 contradicts itself within the paper: the narrative says 202 and the table cell says 201.

**Fix:** Decide the canonical number (the PRISMA table sums to 201; Stage 4 prose says 201 in the first sentence then "202 unique papers" in the last sentence of the same paragraph — the last sentence is wrong). Use **201** everywhere, or recount and use **202** everywhere. Every occurrence must match. The note "202 included papers" in the Stage 4 PRISMA takeaway directly contradicts the Stage 4 opening sentence (n = 201).

---

**ISSUE 2 — MUST-FIX**
**Location:** §2.6.1 (line 262) vs. §1.3 corpus note (line 63)

**Problem — The "2024 or later" percentage is stated differently in two places:**

- §2.6.1: "The combined 2024 to 2026 cohort constitutes **69%** of the corpus" (derived: 78+60 = 138 out of 202 ≈ 68.3%, rounds to 68% or 69% depending on base)
- §1.3 Corpus note: "The **61%** of the corpus published in 2024 or later"

69% vs. 61% — a 8-percentage-point gap for the same stated quantity ("2024 or later"). These cannot both be correct. The §2.6.1 arithmetic with 78+60 = 138/202 = 68.3% is closer to 69% than 61%. The 61% figure appears only once (§1.3) and is inconsistent with the numbers given in §2.6.1.

**Fix:** Either correct §1.3 to 69% (matching §2.6.1 and its breakdown), or re-examine the breakdown and correct §2.6.1 if the underlying counts changed. One of these two figures must be wrong.

---

**ISSUE 3 — MUST-FIX**
**Location:** §2.5.2 Stage 4 (line 239) vs. §2.6.1 temporal span

**Problem — The temporal range contradicts itself:**

- §2.5.1 inclusion criteria table and §2.6.1: coverage from **2015** through June 2026 (§2.6.1 says "5 (2%) predate 2020" and the earliest are described as foundational ML fairness and NLP bias work)
- §2.5.2 Stage 4 final sentence: "The final corpus comprises 202 unique papers spanning **2015 to 2026**."
- §2.5.1 inclusion/exclusion Table 2.2 header says "Published or preprinted on or before June 10, 2026" — consistent with starting no earlier than 2015 per §2.6.1

Actually the 2015 start year in Stage 4 and §2.6.1 match. No issue here after closer reading. Disregard this sub-item.

---

**ISSUE 4 — MUST-FIX**
**Location:** §7 (line 981) and the Figure 3 operator table (lines 960–967)

**Problem — "52 of 68" claim contradicts what can be derived from Figure 3:**

The text at line 981 states: "52 of the 68 component-branch entries sit in the unspecified column of Figure 2."

However Figure 3 (the locus × BCF-operator table) enumerates per-row totals. Adding the Figure 3 row totals: Tool (1+3+1+1+6=12), Memory (2+2+3+1+4=12), Multi-agent (3+1+4+3+1=12), Planning (2+2+2+0+4=10), Personalization (1+4+3+1+3=12), Long-horizon (2+1+4+1+2=10). Total entries = 68. The "Uncharacterized" column sums to 6+4+1+4+3+2 = 20, not 52.

The 52 figure refers to the **unspecified fairness dimension** in Figure 2 (the fairness-dimension axis), while 20 refers to the **uncharacterized operator** in Figure 3. These are different matrices. The text at line 981 correctly says "Figure 2" not "Figure 3" — so the 52/68 claim is about Figure 2.

But Figure 2 is not explicitly reproduced in the text as a table — it is only described. The §7.2 section says multi-agent has "5 group, 1 individual" (=6 tagged), and planning has "4 group, 1 individual" (=5 tagged with group/individual), implying the remaining 68-11 = 57 entries for these two loci plus the other four loci's entries fall to unspecified. The math depends on what the Figure 2 matrix says exactly, and since Figure 2 is not shown as a table (it is described as a figure), the 52/68 cannot be directly verified within the paper's text. This is not strictly an inconsistency but a verifiability gap — readers cannot check the 52 figure. The paper mentions "57/59 component-tagged" in the task brief but the paper itself says "59 papers" and "68 entries."

The task brief mentions "57/59 component-tagged" — but in the paper §7 says **59** papers tagged, generating **68** entries (line 932). The number 57 does not appear in the manuscript at all. This is not an internal inconsistency within the paper itself; the paper is self-consistent at 59/68. Fine.

---

**ISSUE 5 — SHOULD-FIX**
**Location:** §6 agent configuration table (line 877–883) vs. §6.5 results table (line 914–918)

**Problem — C1 rung in §3.8 differs from C1 configuration in §6.1:**

In §3.8, the "C1 rung" of the hiring-screener walkthrough is labelled "add retrieval" (tool-using with retrieval), but the experimental C1 configuration in §6.1 is "Single-LLM with tool use (Schick 2023 Toolformer)" — described as a Toolformer-style tool-use, not specifically retrieval.

This is a mild label ambiguity, not a number error. More concretely: the §6.5 pilot results table (line 914) shows results for C0, C2, and C3 only — C1 was not run in the pilot. The §6.5 text explicitly states "three configurations are run: C0 (single call), C2 (reason-then-decide), and C3" (line 912). The configuration table in §6.1 defines four configurations C0-C3, and the §6.5 results table header column says "Configuration" with rows for C0, C2, C3 — which is consistent. No inconsistency here; the pilot correctly omits C1 with explanation.

However, the §3.8 worked example uses "C0 to C3" as capability rungs of a hiring screener (C0 = bare model, C1 rung = add retrieval, C2 rung = add tools+memory, C3 rung = multi-agent), and the §6.1 experimental configurations also use C0-C3 labels but with different architectures (C1 = Toolformer tool use, C2 = ReAct, C3 = two-agent). The C1 rung in §3.8 maps to "retrieval" while the C1 configuration in §6.1 maps to "tool use" — these are different things with the same label. A reader working through §3.8 then §6.1 will find the C-rung labels reused with different definitions.

**Fix:** Add a parenthetical clarification at the start of §3.8 or §6.1 explicitly noting that the C0–C3 rungs of §3.8 are an analytic decomposition of a worked example, while the C0–C3 configurations of §6.1 are experimental conditions that map to the BCF in a different way. Alternatively, use different notation in one place (e.g., "Rung 0–3" in §3.8 and "Config C0–C3" in §6.1).

---

**ISSUE 6 — MUST-FIX**
**Location:** §2.4 (line 198) vs. §7 (line 932)

**Problem — The number of component-tagged unique papers is stated inconsistently:**

- §2.4 multi-tagging note: "the total of unique papers is **201**"
- §7 tagging convention: "The corpus comprises **202** unique papers. Of these, **59 papers** are tagged to at least one of the six agent-pipeline component branches"

The §2.4 statement "total of unique papers is 201" refers to the overall corpus total (not just component-tagged papers); §7 says the corpus is 202 with 59 component-tagged. These two total-corpus figures (201 vs. 202) are the same 201/202 conflict already flagged in Issue 1. But note that §2.4 makes its "201" statement in the context of the multi-tagging convention, saying cross-cutting papers "are counted once in the unique total." This appears to be saying 201 is the total corpus size, which conflicts with §7's "202 unique papers."

This is the same root conflict as Issue 1, manifesting in a second location.

---

**ISSUE 7 — SHOULD-FIX**
**Location:** §3 intro / Figure 1 caption (line 345–347) vs. §3.0.6 component-assignment table (lines 419–426)

**Problem — Figure 1 caption labels architectural entry loci as "C1-C5" with "T-axis," but §3.0.6 uses the same labels C1-C5 plus a distinct T-axis. However, the Figure 1 caption says "five architectural entry loci (C1-C5)," yet §2.3 identifies **six** components (Components 1-6), with component 6 being long-horizon trajectory execution:**

In §2.3, the components are:
- Component 1: Tool and API selection
- Component 2: Memory and retrieval
- Component 3: Multi-agent orchestration
- Component 4: Planning
- Component 5: User modeling
- Component 6: Long-horizon trajectory execution

But the BCF has five architectural loci C1-C5 plus a temporal T-axis (§3.0.6, §3.6). The Figure 1 caption says "five architectural entry loci (C1-C5), the temporal axis (T-axis) on the feedback edge" — this is consistent with BCF.

The §2.3 text says "We identify **six** components" and lists six items. But the BCF, as explained in §3.6 (the "Why a temporal axis, not a sixth sibling" sub-section), explicitly says long-horizon drift is not a sixth component but a temporal axis. So §2.3 calls it six components but the framework uses five components + temporal axis.

This is a deliberate structural choice in the paper (§3.6 explains it at length), but the §2.3 section introduces "six components" without any caveat that one of them will later be reconceptualized as a temporal axis rather than a component. This creates a jarring inconsistency when a reader first sees "six components" in §2.3 and then encounters "five architectural loci C1-C5" and a temporal axis in §3.

**Fix:** In §2.3, when introducing Component 6 (Long-horizon trajectory execution), add a one-sentence forward-pointer: "Note: §3.6 argues that this is not an independent architectural component but a temporal axis on the feedback edge; we present it here as a sixth conceptual dimension before making that distinction precise in the BCF." This aligns §2.3's pedagogical introduction with §3's formal reframing.

---

**ISSUE 8 — SHOULD-FIX**
**Location:** §2.7 Glossary (line 282) — references "Section 2.7 (Threats to Validity)" from §2.2.1 (line 154), but the section titled "Threats to Validity" is actually §2.8

In §2.2.1 (line 154): "This concern is taken up again in **Section 2.7 (Threats to Validity)**."

But the section numbering in the paper is: §2.7 = "Glossary and Notation" and §2.8 = "Threats to Validity of This Survey."

The cross-reference should say §2.8 (Threats to Validity), not §2.7.

**Fix:** Change "Section 2.7 (Threats to Validity)" to "Section 2.8 (Threats to Validity)" in §2.2.1 line 154.

---

**ISSUE 9 — SHOULD-FIX**
**Location:** §3.8 (line 576) and §6.4 (line 907)

**Problem — "Results pending" placeholder not cleared:**

§3.8 four-step recipe (line 576): "the §6 protocol instantiates on a hiring-style task **(results pending)**"

§4.3 Definitions closing remark (line 695): "The audit protocol of §6 is designed to produce exactly such paired estimates **(results pending)**."

§6.4 (line 907): "FairMedAgent, a forthcoming companion benchmark...its development is independent of this survey's claims." — this is fine, clearly future work.

But the two "results pending" phrases in §3.8 and §4.3 appear to be leftover draft placeholders. §6.5 now exists and reports the pilot. These phrases should either be removed or updated to "results reported in §6.5." They constitute leftover draft text now that §6.5 exists.

**Fix:** In §3.8 line 576 and §4.3 line 695, replace "(results pending)" with "(pilot results in §6.5; full confirmatory study remains future work)" or similar.

---

**ISSUE 10 — SHOULD-FIX**
**Location:** §3.8 line 576 and Table 1

**Problem — "Table 1" is referenced but never reproduced:**

The text at §3.0.3 (line 385) says: "as Table 1 and §7 show, these are also the ones the field has instrumented least." The text at §3.8 (line 574) also mentions the BCF ladder. But Table 1 is never displayed in the manuscript. The abstract and §1.3 describe it as a "coverage table" with inclusion markers. §2.4 mentions it as the table where papers are marked `[adjacent evidence, transferred]`. §2.7 Glossary entry for "Adjacent evidence [transferred]" says it appears "in Tables 1 and 4." Table 4 exists (§5, the Challenges/Solutions/Gaps table). Table 1 does not appear anywhere in the manuscript text.

**Fix:** Either insert Table 1 (the per-paper component-coverage matrix) or, if intentionally omitted as a supplementary item, change every reference to "Table 1" to a note explaining it is in supplementary material or an appendix.

---

**ISSUE 11 — NICE**
**Location:** §2.5.1 PRISMA table (line 225) — The branch-column "Included" numbers do not sum to 201

The PRISMA table lists per-branch "Included" counts: 12+10+9+6+11+9+16+13+45+13+29 = 173. But the total row says 201 (unique). The note explains papers appear in multiple branches, so the sum exceeds (or should exceed) 201, not fall below it. A sum of 173 < 201 means the note's explanation runs backward from what is expected. If multi-branch papers each contribute to multiple rows, the per-branch sum should be ≥ 201 (due to multi-counting), not 173. Either some of the branch "Included" counts are under-stated, or the total of 201 is wrong, or the table is counting only primary-branch papers per row while the total counts multi-tagged papers once. This relationship is not explained and cannot be verified from the text.

**Fix:** Add a table footnote explaining why the column sum (173) is less than the unique total (201): the most likely explanation is that the Included column reports primary-branch tagging only, while the unique total also counts papers tagged as secondary-evidence cross-references not listed in any single branch. If that is the case, state it explicitly.

---

**ISSUE 12 — SHOULD-FIX**
**Location:** §6.5 pilot results / §9.1.4 limitations (line 1089) vs. abstract (line 13)

**Problem — Mild overclaim in the abstract about what the pilot shows:**

Abstract (line 13): "reports a small pilot of an executable cross-framework bias audit whose results illustrate P2 (decision-level parity masking a score-level disparity) and the P3 amplification trend (mean absolute score difference rising as agentic scaffolding increases)"

§9.1.4 Limitations correctly caveats: "Readers should treat P2 and P3 as well-motivated hypotheses...not as empirically confirmed claims."

§6.5 also says: "The monotone MASD trend across C0, C2, and C3 is suggestive of the masking-and-amplification mechanism the BCF predicts, but it rests on one small sample and could reflect score-scale noise rather than a stable effect."

The abstract says the pilot "illustrates" P2 and the P3 "amplification trend," while the body consistently uses "suggestive," "directional," and "consistent with." "Illustrates" is not overclaiming, but P3 "amplification trend" without the word "suggested" implies more certainty than the §6.5 and §9.1.4 language warrants.

**Fix:** Change the abstract's "and the P3 amplification trend (MASD rising...)" to "and is directionally consistent with the P3 amplification trend (MASD rising...)." This keeps the abstract honest while still advertising the pilot result.

---

**SUMMARY TABLE**

| # | Severity | Location | Issue |
|---|---|---|---|
| 1 | MUST-FIX | Abstract, §1.3, §2.4, §2.5, §7, §9, Table 0 | Corpus size oscillates between 201 (PRISMA table, §2.4 multi-tag note, §2.5.1 total, §2.5.2 Stage 4 opening) and 202 (Abstract, §1.3 corpus note, §2.5.2 Stage 4 closing sentence, §7, §9.1.1, Table 0 footnote) — must be unified |
| 2 | MUST-FIX | §1.3 line 63 vs. §2.6.1 | "61% published in 2024 or later" (§1.3) vs. "69%" (§2.6.1); both reference the same cohort; a single PRISMA breakdown produces only one of these |
| 3 | MUST-FIX | §2.2.1 line 154 | Cross-reference "Section 2.7 (Threats to Validity)" is wrong; Threats to Validity is §2.8, not §2.7 (§2.7 is the Glossary) |
| 4 | MUST-FIX | Table 0, §1.3 | Table 0 shows this survey's corpus as "201" while text surrounding Table 0 says "202" — direct table/text contradiction within a single page |
| 5 | SHOULD-FIX | §3.8, §4.3 | Two residual "(results pending)" phrases must be updated now that §6.5 exists |
| 6 | SHOULD-FIX | §2.3 vs. §3.6 | §2.3 introduces "six components" without warning that Component 6 will be reconceptualized as a temporal axis in §3.6, creating a confusing mismatch for readers |
| 7 | SHOULD-FIX | §3.0.3 line 385, and throughout §3 | "Table 1" is referenced repeatedly but never appears in the manuscript body |
| 8 | SHOULD-FIX | §2.5.1 PRISMA table | Branch "Included" column sums to 173, not ≥ 201 as the multi-branch counting convention would predict; no footnote explains the discrepancy |
| 9 | NICE | Abstract | "the P3 amplification trend" phrasing is slightly firmer than the body's consistent "suggestive/directional" language; add "directionally consistent with" |

**Sections that are internally consistent and require no action:** §3.0 (definitions D1–D3), §3.0.5 (P1–P5), §3.0.6 (assignment rules R1–R5), §4.2 (CFR/MASD formulas), §4.3 (TID/ESD/PAD definitions), §6.1–6.4 (protocol specification), §6.5 (pilot results: CFR=0/0/0, MASD=1.2/3.4/6.4, advance-rate=0/0/0 are internally consistent with each other and with the §9.1.4 limitations), §5.1–5.6 (mitigation), §8.1–8.6 (open problems), Table 3 (mitigation map), Table 4 (challenges/solutions/gaps). The Figure 3 operator table row totals are self-consistent (sum to 68). The P1–P5 / D1–D3 cross-references in §3.0.5 are correctly labeled. All C1-C5 locus labels in §3.1–3.6 resolve correctly to their definitions in §3.0.6. The §6 experimental config table (C0–C3) resolves to the BCF conduction profiles as described. The propositions referenced in §6.3 (H1→P2, H2→P3) resolve correctly. The §8 open problems all forward-reference back to correct §3.x / Figure 2 / Figure 3 coordinates. No "TODO," "pending unrun," or other placeholder text was found outside the two "results pending" instances in §3.8 and §4.3 flagged in Issue 5.