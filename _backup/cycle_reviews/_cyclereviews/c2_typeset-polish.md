Now I have a complete picture. Let me compile the full typeset-polish fix list.

---

## TYPESET-POLISH FIX LIST

Document: `C:\Users\rohit\Documents\Research Papers\research-command-center\06_paper_pipeline\AGENT_FAIRNESS_SURVEY\latex\main.tex`
Build: pdflatex x3, stable at 70 pages, 0 LaTeX errors, 0 undefined references after pass 3.

---

### 1. OVERFULL \hbox WARNINGS

After three passes the log shows the following Overfull \hbox entries. They are grouped by cause.

---

#### GROUP A: Table 0 (line 197) — resizebox on a table* uses \columnwidth, not \textwidth

**Root cause.** Table 0 (the survey-comparison table) is declared `\begin{table*}[htbp]` (a full-page-width float in two-column formats). It is wrapped in `\resizebox{\columnwidth}{!}{…}`. In `acmsmall` (single-column) `\columnwidth` = `\textwidth`, so the mismatch does no harm dimensionally — but the table body itself has 10 `p{0.090\textwidth}` columns whose total width (10 × 0.09 + column rules) slightly exceeds the text measure. The resizebox should scale them to fit, but the explicit `p{…}` sizes inside prevent the scaler from shrinking the column entries. Result: ~15 individual overfull hboxes between 1.66 pt and 31.72 pt, all at line 197 (the longtable row for "Organizing axis / Audit/executable metric? / Computational Linguistics" etc.).

**Observed overfull widths at line 197 (Table 0):**
- 8.78 pt — "Organizing" header cell
- 2.46 pt — "dedicated|" cell
- 13.38 pt — "Component-" cell
- 31.73 pt — "Audit/executable" cell (worst)
- 16.85 pt — "Computational" (italic venue name)
- 1.67 pt — "Peripheral|" cell
- 9.82 pt — "Mohammadi" author cell
- 3.15 pt — "Evaluation" cell
- 10.36 pt — "Interactional" cell
- 8.34 pt — "dimensional" cell
- 3.61 pt — "Healthcare|" cell
- 9.47 pt — "Trustworthy" cell
- 20.26 pt — "Mayilvaghanan" (longest author name)
- 6.37 pt — "CFR/MASD" cell

**SEVERITY: should**

**Fix.** Change `\resizebox{\columnwidth}{!}` to `\resizebox{\textwidth}{!}` on line 179, and reduce the 10 column widths from `p{0.090\textwidth}` to `p{0.080\textwidth}` (or use `\linewidth` inside the box). Alternatively, switch to `\footnotesize` (line 177 already has `\small`) inside the tabular, which will reduce cell content enough to stop overflow without changing column specs. The cleanest single-line fix:

```latex
% line 177: change \small to \footnotesize
\centering\footnotesize
% line 179: change \columnwidth to \textwidth
\resizebox{\textwidth}{!}{%
```

Both changes together guarantee all 10 × 0.090 columns fit inside the scaled box.

---

#### GROUP B: Table 2.1 longtable (lines 342, 347) — "Records / Dedup" header cells

**Root cause.** Table 2.1 (the PRISMA search protocol, lines 338–365) uses a raw `longtable` with hand-tuned `p{…}` column widths (8 columns summing to approximately 0.822\textwidth plus separators). The "Records Identified" and "After Dedup" header cells at lines 342 and 347 (`\endfirsthead` / `\endhead` copies of the header) overflow by 4.30 pt and 2.56 pt respectively. The seventh and eighth columns (`p{0.052\textwidth}` and `p{0.045\textwidth}`) are too narrow for the bold header text "Records" and "Dedup".

**SEVERITY: should**

**Fix.** Widen columns 5–8 slightly. Change on line 338:
```latex
% old
|p{0.052\textwidth}|p{0.045\textwidth}|p{0.050\textwidth}|p{0.085\textwidth}|
% new
|p{0.055\textwidth}|p{0.050\textwidth}|p{0.055\textwidth}|p{0.090\textwidth}|
```
Compensate by reducing column 2 from `p{0.165\textwidth}` to `p{0.155\textwidth}`. Total stays under \textwidth.

