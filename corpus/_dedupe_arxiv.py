# -*- coding: utf-8 -*-
"""Resolve the arXiv branch-query overlap.

Re-executes each branch query from _branch_queries.json against the arXiv API,
pages through the full result set, and counts distinct arXiv identifiers. The
per-branch yields sum to 2,751 with multiplicity; this reports how many unique
records that actually is.

Writes _arxiv_dedupe.json and prints a summary.
"""
import json, re, time, io, os, urllib.request, urllib.parse, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
QF = os.path.join(HERE, "_branch_queries.json")
OUT = os.path.join(HERE, "_arxiv_dedupe.json")
API = "http://export.arxiv.org/api/query"
PAGE = 100

def fetch(q, start, tries=6):
    url = "%s?search_query=%s&start=%d&max_results=%d" % (
        API, urllib.parse.quote(q), start, PAGE)
    delay = 4
    for _ in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return r.read().decode("utf-8", "replace")
        except Exception:
            time.sleep(delay); delay = min(delay * 2, 60)
    return None

qs = json.load(io.open(QF, encoding="utf-8"))
if isinstance(qs, dict):
    qs = [{"branch": k, "arxiv": v} for k, v in qs.items()]

per_branch, all_ids = {}, set()
for item in qs:
    b = item.get("branch") or item.get("id") or "?"
    q = item.get("arxiv") or item.get("arxiv_query") or item.get("query")
    if not q:
        continue
    ids, start = set(), 0
    while True:
        xml = fetch(q, start)
        if xml is None:
            break
        found = re.findall(r"<id>http://arxiv\.org/abs/([^<]+)</id>", xml)
        found = [re.sub(r"v\d+$", "", f) for f in found]
        if not found:
            break
        ids.update(found)
        start += PAGE
        if len(found) < PAGE or start > 3000:
            break
        time.sleep(3)
    per_branch[b] = len(ids)
    all_ids |= ids
    print("  %-6s %4d unique (running union %d)" % (b, len(ids), len(all_ids)))
    time.sleep(3)

total_with_multiplicity = sum(per_branch.values())
res = {
    "per_branch_unique": per_branch,
    "sum_with_multiplicity": total_with_multiplicity,
    "unique_across_branches": len(all_ids),
    "cross_branch_duplicates": total_with_multiplicity - len(all_ids),
}
json.dump(res, io.open(OUT, "w", encoding="utf-8"), indent=2)
print("\nsum with multiplicity : %d" % total_with_multiplicity)
print("unique arXiv records  : %d" % len(all_ids))
print("cross-branch dupes    : %d" % res["cross_branch_duplicates"])
