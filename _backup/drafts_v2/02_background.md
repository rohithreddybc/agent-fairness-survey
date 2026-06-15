## 2. Background & Scope

### 2.1 Fairness Definitions

Formal fairness research has converged on three partially complementary families of criteria, each encoding a distinct moral intuition about equitable treatment. Understanding their boundaries, and the impossibility results that connect them, is a prerequisite for the component-level analysis that follows.

#### 2.1.1 Group Fairness

Group fairness requires that outcomes be statistically equivalent across protected demographic groups. The canonical formal treatment in the supervised-learning setting comes from \cite{hardt2016equality}, who distinguish *equality of opportunity* (equal true-positive rates across groups, conditioned on a positive true label) from *equalized odds* (equal both true-positive and false-positive rates). Both criteria reduce fairness to a statistical comparison over a finite set of labeled groups and a classifier's output distribution, making them operationally tractable and empirically dominant in applied auditing. An earlier but complementary lineage grounds group fairness in *disparate impact*: \cite{feldman2015certifying} formalize disparate impact in the legal sense and propose a certification procedure for removing it from classifier predictions, bridging legal doctrine and machine learning practice.

A broader survey of classical ML fairness definitions, cataloging over twenty distinct bias sources across preprocessing, in-processing, and post-processing pipeline stages, is given by \cite{mehrabi2021survey}. \cite{barocas2023fairness} provide a textbook synthesis; \cite{caton2024fairness} offer a more recent CSUR survey of the formal field. That taxonomy serves as this survey's baseline vocabulary; we extend it into the agent components that condition what data reaches the model, how reasoning is structured, and how outputs are translated into consequential actions.

#### 2.1.2 Individual Fairness

Individual fairness is the criterion articulated by \cite{dwork2012fairness} as *fairness through awareness*: similar individuals, judged by a task-relevant similarity metric, should receive similar outcomes, regardless of group membership. This is the classical liberal intuition that like cases be treated alike. Dwork et al.'s paper is correctly characterized as an individual fairness result; it is *not* a source of the group fairness criteria above. The distinction matters: group fairness aggregates over distributions while individual fairness operates on pairs of individuals and requires specifying a task-appropriate similarity metric, a notoriously difficult design choice that has limited the criterion's empirical adoption relative to group-level metrics.

In agentic contexts, individual fairness generalizes naturally to trajectory pairs: two agents processing otherwise-identical applicant profiles that differ only in a protected attribute should reach the same decision via the same decision path. This trajectory-level generalization is rarely formalized in current evaluation practice. Counterfactual auditing methods such as the flip-rate designs of \cite{basu2026names} and \cite{mayilvaghanan2026counterfactual} are beginning to operationalize it.

#### 2.1.3 Counterfactual Fairness

Counterfactual fairness, introduced by \cite{kusner2017counterfactual}, shifts the framing from outcomes to causal mechanisms. A decision is fair toward an individual if it would remain the same in a counterfactual world in which that individual's protected attributes had taken different values, with all *descendants of those attributes in the causal graph* correspondingly intervened upon. More precisely: for an individual with attributes $(A=a, X=x)$, a predictor $\hat{Y}$ is counterfactually fair if $P(\hat{Y}_{A \leftarrow a}(U) = y \mid X=x, A=a) = P(\hat{Y}_{A \leftarrow a'}(U) = y \mid X=x, A=a)$ for all $y$ and all values $a'$. The key causal structure is that the intervention is on the protected attribute and propagates to its descendants in the causal DAG; non-descendants are held fixed. This differs from naive demographic substitution: attributes causally downstream of $A$ (an outcome shaped by historical discrimination, for instance) are also counterfactually altered, preventing the criterion from laundering discrimination through proxy variables.

This causal perspective is particularly consequential for agentic settings, where multi-step decision chains create long causal paths along which demographic signals can propagate and amplify. The Bias Conduction Framework (BCF) developed in Section 3.0 formalizes precisely this propagation structure.

