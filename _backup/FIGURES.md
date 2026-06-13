# FIGURES.md — visual + table specs (agent-fairness survey)

Two signature figures + five tables. Bibkeys reference `references.bib`. LaTeX is
ACM `acmart` double-column ready (`forest`/`booktabs`). Counts come from
`corpus/coverage_matrix.md` (regenerate via `corpus/build_corpus.py`).

---

## Figure 1 — Taxonomy tree (THE organizing visual)
**Caption:** *Where unfairness enters the LLM-agent pipeline. Bias is organized by
agent component (Axis 1), each cross-referenced to evaluation (Axis 2) and
mitigation (Axis 3). Unlike QA-level LLM-fairness taxonomies, the unit of analysis
is the **acting** agent.*

Three-level tree. Root → the 6 components → representative mechanisms + exemplar
cites. Render with `forest`.

```latex
\begin{figure*}[t]\centering
\begin{forest}
for tree={grow=east, parent anchor=east, child anchor=west, anchor=west,
  edge path={\noexpand\path[\forestoption{edge}] (!u.parent anchor) -- +(8pt,0)
    |- (.child anchor)\forestoption{edge label};},
  l sep=12pt, s sep=3pt, font=\small, rounded corners, draw, align=left}
[Fairness in\\LLM Agents, fill=gray!18
  [1. Tool / API selection, fill=blue!8
     [Tool-choice bias; description sensitivity; search/source inheritance\\
      {\tiny blankenstein2025biasbusters, sneh2025tooltweak, xu2026ducx, wu2024rag}]]
  [2. Memory \& retrieval, fill=blue!8
     [RAG fairness; multi-turn accumulation; context-position bias\\
      {\tiny hu2024free, fan2024fairmt, geng2025accumulating, liu2023lost}]]
  [3. Multi-agent delegation, fill=blue!8
     [Persona/role bias; emergent + propagated bias; in-group favoritism\\
      {\tiny gupta2023bias, nguyen2025social, madigan2025emergent, li2025from}]]
  [4. Planning / decomposition, fill=blue!8
     [CoT-reasoning bias; decision disparity; role/task allocation\\
      {\tiny wu2025reasoning, li2025actions, hall2025guiding, parziale2026once}]]
  [5. User modeling / personalization, fill=blue!8
     [Identity inference; name/dialect bias; recommender unfairness\\
      {\tiny kantharuban2024stereotype, pawar2025presumed, mire2025rejected, deldjoo2024cfairllm}]]
  [6. Long-horizon drift, fill=blue!8
     [Multi-turn bias compounding; sycophancy decay; feedback loops\\
      {\tiny ma2026implicit, liu2025truth, wyllie2024fairness, xu2024adapting}]]
]
\end{forest}
\caption{Taxonomy of fairness in LLM-based agents, organized by agent component.}
\label{fig:taxonomy}
\end{figure*}
```

**Text fallback (also good for the README/repo landing page):**
```
Fairness in LLM Agents
├── 1. Tool / API selection ....... tool-choice bias, description sensitivity, search inheritance
├── 2. Memory & retrieval ......... RAG fairness, multi-turn accumulation, context-position bias
├── 3. Multi-agent delegation ..... persona/role bias, emergent & propagated bias, in-group favoritism
├── 4. Planning / decomposition ... CoT-reasoning bias, decision disparity, task allocation
├── 5. User modeling / personalization .. identity inference, name/dialect bias, recommender unfairness
└── 6. Long-horizon drift ......... multi-turn compounding, sycophancy decay, feedback loops
```

---

## Figure 2 — Coverage matrix (THE measurement-gap visual)
**Caption:** *Corpus coverage by agent component (rows) × fairness dimension
(columns). Cells show the number of surveyed papers. The near-empty
**counterfactual** column — the dimension agentic harms most require — exposes the
measurement gap this survey identifies and that an acting-agent benchmark must fill.*

Render as a heatmap (darker = more papers). Data (from `coverage_matrix.md`; the
`(unspec)` column = papers measuring disparity without a named formal dimension):

