"""Coding input for the 59 locus-tagged corpus papers: key, title, abstract (arXiv API, else
Crossref), and the authors' locus tags (branch labels). Writes code_input_existing.jsonl."""
import json, re, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET, pathlib

HERE = pathlib.Path(__file__).resolve().parent
UA = {"User-Agent": "agent-fairness-survey-corpus-extension/1.0"}
NS = {"a": "http://www.w3.org/2005/Atom"}
LOC = {"tool-api-selection-bias": "C1", "memory-retrieval-bias": "C2", "multiagent-delegation-bias": "C3",
       "planning-decomposition-bias": "C4", "user-modeling-personalization-harms": "C5",
       "longhorizon-fairness-drift": "T"}


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        return r.read()


corpus = json.load(open(HERE.parent / "corpus" / "corpus_master.json", encoding="utf-8"))
recs = [p for p in corpus if set(p["branches"]) & set(LOC)]
ids = [p["arxiv_id"] for p in recs if p["arxiv_id"]]
abst = {}
for i in range(0, len(ids), 50):
    root = ET.fromstring(get("http://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"id_list": ",".join(ids[i:i + 50]), "max_results": 50})))
    for e in root.findall("a:entry", NS):
        aid = e.find("a:id", NS).text.rsplit("/", 1)[-1].split("v")[0]
        abst[aid] = " ".join(e.find("a:summary", NS).text.split())
    time.sleep(3)
out = []
for p in recs:
    a = abst.get(p["arxiv_id"]) if p["arxiv_id"] else None
    if not a and p.get("doi"):
        try:
            m = json.loads(get("https://api.crossref.org/works/" + p["doi"]))["message"]
            a = re.sub("<[^>]+>", "", m.get("abstract", "")).strip() or None
        except Exception:
            a = None
    out.append({"key": p["bibkey"], "title": p["title"], "year": p["year"], "venue": p["venue"],
                "abstract": a, "author_summary": p["contribution"].split(" | ")[0],
                "author_locus_tags": [LOC[b] for b in p["branches"] if b in LOC],
                "primary_locus": LOC.get(p["branches"][0])})
with open(HERE / "code_input_existing.jsonl", "w", encoding="utf-8") as f:
    for o in out:
        f.write(json.dumps(o, ensure_ascii=False) + "\n")
print(len(out), "records;", sum(1 for o in out if not o["abstract"]), "without abstract:",
      [o["key"] for o in out if not o["abstract"]])
