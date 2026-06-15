Now I have a complete picture of both documents. Let me compile the inventory.

**Inventory of Every Figure and Table — Takeaways and Placement**

---

**Fig 1 — Taxonomy tree (agent-component taxonomy)**

(a) Takeaway: Unfairness in LLM-based agents enters at six structurally distinct pipeline components — tool selection, memory/retrieval, multi-agent delegation, planning, user modeling, and long-horizon drift — each with its own mechanism of harm, making a single model-level fairness score insufficient.

(b) Placement: Add to caption end after "organized by agent component." — append: "Unfairness enters at six structurally distinct pipeline stages, each with a mechanistically independent bias pathway; a single model-level metric cannot capture all six." Insert in-text at the close of §3 intro paragraph (line ~113), immediately before §3.1: "Figure 1 makes the structural claim concrete: the six entry points are not reducible to one another, which is precisely why QA-level scoring misses component-level disparity."

---

**Fig 2 — Coverage matrix (component × fairness dimension heatmap)**

(a) Takeaway: Across all six agent components, counterfactual fairness — the dimension that agentic action-level harm most requires — is the named framework in exactly one corpus paper, exposing a structural measurement gap that acting-agent benchmarks must fill.

(b) Placement: Add to caption end after "measurement gap this survey identifies": append "— counterfactual fairness, the evaluation mode agentic harm most requires, is applied in exactly one of the 57 component-tagged corpus papers." Insert in-text at the start of §7 (line ~336), immediately after the sentence ending "…cells this matrix leaves blank": "Figure 2 converts that assertion into a coordinate: the near-empty counterfactual column and the unspecified-dominated tool, memory, and personalization rows are the map's two organizing absences." Also cross-reference at the end of §4.4 (line ~229): "Table 2 and Figure 2, read together, make the same gap visible at two levels of granularity — benchmark inventory and corpus-wide coverage."

---

**Table 0 — Differentiation vs. prior surveys (positioning table)**

(a) Takeaway: This survey is the only work that takes the acting agent as its unit of analysis, organizes fairness by agent component across the full pipeline, and pairs a whole-survey fairness scope with an executable audit — a combination none of the five closest neighbors achieves.

(b) Placement: Add to caption end after "closest prior work.": append "No prior survey pairs agent-component organization with whole-survey fairness coverage and an executable audit." Insert in-text at §1.4 (line ~44), immediately after the sentence ending "…three near-neighbors": "Table 0 makes the comparison explicit and falsifiable across five dimensions: organizing axis, unit of analysis, fairness scope, and executability."

---

**Table 1 — Component × harm mechanism × evidence (core of §3)**

(a) Takeaway: Every agent component has at least one well-evidenced harm mechanism, but maturity is uneven — tool selection and user modeling are emerging (●○○), while multi-agent delegation and planning have the densest evidence — signaling where mitigation research should prioritize.

(b) Placement: Add to caption end: append "Maturity ratings (●●● well-studied / ●○○ emerging) reveal that half the pipeline remains at the emerging stage despite documented real-world harm." Insert in-text at the close of §3.7 (line ~169), the cross-cutting compounding section, immediately after "Table 1 summarizes each component's mechanism and evidence": "The maturity column of Table 1 is the secondary message: documentation density does not track deployment stakes, and the components most consequential in practice (tool routing, personalization) are rated ●○○."

---

**Table 2 — Benchmarks × level × domain × agentic? (core of §4)**

(a) Takeaway: Every benchmark in the corpus — clinical, lending, judicial, dialogue — scores model answers rather than agent actions; the "Agentic?" column has no "yes" entry, which is the empirical face of the survey's central measurement-gap claim.

(b) Placement: Add to caption end: append "No row bears 'yes' in the Agentic column — the table is a structured proof that the measurement gap is not a conceptual conjecture but an observed absence in existing infrastructure." Insert in-text at §4.4 (line ~220), immediately after the paragraph-opening sentence "Table 2 provides an inventory…": "The table's most informative column is the last: scanning it top to bottom and finding no 'yes' entry is the structured proof of the measurement gap the survey is built around."

---

**Table 3 — Mitigation × component × stage × evidence (core of §5)**

(a) Takeaway: Mitigation evidence clusters overwhelmingly at the LLM/token level — prompting and alignment — while the agentic components most implicated by the taxonomy (tool selection, retrieval, long-horizon drift) have little to no dedicated mitigation, revealing that the intervention apparatus is as misaligned with agent architecture as the measurement apparatus.

(b) Placement: Add to caption end: append "The table reveals that process-level and architectural interventions — the only tier that acts natively on agent components — constitute a small and recent minority of the mitigation literature." Insert in-text at §5 opening paragraph (line ~239), immediately after "Table 3 maps each mitigation family to the agent component…": "The table's sparsity in the lower rows — architectural and process-level — is the mitigation counterpart to Figure 2's sparsity in the counterfactual column: both reveal a field whose tools are calibrated to an earlier, simpler paradigm."

---

**Flags for figures/tables lacking a clear message or that are redundant:**

- **Table 1** lacks a caption in FIGURES.md (only column specs are given, no drafted caption text). It needs an explicit caption sentence before the ACM-LaTeX port — currently the reader must infer the message from §3.7's prose pointer.

- **Fig 2 and §7 prose** are partially redundant: §§7.1–7.3 narrate the matrix in full, word-for-word, such that a reader who skips the figure loses almost nothing. The figure's value is visual compression; the caption should be strengthened to stand alone with the "exactly one counterfactual paper" punchline so that a two-column reader scanning figures gets the finding without reading three sub-sections.

- **Table 0** is strong but its "Executable?" column label is slightly ambiguous — it blurs audit executability (this survey's §6) with benchmark executability (a property of the compared works). Rename the column to "Audit / executable metric?" and add a footnote distinguishing the two senses before submission.