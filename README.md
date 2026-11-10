# Data and code for "Fairness and Equity in LLM-Based Agents: A Taxonomic Survey"

This repository holds the corpus, search records, reliability checks and audit materials behind the
survey by Rohith Reddy Bellibatlu, Manpreet Singh and Wenbin Zhang (submitted to ACM Computing
Surveys). It holds data and code only; the manuscript is not included.

## Contents

### `corpus/`: the corpus and how it was assembled

The original assembly holds 202 papers; the November 2026 extension (`extension/`, below) adds 39, for 241.

| File | What it is |
|---|---|
| `corpus_master.json`, `corpus_master.md` | The 202 papers with bibliographic metadata, branch tags and the per-paper locus assignment. A paper's primary branch is the first entry of its `branches` list. The paper's "foundations" branch (62 papers) is the union of the labels `foundational-must-cite` (46) and `foundations` (16), and its prior-art branch is the label `prior-art-additions` (29), which is why the file has thirteen labels against the paper's twelve branches. The prior-art branch holds mostly neighbor surveys but also some empirical and framework papers. The `verified` field records how each record was checked (`agent-verified` marks an assisted web lookup). |
| `corpus_master_extended.json` | The 241-paper corpus: the 202 records of `corpus_master.json`, unchanged except for an added `"extension": false` and one metadata correction (the Condon and Jilani record, previously `proceedings2026framework` with unknown authors, now carries its authors and the cited key `condon2026towards`; `previous_bibkey` keeps the old key), followed by the 39 papers admitted by the extension (33 in screening round 1, 2 in round 3, 4 on the round-5 eligibility re-screen, which carry no locus tag), flagged `"extension": true`, with bib key, title, authors, year, venue, arXiv id or DOI, branch labels in the same vocabulary (primary first), the screening verdict, primary branch, locus tags, secondary branches and the pool source. Built by `extension/build_corpus_extended.py`; year and venue come from the survey's bibliography. Every record carries a `category` under the strict rule applied to both cohorts on 10 November 2026 (`extension/CODEBOOK.md` Part G): 110 `topical`, 11 `prior-art`, 93 `contextual` and 27 `contextual-mechanism-precursor` (studies whose bias finding has no demographic, protected or social group as its object; kept and citable as mechanism precursors, not counted as topical). Records whose category changed carry `pre_strict_category`; before the rule the split was 136 topical, 31 prior-art and 74 contextual. 92 papers carry locus tags (104 locus entries); 57 of them, with 64 entries, meet the locus-grid rule and are counted in Figures 8 and 9. |
| `SEARCH_LOG_2026-08-17.md`, `_branch_queries.json` | Every branch query in arXiv API and Scopus syntax, with its yield and execution date. |
| `_arxiv_dedupe.json`, `_dedupe_arxiv.py` | Deduplication of the arXiv side of the search. |
| `_screen_pool.tsv`, `_pool_grp*.tsv`, `_screen_*_results.tsv`, `_screen_full_pool.tsv`, `_screen_pool_b3b5.tsv`, `_fetch_screen_pools.py` | The retrospective second screens, a completeness and eligibility check against corpus membership rather than a conventional inter-rater reliability. Each pool pairs the title and abstract shown to the second screener (an LLM, Claude Sonnet, with no access to the corpus or manuscript) with its decision and a corpus-membership label. **Correction (2026-11-09):** the membership column (column 4) of `_screen_b3b5_results.tsv` is wrong for 12 of its 70 rows (10 corpus papers marked `no`, 2 non-corpus records marked `yes`). The original file is kept unchanged; `_screen_b3b5_results_corrected.tsv` re-derives the column by joining the arXiv identifier against `corpus_master.json`. The paper's statistics were computed with membership from that join (pooled over 99 in-scope records: 66 agreements, Cohen's kappa = 0.281, 30 admissions absent from the corpus against 3 corpus papers rejected) and do not change; the uncorrected column would give 62 agreements and kappa = 0.18. Records the screener marked `POST_CUTOFF` are excluded from these counts. |
| `_adjudicate_input.tsv`, `_ADJUDICATION_2026-08-24.md` | The 32 screener admissions absent from the corpus and the memo reporting their adjudication (20 genuine misses, 7 false positives, 5 borderline). The 32 rows are branch entries for 28 distinct arXiv identifiers (2506.04419, 2512.16532, 2603.18729 and 2605.00382 each appear twice), and the 20/7/5 split counts entries. Read the dated correction at the top of the memo's caveat section. Per-record verdicts were not retained in publishable form. The memo's section numbers predate the final manuscript: its §2.5 is the article's §2.4 and its §2.4 inclusion criteria are the article's §2.3. |
| `_locus_blind.tsv`, `_locus_coder2.tsv` | The locus re-coding: the 57-row sheet given to the second coder, an independent human rater (titles and the authors' one-line contribution summaries from `corpus_master.json`, without the authors' locus labels), and that coder's per-row primary-locus assignment, confidence and reason (44 of 57 agree, Cohen's kappa = 0.73 against the original primary locus). Secondary tags were not re-coded by the human rater. The fairness dimensions and operators of all locus entries were later dual-coded in `extension/`. |
| `_SCREEN_RERUN_NOTE.md` | Working notes on a 580-record re-screen of the branch pools (`_pool_grp*.tsv`). It was not completed under one protocol, and its interim totals are not reported. Its overall totals are not used. Groups B4-B6 and B10-B11 of this re-screen (300 records, `_screen_grpB4_results.tsv` and `_screen_grpB10_results.tsv`) are the source of the 32 adjudicated candidates: their 36 admissions, 32 of them absent from the corpus, are the rows of `_adjudicate_input.tsv`. These groups were screened under two closely related strict prompts, not one: B10-B11 added branch-specific notes to the B4-B6 instruction (see the table in the note). The note's header predates that use. |
| `verify_citations.py`, `VERIFY_RESULTS.md`, `fix_bib_*.py`, `trim_bib_urls.py` | Metadata verification of the corpus records. The script marks an arXiv record `OK` when the normalized title similarity is at least 0.75, so `OK` does not mean an exact title match. `VERIFY_RESULTS.md` is a snapshot from an earlier bibliography and lists a few keys no longer in use; some venue fields in the corpus files predate later publication (for example, two records listed as preprints appeared at Findings of EMNLP 2024 and NeurIPS 2025). `SEARCH_LOG_2026-08-17.md` says the arXiv queries are unbounded in date because the API has no clean date bound; that is inaccurate, since the arXiv API supports `submittedDate` range queries. The queries were run without one, and the cutoff was applied at screening. |

