#!/usr/bin/env python3
"""
verify_citations.py — Phase 4 guardrail: confirm every arXiv id in the corpus
actually resolves, and that the returned title matches what we recorded.

Hits the arXiv Atom API in batches (id_list=...), fuzzy-matches titles, and writes
VERIFY_RESULTS.md flagging: OK | TITLE_MISMATCH | NOT_FOUND. DOI-only and id-less
entries are listed for manual/Crossref check. Deterministic, network-dependent.
"""
from __future__ import annotations
import json, re, time, unicodedata, urllib.request, urllib.parse
from pathlib import Path
from difflib import SequenceMatcher

HERE = Path(__file__).resolve().parent
PAPERS = json.loads((HERE / "corpus_master.json").read_text(encoding="utf-8"))
API = "http://export.arxiv.org/api/query"

def norm(t: str) -> str:
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", t.lower())).strip()

def fetch_batch(ids):
    q = urllib.parse.urlencode({"id_list": ",".join(ids), "max_results": len(ids)})
    req = urllib.request.Request(API + "?" + q, headers={"User-Agent": "survey-verify/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "ignore")

def parse_entries(xml):
    # crude Atom parse: map arxiv id -> title
    out = {}
    for m in re.finditer(r"<entry>(.*?)</entry>", xml, re.S):
        e = m.group(1)
        idm = re.search(r"<id>https?://arxiv\.org/abs/([^<]+)</id>", e)
        tm = re.search(r"<title>(.*?)</title>", e, re.S)
        if idm and tm:
            aid = idm.group(1).split("v")[0].strip()
            out[aid] = re.sub(r"\s+", " ", tm.group(1)).strip()
    return out

def main():
    arxiv_papers = [p for p in PAPERS if p["arxiv_id"]]
    ids = [p["arxiv_id"] for p in arxiv_papers]
    resolved = {}
    B = 25
    for i in range(0, len(ids), B):
        batch = ids[i:i+B]
        try:
            resolved.update(parse_entries(fetch_batch(batch)))
        except Exception as e:
            print(f"batch {i} error: {e}")
        time.sleep(3)  # arXiv API politeness

    rows, n_ok, n_mis, n_missing = [], 0, 0, 0
    for p in arxiv_papers:
        aid = p["arxiv_id"]
        got = resolved.get(aid)
        if got is None:
            status, detail = "NOT_FOUND", ""
            n_missing += 1
        else:
            sim = SequenceMatcher(None, norm(p["title"]), norm(got)).ratio()
            if sim >= 0.75:
                status, detail = "OK", f"{sim:.2f}"
                n_ok += 1
            else:
                status, detail = "TITLE_MISMATCH", f"{sim:.2f} got=\"{got}\""
                n_mis += 1
        rows.append((status, p["bibkey"], aid, p["title"], detail))

    order = {"NOT_FOUND": 0, "TITLE_MISMATCH": 1, "OK": 2}
    rows.sort(key=lambda r: (order[r[0]], r[1]))

    out = [f"# Citation verification (arXiv API)\n",
           f"- arXiv-id papers checked: **{len(arxiv_papers)}**",
           f"- OK: **{n_ok}** · TITLE_MISMATCH: **{n_mis}** · NOT_FOUND: **{n_missing}**",
           f"- DOI-only / no-id (manual check): "
           f"**{sum(1 for p in PAPERS if not p['arxiv_id'])}**\n",
           "| status | bibkey | arXiv | title | detail |",
           "|---|---|---|---|---|"]
    for s, k, a, t, d in rows:
        out.append(f"| {s} | `{k}` | {a} | {t} | {d} |")
    out.append("\n## DOI-only / id-less (verify via Crossref/DOI resolver)\n")
    out.append("| bibkey | doi | title | verified-as |")
    out.append("|---|---|---|---|")
    for p in PAPERS:
        if not p["arxiv_id"]:
            out.append(f"| `{p['bibkey']}` | {p['doi'] or 'NONE'} | {p['title']} | {p['verified']} |")
    (HERE / "VERIFY_RESULTS.md").write_text("\n".join(out), encoding="utf-8")
    print(f"OK={n_ok} MISMATCH={n_mis} NOT_FOUND={n_missing} -> VERIFY_RESULTS.md")

if __name__ == "__main__":
    main()