| Component \ Dimension | group | individual | counterfactual | (unspec) |
|---|---|---|---|---|
| Tool/API selection | 1 | 0 | 0 | 11 |
| Memory & retrieval | 0 | 0 | 0 | 12 |
| Multi-agent delegation | 5 | 1 | 0 | 6 |
| Planning/decomposition | 4 | 1 | 0 | 5 |
| User modeling/personalization | 1 | 0 | 0 | 11 |
| Long-horizon drift | 2 | 0 | 1 | 7 |

**The punchline to state in §7:** across all six agent components, formal
**counterfactual** fairness is measured in **exactly one** corpus paper
(`she2025fairsense`, long-horizon) — yet counterfactual flip is the natural test
for "would this agent have *acted* differently for another demographic?" Group
fairness clusters only where decisions are explicit (multi-agent, planning); tool,
memory, and personalization harms are documented but **rarely formalized**.

```latex
% Heatmap via pgfplots matrix plot or a colored booktabs table.
% Color rule: 0=white, 1-2=blue!15, 3-5=blue!35, 6+=blue!55. Annotate the
% counterfactual column with a red dashed box labeled "measurement gap".
```

---

## Table 0 — Differentiation vs. prior surveys (the positioning table)
**Caption:** *How this survey differs from the closest prior work.*

| Work | Organizing axis | Unit | Fairness coverage | Executable? |
|---|---|---|---|---|
| Chu/Zhang 2024 (`chu2024fairness`) | bias→metric→mitigation | single-turn LLM | **whole survey** | no |
| Gallegos 2024 (`gallegos2024bias`) | metrics/datasets/mitigation | single-turn LLM | whole survey | no |
| Mohammadi 2025 (`mohammadi2025evaluation`) | eval targets/methods | LLM agent | one sub-topic | no |
| Vatsal 2026 (`vatsal2026agentic`) | 7 dimensions, healthcare | clinical agent | 1 of 7 dims | no |
| Mayilvaghanan 2026 (`mayilvaghanan2026counterfactual`) | CFR/MASD | contact-center agent | single domain | yes (1 domain) |
| **This survey** | **agent component** | **acting agent** | **whole survey** | audit (§6) |

---

## Table 1 — Component × harm mechanism × evidence (core of §3)
Columns: Component · Harm mechanism · Representative evidence (2–4 bibkeys) ·
Maturity (●●● well-studied / ●○○ emerging). One row per mechanism (~14 rows).
Built directly from `corpus_master.md` primary-branch groupings.

## Table 2 — Benchmarks × level × domain × agentic? (core of §4)
Columns: Benchmark/dataset · Fairness level (QA / generation / **action**) ·
Domain · Metric · Agentic? (Y/N). Rows: `parrish2022bbq`, `dhamala2021bold`,
`nadeem2021stereoset`, `nangia2020crows`, `smith2022sorry`, `wang2024ceb`,
`fan2024fairmt`, `xiao2025fairmedqa`, `pfohl2024toolbox`, `ghosh2025medequalqa`,
`adappanavar2025mfarm`, `wu2024fmbench`, `azime2025accept`, `hu2025llms`,
`blankenstein2025biasbusters`, `mayilvaghanan2026counterfactual`,
`parziale2026scope`. **Punchline column:** "Agentic?" is N for ~all → the gap.

## Table 3 — Mitigation × component × stage × evidence (core of §5)
Columns: Mitigation family · Targets which component(s) · Pipeline stage
(pre / in-training / inference / post) · Evidence · Agent-level? Rows: prompting
(`li2024prompting`, `zhang2024causal`, `furniturewala2024thinking`); fine-tuning/
alignment (`ouyang2022training`, `chakraborty2024maxmin`, `allam2024biasdpo`,
`kabra2025reasoning`); guardrails (`dong2024building`); multi-agent debiasing
(`owens2024multi`, `xu2024mitigating`, `ki2025multiple`, `choi2025identity`);
inference-time (`li2025fairsteer`); process/constitutional (`bai2022constitutional`,
`huang2024collective`); RAG-level (`kim2024fair`, `kim2025mitigating`).

---

### Production notes
- v1: text-fallback tree + the two tables that carry the argument (Table 0 + the
  coverage matrix). Figures 1–2 as TikZ in v1 if time permits, else v2.
- Keep figures colorblind-safe (single-hue sequential). All cites must exist in
  `references.bib` (verified — see `corpus/VERIFY_RESULTS.md`).
