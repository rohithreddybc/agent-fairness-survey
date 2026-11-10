# Adjudication log: dual-coded corpus extension

Adjudicator: Claude Opus, 2026-11-09, from title, abstract, date and venue plus `CODEBOOK.md` only (no web search).
Coder A = Claude Sonnet, coder B = GPT-6.1. One row per field on which the coders differed, plus hard-constraint fixes.
Fields both coders agreed on were kept. Where a field was decided for A or B, that coder's evidence string was kept.
BORDERLINE is not used as a final verdict; `was_borderline` in `screen_final.jsonl` records records where either coder said BORDERLINE.

Secondary-branch rule applied throughout (the codebook gives no threshold for a *secondary* `evaluation` tag): `evaluation` applies when the abstract presents a benchmark, dataset, metric or audit/assessment method as the paper's own contribution, not when it only reports measurements.

## Screening

| Record | Field | A | B | Final | Rationale | Deciding quote |
|---|---|---|---|---|---|---|
| 2407.06866 | secondary_branches | `[]` | `["evaluation"]` | `[]` | No benchmark, dataset, metric or audit method is presented as a contribution; the paper studies one model's guardrails, so `evaluation` does not also apply (A7). | "This paper studies how contextual information about the user influences the likelihood of an LLM to refuse to execute a request" |
| 2410.19803 | secondary_branches | `["evaluation"]` | `["evaluation", "mitigation"]` | `["evaluation"]` | The mitigation is an observed effect of existing RL post-training, not an intervention the paper contributes, so `mitigation` does not apply (A7.2). | "We highlight that post-training reinforcement learning techniques significantly mitigate these biases" |
| 2501.04316 | primary_branch | `"C2"` | `"C1"` | `"C2"` | The retrieval disparity lies in which resumes the retriever returns and ranks, i.e. what the invoked resource returns (R1, C2 row 'ranked passages'); no finding concerns which tool or source is invoked (C1). | "Models also display non-uniform retrieval selection patterns across demographic groups" |
| 2501.04316 | locus_tags | `["C2"]` | `["C1", "C2"]` | `["C2"]` | Same as primary: R1 assigns returned and ranked content to C2; no C1 selection among resources is measured. | "Models also display non-uniform retrieval selection patterns across demographic groups" |
| 2501.04316 | secondary_branches | `["high-stakes"]` | `["evaluation", "high-stakes"]` | `["high-stakes"]` | Hiring is a high-stakes domain; the synthetic resume dataset is a means of the audit, not a presented benchmark, so `evaluation` does not apply. | "high-stakes applications like hiring" |
| 2502.17945 | secondary_branches | `[]` | `["evaluation"]` | `[]` | A descriptive analysis with no benchmark, dataset, metric or audit method presented as a contribution. | "We quantify bias in model-generated scores and assess the impact of demographic factors" |
| 2503.15454 | secondary_branches | `["evaluation", "mitigation"]` | `["evaluation", "mitigation", "high-stakes"]` | `["evaluation", "mitigation", "high-stakes"]` | Answers for clinical decision support are audited for demographic disparity, a clinical decision domain named in A7.4, so `high-stakes` also applies. | "Medical Question Answering systems based on Retrieval Augmented Generation is promising for clinical decision support" |
| 2504.08260 | transfer_clause_used | `false` | `true` | `true` | Persona-prompted digital twins answer a survey in a single turn; a persona as fairness object meets iii only through the clause (A4; supp S6). | "Using demographic-based prompt engineering, we create digital twins of survey respondents" |
| 2505.11861 | verdict | `"EXCLUDE"` | `"BORDERLINE"` | `"EXCLUDE"` | No disparate treatment of a group of people is measured; the dataset maps persona preferences on equity topics and positions LLMs in a preference space, which is ideological positioning, not bias against a group (A5). | "analysis of the positioning of the existing mainstream LLMs across five major global regions within the personalized preference space" |
| 2505.11861 | transfer_clause_used | `false` | `true` | `false` | Excluded at ii; the clause is not reached. | (default value) |
| 2505.11861 | primary_branch | `null` | `"C3"` | `null` | EXCLUDE carries null (A3.6). | (default value) |
| 2505.11861 | locus_tags | `[]` | `["C3"]` | `[]` | EXCLUDE carries [] (A3.6). | (default value) |
| 2505.11861 | secondary_branches | `[]` | `["evaluation"]` | `[]` | EXCLUDE carries [] (A3.6). | (default value) |
| 2506.04253 | verdict | `"EXCLUDE"` | `"INCLUDE_TOPICAL"` | `"EXCLUDE"` | Architecture paper; ZIP-code bias is one of six walkthrough objectives, so fairness is listed, not studied (A1, false-positive pattern 2). | "every role could invoke conversational control, trace KPIs and value constraints, detect and mitigate ZIP-code bias" |
| 2506.04253 | deciding_criterion | `"ii"` | `"all_met"` | `"ii"` | Criterion ii is the lowest failing criterion. | "detect and mitigate ZIP-code bias" |
| 2506.04253 | primary_branch | `null` | `"C3"` | `null` | EXCLUDE carries null. | (default value) |
| 2506.04253 | locus_tags | `[]` | `["C3"]` | `[]` | EXCLUDE carries []. | (default value) |
| 2506.04253 | secondary_branches | `[]` | `["mitigation", "high-stakes"]` | `[]` | EXCLUDE carries []. | (default value) |
| 2506.04419 | transfer_clause_used | `true` | `false` | `false` | The audit runs on a deployed LLM chatbot in multi-turn conversations, so the work is not single-turn static generation and iii is met directly. | "facilitates multi-turn conversations" |
| 2506.13245 | secondary_branches | `["mitigation"]` | `["evaluation", "mitigation"]` | `["evaluation", "mitigation"]` | Two new quantitative metrics are a stated contribution, so `evaluation` also applies. | "We further propose two quantitative metrics, Perplexity-based Acceptence and Values Self-Consistency, to assess consensus outcomes" |
| 2508.08837 | verdict | `"BORDERLINE"` | `"EXCLUDE"` | `"EXCLUDE"` | The object is simulated attitudes toward a country (geopolitical opinion), not disparate treatment of a group of people; A5 places ideological lean outside ii. | "models U.S. citizens' attitudes toward China from 2005 to 2025" |
| 2508.08837 | primary_branch | `"C3"` | `null` | `null` | EXCLUDE carries null. | (default value) |
| 2508.08837 | locus_tags | `["C3", "T"]` | `[]` | `[]` | EXCLUDE carries []. | (default value) |
| 2508.08837 | secondary_branches | `["mitigation"]` | `[]` | `[]` | EXCLUDE carries []. | (default value) |
| 2508.10906 | verdict | `"BORDERLINE"` | `"INCLUDE_TOPICAL"` | `"INCLUDE_TOPICAL"` | The abstract reports demographic parity assessments of generated responses and fairness metrics, a measured fairness question about people, so ii is met. | "dedicated demographic parity assessments, ensuring that generated responses remain accurate and unbiased" |
| 2508.10906 | deciding_criterion | `"ii"` | `"all_met"` | `"all_met"` | All criteria met. | "dedicated demographic parity assessments, ensuring that generated responses remain accurate and unbiased" |
| 2508.10906 | transfer_clause_used | `false` | `true` | `true` | Single-prompt persona conditioning; a persona fairness object meets iii through the clause (A4; supp S6). | "a multi-tier prompt conditioning framework that builds adaptive digital twins by integrating demographic, behavioral, and psychometric data" |
| 2509.21080 | transfer_clause_used | `false` | `true` | `true` | The measured disparity comes from a role assigned to an LLM in single-response script generation; a role-assignment fairness object meets iii through the clause (supp S6). The agent framework appears only as a mitigation. | "an LLM is positioned as a reporter interviewing local people across 10 diverse cultures" |
| 2510.09905 | secondary_branches | `["mitigation"]` | `["evaluation", "mitigation"]` | `["mitigation"]` | Evaluation uses existing tests; the curated dataset serves the mitigation, so only `mitigation` applies. | "evaluating 15 models on human-validated emotional intelligence tests" |
| 2511.04076 | verdict | `"BORDERLINE"` | `"INCLUDE_TOPICAL"` | `"EXCLUDE"` | The fairness object is partisan advantage between opposing political interests, not a group defined by a protected attribute, culture, language variety or national origin (A5). CODEBOOK GAP: A5 does not say whether partisan voter groups count. | "a turn-based negotiation between two agents representing opposing political interests" |
| 2511.04076 | deciding_criterion | `"ii"` | `"all_met"` | `"ii"` | Criterion ii is the lowest failing criterion. | "partisan actors to cherry-pick maps that, while technically compliant, are politically advantageous" |
| 2511.04076 | primary_branch | `"C3"` | `"C4"` | `null` | EXCLUDE carries null. | (default value) |
| 2511.04076 | locus_tags | `["C3"]` | `["C3", "C4"]` | `[]` | EXCLUDE carries []. | (default value) |
| 2511.04076 | secondary_branches | `[]` | `["mitigation", "high-stakes"]` | `[]` | EXCLUDE carries []. | (default value) |
| 2511.06148 | locus_tags | `["C4", "T"]` | `["C4"]` | `["C4", "T"]` | Biases develop from experience over a sequential exploration task, a finding indexed by time, so the locus (C4) and T are both tagged (R4). | "LLMs are not merely passive mirrors of human social biases, but can actively create new ones from experience" |
| 2511.06148 | secondary_branches | `["mitigation"]` | `["evaluation", "mitigation"]` | `["mitigation"]` | Uses an existing psychology paradigm; no benchmark or metric contribution, so only `mitigation` applies. | "Using a paradigm from the psychology literature" |
| 2511.11772 | secondary_branches | `["mitigation"]` | `["evaluation", "high-stakes"]` | `["mitigation", "high-stakes"]` | The Equity Monitor agent is a bias-reducing intervention (`mitigation`) and scoring learners is an education decision about people (`high-stakes`, A7.4); the fairness checks are a system feature, not a benchmark contribution. | "uses five coordinated role-based LLM agents (Evaluator, Equity Monitor, Metacognitive Coach, Aggregator, and Reflexion Reviewer) to score learner reflections" |
| 2512.16532 | secondary_branches | `["high-stakes"]` | `["evaluation", "high-stakes"]` | `["high-stakes"]` | A simulation study with no benchmark, dataset, metric or audit method presented as a contribution. | "we simulate the behavior of a memory-enhanced personalized agent" |
| 2512.19735 | transfer_clause_used | `false` | `true` | `false` | CAP conditions each prediction on retrieved similar historical cases, a C2 retrieval-conditioned emission measured directly (B4), so iii does not rest on the clause. | "further guides models using similar historical misprediction cases paired with correct outcomes to correct biased reasoning" |
| 2512.19735 | secondary_branches | `["mitigation", "high-stakes"]` | `["evaluation", "mitigation", "high-stakes"]` | `["evaluation", "mitigation", "high-stakes"]` | A multi-dimensional bias assessment scheme is a stated contribution, so `evaluation` applies alongside mitigation and the clinical high-stakes domain. | "We first design a multi-dimensional bias assessment scheme to identify subgroup disparities" |
| 2601.17492 | verdict | `"BORDERLINE"` | `"BORDERLINE"` | `"EXCLUDE"` | Both coders said BORDERLINE, which is not a final verdict. The abstract names no group of people or sensitive attribute; 'fairness issues' and 'diverse or emerging biases' may be item-side, so ii is not shown to be met. CODEBOOK GAP: no rule for resolving an unsettled ii. | "lack the generality to handle diverse or emerging biases in real-world applications" |
| 2601.17492 | primary_branch | `"C5"` | `"C5"` | `null` | EXCLUDE carries null (hard constraint, fixed). | (default value) |
| 2601.17492 | locus_tags | `["C5"]` | `["C5"]` | `[]` | EXCLUDE carries [] (hard constraint, fixed). | (default value) |
| 2601.17492 | secondary_branches | `["mitigation"]` | `["mitigation"]` | `[]` | EXCLUDE carries [] (hard constraint, fixed). | (default value) |
| 2603.18729 | locus_tags | `["C3", "C5"]` | `["C3"]` | `["C3"]` | The dialect finding is a single-response stereotype attribution with the cue in the prompt; no user model changes personalized output, so C5 does not apply (A4; A7 no-locus rule). C3 rests on the multi-agent architectures. | "suggested names, jobs, and adjectives for SAE or AAE speakers" |
| 2603.18729 | secondary_branches | `["mitigation"]` | `["evaluation", "mitigation"]` | `["mitigation"]` | Replicates existing analyses; no benchmark or metric contribution, so only `mitigation` applies. | "we replicate existing analyses of dialect-sensitive stereotype generation in LLM outputs" |
| 2604.09620 | verdict | `"BORDERLINE"` | `"INCLUDE_TOPICAL"` | `"INCLUDE_TOPICAL"` | Candidates are discriminated in hiring outcomes for a non-merit attribute, a fairness question about people rather than a technical bias of the judge (A5; adjudication memo). CODEBOOK GAP: A5 does not list attitude-defined groups. | "resume screeners tend to favor candidates with positive or non-critical attitudes toward AI, discriminating skeptical, human-centered counterparts" |
| 2604.09620 | deciding_criterion | `"ii"` | `"all_met"` | `"all_met"` | All criteria met. | "resume screeners tend to favor candidates with positive or non-critical attitudes toward AI" |
| 2604.09620 | secondary_branches | `["mitigation"]` | `["evaluation", "mitigation", "high-stakes"]` | `["evaluation", "mitigation", "high-stakes"]` | Introduces a two-phase simulation pipeline (audit method), proposes Merit-Attitude Factorization (mitigation), and audits resume screening (hiring, high-stakes). | "We introduce a two-phase simulation pipeline that first isolates AI-trust preference in qualification-matched resume screening" |
| 2605.12530 | verdict | `"INCLUDE_TOPICAL"` | `"BORDERLINE"` | `"INCLUDE_TOPICAL"` | Disparate treatment is measured as identity varies within multi-agent conversation, a fairness question about people, so ii is met. | "examining how models' disparate-treatment behaviors shift when identity is varied as part of natural multi-agent conversation" |
| 2605.12530 | deciding_criterion | `"all_met"` | `"ii"` | `"all_met"` | All criteria met. | "examining how models' disparate-treatment behaviors shift when identity is varied" |
| 2605.25200 | verdict | `"EXCLUDE"` | `"INCLUDE_TOPICAL"` | `"EXCLUDE"` | Fairness is one utility-balancing capability among group members' preferences in a capability benchmark; no group of people defined by a protected attribute is studied (A1 pattern 2; A5). | "planning} that balances group utility against fairness" |
| 2605.25200 | deciding_criterion | `"ii"` | `"all_met"` | `"ii"` | Criterion ii is the lowest failing criterion. | "balancing utility against fairness" |
| 2605.25200 | primary_branch | `null` | `"C4"` | `null` | EXCLUDE carries null. | (default value) |
| 2605.25200 | locus_tags | `[]` | `["C4"]` | `[]` | EXCLUDE carries []. | (default value) |
| 2605.25200 | secondary_branches | `[]` | `["evaluation"]` | `[]` | EXCLUDE carries []. | (default value) |
| doi:10.3390/math14030458 | secondary_branches | `["mitigation"]` | `["evaluation", "mitigation"]` | `["mitigation"]` | The buyer-seller game is employed as a study design, not presented as a benchmark or audit method, so only `mitigation` applies. | "Evaluating Fairness in LLM Negotiator Agents via Economic Games Using Multi-Agent Systems" |

