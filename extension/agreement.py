"""Inter-coder agreement (coder A = Claude Sonnet, coder B = GPT-6.1) and disagreement lists.
Usage: python -I agreement.py  -> agreement.json, disagreements_*.jsonl"""
import json, pathlib, collections

HERE = pathlib.Path(__file__).resolve().parent


def load(name):
    p = HERE / name
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()] if p.exists() else []


def kappa(a, b):
    n = len(a)
    if n == 0:
        return None
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = collections.Counter(a), collections.Counter(b)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / n / n
    return None if pe == 1 else round((po - pe) / (1 - pe), 3), round(po, 3)


def compare(fileA, fileB, idf, fields, tag):
    A, B = load(fileA), load(fileB)
    if not A or not B:
        return None
    ka = {idf(r): r for r in A}
    kb = {idf(r): r for r in B}
    keys = [k for k in ka if k in kb]
    res = {"n_A": len(A), "n_B": len(B), "n_matched": len(keys), "fields": {}}
    dis = []
    for f, norm in fields:
        a = [norm(ka[k].get(f)) for k in keys]
        b = [norm(kb[k].get(f)) for k in keys]
        k, po = kappa(a, b)
        res["fields"][f] = {"kappa": k, "agreement": po, "n": len(keys),
                            "dist_A": collections.Counter(a).most_common(),
                            "dist_B": collections.Counter(b).most_common()}
    for k in keys:
        diffs = {f: [ka[k].get(f), kb[k].get(f)] for f, norm in fields if norm(ka[k].get(f)) != norm(kb[k].get(f))}
        if diffs:
            dis.append({"id": k, "diffs": diffs, "A": ka[k], "B": kb[k]})
    with open(HERE / f"disagreements_{tag}.jsonl", "w", encoding="utf-8") as fh:
        for d in dis:
            fh.write(json.dumps(d, ensure_ascii=False) + "\n")
    res["n_disagreeing_records"] = len(dis)
    return res


ident = lambda x: x
lst = lambda x: tuple(sorted(x or []))
incl = lambda v: "include" if v in ("INCLUDE_TOPICAL", "INCLUDE_PRIOR_ART") else ("borderline" if v == "BORDERLINE" else "exclude")
out = {
    "screen": compare("screen_A.jsonl", "screen_B.jsonl", lambda r: r["id"],
                      [("verdict", ident), ("primary_branch", ident), ("locus_tags", lst)], "screen"),
    "screen_binary": compare("screen_A.jsonl", "screen_B.jsonl", lambda r: r["id"],
                             [("verdict", incl)], "screen_binary"),
    "code_existing": compare("code_existing_A.jsonl", "code_existing_B.jsonl", lambda r: (r["key"], r["locus"]),
                             [("fairness_dimension", ident), ("operator", ident), ("evidence_type", ident),
                              ("demographic", ident)], "code_existing"),
    "code_new": compare("code_new_A.jsonl", "code_new_B.jsonl", lambda r: (r["key"], r["locus"]),
                        [("fairness_dimension", ident), ("operator", ident), ("evidence_type", ident),
                         ("demographic", ident)], "code_new"),
    "mitigation": compare("mitig_A.jsonl", "mitig_B.jsonl", lambda r: r["key"],
                          [("setting", ident), ("effect_direction", ident), ("utility_cost_reported", ident),
                           ("demographic", ident)], "mitigation"),
}
json.dump(out, open(HERE / "agreement.json", "w", encoding="utf-8"), indent=1, default=str)
for t, r in out.items():
    if r:
        print(t, "matched", r["n_matched"], "disagreeing", r["n_disagreeing_records"],
              {f: (v["kappa"], v["agreement"]) for f, v in r["fields"].items()})