### `experiments/section6_audit_v2/`: the illustrative counterfactual audit

It contains the audit specification (`audit_spec.json`), the generation harness (`run_audit.py`, which
needs your own `ANTHROPIC_API_KEY`), the 144 raw decisions (`audit_v2_raw.json`), and the analysis
(`analyze.py`, `recompute_masd.py`, `analysis_summary.json`). See that folder's README for how to
rerun it. The folder name is historical; the audit is reported in the supplement (S23), and the article
points to it from §4.3.

### `extension/`: corpus extension and dual-coded extraction (9-10 November 2026)

The extension ran in three rounds, numbered as in `ADJUDICATION_LOG.md`: round 1 screened a 106-record
candidate pool and coded the existing entries; round 2 coded the entries of the papers admitted in round 1;
round 3 fetched all 183 hits of the targeted query and screened the 123 not screened in round 1, so every
hit has been screened (229 distinct candidates in all), and coded the 2 papers it admitted.

Coder A (Claude Sonnet) and coder B (GPT-6.1, OpenAI) worked independently from title and abstract
only, under one codebook derived from the survey's own definitions. A third pass (Claude Opus)
adjudicated every field on which they differed, with a written rationale and a deciding quote per
field. The 59 original locus-tagged papers keep the authors' human-coded locus tags; only their
fairness dimension, operator, evidence type and demographic fields were dual-coded. The new papers take
their locus tags from the screening. The per-paper fairness-dimension and operator labels behind the
coverage map (Figure 8) and the operator grid (Figure 9) are now released here.