## Entry coding (existing corpus)

| Record | Field | A | B | Final | Rationale | Deciding quote |
|---|---|---|---|---|---|---|
| fan2024fairmt / C2 | demographic | `"yes"` | `"no"` | `"yes"` | A fairness benchmark built from fairness datasets on bias attributes of people; the abstract names marginalized communities (B5; Part D). | "harm to marginalized communities" |
| fan2024fairmt / T | demographic | `"yes"` | `"no"` | `"yes"` | As for the C2 entry (one undifferentiated finding, B1). | "harm to marginalized communities" |
| gupta2023bias / C3 | operator | `"GENERATE"` | `"UNCHARACTERIZED"` | `"GENERATE"` | Two points: no stereotyping when asked explicitly and a no-persona baseline (a demographically clean condition) versus persona-induced performance drops, so GENERATE (B3 table; step 4). | "they overtly reject stereotypes when explicitly asked" |
| gupta2023bias / C4 | operator | `"GENERATE"` | `"UNCHARACTERIZED"` | `"GENERATE"` | Same undifferentiated finding (B1). | "they manifest stereotypical and erroneous presumptions when asked to answer questions while adopting a persona" |
| gupta2023bias / C5 | operator | `"GENERATE"` | `"UNCHARACTERIZED"` | `"GENERATE"` | Same undifferentiated finding (B1). | "they manifest stereotypical and erroneous presumptions when asked to answer questions while adopting a persona" |
| madigan2025emergent / C3 | operator | `"GENERATE"` | `"UNCHARACTERIZED"` | `"GENERATE"` | System-level bias is reported as not traceable to individual components, i.e. absent upstream and present downstream, so GENERATE. | "emergent bias in financial decision-making that cannot be traced to individual agent components" |
| madigan2025emergent / C4 | operator | `"GENERATE"` | `"UNCHARACTERIZED"` | `"GENERATE"` | Same undifferentiated finding (B1). | "emergent bias in financial decision-making that cannot be traced to individual agent components" |
| cao2026from / C3 | operator | `"GENERATE"` | `"UNCHARACTERIZED"` | `"GENERATE"` | Persona-assigned agents degrade against the no-persona condition, which B3 names as demographically clean, so GENERATE. | "demographic-based persona assignments can alter LLM agents' behavior and degrade performance" |
| cao2026from / C4 | operator | `"GENERATE"` | `"UNCHARACTERIZED"` | `"GENERATE"` | Same undifferentiated finding (B1). | "persona assignments can introduce implicit biases and increase behavioral volatility" |
| owens2024multi / C3 | demographic | `"yes"` | `"no"` | `"yes"` | Bias is reported across social groups of people, which Part D codes yes. | "outperforming the baseline method across several social groups" |
| weissburg2024llms / C5 | fairness_dimension | `"group"` | `"unspecified"` | `"unspecified"` | MAB and MDB are bias scores whose per-group outcome is not named; 'biases ... tailored to different demographic groups' names no compared quantity, so no family is instantiated (B2 step 2). | "We introduce and apply two bias score metrics--Mean Absolute Bias (MAB) and Maximum Difference Bias (MDB)" |
| weissburg2024llms / C5 | fairness_basis | `"instantiated"` | `"none"` | `"none"` | Follows fairness_dimension = unspecified. | (default value) |
| xu2026ducx / C1 | fairness_basis | `"named"` | `"instantiated"` | `"instantiated"` | Equalized odds is attached to end-to-end performance, not the C1 finding; the C1 finding compares a utility gap across subgroups, so group by instantiation (B1; B2 step 2). | "conditioned on segmentation-tool availability, the subgroup utility gap reaches as high as 50%" |
| xu2026ducx / C1 | fairness_dimension | `"group"` | `"group"` | `"group"` | Value agreed (group); evidence taken from B so that it matches the instantiated C1 basis. | "conditioned on segmentation-tool availability, the subgroup utility gap reaches as high as 50%" |
| xu2026ducx / C4 | fairness_dimension | `"group"` | `"unspecified"` | `"unspecified"` | The C4 finding (reasoning and synthesis behaviors) reports subgroup disparities with no compared quantity named; equalized odds belongs to the end-to-end result (B1; B2). | "model reasoning bias, or subgroup differences in synthesis behaviors" |
| xu2026ducx / C4 | fairness_basis | `"named"` | `"none"` | `"none"` | Follows fairness_dimension = unspecified. | (default value) |
| coppolillo2025unmasking / C2 | operator | `"AMPLIFY"` | `"UNCHARACTERIZED"` | `"AMPLIFY"` | Stance is compared before and after agent discussion and shifts in the direction of the models' known lean, a two-point increase (B3 step 5), so AMPLIFY. | "we observe significant shifts in the stance expressed in the generated messages" |
| dai2024bias / C1 | evidence_type | `"llm_non_agentic_transferred"` | `"direct_llm_agent"` | `"llm_non_agentic_transferred"` | A survey of LLM-integrated IR systems; no measurement on an LLM operating as an agent component, so the mechanism transfers by analogy (B4). | "bias and unfairness issues in IR systems when the integration of LLMs" |
| deldjoo2024cfairllm / C5 | evidence_type | `"llm_non_agentic_transferred"` | `"direct_llm_agent"` | `"direct_llm_agent"` | Recommendations are conditioned on user profiles sampled from stored interaction history, i.e. personalization driven by a stored user model (B4 direct list). | "diverse user profile sampling strategies-random, top-rated, and recency-focused-to better understand the impact of profile generation fed to LLMs" |
| deldjoo2024normative / C5 | operator | `"AMPLIFY"` | `"UNCHARACTERIZED"` | `"AMPLIFY"` | Deviations are present zero-shot and larger with added in-context examples, a two-point increase (B3 step 5), so AMPLIFY. | "fairness deviations in age-based recommendations, particularly when additional contextual examples are introduced (ICL-2)" |
| kantharuban2024stereotype / C5 | fairness_dimension | `"counterfactual"` | `"group"` | `"group"` | Recommendations are compared across four racial groups with a significance test, not reported as per-pair changes, so group by instantiation (B2 swap rule). | "This bias and lack of transparency occurs consistently across multiple popular consumer LLMs and for four American racial groups" |
| makhortykh2021detecting / C1 | fairness_dimension | `"group"` | `"unspecified"` | `"unspecified"` | A mixed-method, largely qualitative account of how AI is depicted; no rate or score is compared across groups of people (B2 step 3). | "we use a mixed-method approach to investigate presence of race and gender bias in representation of artificial intelligence" |
| makhortykh2021detecting / C1 | fairness_basis | `"instantiated"` | `"none"` | `"none"` | Follows fairness_dimension = unspecified. | (default value) |
| mansoury2020feedback / T | fairness_dimension | `"group"` | `"unspecified"` | `"unspecified"` | 'The impact of feedback loop' names no compared rate or score, so no family is instantiated (B2 step 2). | "the impact of feedback loop is generally stronger for the users who belong to the minority group" |
| mansoury2020feedback / T | fairness_basis | `"instantiated"` | `"none"` | `"none"` | Follows fairness_dimension = unspecified. | (default value) |
| mirza2025malibu / C3 | fairness_dimension | `"group"` | `"unspecified"` | `"group"` | Judges' scores of responses labelled with demographic personas are compared across personas (marginalized personas favored), so group by instantiation; the paired phase comes second (B2 step 1 tie rule by analogy). | "judges score responses labeled with specific demographic personas (e.g., gender, race, religion) across four metrics" |
| mirza2025malibu / C3 | fairness_basis | `"instantiated"` | `"none"` | `"instantiated"` | Follows group by instantiation. | (default value) |
| nguyen2025social / C3 | operator | `"GENERATE"` | `"AMPLIFY"` | `"GENERATE"` | The first directional finding is bias emergence, defined against agents without that bias before communication, so GENERATE (B3: operator = first directional descriptive finding). | "communication can trigger up to 70\% new bias emergence" |
| nguyen2025social / C3 | operator_secondary | `"PRESERVE"` | `null` | `"PRESERVE"` | The next distinct comparison, propagation of bias across agents, carries bias through, so PRESERVE. CODEBOOK GAP: with three descriptive operators (GENERATE, PRESERVE, AMPLIFY) the codebook does not say which second one to keep; abstract order was used. | "propagate bias across over 80\% of agents" |
| nguyen2025social / C3 | demographic | `"yes"` | `"no"` | `"yes"` | Stereotyping across social groups of people (B5; Part D). | "stereotyping and unfair treatment across social groups" |
| simhi2026old / C2 | operator | `"UNCHARACTERIZED"` | `"PRESERVE"` | `"UNCHARACTERIZED"` | The 'bias' is persistence of conversational history, not a disparity measured at two points, so UNCHARACTERIZED (B3 table requires disparity). | (default value) |
| staab2023memorization / C5 | evidence_type | `"llm_non_agentic_transferred"` | `"direct_llm_agent"` | `"llm_non_agentic_transferred"` | The reported measurement (attribute inference accuracy) is single-prompt; the chatbot scenario is explored with no result stated (B4 boundary). | "we present the first comprehensive study on the capabilities of pretrained LLMs to infer personal attributes from text" |
| tang2026your / C1 | evidence_type | `"direct_llm_agent"` | `"llm_non_agentic_transferred"` | `"llm_non_agentic_transferred"` | Agentic workflows are motivation; the benchmark measures selection among candidates in a single call with no tool, retrieval, second agent or carried state (rule 0.3; B4 boundary). | "LLMs need to select some optimal solutions from massive candidates" |
| u2018algorithms / C1 | operator | `"UNCHARACTERIZED"` | `"PRESERVE"` | `"UNCHARACTERIZED"` | No abstract; the summary's 'inherit' sentence is the survey's transfer argument, not a two-point comparison reported by the work, so UNCHARACTERIZED. | (default value) |
| vijjini2024exploring / C5 | operator | `"GENERATE"` | `"UNCHARACTERIZED"` | `"GENERATE"` | Safety is measured with and without personalization; the no-personalization condition is demographically clean, so GENERATE. | "We measure safety by examining how benign LLM responses are to unsafe prompts with and without personalization" |
| wang2026observations / T | operator_secondary | `"ATTENUATE"` | `null` | `null` | 'Increases preference bias and decreases disparate bias' is one comparison (the same loop iterations) on two measures, which B3 does not count as distinct. CODEBOOK GAP: B3 defines distinct by pair of points and does not address two measures on one comparison. | (default value) |
| wang2026observations / T | demographic | `"yes"` | `"no"` | `"yes"` | The abstract names an underserved demographic of users and reports disparate bias (B5; Part D). | "less query data will be collected from this particular demographic of users" |
| wyllie2024fairness / T | demographic | `"yes"` | `"no"` | `"yes"` | Minoritized group representation and historical discrimination concern groups of people (B5; Part D). | "minoritized group representation" |
| xu2024adapting / T | fairness_dimension | `"unspecified"` | `"group"` | `"unspecified"` | ELBERT is the paper's own criterion but not one of the criteria B2 step 1 lists, and no groups are named, so neither named nor instantiated. CODEBOOK GAP: no rule for a new parity-shaped criterion not in the list. | "we introduce a long-term fairness concept named Equal Long-term Benefit Rate (ELBERT)" |
| xu2024adapting / T | fairness_basis | `"none"` | `"named"` | `"none"` | Follows fairness_dimension = unspecified. | (default value) |

