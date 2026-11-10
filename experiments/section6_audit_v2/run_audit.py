#!/usr/bin/env python3
"""
Section 6 audit harness (v2) -- generation + counterfactual name-swap.

Implements the protocol of the paper's Section 6: a resume-screening decision
task under a 2x2 race-by-gender counterfactual. For every (profile, config),
the resume is byte-identical across the four name conditions; only the candidate
name varies (the counterfactual swap). The model under test is queried once per
(profile, config, condition), yielding 12 x 3 x 4 = 144 decisions.

Inputs are read from audit_spec.json (the 12 synthetic profiles, the three
configuration scaffolds C0/C2/C3, the four name conditions WM/WF/BM/BF, the
model id, temperature, and the decision prompt template). The canonical run
analyzed in the paper is the committed audit_v2_raw.json; re-running this script
regenerates that file in the same schema. Scoring/statistics are computed
separately by analyze.py.

Usage:
    export ANTHROPIC_API_KEY=...        # required to call the model
    python run_audit.py                 # writes audit_v2_raw.json

Determinism: temperature is 0 (see audit_spec.json). Provider-side
nondeterminism may still produce small variation across runs; the committed
audit_v2_raw.json is the exact run reported in the paper.
"""
import json
import os
import re
from decimal import Decimal, InvalidOperation
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = json.loads((HERE / "audit_spec.json").read_text(encoding="utf-8"))


def build_prompt(profile, config, condition):
    """Apply the counterfactual name swap and render the decision prompt."""
    return SPEC["decision_prompt_template"].format(
        role=profile["role"],
        name=condition["name"],      # the only field that varies across conditions
        resume=profile["resume"],
        scaffold=config["scaffold"],
    )


def parse_score(value):
    """Accept only an integer, an integral float (85.0) or an integral numeric string ("85") in 0-100.
    Booleans (an int subclass in Python) and values with a fractional part are rejected as None;
    int() would silently truncate 85.7 to 85 and turn True into 1."""
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        n = value
    elif isinstance(value, float):
        if not value.is_integer():
            return None
        n = int(value)
    elif isinstance(value, str):
        try:
            d = Decimal(value.strip())
        except InvalidOperation:
            return None
        if not d.is_finite() or not 0 <= d <= 100 or d != d.to_integral_value():
            return None
        n = int(d)
    else:
        return None
    return n if 0 <= n <= 100 else None


def call_model(prompt):
    """Query the model under test once. Returns (advance: bool|None, score: int|None)."""
    from anthropic import Anthropic  # imported lazily so the file parses without the SDK
    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    msg = client.messages.create(
        model=SPEC["model"],
        max_tokens=200,
        temperature=SPEC["temperature"],
        messages=[{"role": "user", "content": prompt}],
    )
    text = "".join(block.text for block in msg.content if getattr(block, "type", "") == "text")
    m = re.search(r"\{.*\}", text, re.DOTALL)
    if not m:
        return None, None
    obj = json.loads(m.group(0))
    adv = obj.get("advance")
    score = obj.get("score")
    # Accept only a JSON boolean (or the strings "true"/"false"); anything else is unparseable.
    # bool("false") would be True, so strings are mapped explicitly.
    if isinstance(adv, str):
        adv = {"true": True, "false": False}.get(adv.strip().lower())
    elif not isinstance(adv, bool):
        adv = None
    score = parse_score(score)
    return adv, score


def main():
    raw = []
    for profile in SPEC["profiles"]:
        for config in SPEC["configs"]:
            for condition in SPEC["conditions"]:
                advance, score = call_model(build_prompt(profile, config, condition))
                raw.append({
                    "cfg": config["cfg"], "scaffold": config["scaffold"],
                    "pid": profile["pid"], "tier": profile["tier"], "role": profile["role"],
                    "resume": profile["resume"], "cond": condition["cond"],
                    "name": condition["name"], "race": condition["race"],
                    "gender": condition["gender"], "advance": advance, "score": score,
                })
    out = {"summary": {"model": SPEC["model"], "temperature": SPEC["temperature"],
                       "n_decisions": len(raw)},
           "result": {"raw": raw}}
    (HERE / "audit_v2_raw.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"wrote audit_v2_raw.json with {len(raw)} decisions")


if __name__ == "__main__":
    main()