| File | What it is |
|---|---|
| `CODEBOOK.md` | The codebook for screening (Part A), entry coding (Part B) and mitigation extraction (Part C), with the eligibility amendment (Part F), the operator evidence requirement and the strict rule applied to both cohorts (Part G). Rules the survey does not state are marked as the protocol's own. |
| `PROMPT_SCREEN.md`, `PROMPT_CODE.md`, `PROMPT_MITIGATION.md` | The task prompts given to both coders. |
| `build_pool.py`, `pool.jsonl`, `search_log.json` | The round-1 candidate pool: 106 distinct records from the 28 papers behind the 32 adjudicated screener admissions (`../corpus/_adjudicate_input.tsv`), 24 reviewer-identified works, and the top 60 by relevance of 183 hits for one targeted arXiv query (verbatim in `search_log.json`), bounded to submissions on or before 10 June 2026. Six records come from two sources; three query hits were already in the corpus, leaving 103 to screen. `search_log.json` also records the round-3 fetch under its `round2` key (183 results, 123 new). |
| `build_pool_round2.py`, `pool2.jsonl`, `screen_input2.jsonl` | Round 3: fetches all 183 hits of the targeted query and writes the 123 not in `pool.jsonl` and not in the corpus (`pool2.jsonl`, with metadata; `screen_input2.jsonl`, the blind screening input). |
| `screen_input.jsonl`, `screen_A.jsonl`, `screen_B.jsonl`, `screen_final.jsonl` | Round-1 screening of the 103 records by each coder and after adjudication. `screen_final.jsonl` holds the amended verdicts: 35 `INCLUDE_TOPICAL`, 2 `INCLUDE_PRIOR_ART`, 66 `EXCLUDE`. The initial verdicts (31 / 2 / 70) are in `screen_final.preelig.jsonl`; the difference is the 4 records the round-5 eligibility amendment admitted. |
| `screen2_A.jsonl`, `screen2_B.jsonl`, `screen2_final.jsonl` | Round-3 screening of the 123 records: 2 `INCLUDE_TOPICAL` (2509.04794, 2604.18038), 121 `EXCLUDE`. The coders agreed on 122 of 123 verdicts (Cohen's kappa = 0.663; includes are rare); the one disagreement was adjudicated. Pooled over both rounds (226 records), the four-way verdict kappa is 0.863. |
| `build_code_input.py`, `code_input_existing.jsonl`, `code_existing_A.jsonl`, `code_existing_B.jsonl`, `code_existing_final.jsonl` | Entry coding of the 68 locus entries of the 59 original locus-tagged papers. |
| `code_new_input.jsonl`, `code_new_A.jsonl`, `code_new_B.jsonl`, `code_new_final.jsonl` | Round 2: entry coding of the 34 locus entries of the 31 locus-tagged papers admitted in round 1. |
| `code_new2_input.jsonl`, `code_new2_A.jsonl`, `code_new2_B.jsonl`, `code_new2_final.jsonl` | Round 3: entry coding of the 2 locus entries of the 2 papers admitted in round 3. |
| `build_table6.py`, `table6_papers.json`, `mitig_input.jsonl`, `mitig_A.jsonl`, `mitig_B.jsonl`, `mitig_final.jsonl` | Mitigation extraction for the 24 papers cited in the mitigation map (Table 6) before the extension studies were added; its evidence-density column applies the rule stated in that table's notes to `mitig_final.jsonl`. `build_table6.py` takes the manuscript source and bibliography as explicit arguments (`--tex`, `--bib`), since neither is in this package; rows marked as extension studies are skipped. The extension studies added to Tables 5 and 6 are assessed, one model pass from abstracts, in the supplement's table of extension papers against the inventory rules. |
| `agreement.py`, `agreement.json`, `disagreements_*.jsonl` | Cohen's kappa and raw agreement per field before adjudication, and every disagreeing record, for rounds 1 and 2. Run `python -I agreement.py`. Round-3 agreement is reported in the `screen2_*` row above and in the supplement. |
| `ADJUDICATION_LOG.md` | One row per adjudicated field with the rationale and deciding quote, the totals, and the eight cases marked `CODEBOOK GAP`; its Round 3 section covers the round-3 screening and coding. |
| `figure_counts.py`, `figure_counts.json` | Regenerates the cell counts of Figures 8 and 9 from the entries with `grid_eligible` = true: 34 original entries (29 papers) and 64 in all (57 papers); the `extended_corpus` grids are the published figures. Fig. 8 totals group / individual / counterfactual / unspecified = 25 / 0 / 3 / 36; Fig. 9 totals ATTENUATE / PRESERVE / AMPLIFY / GENERATE / uncharacterized = 11 / 0 / 9 / 2 / 42. The grids over all 68 and 104 coded entries are printed too and kept under the `unfiltered_*` keys. Run `python -I figure_counts.py`. |
| `bibkeys.json` | arXiv id (or DOI) to bibliography key for the 39 admitted papers, with the source of the venue metadata. |
| `build_corpus_extended.py` | Writes `../corpus/corpus_master_extended.json` from the includes of `screen_final.jsonl` and `screen2_final.jsonl`, with each record's `category` from `strict_rule.jsonl`. Run `python -I build_corpus_extended.py [--bib REFERENCES.bib]`; without a bibliography, year and venue fall back to the pool's date and "arXiv preprint". |
| `operator_validation.jsonl`, `*_final.prevalidation.jsonl` | Round 4 (10 November 2026): one further adjudication pass (Claude Opus) re-checked the 56 entries with a substantive operator against the stricter evidence rule in `CODEBOOK.md` ("Operator evidence requirement"); 10 changed, 46 confirmed. One row per validated entry; the `*_final.jsonl` coding files carry the result and the new fields `operator_validated` and `perturbation_sensitivity`, and the `prevalidation` files keep the earlier coding. Figure 9 totals moved from 17/2/22/15/48 to 18/0/18/12/56 (before the round-6 rule below). |
| `eligibility_recheck.jsonl`, `screen_final.preelig.jsonl` | Round 5 (10 November 2026): the eligibility amendment of `CODEBOOK.md` Part F, which separates corpus eligibility from locus-grid eligibility, applied by one adjudication pass (Claude Opus) to the 7 extension records excluded on criterion iii or on the transfer test; 4 were admitted without a locus tag. `ADJUDICATION_LOG.md`, round 5, also records the check of the original cohort against the amended rule (no record removed). |
| `strict_rule.jsonl`, `*_final.prestrict.jsonl` | Round 6 (10 November 2026): one strict rule for both cohorts (`CODEBOOK.md` Part G), applied by one adjudication pass (Claude Opus). (a) A topical paper must report a fairness finding about a demographic, protected or social group on LLM decisions or behavior bearing on agents, directly or through the transfer clause; 27 topical papers that fail (24 original, 3 extension) become `contextual-mechanism-precursor`, 19 original prior-art surveys with no agent scope become `contextual`, and one prior-art record that reports its own measurements becomes topical. (b) A locus entry is counted in Figures 8 and 9 only if its paper is topical, its finding is measured at that locus, and it is coded `demographic` = yes; 40 of 104 entries leave the figures. (c) GENERATE needs comparable upstream evidence at the entry's locus (a cue-free condition does not count), and no operator is copied across a paper's loci; 10 operators were recoded. One line per paper and per entry with reason and quote; the coding files gain `grid_eligible` (and `operator_prestrict`, `strict_rule_note` on recoded entries), and the `prestrict` files keep the earlier coding. Lists are in `ADJUDICATION_LOG.md`, round 6. |

## Screening totals, initial and amended

Rounds 1 and 3 screened 226 records (103 + 123). Initial verdicts: 33 admitted (31 topical, 2 prior-art) in
round 1 and 2 topical in round 3, 35 in all; 191 excluded. The round-5 eligibility amendment
(`eligibility_recheck.jsonl`, `CODEBOOK.md` Part F) re-checked the 7 round-1 records excluded on criterion iii or
on the transfer test: 4 were admitted (topical, no locus tag), 3 stay excluded. Amended totals: 39 admitted
(37 topical, 2 prior-art), 187 excluded. These 39 are the extension cohort. The strict rule of Part G
(`strict_rule.jsonl`) then assigns every record of both cohorts a final category. Final categories of the 241 records in
`../corpus/corpus_master_extended.json`: 110 topical, 11 prior-art, 93 contextual, 27 contextual-mechanism-precursor;
the original 202 split 76 / 9 / 93 / 24 and the 39 extension records 34 / 2 / 0 / 3. The locus grids of
Figures 8 and 9 (`extension/figure_counts.json`, `extended_corpus` key) count only entries of topical
papers that are measured at their own locus and coded `demographic` = yes: 64 entries from 57 papers
(34 entries from 29 original papers, 30 from 28 added papers), against 104 coded entries before the strict rule.

## What is not released

The original single-rater, per-paper fairness-dimension and operator labels that the figures carried
before the extension are not released; their column totals are given in the supplement, beside the
dual-coded totals, for comparison.

## License and citation

Code is released under the MIT License. Data files are released under CC BY 4.0. If you use them,
please cite the survey.
