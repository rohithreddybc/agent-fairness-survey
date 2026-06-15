#!/usr/bin/env python3
"""
build_corpus.py — Phase 2 (Architect) dedup + organize for the agent-fairness survey.

Reads corpus_raw.json (the Phase-1 workflow output), dedupes by arXiv id / DOI /
normalized title, merges the branches each paper appears in, and emits:
  - corpus_master.json   (unique papers, with all branches + a stable bibkey)
  - corpus_master.md     (human-readable table, grouped by primary branch)
  - references.bib       (BibTeX; @article for arXiv/journal, @inproceedings unknown)
  - coverage_matrix.md   (papers-per-(component x fairness-dimension) tallies)
  - VERIFY_QUEUE.md      (papers needing Phase-4 existence re-check, riskier first)

Deterministic; no network. Re-runnable.
"""
from __future__ import annotations
import json, re, unicodedata
from pathlib import Path
from collections import defaultdict, OrderedDict

HERE = Path(__file__).resolve().parent
RAW = HERE / "corpus_raw.json"

def norm_title(t: str) -> str:
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-z0-9 ]", " ", t.lower())
    return re.sub(r"\s+", " ", t).strip()

def first_author_last(authors: str) -> str:
    a = authors.split(" and ")[0].split(",")[0].strip()
    a = re.sub(r"\bet al\.?$", "", a).strip()
    toks = [w for w in re.split(r"\s+", a) if w]
    last = toks[-1] if toks else "anon"
    return re.sub(r"[^A-Za-z]", "", last) or "anon"

def title_word(t: str) -> str:
    stop = {"a","an","the","of","in","on","for","and","to","is","are","do","does",
            "toward","towards","how","when","can","with","via","be","or","beyond"}
    for w in norm_title(t).split():
        if w not in stop and len(w) > 2:
            return w
    return "x"

