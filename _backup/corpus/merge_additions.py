#!/usr/bin/env python3
"""Merge CSUR-pass additions (prior-art scans + foundational must-cites) into
corpus_raw.json as new branches, deduped against the existing corpus. Then the
caller reruns build_corpus.py + verify_citations.py."""
from __future__ import annotations
import json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent

def norm(t): return re.sub(r'[^a-z0-9]', '', t.lower())

raw = json.loads((HERE / "corpus_raw.json").read_text(encoding="utf-8"))
seen_ax = set(); seen_ti = set()
for b in raw["result"]:
    for p in b["papers"]:
        if p.get("arxiv_id"): seen_ax.add(p["arxiv_id"].strip())
        seen_ti.add(norm(p["title"]))

def fresh(p):
    ax = (p.get("arxiv_id") or "").strip()
    if ax and ax in seen_ax: return False
    if norm(p["title"]) in seen_ti: return False
    if ax: seen_ax.add(ax)
    seen_ti.add(norm(p["title"]))
    return True

# --- scan additions (prior-art near-neighbors + adjacent ACM surveys) ---
scan_papers = []
for f in ["../reviews/recent-web-surveys.json", "../reviews/acm-dl-scan.json"]:
    for p in json.loads((HERE / f).read_text(encoding="utf-8")).get("papers", []):
        rec = {
            "title": p["title"], "authors": p.get("authors", ""), "year": p.get("year", 0),
            "venue": p.get("venue", ""), "arxiv_id": (p.get("arxiv_id") or "").strip(),
            "doi": (p.get("doi") or "").strip(), "url": p.get("url", ""),
            "contribution": (p.get("overlap", "") + " | DIFF: " + p.get("how_ours_differs", ""))[:400],
            "taxonomy_cell": "prior-art / " + p.get("kind", "related"),
            "verified": p.get("verified", "web-multiple"),
        }
        if fresh(rec): scan_papers.append(rec)

# --- foundational must-cite additions ---
hunter = json.loads((HERE / "hunter_additions.json").read_text(encoding="utf-8"))
hunter_papers = []
for p in hunter:
    rec = {
        "title": p["title"], "authors": p["authors"], "year": p["year"], "venue": p["venue"],
        "arxiv_id": (p.get("arxiv_id") or "").strip(), "doi": (p.get("doi") or "").strip(),
        "url": p.get("url", ""), "contribution": p["contribution"],
        "taxonomy_cell": p["taxonomy_cell"], "verified": p.get("verified", "agent-verified"),
    }
    if fresh(rec): hunter_papers.append(rec)

# normalize arXiv DOIs (10.48550/arXiv.x) -> drop, keep eprint
for p in scan_papers + hunter_papers:
    if p["doi"].lower().startswith("10.48550/arxiv"):
        p["doi"] = ""

raw["result"].append({"branch": "prior-art-additions", "papers": scan_papers})
raw["result"].append({"branch": "foundational-must-cite", "papers": hunter_papers})
(HERE / "corpus_raw.json").write_text(json.dumps(raw, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"added prior-art-additions: {len(scan_papers)}; foundational-must-cite: {len(hunter_papers)}")
print(f"total entries now: {sum(len(b['papers']) for b in raw['result'])}")