#### 2.1.4 Impossibility Results and Metric Tensions

A critical finding for survey readers is that these three families are mutually *incompatible* under general conditions. \cite{kleinberg2017inherent} prove that three natural fairness criteria for risk scores (calibration within groups, balance for the positive class, and balance for the negative class) cannot simultaneously be satisfied except in degenerate cases. \cite{chouldechova2017fair} establishes a parallel impossibility: demographic parity, predictive parity (calibration), and equal false-positive and false-negative rates cannot all hold when base rates differ across groups, making the trade-off not a matter of technical ingenuity but of irreducible normative choice. These impossibility results mean that an agentic deployment *must* make fairness criterion choices that implicitly favor some groups over others; no criterion is neutral. \cite{pessach2022review} and \cite{tang2023what} survey these tensions in more depth.

For agent evaluation, the impossibility results carry a further implication: a system that satisfies group fairness on one metric may violate it on another, and a mitigation that improves counterfactual consistency may worsen demographic parity. The BCF framework's Proposition P4 (Mitigation-matching) addresses this directly by requiring that mitigations be keyed to the specific criterion and conduction signature of the target component, rather than applied globally.

---

### 2.2 LLM Bias: A Brief Inventory and the Agentic Gap

#### 2.2.1 Pre-Agentic Bias in LLMs

The past several years have produced a rich literature measuring bias in large language models as *generators*. \cite{gallegos2024bias} provide an authoritative survey of bias and fairness across the LLM lifecycle, covering stereotyping, toxicity, representational harm, and distributional disparities in generated text; \cite{chu2024fairness} offer a taxonomic treatment organized by fairness dimension and LLM task type, serving as the direct parent lineage for the present work. \cite{blodgett2020language} provide an earlier critical survey emphasizing that framing choices in bias detection encode normative assumptions that researchers must make explicit. \cite{navigli2023biases} catalog bias origins, taxonomize known bias types, and situate them within the broader discourse on responsible AI. \cite{buolamwini2018gender} supply the canonical empirical grounding: commercial gender classifiers exhibit substantially larger error rates for darker-skinned women than for lighter-skinned men, establishing that model-level demographic disparities have measurable real-world consequences before any agentic amplification occurs. \cite{caliskan2017semantics} establish that human-like social biases are present in word embeddings derived from language corpora, tracing the bias back to statistical regularities in training text.

Empirical measurement has been operationalized through benchmark families probing specific bias surfaces:

- **Coreference and gender stereotyping.** \cite{zhao2018gender} introduce WinoBias, pairs of coreference sentences that differ only in whether a gendered pronoun resolves to an occupationally stereotyped referent; \cite{rudinger2018gender} provide the WinoGender companion. Both benchmarks establish that coreference models systematically favor stereotypical assignments.

- **Ambiguous QA.** \cite{parrish2022bbq} (BBQ) uses ambiguous question-answering scenarios to surface stereotypical associations across nine social dimensions including age, race, religion, and disability. The benchmark is adversarially constructed so that a model relying on stereotypes answers differently from a model relying on context.

- **Open-ended generation.** \cite{dhamala2021bold} (BOLD) measures sentiment and regard disparities in open-ended generation conditioned on demographic group membership; \cite{nadeem2021stereoset} (StereoSet) evaluates the trade-off between language modeling ability and stereotypical bias; \cite{nangia2020crows} (CrowS-Pairs) surface biases favoring historically advantaged groups in masked language models; \cite{smith2022sorry} (HolisticBias) extend coverage to over 600 demographic descriptors across thirteen axes.

- **Toxicity.** \cite{gehman2020realtoxicityprompts} (RealToxicityPrompts) evaluate toxic degeneration in language models, showing that even neutral prompts can elicit harmful content with demographic targeting; \cite{hartvigsen2022toxigen} (ToxiGen) extend this to adversarially generated implicit hate speech.

