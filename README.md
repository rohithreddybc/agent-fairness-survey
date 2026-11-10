# Data and code for "Fairness and Equity in LLM-Based Agents: A Taxonomic Survey"

This repository holds the corpus, search records, reliability checks and audit materials behind the
survey by Rohith Reddy Bellibatlu, Manpreet Singh and Wenbin Zhang (submitted to ACM Computing
Surveys). It holds data and code only; the manuscript is not included.

## Contents

### `corpus/`: the corpus and how it was assembled

The original assembly holds 202 papers; the November 2026 extension (`extension/`, below) adds 33, for 235.

| File | What it is |
|---|---|
| `corpus_master.json`, `corpus_master.md` | The 202 papers with bibliographic metadata, branch tags and the per-paper locus assignment. A paper's primary branch is the first entry of its `branches` list. The paper's "foundations" branch (62 papers) is the union of the labels `foundational-must-cite` (46) and `foundations` (16), and its prior-art branch is the label `prior-art-additions` (29), which is why the file has thirteen labels against the paper's twelve branches. The prior-art branch holds mostly neighbor surveys but also some empirical and framework papers. The `verified` field records how each record was checked (`agent-verified` marks an assisted web lookup). |
| `corpus_master_extended.json` | The 235-paper corpus: the 202 records of `corpus_master.json`, unchanged except for an added `"extension": false`, followed by the 33 papers admitted by the extension, flagged `"extension": true`, with bib key, title, authors, year, venue, arXiv id or DOI, branch labels in the same vocabulary (primary first), the screening verdict, primary branch, locus tags, secondary branches and the pool source. Built by `extension/build_corpus_extended.py`; year and venue come from the survey's bibliography. Composition: 130 topical studies, 31 prior-art works, 74 contextual works; 90 locus-tagged papers (88 by primary branch, 2 by a secondary tag only). |
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

Coder A (Claude Sonnet) and coder B (GPT-6.1, OpenAI) worked independently from title and abstract
only, under one codebook derived from the survey's own definitions. A third pass (Claude Opus)
adjudicated every field on which they differed, with a written rationale and a deciding quote per
field. The 59 original locus-tagged papers keep the authors' human-coded locus tags; only their
fairness dimension, operator, evidence type and demographic fields were dual-coded. The new papers take
their locus tags from the screening. The per-paper fairness-dimension and operator labels behind the
coverage map (Figure 8) and the operator grid (Figure 9) are now released here.

| File | What it is |
|---|---|
| `CODEBOOK.md` | The codebook for screening (Part A), entry coding (Part B) and mitigation extraction (Part C). Rules the survey does not state are marked as the protocol's own. |
| `PROMPT_SCREEN.md`, `PROMPT_CODE.md`, `PROMPT_MITIGATION.md` | The task prompts given to both coders. |
| `build_pool.py`, `pool.jsonl`, `search_log.json` | The candidate pool: 106 distinct records from the 28 papers behind the 32 adjudicated screener admissions (`../corpus/_adjudicate_input.tsv`), 24 reviewer-identified works, and the top 60 by relevance of 183 hits for one targeted arXiv query (verbatim in `search_log.json`), bounded to submissions on or before 10 June 2026. Six records come from two sources; three query hits were already in the corpus, leaving 103 to screen. |
| `screen_input.jsonl`, `screen_A.jsonl`, `screen_B.jsonl`, `screen_final.jsonl` | Screening of the 103 records by each coder and after adjudication: 31 `INCLUDE_TOPICAL`, 2 `INCLUDE_PRIOR_ART`, 70 `EXCLUDE`. |
| `build_code_input.py`, `code_input_existing.jsonl`, `code_existing_A.jsonl`, `code_existing_B.jsonl`, `code_existing_final.jsonl` | Entry coding of the 68 locus entries of the 59 original locus-tagged papers. |
| `code_new_input.jsonl`, `code_new_A.jsonl`, `code_new_B.jsonl`, `code_new_final.jsonl` | Entry coding of the 34 locus entries of the 31 new locus-tagged papers. |
| `build_table6.py`, `table6_papers.json`, `mitig_input.jsonl`, `mitig_A.jsonl`, `mitig_B.jsonl`, `mitig_final.jsonl` | Mitigation extraction for the 24 papers cited in the mitigation map (Table 6); its evidence-density column applies the rule stated in that table's caption to `mitig_final.jsonl`. |
| `agreement.py`, `agreement.json`, `disagreements_*.jsonl` | Cohen's kappa and raw agreement per field before adjudication, and every disagreeing record. Run `python -I agreement.py`. |
| `ADJUDICATION_LOG.md` | One row per adjudicated field with the rationale and deciding quote, the totals, and the eight cases marked `CODEBOOK GAP`. |
| `figure_counts.py`, `figure_counts.json` | Regenerates the cell counts of Figures 8 and 9 for the original 68 entries and for all 102 (the `extended_corpus` grids are the published figures). Run `python -I figure_counts.py`. |
| `bibkeys.json` | arXiv id (or DOI) to bibliography key for the 33 admitted papers, with the source of the venue metadata. |
| `build_corpus_extended.py` | Writes `../corpus/corpus_master_extended.json`. |

## What is not released

The original single-rater, per-paper fairness-dimension and operator labels that the figures carried
before the extension are not released; their column totals are given in the supplement, beside the
dual-coded totals, for comparison.

## License and citation

Code is released under the MIT License. Data files are released under CC BY 4.0. If you use them,
please cite the survey.
