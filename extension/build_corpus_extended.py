"""Write ../corpus/corpus_master_extended.json: the 202 original corpus records (unchanged apart from
an added "extension": false and the metadata corrections in METADATA_FIXES) followed by the 41 papers
admitted by the 2026-11 extension: 33 from screening round 1, 2 from round 3 and 2 from round 8
(screen_final.jsonl, screen2_final.jsonl, screen4_final.jsonl), plus 4 admitted on re-screening under the
eligibility amendment of 2026-11-10 (CODEBOOK.md Part F; eligibility_amended = true in screen_final.jsonl).
The 4 carry no locus tag and enter neither coverage figure.

Every record carries a `category` (CODEBOOK.md Part G, strict rule of 2026-11-10): topical, prior-art,
contextual or contextual-mechanism-precursor. It is taken from the paper lines of strict_rule.jsonl
(`category_after`); an original record with no paper line is a contextual work (first branch neither
prior-art nor a topical branch). A record whose category changed under Part G also carries
`pre_strict_category`.

Inputs : ../corpus/corpus_master.json, screen_final.jsonl, screen2_final.jsonl and screen4_final.jsonl
         (verdicts, branches, locus tags), pool.jsonl, pool2.jsonl and pool4.jsonl (title, authors, date, source),
         bibkeys.json (arXiv id or DOI -> bib key),
         a references.bib for year and venue, if one is found (--bib PATH, else ../../review/references.bib;
         otherwise date and "arXiv preprint" are used).
Usage  : python -I build_corpus_extended.py [--bib PATH]
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
CORPUS = HERE.parent / "corpus"
BIB = (pathlib.Path(sys.argv[sys.argv.index("--bib") + 1]) if "--bib" in sys.argv
       else HERE.parent.parent / "review" / "references.bib")
# Corrections to original records whose stored metadata is known to be stale (round-5 review, 3A).
# Only descriptive metadata changes; branches, taxonomy cells and the primary branch are untouched.
METADATA_FIXES = {
    "proceedings2026framework": {
        "authors": "Gary Condon, Musfira Jilani",
        "venue": "Proceedings of the 2026 Conference on Human Centred Artificial Intelligence -- Education and Practice (ACM), pp. 46-52",
        "url": "https://doi.org/10.1145/3777490.3777504",
        "bibkey": "condon2026towards",
        "previous_bibkey": "proceedings2026framework",
        "metadata_corrected": "2026-11-10: authors, venue and bib key synchronized with the cited bibliography entry",
    },
}
BRANCH = {"C1": "tool-api-selection-bias", "C2": "memory-retrieval-bias", "C3": "multiagent-delegation-bias",
          "C4": "planning-decomposition-bias", "C5": "user-modeling-personalization-harms",
          "T": "longhorizon-fairness-drift", "evaluation": "evaluation-metrics-benchmarks",
          "mitigation": "mitigation", "high-stakes": "high-stakes-domains"}


def jl(name):
    return [json.loads(l) for l in open(HERE / name, encoding="utf-8") if l.strip()]


bib = BIB.read_text(encoding="utf-8") if BIB.exists() else ""


def bibfield(key, field):
    m = re.search(r"@\w+\{" + re.escape(key) + r",(.*?)\n\}", bib, re.S)
    if not m:
        return None
    f = re.search(field + r"\s*=\s*[{\"](.*?)[}\"],?\s*\n", m.group(1), re.S)
    return " ".join(f.group(1).replace("{", "").replace("}", "").split()) if f else None


original = json.load(open(CORPUS / "corpus_master.json", encoding="utf-8"))
screen = {r["id"]: r for r in jl("screen_final.jsonl") + jl("screen2_final.jsonl") + jl("screen4_final.jsonl")}
pool = {r["id"]: r for r in jl("pool.jsonl") + jl("pool2.jsonl") + jl("pool4.jsonl")}
keys = json.load(open(HERE / "bibkeys.json", encoding="utf-8"))
strict = {r["key"]: r for r in jl("strict_rule.jsonl") if r["record"] == "paper"}


def category(key):
    r = strict.get(key)
    if r is None:
        return {"category": "contextual"}
    c = {"category": r["category_after"]}
    if r["category_after"] != r["category_before"]:
        c["pre_strict_category"] = r["category_before"]
    return c


out = [{**r, **METADATA_FIXES.get(r.get("bibkey"), {}), "extension": False, **category(r["bibkey"])} for r in original]
for pid, s in screen.items():
    if not s["verdict"].startswith("INCLUDE"):
        continue
    p, k = pool[pid], keys[pid]
    key = k["key"]
    arxiv = None if pid.startswith("doi:") else pid
    doi = pid[4:] if pid.startswith("doi:") else (k["source"].split("doi.org/", 1)[1] if "doi.org/" in k["source"] else "")
    if s["verdict"] == "INCLUDE_PRIOR_ART":
        branches = ["prior-art-additions"]
    else:
        tags = [s["primary_branch"]] + [t for t in s["locus_tags"] if t != s["primary_branch"]]
        branches = [BRANCH[t] for t in tags] + [BRANCH[t] for t in s["secondary_branches"] if t in BRANCH]
    year = bibfield(key, "year") or (p.get("published") or "")[:4]
    venue = bibfield(key, "booktitle") or bibfield(key, "journal") or "arXiv preprint"
    out.append({
        "title": p["title"], "authors": p.get("authors"), "year": int(year) if year.isdigit() else year,
        "venue": venue, "arxiv_id": arxiv or "", "doi": doi,
        "url": f"https://arxiv.org/abs/{arxiv}" if arxiv else (f"https://doi.org/{doi}" if doi else ""),
        "contribution": None, "branches": branches, "taxonomy_cells": [],
        "verified": "extension:" + k["source"], "bibkey": key, "extension": True,
        "screening_verdict": s["verdict"], "primary_branch": s["primary_branch"], "locus_tags": s["locus_tags"],
        "secondary_branches": s["secondary_branches"], "pool_source": p["source"], **category(pid),
    })

json.dump(out, open(CORPUS / "corpus_master_extended.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
ext = [r for r in out if r["extension"]]
print(f"{len(out)} records ({len(original)} original + {len(ext)} extension); "
      f"locus-tagged extension papers: {sum(bool(r['locus_tags']) for r in ext)}")
cats = {}
for r in out:
    cats[r["category"]] = cats.get(r["category"], 0) + 1
print("categories:", cats)