- **Trustworthiness benchmarks.** \cite{wang2023decodingtrust} (DecodingTrust) provide a full assessment of trustworthiness in GPT models, including a fairness dimension alongside stereotyping, privacy, and adversarial robustness; \cite{liang2023holistic} (HELM) offer a broad evaluation framework covering accuracy, calibration, robustness, and bias across dozens of scenarios. \cite{huang2024trustllm} (TrustLLM) extend the trustworthiness assessment to a wide range of LLMs with fairness as a primary evaluation axis.

- **Bias origins and pitfalls.** \cite{blodgett2021stereotyping} audit fairness benchmark datasets and catalog recurring methodological pitfalls, establishing that measurement artefacts can mislead benchmark-based conclusions. This concern is taken up again in Section 2.7 (Threats to Validity).

This body of work has established that LLMs encode and reproduce social stereotypes, exhibit differential performance across demographic groups, and generate text with systematically unequal sentiment toward protected categories.

#### 2.2.2 Why QA-Level Evaluation Is Insufficient for Agents

All of the benchmarks above evaluate **single-turn language generation**: a prompt is supplied, a response is generated, and a fairness metric is computed over the token distribution. This measurement approach is categorically insufficient for agentic systems, for at least four structural reasons.

First, **sequential causation**: a demographic signal present in a user's profile may influence an early tool selection, which constrains subsequent information retrieval, which shapes a planning step that produces the final consequential decision. The bias does not appear in any single response but accumulates across the trajectory. Second, **persistent state**: memory modules, retrieved context, and conversation history create channels through which biased inferences carry forward across sessions, a mechanism absent from single-turn evaluation. Third, **external tools and APIs**: agents interact with external systems that may themselves encode biases in their outputs, creating harm attributable not to the LLM's parameters but to the LLM's tool-selection policy. Fourth, and decisively, **the action-answer gap**: \cite{li2025actions} demonstrate that agent *decisions* reveal implicit biases invisible at the verbal-output level. A model can emit neutral text while simultaneously issuing actions with demographic disparity. BBQ can detect that a model answers a stereotyped question incorrectly; it cannot detect that a hiring agent systematically routes applicants with certain name patterns to lower-quality resume-screening tools.

This measurement gap is the central observation of this survey. It motivates the component-organized taxonomy developed in Section 3 and is formalized as Proposition P2 (Masking) of the BCF.

---

### 2.3 What Is an LLM-Based Agent? Component Anatomy

An LLM-based agent is a system in which a large language model serves as the core reasoning engine within an architecture that supports autonomous, multi-step interaction with external environments \cite{wang2024survey, xi2023rise}. The cognitive architectures survey by \cite{sumers2024cognitive} provides a systematic framework for decomposing these systems into functional constituents; \cite{guo2024large} survey the progress and challenges of multi-LLM agent systems; \cite{durante2024agent} survey multimodal agent interaction. We adopt the formal characterization developed in Section 3.0, treating an agent as a tuple $\langle \pi, T, M, R \rangle$ where $\pi$ is the policy, $T$ is the tool set, $M$ is the memory module, and $R$ is the reward or stopping signal, as the definition against which component-level fairness properties are measured.

The ReAct framework \cite{yao2023react} interleaves chain-of-thought reasoning with tool calls; Toolformer \cite{schick2023toolformer} demonstrates self-supervised tool use; RAG \cite{lewis2020retrieval} grounds generation in retrieved documents; AutoGen \cite{wu2023autogen} and MetaGPT \cite{hong2024metagpt} enable multi-agent delegation and orchestration; generative agent simulations \cite{park2023generative} demonstrate emergent social behavior from agent interaction; Reflexion \cite{shinn2023reflexion} accumulates verbal self-reflections as episodic memory.

We identify six components whose design choices are consequential for fairness, grouped by their primary role in the agent loop:

**Component 1: Tool and API selection.** The agent chooses, at each step, which external tool, API, retriever, or knowledge source to invoke. This choice is a learned behavior conditioned on contextual signals, including potentially demographic signals in the query or retrieved context \cite{blankenstein2025biasbusters}. Tool-selection policy is therefore a locus of discriminatory routing, independently of the final answer quality.

