# Screening task

You are one of two independent coders screening candidate papers for a literature survey on
unfairness in LLM-based agents. The other coder receives these instructions word for word. Work
alone and do not try to guess what the other coder or the survey authors decided.

## Read first

Read `CODEBOOK.md` in full before coding. Part 0 (general rules) and Part A (screening) govern
this task. Where these instructions and the codebook seem to differ, the codebook wins.

## Input

A JSONL file, one paper per line. Each line has these fields:

- `id`: record identifier (copy it unchanged)
- `title`
- `abstract` (may be null or empty)
- `published`: date of first public version, `YYYY-MM-DD`, `YYYY-MM` or `YYYY`
- `venue` (optional)

Ignore any other field, including authors. Use only the title, abstract, date and venue. Do not
use what you may know about a paper from elsewhere, and do not look anything up.

## What to do for each line

Apply the procedure of CODEBOOK.md §A3: compute `post_cutoff` (cutoff 2026-06-10, §A6); check
criteria i, ii, iii, iv, v in order (§A1, §A4, §A5); give the verdict (§A2); for
`INCLUDE_TOPICAL` and `BORDERLINE`, assign primary branch, locus tags and secondary branches
(§A7).

## Output

Exactly one JSON object per input line, in the same order as the input, one object per line.
No other text: no header, no commentary, no Markdown, no code fences, no blank lines. Every key
below must be present, in this order, with exactly these spellings.

```
{"id": "<copied>",
 "verdict": "INCLUDE_TOPICAL" | "INCLUDE_PRIOR_ART" | "EXCLUDE" | "BORDERLINE",
 "verdict_evidence": "<quote>",
 "deciding_criterion": "i" | "ii" | "iii" | "iv" | "v" | "all_met",
 "deciding_criterion_evidence": "<quote>",
 "transfer_clause_used": true | false,
 "transfer_clause_evidence": "<quote>",
 "post_cutoff": true | false,
 "post_cutoff_evidence": "<the published value as given>",
 "primary_branch": "C1" | "C2" | "C3" | "C4" | "C5" | "T" | "evaluation" | "mitigation" | "high-stakes" | null,
 "primary_branch_evidence": "<quote>",
 "locus_tags": [zero or more of "C1","C2","C3","C4","C5","T"],
 "locus_tags_evidence": "<quote>",
 "secondary_branches": [zero or more of "evaluation","mitigation","high-stakes"],
 "secondary_branches_evidence": "<quote>"}
```

(Shown on several lines for readability. Write each object on a single line.)

Constraints:

1. `deciding_criterion` is `all_met` if and only if the verdict is `INCLUDE_TOPICAL` or
   `INCLUDE_PRIOR_ART`.
2. `primary_branch` is `null` and both lists are `[]` when the verdict is `EXCLUDE` or
   `INCLUDE_PRIOR_ART`.
3. If `primary_branch` is a locus, it appears in `locus_tags`. If `primary_branch` is
   `evaluation`, `mitigation` or `high-stakes`, `locus_tags` is `[]` (§A7, precedence 1).
4. `primary_branch` never appears in `secondary_branches`.
5. Each `_evidence` value is a verbatim quote of at most 25 words from the title or abstract,
   or `""` when the field holds its default value (`false`, `null`, `[]`), as in CODEBOOK.md
   §0.4. `post_cutoff_evidence` is always the `published` value.
6. Output must be valid JSON: double quotes, escape any double quote inside a quote as `\"`,
   `true`/`false`/`null` in lower case.
7. The number of output lines equals the number of input lines.

Example output line (invented paper):

{"id": "2601.00001", "verdict": "EXCLUDE", "verdict_evidence": "position bias of LLM judges", "deciding_criterion": "ii", "deciding_criterion_evidence": "LLM judges prefer the first-listed answer regardless of quality", "transfer_clause_used": false, "transfer_clause_evidence": "", "post_cutoff": false, "post_cutoff_evidence": "2026-01-03", "primary_branch": null, "primary_branch_evidence": "", "locus_tags": [], "locus_tags_evidence": "", "secondary_branches": [], "secondary_branches_evidence": ""}