---

#### GROUP C: Table 2.1 longtable (line 355) — "Planning/decomposition|" cell

**Root cause.** Row "Planning/decomposition" in the Branch column (line 355) overflows by 15.17 pt — "Planning/decomposition" is a single unhyphentaed word that is wider than its `p{0.135\textwidth}` column.

**SEVERITY: should**

**Fix.** The word already contains a slash that TeX does not treat as a hyphenation point. Insert a discretionary zero-width break after the slash on line 355:
```latex
% old
Planning/decomposition & ...
% new
Planning/\allowbreak decomposition & ...
```
Alternatively rename to "Planning \& decomp." in the cell only.

---

#### GROUP D: Contribution 2 paragraph (line 143) — "Trajectory-level" runs over

**Root cause.** The Contribution 2 bold-plus-normal inline paragraph at line 143 has the word "trajectory-level" at the start of a line that cannot be broken further. Overfull by 1.62 pt (barely visible). Cause: the bold lead-in "Contribution 2: Trajectory-level and action-level disparity metrics." is a run-on sentence with few hyphenation opportunities.

**SEVERITY: nice**

**Fix.** Insert `\linebreak[2]` after "metrics." or add `\-` inside "dis\-par\-ity" earlier in the paragraph to give TeX a hyphenation point. Alternatively add `\sloppy` scoped to just this paragraph with `{\sloppy … \par}`.

---

#### GROUP E: Venue distribution paragraph (lines 491–492) — long citation parenthetical

**Root cause.** Line 491 contains the sentence "arXiv preprints (62 papers, 31%), ACL-family venues (ACL, EMNLP, NAACL, Findings) (41 papers, 20%), NeurIPS/ICML/ICLR". The slash-separated string "NeurIPS/ICML/ICLR" (29.99 pt overflow) cannot be broken because TeX does not hyphenate across slashes.

**SEVERITY: must** (30 pt overflow is visually noticeable — a black rectangle protrudes into the margin in the rendered PDF)

**Fix.** Insert `\allowbreak` after each slash on line 491:
```latex
NeurIPS\allowbreak/\allowbreak ICML\allowbreak/\allowbreak ICLR
```
Or reword to "NeurIPS, ICML, and ICLR" which breaks naturally.

---

#### GROUP F: BCF paragraph (lines 862–863) — "technical-evaluator-"

**Root cause.** Line 862: the hyphenated compound "technical-evaluator-agent" starts a new line and TeX cannot break it further. Overfull by 1.01 pt (trivially small, not visible at normal resolution).

**SEVERITY: nice**

**Fix.** Hyphenate "tech\-nical-eval\-u\-a\-tor-agent" at the first compound to give TeX a break point, or add `\sloppy` scoped to this paragraph only.

---

#### GROUP G: Table 3 longtable (lines 911, 1059, 1069) — narrow "Entry Locus" / "Intervention Class" cells

**Root cause.** Table 3 (Mitigation Map, line 1170) has entries "Delegation/assignment|" (11.81 pt, line 911), "Toxicity/bias/value|" (1.57 pt, line 1059), and "type/toxicity/performance|" (13.03 pt, line 1069). The slashed compound words in the Evidence Density / Primary Metric columns exceed their narrow `p{0.075\textwidth}` column.

**SEVERITY: should**

**Fix.** As with Group C: insert `\allowbreak` after each slash in those specific cells:
```latex
Toxicity\allowbreak/\allowbreak bias\allowbreak/\allowbreak value
type\allowbreak/\allowbreak toxicity\allowbreak/\allowbreak performance
Delegation\allowbreak/\allowbreak assignment
```

---

#### GROUP H: Table 2 longtable (lines 1042–1043, 1047–1048) — "Agentic?" and "Code/Data" header cells