**Component 2: Memory and retrieval.** Agents maintain in-context history and external memory stores indexed for retrieval \cite{lewis2020retrieval}. The retrieval function's ranking can encode demographic disparities, and the model then generates conditioned on a potentially biased information set. Accumulation over turns adds a temporal dimension \cite{fan2024fairmt}.

**Component 3: Multi-agent orchestration and delegation.** Modern deployments distribute tasks across networks of specialized agents \cite{wu2023autogen, park2023generative}. Role assignment is a direct channel for bias: if persona or role assignment correlates with protected attributes, downstream behaviors of the assigned agent differ systematically \cite{gupta2023bias, nguyen2025social}.

**Component 4: Planning and task decomposition.** Agents decompose high-level goals into subtask sequences, often via chain-of-thought or structured planning. The ordering and framing of subtasks can encode implicit assumptions about whose needs are primary, assumptions that may vary systematically by demographic context \cite{li2025actions, wu2025reasoning}.

**Component 5: User modeling and personalization.** Agents adapt to individual users by inferring preferences, expertise, and identity from interaction history or profile data \cite{kantharuban2024stereotype}. This adaptive capacity creates a personalization-stereotyping tension: inferences that improve average-case utility for a group may simultaneously instantiate harmful stereotypes for individual users who deviate from that group's statistical profile.

**Component 6: Long-horizon trajectory execution.** Over extended multi-turn interactions or autonomous task executions, small per-step biases can compound into large cumulative disparities \cite{ma2026implicit, wyllie2024fairness}. This longitudinal dimension is not captured by any existing single-turn benchmark and constitutes the most undertheorized component in current fairness research.

These six components form the organizing axis of the taxonomy in Section 3. The BCF framework formalizes how bias propagates across them. Two classes of agent evaluation benchmarks assess the broader capabilities of agents without a fairness lens, and both must be acknowledged here: WebArena \cite{zhou2024webarena}, AgentBench \cite{liu2024agentbench}, SWE-bench \cite{jimenez2024swe}, and Mind2Web \cite{deng2023mind2web} evaluate task completion in realistic environments and could, in principle, be demographically instrumented; their current designs do not include demographic counterfactual conditions, which is precisely the gap Section 4.3 formalizes as action-level disparity metrics.

---

### 2.4 Scope and Coverage Decisions

**Survey scope.** This survey covers empirical and theoretical research on unfairness and inequity arising specifically within the architecture of LLM-based agent systems, meaning systems performing multi-step, tool-augmented, or multi-agent reasoning toward a goal in a consequential domain. We do not survey the broader literature on bias in static LLM generation except insofar as those findings illuminate mechanisms operative in agentic settings; that literature is ably synthesized by \cite{gallegos2024bias} and \cite{chu2024fairness}. We exclude non-LLM agents (classical planning systems, reinforcement learning agents without LLM backbones), though we draw on classical fair sequential decision-making results \cite{hu2022achieving, xu2024adapting} where they provide theoretical grounding, and on recommender-system fairness \cite{zehlike2022fairness, wang2023survey} where the feedback-loop dynamics parallel agentic deployment.

**Inclusion criteria.** A paper was included if it satisfied all of the following: (i) the system studied uses an LLM as a primary reasoning component; (ii) the paper addresses bias, fairness, equity, or disparate treatment in outcomes or behaviors; (iii) the paper's findings bear on at least one of the six agent components identified above, or on the evaluation or mitigation of bias in such components. Papers exclusively studying static generation tasks without an agentic framing were included only when the mechanism they document is demonstrably operative in agentic settings; such papers are marked *[adjacent evidence, transferred]* in the coverage table (Table 1, §3 header). Papers from non-LLM recommender systems or classical ML fairness were included only when directly cited by the agent fairness literature or when they provide the only available formal grounding for a mechanism.