def main() -> None:
    data = json.loads(RAW.read_text(encoding="utf-8"))
    # dedup key: arxiv_id > doi > norm_title
    by_key: "OrderedDict[str, dict]" = OrderedDict()
    title_index: dict[str, str] = {}

    for branch in data["result"]:
        bname = branch["branch"]
        for p in branch["papers"]:
            ax = (p.get("arxiv_id") or "").strip()
            doi = (p.get("doi") or "").strip()
            nt = norm_title(p["title"])
            key = f"arxiv:{ax}" if ax else (f"doi:{doi}" if doi else f"title:{nt}")
            # collapse same-title duplicates that differ on id presence
            if key not in by_key and nt in title_index:
                key = title_index[nt]
            if key not in by_key:
                by_key[key] = {
                    "title": p["title"], "authors": p["authors"], "year": p["year"],
                    "venue": p["venue"], "arxiv_id": ax, "doi": doi,
                    "url": p.get("url", ""), "contribution": p["contribution"],
                    "branches": [], "taxonomy_cells": [], "verified": p.get("verified", ""),
                }
                title_index[nt] = key
            rec = by_key[key]
            if bname not in rec["branches"]:
                rec["branches"].append(bname)
            tc = p.get("taxonomy_cell", "")
            if tc and tc not in rec["taxonomy_cells"]:
                rec["taxonomy_cells"].append(tc)
            # prefer a record that has an arxiv_id / doi / longer contribution
            if ax and not rec["arxiv_id"]:
                rec["arxiv_id"] = ax
            if doi and not rec["doi"]:
                rec["doi"] = doi
            if len(p["contribution"]) > len(rec["contribution"]):
                rec["contribution"] = p["contribution"]

    papers = list(by_key.values())

    # assign stable bibkeys (dedupe collisions with a,b,c)
    used: dict[str, int] = defaultdict(int)
    for p in papers:
        base = f"{first_author_last(p['authors']).lower()}{p['year']}{title_word(p['title'])}"
        n = used[base]; used[base] += 1
        p["bibkey"] = base if n == 0 else base + chr(ord('a') + n)

    papers.sort(key=lambda x: (-len(x["branches"]), x["bibkey"]))

    (HERE / "corpus_master.json").write_text(
        json.dumps(papers, indent=2, ensure_ascii=False), encoding="utf-8")

    # ---- corpus_master.md ----
    primary = defaultdict(list)
    for p in papers:
        primary[p["branches"][0]].append(p)
    BRANCH_ORDER = [b["branch"] for b in data["result"]]
    lines = [f"# Master corpus — {len(papers)} unique papers "
             f"(deduped from {sum(len(b['papers']) for b in data['result'])} entries)\n",
             "Sorted within each primary branch. `×N` = appears in N taxonomy branches "
             "(cross-cutting). Full records in `corpus_master.json`.\n"]
    for b in BRANCH_ORDER:
        ps = primary.get(b, [])
        if not ps: continue
        lines.append(f"\n## {b}  ({len(ps)} papers)\n")
        lines.append("| bibkey | Title | Authors | Yr | Venue | arXiv/DOI | × |")
        lines.append("|---|---|---|---|---|---|---|")
        for p in ps:
            idr = p["arxiv_id"] or p["doi"] or "—"
            lines.append(f"| `{p['bibkey']}` | {p['title']} | {p['authors']} | "
                         f"{p['year']} | {p['venue']} | {idr} | {len(p['branches'])} |")
    (HERE / "corpus_master.md").write_text("\n".join(lines), encoding="utf-8")

    # ---- references.bib ----
    def esc(s): return s.replace("&", r"\&").replace("%", r"\%").replace("_", r"\_")
    bib = []
    for p in papers:
        etype = "article"
        fields = [f"  title = {{{esc(p['title'])}}}",
                  f"  author = {{{esc(p['authors'])}}}",
                  f"  year = {{{p['year']}}}"]
        if p["venue"]:
            key = "journal" if ("arxiv" in p["venue"].lower() or "preprint" in p["venue"].lower()) else "booktitle"
            fields.append(f"  {key} = {{{esc(p['venue'])}}}")
        if p["arxiv_id"]:
            fields.append(f"  eprint = {{{p['arxiv_id']}}}")
            fields.append("  archivePrefix = {arXiv}")
        if p["doi"]:
            fields.append(f"  doi = {{{p['doi']}}}")
        if p["url"]:
            fields.append(f"  url = {{{p['url']}}}")
        bib.append(f"@{etype}{{{p['bibkey']},\n" + ",\n".join(fields) + "\n}")
    (HERE.parent / "references.bib").write_text("\n\n".join(bib) + "\n", encoding="utf-8")

    # ---- coverage matrix (component x fairness dimension) ----
    COMPONENTS = {
        "tool-api-selection-bias": "Tool/API selection",
        "memory-retrieval-bias": "Memory & retrieval",
        "multiagent-delegation-bias": "Multi-agent delegation",
        "planning-decomposition-bias": "Planning/decomposition",
        "user-modeling-personalization-harms": "User modeling/personalization",
        "longhorizon-fairness-drift": "Long-horizon drift",
    }
    DIMS = ["group", "individual", "counterfactual"]
    def dim_of(p):
        blob = (p["contribution"] + " " + " ".join(p["taxonomy_cells"])).lower()
        ds = []
        if "counterfactual" in blob or "flip" in blob or "cfr" in blob: ds.append("counterfactual")
        if "group" in blob or "demographic parity" in blob or "equal" in blob: ds.append("group")
        if "individual" in blob: ds.append("individual")
        return ds or ["(unspec)"]
    grid = defaultdict(lambda: defaultdict(int))
    for p in papers:
        comps = [COMPONENTS[b] for b in p["branches"] if b in COMPONENTS]
        for c in comps:
            for d in dim_of(p):
                grid[c][d] += 1
    cm = ["# Coverage matrix — agent component × fairness dimension\n",
          "Cell = count of corpus papers touching that component with that fairness "
          "framing (a paper may count in several). Empties expose the measurement gap.\n",
          "| Component \\ Dimension | group | individual | counterfactual | (unspec) |",
          "|---|---|---|---|---|"]
    for c in COMPONENTS.values():
        row = grid[c]
        cm.append(f"| {c} | {row.get('group',0)} | {row.get('individual',0)} | "
                  f"{row.get('counterfactual',0)} | {row.get('(unspec)',0)} |")
    (HERE / "coverage_matrix.md").write_text("\n".join(cm), encoding="utf-8")

    # ---- verify queue (riskier first: future-dated 2026+ arXiv, no id) ----
    def risk(p):
        r = 0
        ax = p["arxiv_id"]
        if ax and re.match(r"^26\d\d\.", ax): r += 2   # 2026 ids — recent, re-check
        if not ax and not p["doi"]: r += 3              # no resolvable id at all
        if p["verified"] == "web-multiple-sources": r += 1
        return r
    risky = sorted([p for p in papers if risk(p) > 0], key=lambda x: -risk(x))
    vq = ["# Phase-4 verification queue\n",
          "Every citation gets checked, but these are higher-risk (recent 2026 arXiv ids, "
          "or no resolvable id). Confirm existence + correct attribution before v1.\n",
          "| risk | bibkey | Title | arXiv/DOI | verified-as |",
          "|---|---|---|---|---|"]
    for p in risky:
        vq.append(f"| {risk(p)} | `{p['bibkey']}` | {p['title']} | "
                  f"{p['arxiv_id'] or p['doi'] or 'NONE'} | {p['verified']} |")
    (HERE / "VERIFY_QUEUE.md").write_text("\n".join(vq), encoding="utf-8")

    print(f"unique papers: {len(papers)}")
    print(f"cross-cutting (>=3 branches): {sum(1 for p in papers if len(p['branches'])>=3)}")
    print(f"verify-queue size: {len(risky)}")
    print("wrote: corpus_master.json/.md, references.bib, coverage_matrix.md, VERIFY_QUEUE.md")

if __name__ == "__main__":
    main()