**Root cause.** Table 2 (line 1038) has a `p{0.075\textwidth}` column for "Agentic?" (overflow 1.04 pt) and `p{0.085\textwidth}` for "Code/Data released?" (overflow 3.47 pt). Both appear in the `\endfirsthead` header at line 1042 and the `\endhead` repeat at line 1047.

**SEVERITY: nice**

**Fix.** Widen these two columns by 0.005\textwidth each and reduce one of the wider text columns (e.g., "Primary metric" from 0.180 to 0.170) to compensate. Or add a forced line break in the header cell: `Code/Data\\released?` using a `\thead{…}` from `booktabs` or simply `\shortstack`.

---

#### GROUP I: Table 3 longtable (lines 1174–1175, 1179–1180) — "Evidence" header cell

**Root cause.** The column header "Evidence Density" in Table 3 overflows its `p{0.075\textwidth}` column by 2.23 pt, appearing in both the `\endfirsthead` (line 1174) and `\endhead` (line 1179) copies.

**SEVERITY: nice**

**Fix.** Change the header cell to `Evidence\\Density` with `\shortstack[l]{Evidence\\Density}` so it wraps, or widen the column from `p{0.075\textwidth}` to `p{0.085\textwidth}` and reduce "Representative Evidence" from `p{0.140\textwidth}` to `p{0.130\textwidth}`.

---

#### GROUP J: Escalation/deferral paragraph (lines 1284–1285) — inline math overfull

**Root cause.** Line 1284: "Escalation/deferral disparity ($\Delta_{\mathrm{esc}}$ at routing)" overflows by 7.77 pt. The inline math followed by the continuation text "differential rates of human escalation" pushes the line over. The slash in "Escalation/deferral" cannot break.

**SEVERITY: should**

**Fix.** Insert `\allowbreak` after the slash: `Escalation\allowbreak/\allowbreak deferral disparity`. The inline math will then be pushed to the next line cleanly.

---

#### GROUP K: Open-problems paragraph (lines 1483–1484) — "acting-agent" compound

**Root cause.** Line 1483: "A minimal acting-agent fairness benchmark requires" overflows by 4.88 pt. "acting-agent" is a novel compound that the hyphenation dictionary does not split further.

**SEVERITY: should**

**Fix.** Hyphenate: `act\-ing-agent` — this gives TeX a break point between "acting" and "-agent" that is typographically sensible.

---

#### GROUP L: pgfplots figure (lines 468–469) — figure caption overflow

**Root cause.** Lines 468–469 produce a 9.09 pt overfull inside the pgfplots `tikzpicture` environment. The `\caption` at line 469 contains "The 2024 to 2026 cohort (78 + 53 = 131 papers, 65%)" — the plus sign and numerals cannot be broken. The figure itself is set to `width=\columnwidth` but the pgfplots output box is slightly wider due to the axis labels.

**SEVERITY: nice**

**Fix.** Change `width=\columnwidth` to `width=0.96\columnwidth` on line 450. This gives pgfplots enough slack to place axis labels without exceeding the text measure.

---

### 2. UNDERFULL \vbox WARNINGS

The log reports 13 `\Underfull \vbox` warnings. All are of the form "Underfull \vbox … has occurred while \output is active" and originate from page-breaking around large floats (longtables, figures, and the pilot results table).

| PDF page | Badness | Cause | Fixable? |
|---|---|---|---|
| ~20 (after abstract/maketitle) | 10000 | acmsmall inserts a large stretch glue after the author block; the page has too little content | Harmless — standard for first-page ACM layout |
| ~23–24 | 10000 | Pages following the PRISMA TikZ figure; longtable breakpoints leave half-empty pages | Harmless — float spillage |
| ~25–31 | 10000 | Pages during the Table 0 float sequence; `table*` placement leaves vertical whitespace | Harmless — float placement |
| ~35–37 | 10000 | Pages during longtable 2.1; the table's `\bottomrule` ends mid-page | Harmless |
| ~43 | 6396 | Infinite glue shrinkage on p.42 triggers a vbox badness carry | **Fixable** — see below |
| ~51 | 5359 | Same infinite-glue issue on p.49/51 | **Fixable** — see below |
| ~63 | 4024 | Page before pilot results table; text ends near top of page | Harmless |
| ~66–69 | 10000/6396 | Bibliography pages; bibliography entries vary in height and leave inter-entry vertical glue | Harmless — standard natbib/acmart behaviour |