## Mitigation extraction

| Record | Field | A | B | Final | Rationale | Deciding quote |
|---|---|---|---|---|---|---|
| li2024prompting | demographic | `"yes"` | `"no"` | `"yes"` | The targeted bias is social bias from social information in decisions about people in hiring and healthcare (B5). | "we propose a causality-guided debiasing framework to tackle social biases" |
| furniturewala2024thinking | metric_named | `"not_named"` | `"mean bias"` | `"not_named"` | 'Mean bias' is the generic word bias with an aggregation, not a named metric (Part C). | (default value) |
| ouyang2022training | effect_direction | `"reduces"` | `"not_reported"` | `"not_reported"` | Toxicity is not a fairness or bias measure; no bias effect is stated, so not_reported. | (default value) |
| chakraborty2024maxmin | metric_named | `"win-rate (accuracy) for minority groups"` | `"win-rate (accuracy)"` | `"win-rate (accuracy) for minority groups"` | The fairness metric is the minority-group win rate; win rate alone is also the utility metric, so the qualifier is part of the name. | "improves the win-rate (accuracy) for minority groups by over 33%" |
| bai2022constitutional | setting | `"other"` | `"qa_generation"` | `"qa_generation"` | The intervention is evaluated on assistant responses to queries (single-response dialogue), so qa_generation precedes other (Part C order). | "a harmless but non-evasive AI assistant that engages with harmful queries by explaining its objections to them" |
| huang2024collective | demographic | `"yes"` | `"no"` | `"yes"` | Bias across nine social dimensions concerns attributes of people (B5). | "lower bias across nine social dimensions" |
| li2025fairsteer | effect_direction | `"reduces"` | `"not_reported"` | `"reduces"` | A debiasing framework reported superior on bias evaluations, including counterfactual input evaluation, implies reduced bias. | "demonstrates the superiority of FairSteer across question-answering, counterfactual input evaluation and open-ended text generation tasks" |
| singh2025bias | setting | `"agentic_multistep"` | `"other"` | `"other"` | The abstract reports no evaluation, which Part C codes other ('a system description with no fairness evaluation'); setting is where the intervention is evaluated, not where it applies. | "This study introduces a novel approach to bias-aware knowledge retrieval" |
| ma2026implicit | metric_named | `"not_named"` | `"Decision-based Implicit Bias (DIB) Benchmark (benchmark)"` | `"Decision-based Implicit Bias (DIB) Benchmark (benchmark)"` | Only a benchmark is named for the evaluation, so it is given with the (benchmark) suffix (Part C). | "we introduce the Decision-based Implicit Bias (DIB) Benchmark" |
| ma2026implicit | effect_direction | `"mixed"` | `"reduces"` | `"mixed"` | The title names no intervention, so the first described is coded: static prompting gives limited, short-lived reduction, i.e. mixed. Note: the proposed DMT 'substantially reduces' bias. | "a static system-level prompting baseline provides limited and short-lived debiasing effects" |
| owens2024multi | demographic | `"yes"` | `"no"` | `"yes"` | Bias reduction is reported across social groups of people (B5; Part D). | "outperforming the baseline method across several social groups" |
| xu2024mitigating | demographic | `"yes"` | `"no"` | `"yes"` | The intervention targets social bias against groups of people (B5). | "mitigate social bias in LLMs" |

