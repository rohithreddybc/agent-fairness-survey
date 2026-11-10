# Mitigation-extraction task

You are one of two independent coders extracting what published bias-mitigation papers report,
for a literature survey on unfairness in LLM-based agents. The other coder receives these
instructions word for word. Work alone and do not try to guess what the other coder or the
survey authors decided.

## Read first

Read `CODEBOOK.md` in full before coding. Part 0 (general rules), Part C (mitigation
extraction), §B5 (demographic) and Part D (defaults) govern this task. Where these instructions
and the codebook seem to differ, the codebook wins.

## Input

A JSONL file, one paper per line. Each line has these fields:

- `key`: paper identifier (copy it unchanged)
- `title`
- `year`, `venue`
- `abstract` (may be null)

Ignore any other field. Use only the fields above, and do not use what you may know about a
paper from elsewhere or look anything up. If a paper proposes or evaluates several
interventions, code the main one: the intervention named in the title, or else the first one
the abstract describes.

## Output

Exactly one JSON object per input line, in the same order as the input, one object per line.
No other text: no header, no commentary, no Markdown, no code fences, no blank lines. Every key
below must be present, in this order, with exactly these spellings.

```
{"key": "<copied>",
 "setting": "agentic_multistep" | "single_decision" | "qa_generation" | "other",
 "setting_evidence": "<quote>",
 "metric_named": "<verbatim metric name(s), '; '-separated>" | "not_named",
 "metric_named_evidence": "<quote>",
 "effect_direction": "reduces" | "mixed" | "none" | "increases" | "not_reported",
 "effect_direction_evidence": "<quote>",
 "utility_cost_reported": "yes" | "no",
 "utility_cost_reported_evidence": "<quote>",
 "demographic": "yes" | "no",
 "demographic_evidence": "<quote>"}
```

(Shown on several lines for readability. Write each object on a single line.)

Constraints:

1. `setting` follows the precedence of CODEBOOK.md Part C when several settings are evaluated.
2. `metric_named` copies the metric's name as the abstract writes it; a benchmark named in place
   of a metric carries the suffix ` (benchmark)`.
3. Each `_evidence` value is a verbatim quote of at most 25 words from the title or abstract,
   or `""` when the field holds its default (`not_named`, `not_reported`, `no`), as in
   CODEBOOK.md §0.4. `setting_evidence` is never empty.
4. Output must be valid JSON: double quotes, escape any double quote inside a quote as `\"`.
5. The number of output lines equals the number of input lines.

Example output line (invented paper):

{"key": "roe2025example", "setting": "agentic_multistep", "setting_evidence": "three LLM agents critique and revise each other's answers", "metric_named": "BBQ (benchmark)", "metric_named_evidence": "bias on BBQ falls by 40%", "effect_direction": "reduces", "effect_direction_evidence": "bias on BBQ falls by 40%", "utility_cost_reported": "yes", "utility_cost_reported_evidence": "with accuracy unchanged", "demographic": "yes", "demographic_evidence": "gender and race bias"}