**Multi-tagging convention.** A paper may be tagged to multiple components when its findings are mechanistically relevant to each. The coverage matrix in §7 counts such papers in each tagged cell; the total of unique papers is 201. Papers that cross-cut four or more sections (e.g., \cite{gallegos2024bias} ×4, \cite{fan2024fairmt} ×3) are counted once in the unique total.

---

### 2.5 Systematic Search and Corpus Construction

#### 2.5.1 Search Protocol

The corpus was assembled through a systematic multi-branch search following PRISMA-style conventions \cite{moher2009preferred}. Search queries were issued across the following databases: arXiv (cs.AI, cs.CL, cs.LG, cs.IR), ACL Anthology, ACM Digital Library, NeurIPS/ICML/ICLR proceedings archives, FAccT proceedings, AAAI proceedings, and IEEE Xplore, supplemented by forward and backward citation chasing from anchor papers. Searches were conducted between January 2026 and June 2026; the literature cutoff date is **June 10, 2026**. Papers published after that date are not included.

Each of the seven taxonomy branches received a dedicated search string constructed from the intersection of (a) an agent/agentic qualifier and (b) a fairness/bias qualifier, with branch-specific terms. The eighth branch (foundations and adjacent evidence) was populated by backward citation chasing from the agent-fairness corpus rather than independent search.

**Table 2.1 — Search Protocol by Branch.** *Takeaway: the branch structure maps directly onto the six BCF entry loci plus evaluation and mitigation; no branch has fewer than 10 identified records before deduplication.*

| Branch | Primary Search String | Supplementary Terms | Databases | Records Identified | After Dedup | After Screen | Included |
|---|---|---|---|---|---|---|---|
| Tool/API selection | "tool selection bias" OR "tool use fairness" LLM agent | tool-calling, function-calling, API bias, routing bias | arXiv, ACL, ACM DL | 47 | 34 | 18 | 12 |
| Memory & retrieval | RAG fairness OR "retrieval bias" LLM | retrieval-augmented, knowledge store, context accumulation, multi-turn bias | arXiv, ACL, ACM DL, SIGIR | 52 | 38 | 16 | 10 |
| Multi-agent delegation | "multi-agent bias" OR "role assignment bias" LLM | persona bias, delegation fairness, emergent bias, agent interaction | arXiv, ACL, ACM DL, AAAI | 41 | 31 | 14 | 9 |
| Planning/decomposition | "reasoning bias" LLM agent OR "planning fairness" | chain-of-thought bias, task allocation, decomposition disparity | arXiv, ACL, ICML | 28 | 21 | 9 | 6 |
| User modeling/personalization | "personalization bias" LLM OR "user modeling fairness" | name-based bias, dialect fairness, stereotype personalization | arXiv, ACL, ACM DL | 44 | 33 | 15 | 11 |
| Long-horizon drift | "long-term fairness" LLM OR "feedback loop bias" agent | sycophancy drift, memory accumulation, sequential fairness | arXiv, AAAI, ICML, FAccT | 38 | 29 | 12 | 9 |
| Evaluation & benchmarks | "agent fairness benchmark" OR "fairness evaluation LLM agent" | counterfactual evaluation, action-level disparity, audit | arXiv, ACL, ACM DL, NeurIPS | 61 | 44 | 22 | 16 |
| Mitigation | "LLM debiasing agent" OR "fairness mitigation agentic" | RLHF fairness, RAG debiasing, prompt debiasing, constitutional AI | arXiv, ACL, NeurIPS, AAAI | 55 | 40 | 17 | 13 |
| Foundations (backward chase) | — | Parent surveys, impossibility results, classical ML fairness | All databases + Google Scholar | 93 | 74 | 61 | 45 |
| High-stakes domains | "LLM hiring bias" OR "LLM clinical fairness" OR "LLM lending bias" | resume screening, medical decision, credit, education, judicial | arXiv, Nature, EMNLP, PNAS | 48 | 36 | 19 | 13 |
| Prior-art additions | Neighbor survey search: ranjan2025, binkyte2025, ebrahimi2025 + forward chain | adjacent CSUR trustworthy-AI surveys | ACM DL, arXiv, ResearchGate | 41 | 35 | 31 | 29 |
| **Total** | | | | **548** | **415** | **234** | **201** (unique) |