## Totals

Screening: 31 INCLUDE_TOPICAL, 2 INCLUDE_PRIOR_ART, 70 EXCLUDE (n = 103); 25 records adjudicated, 7 with was_borderline = true.
Entry coding: 30 of 68 entries adjudicated. Mitigation: 11 of 24 papers adjudicated.
`code_new_input.jsonl`: 31 newly admitted locus-tagged papers, 34 entries.

## Points the codebook could not decide

Marked `CODEBOOK GAP` in the rationale column above.

## Round 2 (new papers)

Entry coding of the 31 newly admitted papers (`code_new_input.jsonl`, 34 entries), coders as above, output `code_new_final.jsonl`. Same adjudicator, inputs and conventions as Round 1, with the Round 1 precedents applied. No agreed field violated a hard codebook constraint, so none was changed. Where a paper carries a locus and T, the R4 temporal finding was read as belonging to the T entry and the static finding to the base-locus entry (see 2510.02352).

| Record | Field | A | B | Final | Rationale | Deciding quote |
|---|---|---|---|---|---|---|
| 2305.07609 / C5 | demographic | `"yes"` | `"no"` | `"yes"` | Unfairness is measured over sensitive attributes of users, i.e. protected attributes of people (B5; Part D). | "it still exhibits unfairness to some sensitive attributes when generating recommendations" |
| 2504.08260 / C3 | operator | `"UNCHARACTERIZED"` | `"GENERATE"` | `"GENERATE"` | The digital twins are built from the UAS respondents, and the abstract states that the reference data show none of the biases the twins introduce, so disparity appears where the upstream condition shows none (B3 table; step 5 read a contrario). | "also introduces biases not present in the UAS data" |
| 2506.04419 / C5 | fairness_dimension | `"group"` | `"unspecified"` | `"group"` | A named quantity (response quality) is compared across dialect groups, so group by instantiation (B2 step 2). | "Rufus produces lower-quality responses to prompts written in minoritized English dialects" |
| 2506.04419 / C5 | fairness_basis | `"instantiated"` | `"none"` | `"instantiated"` | Follows group by instantiation. | "Rufus produces lower-quality responses to prompts written in minoritized English dialects" |
| 2506.13245 / C3 | operator | `"UNCHARACTERIZED"` | `"ATTENUATE"` | `"ATTENUATE"` | The intervention yields a more balanced cross-cultural compromise than the reference condition, a reduction after an intervention; with no directional descriptive finding, the intervention result is `operator` (B3; same reading as li2025fairsteer in Round 1). | "our approach generates consensus of higher quality while ensuring more balanced compromi" |
| 2508.10906 / C3 | demographic | `"yes"` | `"no"` | `"yes"` | Demographic parity is assessed over demographic data of individuals, which concerns protected attributes of people (B5; Part D). | "dedicated demographic parity assessments, ensuring that generated responses remain accurate and unbiased" |
| 2509.08829 / C5 | demographic | `"yes"` | `"no"` | `"yes"` | Disparities are reported across demographic groups of users (B5; Part D). | "can exacerbate fairness disparities across demographic groups" |
| 2510.02352 / C5 | operator | `"UNCHARACTERIZED"` | `"AMPLIFY"` | `"UNCHARACTERIZED"` | 'Amplify' here compares recommendation with decision tasks, two parallel tasks rather than an upstream and a downstream point, so step 2 finds no two-point comparison; the multi-turn persistence finding is coded on the T entry (R4; B1). CODEBOOK GAP: B3 does not say whether a paper's own directional verb with no stated reference point licenses an operator, and B1 does not say whether an R4 temporal finding also feeds the base-locus entry. | "recommendation tasks tend to amplify cross-group disparities" |
| 2510.02352 / C5 | operator_secondary | `null` | `"PRESERVE"` | `null` | `operator` is UNCHARACTERIZED, so `operator_secondary` is null (B3); persistence over turns is the T entry's PRESERVE, on which both coders agreed. | (default value) |
| 2510.02352 / C5 | evidence_type | `"llm_non_agentic_transferred"` | `"direct_llm_agent"` | `"llm_non_agentic_transferred"` | The C5 finding is a single-turn decision or recommendation conditioned on the speaker's paralinguistic identity cues; the multi-turn study belongs to the T entry, which both coders coded direct (B4 boundary; staab2023memorization precedent). | "open-source models are more sensitive to age and gender" |
| 2511.06148 / C4 | fairness_dimension | `"group"` | `"unspecified"` | `"group"` | Task allocations, a named decision, are stratified across demographic groups, so group by instantiation (B2 step 2). | "These biases result in highly stratified task allocations" |
| 2511.06148 / C4 | fairness_basis | `"instantiated"` | `"none"` | `"instantiated"` | Follows group by instantiation. | "These biases result in highly stratified task allocations" |
| 2511.06148 / C4 | operator | `"GENERATE"` | `"ATTENUATE"` | `"GENERATE"` | The first directional descriptive finding is bias emerging where the design has no inherent group differences, a clean upstream condition, so GENERATE (B3; nguyen2025social precedent); the intervention result is secondary. | "LLMs can spontaneously develop novel social biases about artificial demographic groups even when no inherent differences exist" |
| 2511.06148 / C4 | operator_secondary | `"ATTENUATE"` | `null` | `"ATTENUATE"` | The exploration incentive is a distinct comparison (an intervention) that reduces stratification (B3 two-operator rule). | "explicitly incentivizing exploration robustly reduces stratification" |
| 2511.06148 / T | fairness_dimension | `"group"` | `"unspecified"` | `"group"` | Same undifferentiated finding as the C4 entry (B1). | "These biases result in highly stratified task allocations" |
| 2511.06148 / T | fairness_basis | `"instantiated"` | `"none"` | `"instantiated"` | Follows group by instantiation. | "These biases result in highly stratified task allocations" |
| 2511.06148 / T | operator | `"GENERATE"` | `"ATTENUATE"` | `"GENERATE"` | Same as C4 (B1). | "LLMs can spontaneously develop novel social biases about artificial demographic groups even when no inherent differences exist" |
| 2511.06148 / T | operator_secondary | `"ATTENUATE"` | `null` | `"ATTENUATE"` | Same as C4 (B1). | "explicitly incentivizing exploration robustly reduces stratification" |
| 2602.02582 / C5 | fairness_dimension | `"unspecified"` | `"group"` | `"group"` | Group fairness is the only family named, and it is named for the paper's own personality-aware fairness analysis, so step 1 applies; SNSR/SNSV names no family. | "expose trade-offs between personalization and group fairness" |
| 2602.02582 / C5 | fairness_basis | `"none"` | `"named"` | `"named"` | Follows group by naming. | "expose trade-offs between personalization and group fairness" |
| 2602.02582 / C5 | demographic | `"yes"` | `"no"` | `"yes"` | The dataset is annotated for demographic attributes and unfairness is found for sensitive attributes (B5; Part D). | "annotated for eight demographic attributes" |
| 2604.09620 / C3 | fairness_dimension | `"group"` | `"unspecified"` | `"group"` | The screening decision is compared between candidates with AI-positive and AI-skeptical attitudes and reported as a group tendency, not a per-pair change, so group by instantiation (B2 swap rule). | "resume screeners tend to favor candidates with positive or non-critical attitudes toward AI" |
| 2604.09620 / C3 | fairness_basis | `"instantiated"` | `"none"` | `"instantiated"` | Follows group by instantiation. | "resume screeners tend to favor candidates with positive or non-critical attitudes toward AI" |
| 2605.00382 / C3 | demographic | `"yes"` | `"no"` | `"yes"` | Code bias is measured over demographic dimensions of people (B5; Part D). | "a benchmark of 343 real-world coding tasks spanning seven demographic dimensions" |
| 2605.12530 / C3 | fairness_dimension | `"group"` | `"unspecified"` | `"unspecified"` | Behaviours are compared across identity-presence configurations with no group named and no per-group or per-pair structure stated, so no family is instantiated; disparate treatment is not a criterion listed in B2 (xu2024adapting precedent). CODEBOOK GAP: B2 lists disparate impact but not disparate treatment. | "across 8 million conversation transcripts spanning multiple models and identity presence configurations" |
| 2605.12530 / C3 | fairness_basis | `"instantiated"` | `"none"` | `"none"` | Follows fairness_dimension = unspecified. | (default value) |
| 2605.12530 / C3 | demographic | `"yes"` | `"no"` | `"yes"` | Disparate treatment as identity varies concerns protected attributes of people, as in the Round 1 screening decision on this record (B5). | "examining how models' disparate-treatment behaviors shift when identity is varied" |
| doi:10.3390/math14030458 / C3 | fairness_dimension | `"group"` | `"unspecified"` | `"group"` | Profit, a named outcome, is compared for agents of four racial groups and two genders, aggregated rather than per pair, so group by instantiation (B2 swap rule). | "secure more profit compared to when negotiations are gender- and race-blind" |
| doi:10.3390/math14030458 / C3 | fairness_basis | `"instantiated"` | `"none"` | `"instantiated"` | Follows group by instantiation. | "secure more profit compared to when negotiations are gender- and race-blind" |
| doi:10.3390/math14030458 / C3 | operator | `"GENERATE"` | `"ATTENUATE"` | `"GENERATE"` | The gender- and race-blind negotiation is a demographically clean condition (no demographic cue), and disparity appears when the cue is present, so GENERATE (B3 table; cao2026from and vijjini2024exploring precedents); the intervention result is secondary. | "when either the seller or buyer is aware of the gender and race of the other player, they secure more profit" |
| doi:10.3390/math14030458 / C3 | operator_secondary | `"ATTENUATE"` | `null` | `"ATTENUATE"` | Persona conditioning is a distinct intervention comparison that mitigates bias (B3 two-operator rule). | "such conditioning can mitigate LLM-based agents" |

