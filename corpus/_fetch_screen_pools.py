# -*- coding: utf-8 -*-
"""Re-execute the ten branch queries and capture the relevance-ranked pool
each returns, with title and abstract, for a logged screening pass.

Writes _screen_full_pool.tsv: branch, arxiv_id, title, abstract.
Deliberately slow: arXiv asks for >=3s between calls and rate-limits bursts.
"""
import io, json, re, time, urllib.parse, urllib.request

HERE = io.open(__file__).name.rsplit("\\", 1)[0] if "\\" in __file__ else "."
BASE = "http://export.arxiv.org/api/query"
PER_BRANCH = 60          # top-N relevance-ranked per branch, fixed and reported
SLEEP_OK = 6.0
SLEEP_RETRY = 30.0
MAX_TRIES = 6

queries = json.loads(io.open("_branch_queries.json", encoding="utf-8").read())

def fetch(q, n):
    url = "%s?search_query=%s&start=0&max_results=%d&sortBy=relevance" % (
        BASE, urllib.parse.quote(q), n)
    for attempt in range(MAX_TRIES):
        try:
            with urllib.request.urlopen(url, timeout=90) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:
            print("    retry %d (%s)" % (attempt + 1, str(e)[:60]), flush=True)
            time.sleep(SLEEP_RETRY)
    return None

def parse(xml):
    out = []
    for m in re.finditer(r"<entry>(.*?)</entry>", xml, re.S):
        e = m.group(1)
        i = re.search(r"<id>http://arxiv\.org/abs/([^<]+)</id>", e)
        t = re.search(r"<title>(.*?)</title>", e, re.S)
        s = re.search(r"<summary>(.*?)</summary>", e, re.S)
        if not (i and t):
            continue
        aid = re.sub(r"v\d+$", "", i.group(1))
        ti = re.sub(r"\s+", " ", t.group(1)).strip()
        ab = re.sub(r"\s+", " ", s.group(1)).strip() if s else ""
        if len(ab) > 1200:
            ab = ab[:1200]
        out.append((aid, ti, ab))
    return out

rows = []
for q in queries:
    print("%s %s ..." % (q["branch"], q["name"]), flush=True)
    xml = fetch(q["arxiv_query"], PER_BRANCH)
    if xml is None:
        print("  FAILED", flush=True)
        continue
    recs = parse(xml)
    print("  got %d" % len(recs), flush=True)
    for aid, ti, ab in recs:
        rows.append("%s\t%s\t%s\t%s" % (q["branch"], aid, ti, ab))
    time.sleep(SLEEP_OK)

io.open("_screen_full_pool.tsv", "w", encoding="utf-8").write("\n".join(rows))
print("TOTAL POOL ROWS: %d" % len(rows))
