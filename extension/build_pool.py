"""Build the candidate pool for the corpus extension (2026-11-09).

Sources:
  A. the 32 adjudication rows in ../corpus/_adjudicate_input.tsv (28 distinct arXiv ids)
  B. works identified by external review of the manuscript (REVIEW_IDS below)
  C. one targeted arXiv query aimed at component-level / counterfactual agent fairness
     (TARGETED_QUERY), top 60 by relevance, submitted on or before the 10 June 2026 cutoff
Writes pool.jsonl (one record per distinct paper) and search_log.json.
"""
import json, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET, csv, datetime, pathlib

HERE = pathlib.Path(__file__).resolve().parent
CORPUS = HERE.parent / "corpus"
NS = {"a": "http://www.w3.org/2005/Atom"}
UA = {"User-Agent": "agent-fairness-survey-corpus-extension/1.0"}

REVIEW_IDS = ["2512.16532", "2410.19803", "2407.06866", "2510.09905", "2305.07609", "2410.08948",
              "2511.06148", "2605.12530", "2503.15454", "2509.26584", "2410.02736", "2305.17926",
              "2404.13076", "2411.15594", "2312.03689", "2406.15484", "2405.04412", "2501.05396",
              "2601.17087", "2510.01164", "2508.02630", "2506.04419", "2403.00742"]
NON_ARXIV = [{"id": "doi:10.3390/math14030458",
              "title": "Evaluating Fairness in LLM Negotiator Agents via Economic Games Using Multi-Agent Systems",
              "authors": "Khaki, Choi", "published": "2026-01", "venue": "Mathematics 14(3), 458",
              "abstract": None, "source": "review"}]
TARGETED_QUERY = ('(abs:agent OR abs:agentic OR abs:"multi-agent" OR abs:"tool use") AND '
                  '(abs:counterfactual OR abs:"name swap" OR abs:"demographic swap" OR abs:"intermediate" '
                  'OR abs:"trajectory" OR abs:"pipeline") AND (abs:fairness OR abs:bias OR abs:discrimination) '
                  'AND (abs:"language model" OR abs:LLM) AND submittedDate:[200001010000 TO 202606102359]')


def fetch(params):
    url = "http://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        root = ET.fromstring(r.read())
    total = root.find("{http://a9.com/-/spec/opensearch/1.1/}totalResults")
    out = []
    for e in root.findall("a:entry", NS):
        aid = e.find("a:id", NS).text.rsplit("/", 1)[-1].split("v")[0]
        out.append({"id": aid,
                    "title": " ".join(e.find("a:title", NS).text.split()),
                    "authors": ", ".join(a.find("a:name", NS).text for a in e.findall("a:author", NS)),
                    "published": e.find("a:published", NS).text[:10],
                    "abstract": " ".join(e.find("a:summary", NS).text.split())})
    return out, (int(total.text) if total is not None else None)


def main():
    pool = {}
    with open(CORPUS / "_adjudicate_input.tsv", encoding="utf-8") as f:
        for row in csv.reader(f, delimiter="\t"):
            if len(row) < 4:
                continue
            rec = pool.setdefault(row[1], {"id": row[1], "title": row[2], "abstract": row[3],
                                           "source": [], "branch_entries": []})
            rec["source"].append("adjudication") if "adjudication" not in rec["source"] else None
            rec["branch_entries"].append(row[0])
    corpus_ids = {p["arxiv_id"] for p in json.load(open(CORPUS / "corpus_master.json", encoding="utf-8")) if p["arxiv_id"]}
    ids = [i for i in REVIEW_IDS]
    got, _ = fetch({"id_list": ",".join(ids), "max_results": len(ids)})
    time.sleep(3)
    for g in got:
        rec = pool.setdefault(g["id"], {**g, "source": [], "branch_entries": []})
        rec.update({k: v for k, v in g.items() if k != "id"})
        if "review" not in rec["source"]:
            rec["source"].append("review")
    for n in NON_ARXIV:
        pool[n["id"]] = {**n, "source": ["review"], "branch_entries": []}
    tq, total = fetch({"search_query": TARGETED_QUERY, "sortBy": "relevance", "max_results": 60})
    time.sleep(3)
    for g in tq:
        rec = pool.setdefault(g["id"], {**g, "source": [], "branch_entries": []})
        for k, v in g.items():
            rec.setdefault(k, v)
        if "targeted-search" not in rec["source"]:
            rec["source"].append("targeted-search")
    # fill missing metadata for adjudication rows
    need = [k for k, v in pool.items() if not k.startswith("doi:") and "published" not in v]
    if need:
        got, _ = fetch({"id_list": ",".join(need), "max_results": len(need)})
        for g in got:
            pool[g["id"]].update({k: v for k, v in g.items() if k not in ("id", "abstract")})
    for k, v in pool.items():
        v["in_corpus"] = k in corpus_ids
    with open(HERE / "pool.jsonl", "w", encoding="utf-8") as f:
        for v in pool.values():
            f.write(json.dumps(v, ensure_ascii=False) + "\n")
    json.dump({"run": datetime.datetime.now().isoformat(timespec="seconds"),
               "targeted_query": TARGETED_QUERY, "targeted_total_results": total,
               "targeted_taken": len(tq), "review_ids": REVIEW_IDS + [n["id"] for n in NON_ARXIV],
               "pool_size": len(pool),
               "already_in_corpus": sum(v["in_corpus"] for v in pool.values())},
              open(HERE / "search_log.json", "w"), indent=1)
    print(json.load(open(HERE / "search_log.json")))


if __name__ == "__main__":
    main()