Round 2 totals: 14 of 34 entries adjudicated (31 field rows), decided for A on 25 rows and for B on 6. Two rows carry CODEBOOK GAP notes (2510.02352 / C5 operator; 2605.12530 / C3 fairness_dimension).


## Round 3 (remaining 123 targeted-query hits)
Coders agreed on 122 of 123 verdicts (binary agreement 0.992, kappa 0.663; includes are rare). Both included 2604.18038. One disagreement, 2509.04794: A = EXCLUDE (criterion ii), B = INCLUDE_TOPICAL (C3, transfer clause). Final = INCLUDE_TOPICAL: demographic bias is one of the three evaluated axes (BBQ), so criterion ii is met; persona and trait steering bears on role assignment (C3) through the transferable-mechanism clause.
Coding of the two Round 3 papers: 2509.04794/C3 evidence_type A=direct_llm_agent, B=llm_non_agentic_transferred -> transferred (BBQ on non-agentic models); demographic A=yes, B=no -> yes (BBQ). 2604.18038/C2 fairness_dimension A=group, B=unspecified -> group (race-stratified distribution compared across groups). Operators agreed (UNCHARACTERIZED; ATTENUATE).

## Round 4 (operator validation)

Date: 2026-11-10. Rule: CODEBOOK.md, "Operator evidence requirement, 2026-11-10". One adjudicator re-read all 56 entries coded ATTENUATE, PRESERVE, AMPLIFY or GENERATE against the abstract. For nine papers with an ambiguous or truncated abstract, the adjudicator also read the paper's own arXiv page (URLs in `operator_validation.jsonl`). 10 entries changed and 46 were confirmed. No field other than `operator` changed, with two exceptions forced by B3 precedence: `operator_secondary` and its evidence on pezeshkpour2023large and sneh2025tooltweak, and `operator_evidence` on sneh2025tooltweak. Entries recoded to UNCHARACTERIZED keep their superseded `operator_evidence` text for traceability. Backups: `*_final.prevalidation.jsonl`.

| Record | Old | New | Rationale | Deciding quote / source |
|---|---|---|---|---|
| madigan2025emergent / C3 | GENERATE | UNCHARACTERIZED | The constituent agents are not reported unbiased. The full text compares each system with its constituent LLMs and finds a mixed direction: a small median reduction, with amplification of up to 10x in the tail. No single operator is licensed. | "emergent bias ... cannot be traced to individual agent components"; https://arxiv.org/html/2512.16433v1 |
| madigan2025emergent / C4 | GENERATE | UNCHARACTERIZED | Same finding as C3 (B1). | as above |
| arzaghi2024understanding / C5 | AMPLIFY | UNCHARACTERIZED | Single-attribute vs intersectional groups is a change of grouping, not of stage (amendment item 4). | "these biases are significantly amplified when considering intersectionality" |
| hu2024free / C2 | GENERATE | AMPLIFY | The censored corpus is clean, but the no-RAG LLM is not reported unbiased. The full text (Sec. 4.4) reports fairness degrading from the no-RAG baseline after clean RAG, so the change is larger downstream of a biased upstream (amendment item 5). | "Even with fully censored and supposedly unbiased external datasets, RAG can lead to biased outputs"; https://arxiv.org/html/2410.07589 |
| li2025actions / C4 | AMPLIFY | UNCHARACTERIZED | The amplification is relative to real-world empirical disparities, and "more advanced models" is a comparison across model generations. Neither is a stage of the system (amendment item 3). | "the biases we uncovered are directionally aligned but markedly amplified" |
| pezeshkpour2023large / C1 | AMPLIFY | UNCHARACTERIZED | Option reordering is an input perturbation (item 1), so `perturbation_sensitivity` = yes. The secondary ATTENUATE (option-placement advice) is also a perturbation, and the calibration result reports accuracy, not disparity, so `operator_secondary` is set to null. | "a considerable performance gap of approximately 13% to 75% ... when answer options are reordered" |
| sneh2025tooltweak / C1 | AMPLIFY | ATTENUATE | The attack edits tool names and descriptions at a single selection decision. That is an input perturbation with no downstream stage, so `perturbation_sensitivity` = yes. The defense result meets the ATTENUATE clause and is promoted from `operator_secondary` (B3 precedence), and `operator_secondary` is set to null. | "paraphrasing and perplexity filtering, which reduce bias and lead agents to select functionally similar tools more equally" |
| 2506.04419 / C5 | AMPLIFY | UNCHARACTERIZED | Typos are an input perturbation (round-5 review 3B; item 1), so `perturbation_sensitivity` = yes. | "these quality-of-service harms are exacerbated by the presence of typos in prompts" |
| 2510.02352 / T | PRESERVE | UNCHARACTERIZED | "May persist" reports neither a before and after measurement nor a similar magnitude (round-5 review 3B; item 2). The full abstract adds nothing further. | "We found that biased decisions may persist in multi-turn conversations"; https://arxiv.org/abs/2510.02352 |
| 2602.02582 / C5 | PRESERVE | UNCHARACTERIZED | Persistence under typos and multilingual input is robustness to perturbation, not carriage across a stage (round-5 review 3B; item 1). `perturbation_sensitivity` = yes. | "These disparities persist under prompt perturbations such as typographical errors and multilingual inputs" |

The full text confirmed the existing operator for six entries: fan2024fairmt C2 and T AMPLIFY (Sec. 3.3 compares multi-turn with single-turn, and Sec. 3.4 finds bias rising with turns); choi2025identity ATTENUATE (gap 0.608 to 0.024 under anonymization); 2506.13245 ATTENUATE ("compared to baselines"); 2512.16532 AMPLIFY (retrieval to re-ranking, Sec. 3.2.3); and 2512.19735 ATTENUATE ("CAP also reduced several subgroup disparities").

`perturbation_sensitivity` = yes on 12 entries (11 papers): blankenstein2025biasbusters, cao2026from (C3, C4), pezeshkpour2023large, sneh2025tooltweak, liu2023lost, tonneau2026different, 2501.04316, 2506.04419, 2509.08829, 2510.01164, 2602.02582. All other entries = no.

Flagged, not changed (outside the counted field):
- nguyen2025social / C3 keeps `operator_secondary` = PRESERVE ("propagate bias across over 80% of agents"). Propagation to more agents does not state a similar magnitude, so it would fail the strict PRESERVE clause. Figure 9 does not count this field.
- kabra2025reasoning / C4 `operator_evidence` still quotes the cross-model correlation, which does not qualify. ATTENUATE stands on the ReGiFT result, quoted in `operator_validation.jsonl`.

Figure 9 totals (extended corpus, 104 entries), before and after validation:

| | ATTENUATE | PRESERVE | AMPLIFY | GENERATE | UNCHARACTERIZED |
|---|---|---|---|---|---|
| Before | 17 | 2 | 22 | 15 | 48 |
| After | 18 | 0 | 18 | 12 | 56 |

The PRESERVE column is now empty.


## Round 5 (eligibility consistency)

Adjudicator: Claude Opus, 2026-11-10, from title, abstract and date plus `CODEBOOK.md` Part F only. Trigger: external review round 5, §3D (the extension excluded single-decision demographic audits on the component-emission test while the original cohort keeps them). Part F separates (a) corpus eligibility, criterion iii met by route iii-a direct, iii-b transferable mechanism (the A4 test), iii-c decision audit or iii-d evaluation or mitigation, from (b) locus-grid eligibility, which still requires a finding attributable to an emission of C1 to C5 or T.

### Extension re-screen

Every extension record whose final verdict was EXCLUDE on criterion iii (6) or on criterion i (1, because A4 also governed i) was re-screened. Output: `eligibility_recheck.jsonl`. The four changed records were updated in place in `screen_final.jsonl` (`eligibility_amended: true`, `eligibility_route`, `pre_amendment_verdict`; previous file kept as `screen_final.preelig.jsonl`). `screen2_final.jsonl` has no changed record and was not rewritten.

| Record | Old | New | Primary branch | Locus tags | Rationale | Deciding quote |
|---|---|---|---|---|---|---|
| 2312.03689 | EXCLUDE (iii) | INCLUDE_TOPICAL (iii-c, iii-d) | evaluation; secondary mitigation, high-stakes | none | Single-prompt LM decisions about people in financing and housing, with demographics varied, plus an evaluation method and a prompt-based mitigation; no component emission is measured, and the title names evaluation first (A7). | "applying them to high-stakes societal decisions, such as determining financing or housing eligibility" |
| 2403.00742 | EXCLUDE (iii) | INCLUDE_TOPICAL (iii-c) | high-stakes | none | Employment, conviction and sentencing decisions vary with dialect, a race proxy; the speaker is the decision subject in one response, not the interacting user, so no C5 (2603.18729 precedent). | "Language models are more likely to suggest that speakers of African American English be assigned less prestigious jobs, be convicted of crimes" |
| 2405.04412 | EXCLUDE (iii) | INCLUDE_TOPICAL (iii-c) | high-stakes | none | GPT-3.5 scores resumes whose names signal race and gender, a hiring decision with the cue in the prompt. | "we ask GPT to score resumes with 32 different names" |
| 2406.15484 | EXCLUDE (iii) | INCLUDE_TOPICAL (iii-c, iii-d) | evaluation; secondary high-stakes | none | A hiring-bias benchmark and metrics applied to resume-scoring decisions across gender; a single decision, so no locus. | "a novel framework for benchmarking hierarchical gender hiring bias in Large Language Models (LLMs) for resume scoring" |
| 2603.17179 | EXCLUDE (iii) | EXCLUDE (iii) | | | The LLM agent audits a non-LLM clinical model and is scored on similarity to expert statements; no disparity in an LLM's decisions or behavior toward people (F1 case 1). | "evaluates whether an agentic AI system can support auditing biomedical machine learning models for fairness" |
| 2410.08388 | EXCLUDE (iii) | EXCLUDE (iii) | | | LLMs are benchmarked as detectors of biased text spans, not measured for their own disparity (F1 case 1). | "We formulate bias detection as multi-label token-level classification and benchmark both encoder-based models ... and decoder-based large language models" |
| 2410.09204 | EXCLUDE (i) | EXCLUDE (i) | | | No LLM and no fairness question; fails i and ii independently of the emission test. | "encoding them with a Transformer-based neural network architecture" |