*Note: rows do not sum to 201 because papers appearing in multiple branches are deduplicated at the final stage; the multi-tag convention is applied after inclusion decisions are finalized.*

#### 2.5.2 PRISMA Flow (Figure 0)

The corpus assembly followed four stages:

**Stage 1: Identification (n = 548).** Database searches across the branches above yielded 548 candidate records, including duplicates across branches.

**Stage 2: Deduplication (n = 415).** After removing records identified in multiple branch searches, 415 unique records remained.

**Stage 3: Screening (n = 234).** Title and abstract screening applied the inclusion criteria from §2.4: (i) LLM as primary reasoning component; (ii) addresses bias, fairness, equity, or disparate treatment; (iii) findings bear on at least one of the six agent components or on evaluation/mitigation thereof. Records failing criterion (i) (e.g., classical NLP, non-LLM agents) or criterion (ii) (e.g., capability benchmarks without fairness content) were excluded at this stage. Records passing abstract screen proceeded to full-text review. Exclusion reasons at this stage: non-LLM system (81 records), no fairness content (73 records), duplicate venue version (27 records).

**Stage 4: Inclusion (n = 201).** Full-text review confirmed inclusion criteria and assigned branch tags. Records excluded at this stage failed criterion (iii), typically single-turn generation studies with no agentic framing, or were superseded by a more recent version of the same work. The final corpus comprises 201 unique papers spanning 2015 to 2026.

*Figure 0 — PRISMA Flow Diagram* renders this four-stage funnel with counts at each node and branching reason labels. *Takeaway: the corpus construction is transparent and reproducible; the 201 included papers represent systematic coverage rather than convenience selection.*

#### 2.5.3 Inclusion/Exclusion Criteria Summary

**Table 2.2 — Inclusion and Exclusion Criteria.** *Takeaway: the criteria operationalize a single principle — fairness as a property of agent actions, not merely of model outputs.*

| Criterion | Included | Excluded |
|---|---|---|
| System type | LLM as primary reasoning component (including fine-tuned variants) | Classical NLP models, RL agents without LLM backbone, symbolic planners |
| Fairness content | Studies bias, fairness, equity, or disparate treatment in outcomes or behavior | Pure capability evaluation, no fairness angle |
| Agent component relevance | Findings bear on at least one of the six components, or on evaluation/mitigation thereof | Exclusively single-turn static generation with no agentic framing; included only if mechanism transfers to agentic settings (marked *[adjacent]*) |
| Language | English-language papers | Non-English (pragmatic exclusion; acknowledged as limitation in §2.7) |
| Temporal scope | Published or preprinted on or before June 10, 2026 | Post-cutoff publications |
| Availability | Full text accessible | Extended abstracts only, inaccessible preprints |

---

### 2.6 Temporal and Venue Distribution

#### 2.6.1 Publication Trend

The agent fairness literature is a recent and rapidly growing subfield. Of the 201 corpus papers, **5 (2%)** predate 2020 (primarily foundational ML fairness and NLP bias work), **22 (11%)** fall in 2020 to 2022, **36 (18%)** in 2023, **78 (39%)** in 2024, and **60 (30%)** in 2025 to 2026 (through June cutoff). The combined 2024 to 2026 cohort constitutes **69%** of the corpus, reflecting the field's rapid emergence following the widespread deployment of instruction-tuned and tool-augmented LLMs.

Three inflection events are visible in the component-level publication trajectory:

1. **ReAct (late 2022, published ICLR 2023 \cite{yao2023react}).** The formalization of reasoning-and-acting brought agentic behavior into mainstream NLP evaluation. A measurable uptick in tool-selection and planning fairness papers appears in the 2023 to 2024 cohort, as researchers applied bias probing to the new approach.

