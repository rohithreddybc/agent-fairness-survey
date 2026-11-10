"""Regenerate the counts behind the coverage map (Fig. 8: locus x fairness dimension) and the
operator grid (Fig. 9: locus x conduction operator) from the released, dual-coded entries.

Inputs : code_existing_final.jsonl (59 original locus-tagged papers, 68 entries)
         code_new_final.jsonl, code_new2_final.jsonl (papers added by the 2026 extension)
Output : figure_counts.json and a printed summary. One entry = one (paper, locus) pair.

The figures count only entries with grid_eligible = true (CODEBOOK.md Part G (b), strict rule of
2026-11-10; one row per decision in strict_rule.jsonl). The unfiltered grids over all coded entries are
printed first and written under the "unfiltered_*" keys, for transparency.
"""
import json, pathlib, collections

HERE = pathlib.Path(__file__).resolve().parent
LOCI = ["C1", "C2", "C3", "C4", "C5", "T"]
DIMS = ["group", "individual", "counterfactual", "unspecified"]
OPS = ["ATTENUATE", "PRESERVE", "AMPLIFY", "GENERATE", "UNCHARACTERIZED"]


def load(name):
    p = HERE / name
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()] if p.exists() else []


def grid(entries, field, cols):
    g = {l: {c: 0 for c in cols} for l in LOCI}
    for e in entries:
        g[e["locus"]][e[field]] += 1
    return g


def show(title, g, cols):
    print(title)
    print("      " + " ".join(f"{c[:6]:>7}" for c in cols) + "    total")
    for l in LOCI:
        print(f"{l:5} " + " ".join(f"{g[l][c]:7d}" for c in cols) + f"  {sum(g[l].values()):7d}")
    print("total " + " ".join(f"{sum(g[l][c] for l in LOCI):7d}" for c in cols)
          + f"  {sum(sum(r.values()) for r in g.values()):7d}\n")


existing, new = load("code_existing_final.jsonl"), load("code_new_final.jsonl") + load("code_new2_final.jsonl")
out = {}
elig = lambda es: [e for e in es if e.get("grid_eligible") is True]
for name, ents in (("unfiltered_original_corpus", existing), ("unfiltered_extended_corpus", existing + new),
                   ("original_corpus", elig(existing)), ("extended_corpus", elig(existing + new))):
    papers = {e["key"] for e in ents}
    d, o = grid(ents, "fairness_dimension", DIMS), grid(ents, "operator", OPS)
    sec = collections.Counter(e["operator_secondary"] for e in ents if e.get("operator_secondary") not in (None, "", "NONE"))
    ev = collections.Counter(e["evidence_type"] for e in ents)
    demo = collections.Counter(e["demographic"] for e in ents)
    out[name] = {"papers": len(papers), "entries": len(ents), "dimension_grid": d, "operator_grid": o,
                 "operator_secondary": dict(sec), "evidence_type": dict(ev), "demographic": dict(demo)}
    print(f"== {name}: {len(papers)} papers, {len(ents)} entries; evidence {dict(ev)}; demographic {dict(demo)}")
    show("Fig. 8 locus x dimension", d, DIMS)
    show("Fig. 9 locus x operator", o, OPS)
json.dump(out, open(HERE / "figure_counts.json", "w", encoding="utf-8"), indent=1)