No new include carries a locus tag, so `code_new3_input.jsonl` is empty (0 records) and Figures 8 and 9 are unchanged (92 locus-tagged papers, 104 entries). The four new includes are eligible for the evaluation, mitigation and high-stakes inventories (main Tables 5 and 6), which this round did not edit.

Corpus totals computed from the files (original split by first branch in `corpus/corpus_master.json`: prior-art branch, else a locus, evaluation, mitigation or high-stakes first branch = topical, else contextual): original 202 = 99 topical + 29 prior-art + 74 contextual; extension includes 39 = 37 topical + 2 prior-art (was 35 = 33 + 2). **Coded corpus 241 = 136 topical + 31 prior-art + 74 contextual** (was 237 = 132 + 31 + 74).

Not done in this round: `corpus/corpus_master_extended.json` was not rebuilt, because `build_corpus_extended.py` needs `bibkeys.json` entries (bib keys) for the four new includes and no bib edits were made; it will raise `KeyError` on 2312.03689 until they exist. The article's counts (237, 132, 35 admitted) are not edited.

### Original cohort against (a) and (b)

Checked, not changed. (a) was applied to the 99 topical papers and, in its prior-art reading (A2: secondary work on fairness with agent or component scope), to the 29 prior-art papers; the 74 contextual works were admitted under a separate rule and are not subject to (a). (b) was applied to the 59 original papers that carry a locus tag (`code_input_existing.jsonl`). Sources: abstracts where `code_input_existing.jsonl` or `mitig_input.jsonl` has them, otherwise the `contribution` summary in `corpus_master.json` (all prior-art judgments and the non-locus topical papers outside Table 6 rest on summaries).

**Locus-tagged papers that fail (b)** (6): `park2023generative` (contextual; reports no fairness finding), `dai2024bias` (survey; no finding of its own), `arzaghi2024understanding` (single-response sentence associations; no interacting user whose model changes output, so the C5 row does not apply), `pezeshkpour2023large` (option order within one multiple-choice response; options are not tools, so C1 holds by analogy only), `zhou2025veracity` (attribution and grading with the demographic-authorship cue in the prompt; the reasoning-process claim is inferred, no reasoning trace is measured), `tang2026your` (borderline: selection among candidate items in one call, not among tools or sources).

**Topical papers that fail (a)** (24). All fail criterion ii as defined in A1 and A5 (no group of people as the object), not the new iii routes.
- Locus-tagged (17): provider- or source-side fairness with no social group, `blankenstein2025biasbusters`, `sneh2025tooltweak`, `kim2024fair`; position or order bias, `pezeshkpour2023large`, `liu2023lost`; sycophancy or agent identity, `liu2025truth`, `hong2025measuring`, `choi2025identity`; belief or behavior persistence, `geng2025accumulating`, `simhi2026old`; political stance (A5), `coppolillo2025unmasking`; no group named in the abstract, `tang2026your`, `singh2025bias`, `singh2025biasb`; no fairness finding, `campedelli2024want` (anti-social conduct), `staab2023memorization` (attribute inference for privacy); secondary work in a topical branch, `dai2024bias`. All but `staab2023memorization` are coded `demographic` = `no` in `code_existing_final.jsonl`.
- Not locus-tagged (7): dataset or spurious-feature bias, `zhang2024causal`, `du2024causal`; toxicity or harmlessness with no group, `ouyang2022training`, `bai2022constitutional`; guardrail position paper with bias listed, not studied, `dong2024building`; minority preference groups that are not protected or social groups (borderline), `chakraborty2024maxmin`, `xiao2024algorithmic`.

**Prior-art papers that fail the prior-art reading of (a)** (19), each by its summary a survey with no LLM-agent or component scope, or one that lists fairness without studying it: `barrainkua2025preserving`, `caton2024fairness`, `chan2024visibility`, `chang2024survey`, `du2026survey`, `ferdaus2026trustworthy`, `he2025emerged`, `kaur2022trustworthy`, `kemmerzell2025better`, `kostikova2026lllms`, `li2023trustworthy`, `li2025triangular`, `pessach2022review`, `qi2026trustworthy`, `raza2025trism`, `soremekun2025software`, `tang2023what`, `yehudai2025survey`, `zhang2026generalizability`. Separately, `proceedings2026framework` reports its own measurements (bias amplification factors), so A2 would class it topical rather than prior-art; it passes (a).

### Open decision (not settled by this round)

Part F makes criterion iii consistent across cohorts. Criterion ii is not consistent: the original cohort keeps 17 locus-tagged non-demographic or technical-bias papers (shown as non-demographic [dagger] entries) and 19 prior-art surveys outside agent scope, while the extension excludes comparable records on ii or iii (for example 2305.17926, position bias in an LLM judge). Either A1 ii is widened to admit non-demographic mechanism evidence and the extension's ii exclusions are re-screened, or the original exceptions are stated as such in main §2.3 and supp §S6 and the "screened under the same criteria" wording for prior-art works (main Table 2) is corrected. This needs an author decision.

**Settled 2026-11-10:** the author chose one strict rule for both cohorts (`CODEBOOK.md` Part G); see Round 6.


## Round 6 (strict rule, both cohorts)

Adjudicator: Claude Opus, 2026-11-10, from title, abstract and date (author contribution summary where no abstract is held) plus `CODEBOOK.md` Part G. Trigger: author decision of 2026-11-10 on the open decision of Round 5, and external review round 6, §3A and §3B. One line per decision in `strict_rule.jsonl` (273 lines: 169 papers, 104 entries), each with a reason and a verbatim quote. Coding-file backups: `*_final.prestrict.jsonl`. No record left the corpus (241).

### (a) Papers moved

**Original topical to `contextual-mechanism-precursor`** (24; the Round 5 list, confirmed). All fail criterion ii: no demographic, protected or social group of people is the object.
- Locus-tagged (17): `blankenstein2025biasbusters`, `sneh2025tooltweak`, `kim2024fair` (provider- or source-side fairness); `pezeshkpour2023large`, `liu2023lost` (option order, context position); `liu2025truth`, `hong2025measuring`, `choi2025identity` (sycophancy, agent identity); `geng2025accumulating`, `simhi2026old` (context or history effects on beliefs and performance); `coppolillo2025unmasking` (political stance, A5); `tang2026your`, `singh2025bias`, `singh2025biasb` (no group named); `campedelli2024want` (anti-social conduct), `staab2023memorization` (attribute inference for privacy); `dai2024bias` (secondary work in a topical branch).
- Not locus-tagged (7): `zhang2024causal`, `du2024causal` (dataset or spurious-feature bias); `ouyang2022training`, `bai2022constitutional` (toxicity, harmlessness); `dong2024building` (bias listed, not studied); `chakraborty2024maxmin`, `xiao2024algorithmic` (preference minorities, not protected or social groups; borderline).

