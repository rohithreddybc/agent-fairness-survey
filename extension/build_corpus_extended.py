"""Write ../corpus/corpus_master_extended.json: the 202 original corpus records (unchanged apart from
an added "extension": false) followed by the 33 papers admitted by the 2026-11 extension.

Inputs : ../corpus/corpus_master.json, screen_final.jsonl (verdicts, branches, locus tags),
         pool.jsonl (title, authors, date, source), bibkeys.json (arXiv id or DOI -> bib key),
         ../../review/references.bib if present (year and venue; otherwise date and "arXiv preprint").
Usage  : python -I build_corpus_extended.py
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
CORPUS = HERE.parent / "corpus"
BIB = HERE.parent.parent / "review" / "references.bib"
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
screen = {r["id"]: r for r in jl("screen_final.jsonl")}
pool = {r["id"]: r for r in jl("pool.jsonl")}
keys = json.load(open(HERE / "bibkeys.json", encoding="utf-8"))

out = [{**r, "extension": False} for r in original]
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
        "secondary_branches": s["secondary_branches"], "pool_source": p["source"],
    })

json.dump(out, open(CORPUS / "corpus_master_extended.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
ext = [r for r in out if r["extension"]]
print(f"{len(out)} records ({len(original)} original + {len(ext)} extension); "
      f"locus-tagged extension papers: {sum(bool(r['locus_tags']) for r in ext)}")
