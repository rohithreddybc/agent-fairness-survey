"""Round 2 of the targeted query: fetch ALL hits of the TARGETED_QUERY in build_pool.py (the first
round screened only the top 60 by relevance) and write the ones not yet in pool.jsonl and not in
the corpus to screen_input2.jsonl (blind: id, title, published, abstract) and pool2.jsonl."""
import json, pathlib, time
from build_pool import fetch, TARGETED_QUERY

HERE = pathlib.Path(__file__).resolve().parent
seen = {json.loads(l)["id"] for l in open(HERE / "pool.jsonl", encoding="utf-8")}
corpus = {p["arxiv_id"] for p in json.load(open(HERE.parent / "corpus" / "corpus_master.json", encoding="utf-8")) if p["arxiv_id"]}
hits, total = [], None
for start in (0, 100):
    got, total = fetch({"search_query": TARGETED_QUERY, "sortBy": "relevance", "start": start, "max_results": 100})
    hits += got
    time.sleep(3)
new = [h for h in {h["id"]: h for h in hits}.values() if h["id"] not in seen and h["id"] not in corpus]
with open(HERE / "pool2.jsonl", "w", encoding="utf-8") as f:
    for h in new:
        f.write(json.dumps({**h, "source": ["targeted-search-round2"]}, ensure_ascii=False) + "\n")
with open(HERE / "screen_input2.jsonl", "w", encoding="utf-8") as f:
    for h in sorted(new, key=lambda h: h["id"]):
        f.write(json.dumps({k: h[k] for k in ("id", "title", "published", "abstract")}, ensure_ascii=False) + "\n")
log = json.load(open(HERE / "search_log.json"))
log["round2"] = {"total_results": total, "fetched": len(hits), "new_unscreened": len(new)}
json.dump(log, open(HERE / "search_log.json", "w"), indent=1)
print(log["round2"])
