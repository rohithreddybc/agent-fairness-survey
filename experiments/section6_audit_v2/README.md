# Illustrative audit (v2) — replication package

Controlled resume-screening audit under a 2×2 race-by-gender counterfactual, as
reported in the supplement (S23, "An Illustrative Endpoint-Only Audit") of *Fairness and Equity in
LLM-Based Agents: A Taxonomic Survey*; the article points to it from §4.3. The folder name is historical.

Notes added 2026-11-09:

- `analyze.py` reports under the name `cfr` the share of profiles whose decision differs under at least one
  of the four names (a profile-level any-disagreement rate). The Counterfactual Flip Rate of the paper's
  Definition 4.1, averaged over the six pairs of name conditions, is 0.083 (C0), 0.097 (C2) and 0.056 (C3);
  the paper reports both.
- C2 and C3 are prompt-scaffold conditions. The harness asks for a JSON decision with a 200-token output
  budget and keeps only the parsed decision and score, so it does not record whether deliberation occurred.
- `run_audit.py` converts the decision field with `bool()` and does not validate the schema or the score
  range; a string such as "false" would be read as true. The committed decisions are already parsed, so this
  cannot be checked after the fact; a re-run should validate the output and keep the raw responses.
- `recompute_masd.py` describes an earlier version of `analyze.py`; the current `analyze.py` computes both the
  pairwise MASD reported in the paper and the per-profile score range.

## Pipeline

```
audit_spec.json   →  run_audit.py   →  audit_v2_raw.json  →  analyze.py  →  analysis_summary.json
(inputs/protocol)    (harness +         (144 raw            (CFR/MASD +     (per-config
                      name-swap)         decisions)          bootstrap CIs)   summary)
```

## Files

| File | Role |
|------|------|
| `audit_spec.json` | Inputs and protocol: the 12 synthetic profiles (6 strong, 6 borderline), the three configuration scaffolds (C0 single call, C2 reason-then-decide, C3 recruiter–reviewer deliberation), the four name conditions (WM/WF/BM/BF), the model id, temperature, and the decision prompt template. |
| `run_audit.py` | Generation harness. Applies the counterfactual name swap (resume byte-identical across the four conditions; only the name changes) and queries the model under test, producing `audit_v2_raw.json`. Requires `ANTHROPIC_API_KEY`. |
| `audit_v2_raw.json` | The 144 raw decisions (advance + 0–100 score per profile × config × condition). This is the exact run analyzed in the paper. |
| `analyze.py` | Computes per-configuration CFR, MASD, advance-rate disparity, and the 2×2 race/gender score effects with deterministic bootstrap 95% CIs (fixed seed). |
| `analysis_summary.json` | Machine-readable summary emitted by `analyze.py`. |

## Reproduce

```bash
# re-run the analysis on the committed decisions (no API key needed):
python analyze.py

# regenerate the raw decisions from scratch (queries the model; needs a key):
export ANTHROPIC_API_KEY=...
python run_audit.py
python analyze.py
```

Model: `claude-haiku-4-5`, temperature 0. The committed `audit_v2_raw.json` is the
canonical run; provider-side nondeterminism may produce small variation on re-runs.