**The two "ignored error: Infinite glue shrinkage found in box being split" messages on pages 42, 49, and 51** are the only structurally notable vbox warnings. They indicate that a `\stretch` or `\vfill` inside a longtable row is being split across a page break, which confuses TeX's page splitter. The trigger is almost certainly the rows in Table 4 (lines 1231–1236) that contain very long cell texts with paragraph content — some cells contain `\item`-like multi-sentence blocks that produce `\parskip` inside a `p{…}` column, and when those rows are split, infinite glue error emerges.

**SEVERITY: should** (for the infinite-glue errors on pages 42/49/51)

**Fix.** Add `\pagebreak[0]` before the rows of Table 4 that are longest (the "Memory & Retrieval" and "Long-horizon Drift" rows at lines 1232 and 1236), or add `\nopagebreak` before those rows to prevent splitting them. The cleaner fix is to add `\setlength{\extrarowheight}{2pt}` in the Table 4 `\begingroup` and remove any `\vfill` or `\stretch` that may have been silently inserted by the editor.

All other underfull vbox warnings (badness 10000 on pages with large floats) are structurally harmless in an ACM CSUR submission and require no fix.

---

### 3. PAGE FOOTER: "Article ." — MISSING METADATA

**Issue confirmed visually.** Every page footer (pages 1–70) reads:

> `ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: June 2026.`

The word "Article" is followed by a period with no article number — the token `\acmArticle` is unset, producing a blank. Similarly, `Vol. 1` and `No. 1` appear only because `acmsmall` provides fallback defaults when `\acmVolume` and `\acmNumber` are absent; those defaults (both "1") happen to be the fallback values, which is fortunate but fragile.

The ACM Reference Format block on page 1 reads:

> `In Proceedings of . ACM, New York, NY, USA, 70 pages.`

The "Proceedings of ." is produced by `\acmConference{}{}{}{}` at line 44 with all four arguments empty. For a journal submission this is wrong — CSUR papers do not appear in conference proceedings, and this line should be removed or replaced.

**SEVERITY: must** for both issues.

**Fix — exact lines to add/change:**

Remove line 44 entirely (or comment it out). CSUR is a journal; `\acmConference` is for conference papers and should not be set at all for a CSUR submission. Its presence forces the "In Proceedings of ." spurious text into the ACM Reference Format block.

```latex
% REMOVE or comment out line 44:
% \acmConference{}{}{}{}
```

Then add the three missing metadata commands directly after line 5 (`\acmYear{2026}`):

```latex
\acmVolume{1}
\acmNumber{1}
\acmArticle{1}
```

Place them at lines 6–8, pushing the existing comment on line 8 down. After this change the footer will read:

> `ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: June 2026.`

and the ACM Reference Format block will drop the "Proceedings of ." fragment. Note: for final camera-ready the ACM production team will supply the real volume/number/article values; these placeholders suppress the blank in the preprint.

---

### 4. TEXT-MODE COMPARISON OPERATORS IN MATH CONTEXT

**Issue.** Line 141 (Contribution 1 description) and line 1532 (Conclusion) both contain:

```
ATTENUATE $\varphi$<1 / PRESERVE $\varphi$$\approx$1 / AMPLIFY $\varphi$>1
```

Here `<` and `>` appear **outside** any math environment — they are bare text-mode characters sitting between closing `$` and the numeral `1`. In text mode `<` and `>` are not comparison operators; they render as the wrong glyphs in some fonts and are not semantically tagged as math. The pattern `$\varphi$<1` should be `$\varphi < 1$`.