2. **AutoGen and GPT-4 function-calling (2023 \cite{wu2023autogen}).** The accessibility of multi-agent orchestration and native function-calling APIs catalyzed the multi-agent delegation fairness literature, which is almost entirely 2024 to 2026.

3. **GPT-4 and the clinical deployment wave (2023 to 2024).** The application of frontier models to clinical decision support \cite{omar2025sociodemographic, poulain2024bias, zack2024coding} triggered a wave of domain-specific fairness audits that now constitute the high-stakes-domains branch.

The long-horizon drift and memory components are the *latest* to receive empirical attention: the first dedicated papers on LLM long-term memory bias (\cite{ma2026implicit}) and feedback-loop amplification (\cite{wyllie2024fairness, wang2026observations}) date to 2024 to 2026. This temporal lag is itself informative. The components that are hardest to evaluate, because they require multi-session or multi-turn experimental designs, have attracted attention last.

#### 2.6.2 Venue Distribution

The corpus spans twelve venue categories. The five largest are: arXiv preprints (62 papers, 31%), ACL-family venues (ACL, EMNLP, NAACL, Findings) (41 papers, 20%), NeurIPS/ICML/ICLR (28 papers, 14%), ACM venues (FAccT, SIGKDD, SIGIR, CIKM, DL proceedings) (24 papers, 12%), and domain-specific venues (Nature Medicine, PNAS Nexus, The Lancet Digital Health, AAAI, ICSE) (19 papers, 9%). The remaining 27 papers (14%) appear in IEEE venues, TMLR, Frontiers, and preprint archives (ResearchGate, TechRxiv).

Several observations follow. First, the arXiv share is high (31%), reflecting the recency of the field: many 2025 to 2026 papers are under review or in proceedings preparation. Second, the ACM FAccT representation (9 papers) is lower than the field's importance would suggest, indicating that agent fairness has not yet been fully claimed by the accountability community; it currently sits across NLP venues, systems venues, and domain journals. Third, 10 papers appear in CSUR or ACM Computing Surveys directly, indicating that the survey genre has begun to engage this territory, and the differentiation analysis in §1.4 and Table 0 is therefore essential to establishing the present survey's novelty.

---

### 2.7 Glossary and Notation

The following terms and notation are used throughout this survey. Terms coined or given specific technical meanings here are marked with a dagger (†).

**Agent loop** $\langle \pi, T, M, R \rangle$: the formal object of analysis in the BCF (Definition D1, §3.0). $\pi$ = policy (the LLM-backed decision function), $T$ = tool set, $M$ = memory module (in-context + external), $R$ = reward/stopping signal.

**Bias Conduction Framework (BCF)†**: the organizing framework of this survey (§3.0), which analyzes fairness as a property of how demographic disparity is *conducted* (attenuated, preserved, amplified, or generated) across pipeline edges in an agent loop.

**Conduction operator $\phi$†**: the scalar multiplier describing how a pipeline edge transforms component-level disparity. $\phi < 1$ = ATTENUATE; $\phi \approx 1$ = PRESERVE; $\phi > 1$ = AMPLIFY; $\phi$ acting on zero input = GENERATE.

**Counterfactual Flip Rate (CFR)**: the fraction of agent evaluations that reverse when the input is perturbed by a demographic swap alone \cite{mayilvaghanan2026counterfactual}. Generalized to any agent component in §4.2.

**Mean Absolute Score Difference (MASD)**: the mean absolute change in a continuous agent score (confidence, rank, quality rating) across counterfactual pairs \cite{mayilvaghanan2026counterfactual}.

**Component counterfactual disparity $\Delta_c$†**: the counterfactual disparity attributable to component $c$ alone, measured via trace-replay (Definition D2, §3.0).

