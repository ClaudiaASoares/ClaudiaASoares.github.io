# Concepts for the research page review

Reviewed on 13 October 2026. These definitions govern the proposed introduction,
topic names and paper assignments. They are checked against the current website,
publication records and proposal sources below. A proposed topic is an editorial
choice. Its inclusion does not establish a research result or project funding.

| Concept | Definition and usage boundary |
| --- | --- |
| Machine learning | Methods that fit models or decision rules using data. Specify the learning setting when making a result claim. |
| Optimisation | The formulation and solution of an objective subject to its specified domain and constraints. Use this spelling in prose. Preserve spellings within publication titles. |
| Sequential decision-making | Choosing decisions over time using the information available at each decision. Online learning and reinforcement learning are particular settings with distinct feedback protocols. |
| Optimisation and Sequential Decision-Making | Proposed topic covering optimisation methods, online learning, reinforcement learning and proposed agentic decision-making. A static optimiser is not thereby an online learning algorithm. |
| Online learning | Sequential learning in which observations, losses or constraints are revealed over time under a specified feedback protocol. Do not substitute continual learning. |
| Reinforcement learning | Learning a policy through interactions and rewards. An empirical reinforcement learning result does not establish a constraint bound. |
| Agentic decision-making | Selection and execution of decisions by an AI agent using its available observations and permitted tools or components. Runtime component substitution is the specific proposed question in GUARDA. |
| Decision architecture | The tuple of components an agent runs, including its operator, model class, planning horizon, planning objective and subgoal structure. Use the definition in ERC2027 when discussing GUARDA. |
| Substitution | Replacement of one component of a decision architecture by another. Preservation of bounds after an adaptively selected sequence is a proposed GUARDA result. |
| Convergence bound | A proved statement about the behaviour of an algorithm's iterates or objective values under specified assumptions. It does not establish per-round feasibility. |
| Constraint bound | A proved upper bound on a specified constraint metric under stated assumptions. Distinguish aggregate violation from per-round feasibility. |
| Cumulative squared violation | The sum of squared constraint violations over the evaluation horizon. Use the full term when reporting the CLASP result. |
| Resource constraint | A stated restriction on computation, communication or evidence-review effort. These quantities are measured separately. |
| Federated learning | Learning with data partitioned across participating data owners under a specified coordination protocol. Data remaining local does not itself prove privacy. |
| Distributed optimisation | Solution of an optimisation problem through computations and specified information exchange across nodes. It includes distributed estimation and need not be federated learning. |
| Federated Learning and Distributed Optimisation | Proposed topic covering federated learning and distributed optimisation. Network localisation belongs through distributed estimation, not through a claim that it is federated learning. |
| Estimation | Inference of specified unknown quantities from observations under a stated observation or uncertainty model. |
| Robust estimation | Estimation with an explicit treatment of bounded, non-Gaussian or model-mismatched observations. |
| Learning and Estimation under Uncertainty | Proposed topic covering probabilistic forecasting, robust estimation, statistical consistency and system identification. A diagnostic or estimated confidence is not a proved bound. |
| Probabilistic modelling | Specification and use of probability distributions for observations or unknown quantities, with assumptions stated. |
| Physical model | A mathematical description of physical evolution or measurement relationships used by a method. Distinguish specified physics from learned components. |
| System identification | Estimation of a dynamical model from observed inputs and outputs or state trajectories. |
| Geometric prior | A specified geometric structure incorporated into a model or learning procedure. |
| Interpretable model | A model whose components or decision mechanism can be inspected directly. Do not use an explanation method as evidence that the underlying model is interpretable. |
| Explanation method | A procedure producing a representation of how a model output depends on inputs or model components. Its fidelity and human evaluation are separate properties. |
| Interpretability and Geometric Learning | Proposed topic covering interpretable models, explanation methods and methods that use geometric priors. It includes 3D shape modelling and facial animation. Distinguish model interpretability from post-hoc explanation. |
| AI for Space Operations | Proposed application topic covering orbital estimation, conjunction analysis, satellite-network decisions and information support for space operations. A general method is included only with a stated space connection. |
| Clinical decision support | Methods supplying information to a clinician's decision process. Model evaluation does not itself establish clinical effectiveness. |
| AI for Clinical Decision Support and Health Services | Proposed application topic covering clinical evidence extraction, treatment eligibility research, triage, referral networks and health-service forecasting. General explanation methods retain their methodological topic. |
| Treatment eligibility | Whether a treatment class satisfies the specified clinical criteria for consideration. It is distinct from the clinical team's treatment decision. |
| Decision sufficiency | In RESOLVE-LUNG, mandatory evidence requirements are met and all retained plausible patient states imply the same treatment eligibility set. This remains a proposed research formulation. |
| Scientific-state revision | Change to an explicit scientific state in response to evidence, uncertainty or failure. SciRevBench proposes evaluating this change across research histories. |
| Trustworthy machine learning | Methods evaluated through stated properties such as robustness, interpretability, calibration or constraint compliance. Specify the property supporting each claim. |
| Preprint | A publicly deposited manuscript. The deposit does not establish conference acceptance or journal publication. |
| Publication record | An entry in the website's publication collection. The collection includes a thesis, so its record count is not a count of journal and conference papers. |
| Missing topic reference | A publication record not referenced by the relevant topic page. This is distinct from a missing entry in the main publication collection. |

## Sources

- Current `_research/*.md`, `_publications/*.md` and `markdown_generator/pubs.bib`.
- [Live research page](https://claudiaasoares.github.io/research/) and [publications page](https://claudiaasoares.github.io/publications/), checked in the browser on 13 October 2026.
- [Public author records on arXiv](https://arxiv.org/search/?query=Soares%2C+Claudia&searchtype=author&abstracts=show&order=-announced_date_first&size=50), both result pages checked on 13 October 2026. Deduplicate versions and exclude withdrawn manuscripts from additions.
- Current ERC2027 `CONCEPTS.md`, `sections/B1_abstract.tex`, `sections/B1_cv.tex` and `refs.bib`.
- Current CaixaResearch `CONCEPTS.md` and `RESEARCH_DIRECTION.md`.
- Current Samsung2026 `CONCEPTS.md` and SciRevBench hypotheses/work-plan document.
- Current Epic MEGA Grant `CONCEPTS.md`. STEmo is described there as a WACV submission, not an accepted publication or verified public release.