**SEVERITY: must** — the glyphs render incorrectly in the Libertine text font and will fail ACM accessibility tagging.

**Fix — two occurrences:**

Line 141 (Contribution 1, inside the abstract-like text block):
```latex
% old:
(ATTENUATE $\varphi$<1 / PRESERVE $\varphi$$\approx$1 / AMPLIFY $\varphi$>1 / GENERATE $\varphi$ on zero input)
% new:
(ATTENUATE $\varphi < 1$ / PRESERVE $\varphi \approx 1$ / AMPLIFY $\varphi > 1$ / GENERATE $\varphi$ on zero input)
```

Line 1532 (Conclusion, same phrasing repeated):
```latex
% old:
D3 defines the conduction operators (ATTENUATE $\varphi$<1, PRESERVE $\varphi$$\approx$1, AMPLIFY $\varphi$>1, GENERATE $\varphi$ on zero input)
% new:
D3 defines the conduction operators (ATTENUATE $\varphi < 1$, PRESERVE $\varphi \approx 1$, AMPLIFY $\varphi > 1$, GENERATE $\varphi$ on zero input)
```

The same pattern also appears at line 504 (Glossary entry for "Conduction operator"):
```
$\phi < 1$ = ATTENUATE; $\phi \approx 1$ = PRESERVE; $\phi > 1$ = AMPLIFY
```
That occurrence (line 504) is **correctly written** — it already uses full math mode. No change needed there.

---

### 5. TABLE CELL CROSSING A COLUMN RULE

**Issue confirmed visually (page 42, Table 2).** The CEB row (line 1069, `wang2024ceb`) has the primary metric text:

```
Composite stereotype/toxicity/performance
```

in a `p{0.180\textwidth}` "Primary metric" column. The slashed compound "stereotype/toxicity/performance" is too wide for the column and visually bleeds into the adjacent "Agentic?" column's left rule. Visible at normal reading zoom in the rendered PDF (confirmed in `tbl05.png`).

**SEVERITY: must** — text crossing a column rule is a production-quality error.

**Fix.** Insert `\allowbreak` after each slash in that cell, line 1069:
```latex
% old:
CEB \cite{wang2024ceb} & QA/Gen & General (compositional) & Composite stereotype/toxicity/performance & No & Yes \\
% new:
CEB \cite{wang2024ceb} & QA/Gen & General (compositional) & Composite stereotype\allowbreak/\allowbreak toxicity\allowbreak/\allowbreak performance & No & Yes \\
```

The same pattern appears in "TrustGPT" row (line 1059): "Toxicity/bias/value" also overflows. Same fix:
```latex
Toxicity\allowbreak/\allowbreak bias\allowbreak/\allowbreak value
```

---

### 6. ADDITIONAL COSMETIC ISSUES

**6a. `\acmConference{}{}{}{}` generates "In Proceedings of . ACM …" in the ACM Reference Format block** (page 1, visible at full zoom). Already covered under item 3 above — remove this line.

**6b. `\setcopyright{none}` + `\acmDOI{}` + `\acmISBN{}` produce a blank copyright/license footer block on page 1.** Visible in `page01.png`: a faint horizontal rule appears below the affiliations with just a comma and "2026." The ACM production team will replace these; for internal preprint review this is expected and harmless. No fix required.

**6c. The section hierarchy uses `\subsection{}` for top-level sections** (lines 123, 219, etc.) — there is no `\section{}`. In `acmsmall` this means the top-level divisions are numbered "0.1", "0.2", etc. and the running header reads "Fairness and Equity in LLM-Based Agents: A Taxonomic Survey" throughout with no section title. This appears to be intentional (the author may have wanted the numbering starting from 0 for the BCF sections) but is non-standard. ACM production will reassign numbering. No urgent fix required for the preprint.

**SEVERITY: nice** — flag only if submitting to ACM ScholarOne, where the section-number format may trigger a style check.