**Trajectory disparity $\Delta_\tau$†**: the total counterfactual disparity observed over a complete agent trajectory, approximated by the conduction equation $\Delta_\tau \approx \sum_c \Delta_c \cdot \prod_{e > c} \phi_e$ with feedback recurrence $\Delta^{(t+1)} = \phi_{\text{fb}} \cdot \Delta^{(t)} + \Delta_{\text{entry}}$.

**Agentic multiplier (P3, Super-additivity)†**: the BCF proposition that trajectory disparity can exceed the sum of component disparities when amplifying conduction operators compose; equivalently, the agent pipeline is a super-additive bias transformer.

**Action-level disparity†**: disparity measured over an agent's *actions* (tool invocations, decisions, escalations) rather than over its textual output. Formalized in §4.3 as tool-invocation disparity, escalation-rate disparity, and plan-allocation disparity.

**Long-horizon fairness drift†**: the temporal degradation or amplification of fairness properties across turns, sessions, or deployment feedback cycles, even when the per-step model is held fixed.

**Adjacent evidence [transferred]**: notation used in Tables 1 and 4 to flag papers from non-agentic settings whose documented mechanism is asserted to operate in agentic settings; the transfer argument is given in the relevant §3.x entry.

**CFR subscript notation**: $\text{CFR}_c$ denotes the counterfactual flip rate measured at component $c$; $\text{CFR}_\tau$ denotes the end-to-end trajectory flip rate.

---

### 2.8 Threats to Validity of This Survey

Any systematic survey carries validity threats that should be made explicit. We identify four categories.

#### 2.8.1 Selection Bias

The corpus was assembled primarily from English-language papers indexed in arXiv, ACL Anthology, and ACM Digital Library. Non-English research, including substantial work from Chinese NLP venues on Chinese LLM fairness, is systematically underrepresented. Similarly, industry research that is not publicly disclosed is absent. The arXiv-heavy composition (31%) means the corpus captures working papers that have not yet completed peer review; some may be revised or retracted. We mitigate this by requiring that preprints be self-consistent and that their core claims be supported by the experimental design reported.

The search strategy was branch-structured, which creates a risk that papers addressing multiple components simultaneously are attributed primarily to the branch under which they were first encountered. The multi-tagging convention (§2.4) partially addresses this, but papers at the intersection of underrepresented branch pairs (e.g., tool-selection × long-horizon) may be missed if neither branch search used terms that surface the intersection.

#### 2.8.2 Construct Validity

The six component taxonomy is a construct, not a natural kind. Some bias phenomena do not fit cleanly into a single component: a persona-conditioned retrieval agent collapses Components 1, 2, and 5 into a single mechanism. The component-assignment rules in §3.0 adopt a *proximate cause* convention, tagging a paper to the component that is the most proximate locus of the reported disparity, but this convention involves judgment. Readers who categorize a boundary paper differently from this survey's assignment will find that cell counts in the coverage matrix shift slightly; the qualitative conclusions (empty counterfactual column, unspecified-dominated rows for tool/memory/personalization) are reliable under reasonable reassignments.

#### 2.8.3 Publication Bias

Positive findings are more likely to be published and more likely to be submitted to the high-visibility venues this search prioritizes. Null results, meaning LLM agents that show no meaningful fairness disparity across components, are underrepresented in the corpus. This creates a systematically alarming picture: the corpus is weighted toward papers that find and document disparities, not papers that find none. Readers should interpret the corpus as establishing that disparity *can* and *does* occur at each component, not that it *always* occurs or that it is comparably severe across deployment contexts.

#### 2.8.4 Recency Bias

The 69% concentration of papers in 2024 to 2026 means the survey reflects a rapidly changing field. Findings from 2024 papers may already have been partially addressed by 2026 mitigations not yet captured in the corpus. Conversely, the long-horizon and multi-agent components, where empirical papers are newest and most sparse, may have received substantially more attention by the time this survey reaches print, making the "open edge" assessments in §3.x optimistic. We treat this as a motivating condition, not a confound: the survey's goal is to provide a structured framework for the field's future development, not to give a final accounting of a stable literature.