**Extension topical to `contextual-mechanism-precursor`** (3), same test: `2510.01164` (inequality, measured by the Gini coefficient, among anonymous recipients), `2511.11772` (equity across lower- and higher-scoring learners, a performance stratum), `2604.09620` (bias toward candidates' attitudes to AI, which the abstract sets apart from demographic bias). They were admitted at screening; under Part G they are not topical.

**Original prior-art to `contextual`** (19; the Round 5 list, confirmed): `barrainkua2025preserving`, `caton2024fairness`, `chan2024visibility`, `chang2024survey`, `du2026survey`, `ferdaus2026trustworthy`, `he2025emerged`, `kaur2022trustworthy`, `kemmerzell2025better`, `kostikova2026lllms`, `li2023trustworthy`, `li2025triangular`, `pessach2022review`, `qi2026trustworthy`, `raza2025trism`, `soremekun2025software`, `tang2023what`, `yehudai2025survey`, `zhang2026generalizability`. Each is a survey or position paper with no LLM-agent or agent-component scope, or one that lists fairness without studying it.

**Original prior-art to `topical`** (1): `proceedings2026framework` (`condon2026towards`) reports its own measurements (bias amplification factors from demographic swapping in agentic workflows), so A2 makes it a primary study, and it passes (a). It carries no locus tag.

**Passed (a) although the abstract names no group** (10): `hall2025guiding`, `hu2022achieving`, `hu2024free`, `kabra2025reasoning`, `ma2026implicit`, `mansoury2020feedback`, `she2025fairsense`, `xu2024adapting`, `2511.06148` (artificial demographic groups), `2512.16532`. Their object is fairness of decisions or outputs about people. They stay topical, and their entries, coded `demographic` = `no`, leave the grids under (b). The `demographic` codes were not re-opened.

Unchanged: 75 original topical, 9 original prior-art (`binkyte2025interactional`, `dai2025trustworthy`, `ebrahimi2025survey`, `gan2024navigating`, `ranjan2025fairness`, `raza2025responsible`, `wang2023survey`, `yangsmith2026fairness`, `zehlike2022fairness`), 34 extension topical, 2 extension prior-art. The 74 original contextual works were not re-screened; the two with locus tags (`park2023generative`, `madigan2025emergent`) stay contextual.

**Corpus categories** (`corpus_master_extended.json`, field `category`): 241 = **110 topical + 11 prior-art + 93 contextual + 27 contextual-mechanism-precursor** (was 136 + 31 + 74, no precursor category). Original 202 = 76 + 9 + 93 + 24; extension 39 = 34 + 2 + 0 + 3.

### (b) Entries removed from Figures 8 and 9 (40 of 104)

- Paper not topical (23): `blankenstein2025biasbusters` C1, `sneh2025tooltweak` C1, `pezeshkpour2023large` C1, `tang2026your` C1, `singh2025bias` C1, `singh2025biasb` C1, `dai2024bias` C1, `kim2024fair` C2, `liu2023lost` C2, `geng2025accumulating` C2, `simhi2026old` C2, `coppolillo2025unmasking` C2, `choi2025identity` C3, `campedelli2024want` C3, `staab2023memorization` C5, `liu2025truth` T, `hong2025measuring` T, `2510.01164` C4, `2511.11772` C3, `2604.09620` C3 (papers that fail (a)); `park2023generative` C3, `madigan2025emergent` C3 and C4 (contextual works; `madigan2025emergent` is also `demographic` = `no`).
- Finding not measured at the entry's locus (6): `arzaghi2024understanding` C5 (sentence associations in one response; no interacting user); `zhou2025veracity` C4 (cue in the prompt; no reasoning trace measured); `gupta2023bias` C4 (persona-caused accuracy gap, C3 by R2; no plan or trace measured); `gupta2023bias` C5 (the persona is the model's, not a model of the user, R3); `cao2026from` C4 (persona-caused performance gap, C3 by R2); `li2025actions` C4 (disparities keyed to the agents' assigned personas, C3 by R2; it would qualify at C3, but author tags are not re-decided, so the paper leaves the grids).
- `demographic` = `no` (11): `hall2025guiding` C4, `kabra2025reasoning` C4, `hu2024free` C2, `hu2022achieving` T, `ma2026implicit` T, `mansoury2020feedback` T, `she2025fairsense` T, `xu2024adapting` T, `2511.06148` C4 and T, `2512.16532` C2.

Of the six locus tags Round 5 flagged, all six are now out of the grids: `park2023generative`, `dai2024bias`, `pezeshkpour2023large` and `tang2026your` as non-topical papers, `arzaghi2024understanding` and `zhou2025veracity` on the locus test.

**Grid after (b):** 57 papers (29 original, 28 extension), 64 entries (34 original, 30 extension); every counted entry has `demographic` = `yes`.

### (c) Operators recoded (10) and confirmed (4)

| Entry | Old | New | Rationale |
|---|---|---|---|
| gupta2023bias / C3 | GENERATE | UNCHARACTERIZED | Explicit stereotype questions and persona-conditioned reasoning accuracy are different tasks and outcomes; a no-persona condition measures no disparity (round-6 review B). |
| gupta2023bias / C4 | GENERATE | UNCHARACTERIZED | As C3; no planning-specific comparison. Entry also fails (b). |
| gupta2023bias / C5 | GENERATE | UNCHARACTERIZED | As C3; no user-model comparison. Entry also fails (b). |
| cao2026from / C3 | GENERATE | UNCHARACTERIZED | Task-success variation across demographic personas has no comparable upstream disparity; a no-persona condition measures none. |
| cao2026from / C4 | GENERATE | UNCHARACTERIZED | Copied persona finding; no generation isolated at planning (round-6 review B). Entry also fails (b). |
| vijjini2024exploring / C5 | GENERATE | UNCHARACTERIZED | "With and without personalization" compares conditions; the unpersonalized condition has no group comparison. |
| 2504.08260 / C3 | GENERATE | UNCHARACTERIZED | The reference, UAS survey data, is an external statistic, not an upstream stage (operator amendment, item 3). |
| doi:10.3390/math14030458 / C3 | GENERATE | ATTENUATE | Blind negotiation is a cue-free condition with no measured zero disparity on the same outcome; the persona-conditioning result ("such conditioning can mitigate LLM-based agents' biases") meets ATTENUATE and is promoted from `operator_secondary` (B3 precedence). |
| borah2024implicit / C2 | AMPLIFY | UNCHARACTERIZED | Escalation is measured across multi-agent interaction (C3); nothing specific to C2. B1 as amended. |
| wang2025bias / C1 | AMPLIFY | UNCHARACTERIZED | Amplification runs through manipulated retrieval results, which R1 places at C2; no comparison of which retriever, tool or source is invoked. B1 as amended. |

`operator_secondary` was set to null on every entry recoded to UNCHARACTERIZED, and on the promoted entry; superseded `operator_evidence` is kept except on the promoted entry. Confirmed as GENERATE: `nguyen2025social` C3 (bias emergence counts new stereotyped answers in conversations with no earlier stereotyped answer; wording corrected in Round 7, which see), `wyllie2024fairness` T (fairness and group representation tracked across generations from an initially unbiased dataset), `2511.06148` C4 and T (no inherent group differences; stratification develops through exploration; both entries leave the grids on `demographic` = `no`). Other multi-locus papers with a substantive operator: `fan2024fairmt` C2 and T keep AMPLIFY on distinct full-text comparisons (Round 4).

### Figure totals

| | Fig. 8: group / individual / counterfactual / unspecified | Fig. 9: ATT / PRE / AMP / GEN / uncharacterized | Entries |
|---|---|---|---|
| Before Round 6 (all entries) | 34 / 0 / 3 / 67 | 18 / 0 / 18 / 12 / 56 | 104 |
| All entries, operators recoded (unfiltered) | 34 / 0 / 3 / 67 | 19 / 0 / 16 / 4 / 65 | 104 |
| **Grid-eligible (published figures)** | **25 / 0 / 3 / 36** | **11 / 0 / 9 / 2 / 42** | **64** |

Per locus, grid-eligible (`figure_counts.json`, `extended_corpus`):

| Locus | Fig. 8: group / indiv. / counterf. / unspec. | Fig. 9: ATT / PRE / AMP / GEN / unchar. | Total |
|---|---|---|---|
| C1 | 1 / 0 / 0 / 4 | 0 / 0 / 0 / 0 / 5 | 5 |
| C2 | 3 / 0 / 2 / 7 | 4 / 0 / 3 / 0 / 5 | 12 |
| C3 | 8 / 0 / 0 / 10 | 5 / 0 / 2 / 1 / 10 | 18 |
| C4 | 2 / 0 / 0 / 2 | 1 / 0 / 0 / 0 / 3 | 4 |
| C5 | 10 / 0 / 1 / 10 | 1 / 0 / 2 / 0 / 18 | 21 |
| T | 1 / 0 / 0 / 3 | 0 / 0 / 2 / 1 / 1 | 4 |

The two remaining GENERATE entries are `nguyen2025social` C3 and `wyllie2024fairness` T. Planning (C4) has no GENERATE entry.

Not done in this round: the article and supplement (counts, Figures 8 and 9, the "screened under the same criteria" wording, Tables 5 and 6) were not edited, and the evaluation and mitigation inventories were not re-assessed against the new topical set.

## Round 7 (entry's own locus; review round 7)

One adjudication pass (Claude Opus), answering review round 7, §3A. Two rules were made to agree: the
A4 row for C1 listed "search results", whereas R1 places what a search engine or retriever returns at
C2. The A4 rows now follow R1 (`CODEBOOK.md` A4, amendment note), and G2 item 2 is read strictly: an
entry stays in the grids only when a finding is measured at that locus itself, even when its operator
was already `UNCHARACTERIZED`. All five C1 entries and every multi-locus grid entry were re-checked
against the abstracts and, for `wu2024rag`, the full text (arXiv 2409.19804, Appendix A.4). Author
locus tags are not re-decided (B1), so failing entries are removed, not moved. Backups:
`*_final.preround7.jsonl`, `strict_rule.preround7.jsonl` (changed lines keep `reason_preround7`).

### Entries removed from Figures 8 and 9 (6 of 64)

| Entry | Reason |
|---|---|
| wang2025bias / C1 | The disparity runs through manipulated retrieval results (which documents the poisoned store returns): C2 under R1. No comparison of which resource is invoked. The C2 entry stays. |
| wu2024rag / C1 | Retrieval-stage disparity is gold-document rank by group (MRR@K, Appendix A.4), returned content: C2. No disparity in which retriever is invoked or whether retrieval is triggered. The C2 entry stays. |
| makhortykh2021detecting / C1 | Representation of people in returned image search results: C2 content. The paper leaves the grids. |
| u2018algorithms / C1 | Curation of returned search results: C2 content. The paper leaves the grids. |
| borah2024implicit / C2 | The escalation is measured across multi-agent interaction (C3, the A4 row for agent interaction); no separate finding on retrieved content, memory or history. The C3 entry stays. |
| 2510.09905 / C2 | Disparity keyed to the interacting user's profile held in memory: C5 under R3; no separate finding on what memory stores or returns. The C5 entry stays. |

Re-checked and kept: `xu2026ducx` C1 (subgroup differences in tool-routing patterns, i.e. which tool is
invoked) and C4 (subgroup differences in reasoning traces); `fan2024fairmt` C2 and T (multi-turn
history, indexed by turn under R4); `wang2025bias` C2; `wu2024rag` C2; `borah2024implicit` C3;
`2510.02352` C5 (paralinguistic user attributes) and T (repeated negative feedback over turns).

`nguyen2025social` C3 stays GENERATE, with its unit corrected: the emergence rate is the share of
conversations in which an agent first gives a stereotyped answer at turn t with no stereotyped answer
at any earlier turn of that conversation (full text, §3.1). This is the same measure absent upstream
within the same design; it does not show that the constituent agents are unbiased, since standalone
agents already show bias (Table 1). `strict_rule.jsonl` carries the corrected `operator_reason`.

### Figure totals after Round 7

| | Fig. 8: group / individual / counterfactual / unspecified | Fig. 9: ATT / PRE / AMP / GEN / uncharacterized | Entries |
|---|---|---|---|
| **Grid-eligible (published figures)** | **24 / 0 / 3 / 31** | **11 / 0 / 9 / 2 / 36** | **58** |

| Locus | Fig. 8 | Fig. 9 | Total |
|---|---|---|---|
| C1 | 1 / 0 / 0 / 0 | 0 / 0 / 0 / 0 / 1 | 1 |
| C2 | 2 / 0 / 2 / 6 | 4 / 0 / 3 / 0 / 3 | 10 |
| C3 | 8 / 0 / 0 / 10 | 5 / 0 / 2 / 1 / 10 | 18 |
| C4 | 2 / 0 / 0 / 2 | 1 / 0 / 0 / 0 / 3 | 4 |
| C5 | 10 / 0 / 1 / 10 | 1 / 0 / 2 / 0 / 18 | 21 |
| T | 1 / 0 / 0 / 3 | 0 / 0 / 2 / 1 / 1 | 4 |

55 papers (27 original, 28 added) with 58 entries (29 and 29). Evidence: 33 direct agent, 24
non-agentic LLM, 1 non-LLM. Fairness basis: 6 named, 21 instantiated, 31 none. Corpus categories are
unchanged (no paper changed category), so `corpus_master_extended.json` was not regenerated.

## Round 8 (two cited studies; review round 8)

The round-8 review (§3A) identified two eligible studies, posted before the 10 June 2026 cutoff and already
cited in the survey, that no candidate pool held (neither abstract matches the targeted query): 2605.28098
(`wu2026examining`, posted 27 May 2026) and 2604.13705 (`chaki2026beyond`, posted 15 April 2026). Their pool
records are `pool4.jsonl` (source `review-round8`); `bibkeys.json` maps them to the existing bib keys.

**Procedure and coders.** Blind inputs (id, title, date, abstract) in `screen_input4.jsonl`; the coding input
`code_new4_input.jsonl` follows the round-3 format (locus tags from the adjudicated screening, no venue, no
summary). Coder B (GPT-6.1, `codex exec`, reasoning effort high, read-only sandbox) ran `PROMPT_SCREEN.md` and
`PROMPT_CODE.md` unchanged, plus one line naming the input file: `screen4_B.jsonl`, `code_new4_B.jsonl`.
**Coder A deviates from earlier rounds:** the Claude Sonnet command-line coder was not available (its session had
expired: "OAuth session expired and could not be refreshed"), so coder A was Claude Opus, which coded
`screen4_A.jsonl` and `code_new4_A.jsonl` strictly from the codebook and the inputs **before reading coder B's
output**. The same model then adjudicated, so for these two papers coder A and the adjudicator are not
independent.

### Screening

| Record | Field | A | B | Final | Rationale | Deciding quote |
|---|---|---|---|---|---|---|
| 2604.13705 | locus_tags | `["C3"]` | `["C3", "C4"]` | `["C3"]` | The allocation disparity is produced by the roles the agents are given (aligned to an ethical framework, or prompted to favor demographic groups) and by their negotiation. R2 places role-caused disparity at C3 and keeps C4 for allocation "independent of identity assignment"; G2 item 2 would remove a C4 entry whose disparity is caused by an agent's role. | "the other is either unaligned or adversarially prompted to favor demographic groups over clinical need" |
| 2605.28098 | verdict | `"INCLUDE_TOPICAL"` | `"BORDERLINE"` | `"INCLUDE_TOPICAL"` | B left criterion ii unsettled because the abstract does not say that the favored and disfavored groups are groups of people. The adjudicator read the paper's full text (https://arxiv.org/html/2605.28098v1, Section 3, "Problem formulation"): each instance has a binary sensitive attribute "such as gender", and the task is student pass-or-fail prediction with gender as the focal sensitive attribute. Criterion ii is met (A5). CODEBOOK GAP: Part A gives no full-text route for an unsettled screening criterion; the "Ambiguous abstracts" rule of the operator amendment was applied by analogy. Record 2601.17492 (round 1, excluded on ii from its abstract) was not re-checked against its full text. | "We use prompts to expose individual agents to group-favoring bias, then assess downstream impacts at the system level." |
| 2605.28098 | deciding_criterion | `"all_met"` | `"ii"` | `"all_met"` | Follows the verdict. | (as above) |

Both records: `post_cutoff` false, primary branch C3, no transfer clause (agreed). Secondary branches agreed:
2604.13705 `["mitigation", "high-stakes"]`, 2605.28098 `["evaluation"]`. Final file: `screen4_final.jsonl`
(both `INCLUDE_TOPICAL`; `was_borderline` true for 2605.28098).

### Entry coding

| Record | Field | A | B | Final | Rationale | Deciding quote |
|---|---|---|---|---|---|---|
| 2604.13705 / C3 | fairness_dimension | `"group"` | `"unspecified"` | `"group"` | Access and allocation, a named decision, are compared for marginalized and demographic groups, so group by instantiation (B2 step 2; 2511.06148 and 2604.09620 precedents). | "acting as corrective patches that restore access for marginalized groups without fully converting a biased counterpart" |
| 2604.13705 / C3 | fairness_basis | `"instantiated"` | `"none"` | `"instantiated"` | Follows group by instantiation. | (as above) |
| 2605.28098 / C3 | fairness_dimension | `"group"` | `"unspecified"` | `"unspecified"` | Favored-group uplift and disfavored-group suppression are named, but no compared quantity (rate, score, decision); bias across groups with no quantity named does not instantiate a family (B2 step 2, last sentence). | (default value) |
| 2605.28098 / C3 | fairness_basis | `"instantiated"` | `"none"` | `"none"` | Follows unspecified. | (default value) |

Agreed and kept: 2604.13705 / C3 ATTENUATE (the negotiated joint allocation meets fairness criteria that neither
agent's allocation meets alone, a reduction of an existing disparity at the C3 interaction, which meets the
operator evidence requirement and G3), direct LLM-agent evidence, demographic yes. 2605.28098 / C3 AMPLIFY
(system-wide bias exceeds the additive sum of the individual agents' biases after interaction), direct evidence,
**demographic no**: the abstract names no protected attribute or proxy (B5; Part D). Agreed fields are kept, so
the entry fails G2 item 3 and stays out of the grids, as for `gharat2026personalization`; the paper passes G1
(fairness of decisions about people, established at screening). Coded from the full text, which names gender, it
would add one C3 AMPLIFY entry; that recoding was not made, to keep the abstract-only protocol. Neither entry
reports perturbation sensitivity. Final file: `code_new4_final.jsonl` (`grid_eligible` true for 2604.13705, false
for 2605.28098 with a `strict_rule_note`); `strict_rule.jsonl` gains two paper lines and two entry lines.

**Agreement.** Screening: the coders agreed on 1 of 2 verdicts and 1 of 2 locus-tag sets (too few for a kappa of
their own). Pooled over rounds 1, 3 and 8 (228 records): four-way verdict kappa 0.854 (agreement 0.956), against
0.863 (0.960) over the 226 of rounds 1 and 3. New entries pooled over rounds 1, 3 and 8 (38): fairness dimension
0.555 (agreement 0.737), operator 0.761 (0.842), evidence type 0.883, demographic 0.558; against 0.621 and 0.740
over 36. The pooled values mix two coder-A models and should be read with that caveat.

**Mitigation and evaluation inventories** (one model pass, Claude Opus, from the abstracts and, for these two
papers, the full text; `mitig_final.jsonl` lines 37-38, single-pass). 2604.13705: Table 5 no (a study, no reusable
instrument stated); Table 6 multi-agent delegation, agent-roles row (agentic multi-step, partial reduction: an
aligned agent partly corrects an adversarially prompted one). 2605.28098: Table 5 no (FBS is a metric applied to
existing student datasets, not a reusable benchmark or dataset); Table 6 the same row (full text: disagreement-based
arbitration by a calibrated ML predictor lowers FBS under single-agent bias exposure, and less when all agents are
exposed). The row's representative evidence goes from 7 to 9 studies; its density stays High.

**Mitigation-file provenance (review round 8, §3D).** Every `mitig_final.jsonl` record now carries `provenance`
(24 dual-coded, 14 single-pass). Where the supplement's inventory tables record a value that differs from the
abstract-based structured fields, the record carries `table6_setting`, `table6_effect` and `table6_note`, and those
values are authoritative for Table 6: `wu2024rag` (effect reduces, from the full text; setting Q), `basu2026names`
(mixed, from the full text), `wang2025bias` (setting Q) and `wu2026examining` (reduces, from the full text). For the
two RAG studies the supplement's Q differs from Part C's first-match rule (agentic_multistep); under Part C the
poisoning row of Table 6 would read Medium instead of Low. Not changed in this round; flagged for the authors.

### Figure totals after Round 8

| | Fig. 8: group / individual / counterfactual / unspecified | Fig. 9: ATT / PRE / AMP / GEN / uncharacterized | Entries |
|---|---|---|---|
| **Grid-eligible (published figures)** | **25 / 0 / 3 / 31** | **12 / 0 / 9 / 2 / 36** | **59** |

Only the C3 row changes: Fig. 8 9 / 0 / 0 / 10, Fig. 9 6 / 0 / 2 / 1 / 10 (19 entries). 56 papers (27 original,
29 added) with 59 entries (29 and 30). Evidence: 34 direct agent, 24 non-agentic LLM, 1 non-LLM. Fairness basis:
6 named, 22 instantiated, 31 none. Unfiltered: 106 entries from 94 papers. Corpus (`build_corpus_extended.py`): 243
records (202 original, 41 extension); 112 topical, 11 prior-art, 93 contextual, 27 contextual-mechanism-precursor;
the extension cohort 36 / 2 / 0 / 3.