**6d. Alt-text missing for figures.** The log warns "A possible image without description on input line 1448" (and a class-level warning for all figures lacking `\Description{…}`). Every `\begin{figure}` environment in the document should have a `\Description{…}` command immediately after `\caption{…}` for ADA / EAA accessibility compliance (which acmsmall actively warns about). This affects the PRISMA figure (line 384), the temporal distribution bar chart (line 446), the coverage heatmap, and the operator matrix. **SEVERITY: should** for a journal submission.

**6e. Infinite-glue shrinkage on pages 42, 49, 51** (noted under item 2). These "ignored errors" are suppressed by the engine but indicate that a longtable row in Table 4 is being split at a position with unbounded shrink glue. They produce visually tolerable output but are a latent risk for different paper sizes or column widths. Fix as described in item 2.

**6f. The `resizebox{\columnwidth}{!}` pattern used in Table 0** (line 179) applies the scaler to the box containing the tabular, but the `p{0.090\textwidth}` column widths inside the tabular are set in `\textwidth` units before scaling, so the explicit widths override the scaler for content overflow. The scaler only reduces the typeset box; it cannot force narrow paragraph columns to rewrap their content. This is why Table 0 still overflows despite being inside a `resizebox`. The fix in item 1 (Group A) addresses this structurally.

---

### SUMMARY PRIORITY TABLE

| # | SEVERITY | Location | Issue | Fix |
|---|---|---|---|---|
| 3 | must | Lines 4–44 (preamble) | "Article ." in footer; "Proceedings of ." in ACM ref | Remove `\acmConference{}{}{}{}`; add `\acmVolume{1}\acmNumber{1}\acmArticle{1}` after line 5 |
| 4 | must | Lines 141, 1532 | `$\varphi$<1` — comparison in text mode | Change to `$\varphi < 1$` (both occurrences) |
| 5 | must | Line 1069 (Table 2, CEB row) | Cell text bleeds across column rule | `\allowbreak` after each `/` in "stereotype/toxicity/performance" |
| E | must | Line 491 | "NeurIPS/ICML/ICLR" — 30 pt overfull | `\allowbreak` after slashes, or reword to comma list |
| A | should | Lines 177, 179–180 (Table 0) | ~15 overfull hbox, up to 31.7 pt | `\footnotesize` + `\resizebox{\textwidth}{!}` |
| B | should | Lines 338, 342, 347 (Table 2.1) | "Records"/"Dedup" header overflow | Widen columns 5–8 by 0.005\textwidth each |
| C | should | Line 355 (Table 2.1) | "Planning/decomposition" 15 pt overfull | `\allowbreak` after `/` |
| G | should | Lines 911, 1059, 1069 (Table 3) | Slashed compound cells overflow | `\allowbreak` after each `/` |
| J | should | Lines 1284–1285 | "Escalation/deferral" 7.77 pt overfull | `\allowbreak` after `/` |
| K | should | Lines 1483–1484 | "acting-agent" 4.88 pt overfull | `act\-ing-agent` |
| 2 | should | Pages 42, 49, 51 | Infinite glue shrinkage in Table 4 longtable | `\pagebreak[0]` before long rows |
| 6d | should | All figures | Missing `\Description{…}` alt-text | Add `\Description{…}` after each `\caption` |
| D | nice | Line 143 | "Trajectory-level" 1.62 pt overfull | `{\sloppy …\par}` around paragraph |
| F | nice | Lines 862–863 | "technical-evaluator-" 1.01 pt overfull | `\-` hyphen hint |
| H | nice | Lines 1042, 1047 | "Agentic?", "Code/Data" header cells | `\shortstack` or widen columns |
| I | nice | Lines 1174, 1179 | "Evidence Density" header overflow | `\shortstack` or widen column |
| L | nice | Lines 468–469 | pgfplots figure 9 pt overfull | `width=0.96\columnwidth` |
| 6c | nice | Line 123 ff | `\subsection` used as top-level (numbers "0.1") | Change to `\section` if standard numbering wanted |