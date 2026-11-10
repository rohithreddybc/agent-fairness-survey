"""Parse tab:mitigation-map from review/main.tex into table6_papers.json, with title and abstract
per cited key (code_input_existing.jsonl first, then corpus_master.json + arXiv API)."""
import json, re, sys, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET, pathlib

ROOT = pathlib.Path(sys.argv[1])  # .../ResearchPaper7
EXT = ROOT / "data_release" / "extension"
UA = {"User-Agent": "agent-fairness-survey-corpus-extension/1.0 (mailto:rohithreddybc@gmail.com)"}
NS = {"a": "http://www.w3.org/2005/Atom"}

tex = (ROOT / "review" / "main.tex").read_text(encoding="utf-8")
block = tex[tex.index(r"\label{tab:mitigation-map}"):]
block = block[block.index(r"\endfoot") + len(r"\endfoot"):block.index(r"\end{xltabular}")]


def clean(s):
    s = re.sub(r"\(\\S\\ref\{[^}]*\}\)", "", s)
    s = s.replace(r"\allowbreak", "").replace(r"$\rightarrow$", "->").replace(r"$^{\dagger}$", " [dagger]")
    s = re.sub(r"\\textbf\{([^}]*)\}", r"\1", s)
    s = s.replace("$", "")
    return " ".join(s.split()).strip()


rows = []
for line in block.splitlines():
    line = line.strip()
    if "&" not in line or not line.endswith(r"\\"):
        continue
    cells = [c.strip() for c in line[:-2].split("&")]
    if len(cells) != 6:
        raise SystemExit("unexpected row: " + line)
    keys = []
    for m in re.finditer(r"\\cite\{([^}]*)\}(\$\^\{\\dagger\}\$)?", cells[4]):
        for k in m.group(1).split(","):
            keys.append({"key": k.strip(), "dagger_in_table": bool(m.group(2))})
    rows.append({"row": len(rows) + 1, "entry_locus": clean(cells[0]), "operator_targeted": clean(cells[1]),
                 "pipeline_stage": clean(cells[2]), "intervention_class": clean(cells[3]),
                 "evidence_density": clean(cells[5]), "intervention_class_dagger": "[dagger]" in clean(cells[3]),
                 "keys": keys})

existing = {}
for l in open(EXT / "code_input_existing.jsonl", encoding="utf-8"):
    o = json.loads(l)
    existing[o["key"]] = o
corpus = {p["bibkey"]: p for p in json.load(open(ROOT / "data_release" / "corpus" / "corpus_master.json", encoding="utf-8"))}
bib = (ROOT / "review" / "references.bib").read_text(encoding="utf-8")


def bib_title(k):
    m = re.search(r"@\w+\{" + re.escape(k) + r",(.*?)\n\}", bib, re.S)
    if not m:
        return None
    t = re.search(r"title\s*=\s*[{\"](.*?)[}\"],?\s*\n", m.group(1), re.S)
    return " ".join(t.group(1).replace("{", "").replace("}", "").split()) if t else None


# A dagger on the intervention-class cell marks the paper whose method that cell names:
# the single cited key, or for row 3 ("Alignment / MaxMin-RLHF[dagger]") chakraborty2024maxmin.
CLASS_DAGGER_KEY = {"MaxMin-RLHF": "chakraborty2024maxmin"}
for r in rows:
    if r["intervention_class_dagger"]:
        target = (r["keys"][0]["key"] if len(r["keys"]) == 1 else
                  next((v for t, v in CLASS_DAGGER_KEY.items() if t in r["intervention_class"]), None))
        for k in r["keys"]:
            if k["key"] == target:
                k["dagger_in_table"] = True
                k["dagger_from"] = "intervention-class cell"

allkeys = []
for r in rows:
    for k in r["keys"]:
        if k["key"] not in allkeys:
            allkeys.append(k["key"])

need = [corpus[k]["arxiv_id"] for k in allkeys
        if k not in existing and k in corpus and corpus[k].get("arxiv_id")]
fetched = {}
for i in range(0, len(need), 40):
    url = "http://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"id_list": ",".join(need[i:i + 40]), "max_results": 40})
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as resp:
        root = ET.fromstring(resp.read())
    for e in root.findall("a:entry", NS):
        idel = e.find("a:id", NS)
        if idel is None or e.find("a:summary", NS) is None:
            continue
        aid = re.sub(r"v\d+$", "", idel.text.rsplit("/abs/", 1)[-1])
        fetched[aid] = {"title": " ".join(e.find("a:title", NS).text.split()),
                        "abstract": " ".join(e.find("a:summary", NS).text.split()),
                        "published": e.find("a:published", NS).text[:10]}
    time.sleep(3)

papers = {}
for k in allkeys:
    p = {"key": k, "rows": [r["row"] for r in rows if any(x["key"] == k for x in r["keys"])],
         "dagger_in_table": any(x["dagger_in_table"] for r in rows for x in r["keys"] if x["key"] == k),
         "in_corpus": k in corpus, "title": None, "year": None, "venue": None, "arxiv_id": None,
         "abstract": None, "abstract_source": None}
    if k in corpus:
        c = corpus[k]
        p.update(title=c["title"], year=c["year"], venue=c["venue"], arxiv_id=c.get("arxiv_id") or None)
    if k in existing and existing[k].get("abstract"):
        p.update(abstract=existing[k]["abstract"], abstract_source="code_input_existing.jsonl")
    elif p["arxiv_id"] and p["arxiv_id"] in fetched:
        p.update(abstract=fetched[p["arxiv_id"]]["abstract"], abstract_source="arXiv API " + p["arxiv_id"])
    if not p["title"]:
        p["title"] = bib_title(k)
    if not p["abstract"]:
        p["abstract_source"] = ("not in corpus_master.json" if not p["in_corpus"]
                                else "no arXiv id; abstract not fetched" if not p["arxiv_id"]
                                else "arXiv fetch returned nothing")
    papers[k] = p

out = {"source": "review/main.tex, Table tab:mitigation-map (identical rows in submit/main.tex)",
       "built": time.strftime("%Y-%m-%d"),
       "note": "rows = Table 6 rows in printed order; papers = distinct cited keys (a key cited in two rows appears once, with both row numbers). Empty rows carry no keys.",
       "rows": rows, "papers": list(papers.values())}
json.dump(out, open(EXT / "table6_papers.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(rows), "rows;", len(papers), "keys;", "missing abstract:",
      [(p["key"], p["abstract_source"]) for p in papers.values() if not p["abstract"]])
