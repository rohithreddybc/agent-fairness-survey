# Entry-coding task

You are one of two independent coders extracting codes from papers for a literature survey on
unfairness in LLM-based agents. The other coder receives these instructions word for word. Work
alone and do not try to guess what the other coder or the survey authors decided.

## Read first

Read `CODEBOOK.md` in full before coding. Part 0 (general rules), Part B (entry coding) and
Part D (defaults) govern this task. Where these instructions and the codebook seem to differ,
the codebook wins.

## Input

A JSONL file, one paper per line. Each line has these fields:

- `key`: paper identifier (copy it unchanged)
- `title`
- `year`, `venue`
- `abstract` (may be null)
- `author_summary`: a one-line summary of the paper (may be null)
- `author_locus_tags`: the paper's locus tags, a list drawn from `C1`..`C5`, `T`
- `primary_locus`: one of those tags, or null

The locus tags are **given**. Do not add, drop or change them, and do not judge whether they are
right. Ignore any other field. Use only the fields above, and do not use what you may know about
a paper from elsewhere or look anything up. The author summary may help you understand the
paper, but evidence quotes come from the title and abstract unless the abstract is null
(CODEBOOK.md §0.4).

## What to do for each line

For **each** tag in `author_locus_tags`, in the order given, produce one entry (CODEBOOK.md
§B1) and code: `fairness_dimension` and `fairness_basis` (§B2), `operator` and
`operator_secondary` (§B3), `evidence_type` (§B4), `demographic` (§B5).

## Output

One JSON object per **entry**, so a paper with three tags produces three lines. Keep the input
order of papers, and within a paper the order of its tags. No other text: no header, no
commentary, no Markdown, no code fences, no blank lines. Every key below must be present, in
this order, with exactly these spellings.

```
{"key": "<copied>",
 "locus": "C1" | "C2" | "C3" | "C4" | "C5" | "T",
 "is_primary_locus": true | false,
 "fairness_dimension": "group" | "individual" | "counterfactual" | "unspecified",
 "fairness_basis": "named" | "instantiated" | "none",
 "fairness_dimension_evidence": "<quote>",
 "operator": "ATTENUATE" | "PRESERVE" | "AMPLIFY" | "GENERATE" | "UNCHARACTERIZED",
 "operator_evidence": "<quote>",
 "operator_secondary": "ATTENUATE" | "PRESERVE" | "AMPLIFY" | "GENERATE" | null,
 "operator_secondary_evidence": "<quote>",
 "evidence_type": "direct_llm_agent" | "llm_non_agentic_transferred" | "non_llm_transferred",
 "evidence_type_evidence": "<quote>",
 "demographic": "yes" | "no",
 "demographic_evidence": "<quote>"}
```

(Shown on several lines for readability. Write each object on a single line.)

Constraints:

1. `is_primary_locus` is `true` only when `locus` equals `primary_locus`.
2. `fairness_basis` is `none` if and only if `fairness_dimension` is `unspecified`.
3. `operator_secondary` is `null` unless the abstract reports two distinct findings with
   different operators (§B3); it is never equal to `operator` and never `UNCHARACTERIZED`. If
   `operator` is `UNCHARACTERIZED`, `operator_secondary` is `null`.
4. Each `_evidence` value is a verbatim quote of at most 25 words from the title or abstract;
   `""` when the field holds its default (`unspecified`, `UNCHARACTERIZED`, `null`, `no` with
   no group named); prefixed `SUMMARY: ` and quoted from the author summary only when the
   abstract is null (§0.4). `evidence_type_evidence` is never empty.
5. Output must be valid JSON: double quotes, escape any double quote inside a quote as `\"`,
   `true`/`false`/`null` in lower case.
6. The number of output lines equals the total number of tags across all input lines.

Example output line (invented paper):

{"key": "doe2025example", "locus": "C2", "is_primary_locus": true, "fairness_dimension": "group", "fairness_basis": "instantiated", "fairness_dimension_evidence": "approval rates for Black and white applicants differ by 7 points", "operator": "GENERATE", "operator_evidence": "without retrieved case files the model shows no significant gap", "operator_secondary": null, "operator_secondary_evidence": "", "evidence_type": "direct_llm_agent", "evidence_type_evidence": "a retrieval-augmented loan-review agent", "demographic": "yes", "demographic_evidence": "Black and white applicants"}
