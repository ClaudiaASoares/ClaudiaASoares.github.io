# Research terminology

These definitions govern the research pages. The five topic names were approved
in the conversation on 19 October 2026. Use each term with the meaning below.
Publication titles retain their published spelling.

| Concept | Definition and usage boundary |
| --- | --- |
| Trustworthy machine learning | Machine learning assessed through specified properties, such as robustness, interpretability or constraint compliance. State the property supporting a result claim. |
| Optimisation | The formulation and solution of an objective over a specified domain and constraints. Use this spelling in prose. |
| Sequential decision-making | Choosing decisions over time using the information available at each decision. Online learning and reinforcement learning have distinct feedback protocols. |
| Optimisation and Sequential Decision-Making | The research topic covering optimisation methods, estimation and system identification, constrained online learning, reinforcement learning, operational decision support and agentic decision-making. Listing a predictive model here does not make it an online learning algorithm. |
| Operational decision support | Prediction or analysis supplying information for a specified operational decision, including transport and industrial production. Prediction accuracy alone does not establish an improvement in the resulting decisions. |
| Online learning | Sequential learning in which observations, losses or constraints are revealed over time under a specified feedback protocol. |
| Reinforcement learning | Learning a policy through interactions and rewards. An empirical result does not establish a constraint bound. |
| Agentic decision-making | Selection and execution of decisions by an AI agent using its observations and permitted tools or components. The research direction studies component substitutions during operation. |
| Decision architecture | The tuple of components an agent runs, comprising its operator, model class, planning horizon, planning objective and subgoal structure. |
| Substitution | Replacement of one component of a decision architecture by another. Preservation of bounds after a sequence of agent-selected substitutions is a research question. |
| Regret | Accumulated loss relative to a specified reference over a stated horizon. Each result must identify its reference and assumptions. |
| Cumulative squared violation | The sum of squared constraint violations over the evaluation horizon. An aggregate bound does not establish satisfaction of constraints at every step. |
| Algorithmic guarantee | A proved statement under specified assumptions. CLASP supplies established bounds. Extensions under substitutions are research questions. |
| Physical loss | The fixed criterion used to evaluate physical decisions in the research on agentic decision-making. It is distinct from a planning objective that the agent may replace. |
| Federated learning | Learning with data partitioned across participating data owners under a specified coordination protocol. Local data storage alone does not establish privacy. |
| Distributed learning | Learning through computations and specified information exchange across nodes. Federated learning is a particular setting involving participating data owners. |
| Vertical federated learning | Federated learning in which participants hold different features for aligned samples. |
| Distributed optimisation | Solution of an optimisation problem through computations and specified information exchange across nodes. It also supports distributed estimation. |
| Federated Learning and Distributed Optimisation | The research topic covering federated learning, communication constraints and optimisation or estimation across nodes. |
| Estimation | Inference of specified unknown quantities from observations under a stated observation or uncertainty model. |
| System identification | Estimation of a dynamical model from observations of a system. It supports control but does not itself establish a control guarantee. |
| Network localisation | Estimation of the positions of nodes from a specified set of measurements and an observation model. It belongs here through distributed estimation. |
| Geometric prior | A specified geometric structure incorporated into a model or learning procedure. |
| Geometric learning | Learning methods that incorporate specified geometric structure, including the geometric priors used in SCENE-Net. |
| Interpretable model | A model whose components or decision mechanism can be inspected. A post-hoc explanation does not by itself establish model interpretability. |
| Shape modelling | Representation and estimation of three-dimensional shape from observations, including incomplete point clouds. |
| Inverse rigging | Estimation of the controls of a facial model from a specified target shape or motion. |
| Facial motion | Time-varying facial control values before they drive a character. |
| Facial animation | The rendered change in a character driven by facial motion. |
| Facial-motion generation | Generation of facial control sequences. The STEmo baselines use ordered pairs of emotion categories; free-form control is not an established capability. |
| Geometric Learning and Facial Animation | The research topic connecting geometric learning and shape modelling with inverse rigging, facial-motion generation and analysis of the geometry of learned representations. It does not imply that every generation model is interpretable. |
| Geometry of learned representations | Specified geometric or spectral properties of model representations, as in the spectral diagnostics of medical vision-language representations. |
| STEmo | A facial-motion dataset described in a manuscript under review. Unreal Engine integration is a research direction, distinct from the dataset and generation baselines. |
| AI for Space Operations | The application topic covering orbit estimation, conjunction analysis, satellite-network decisions and information support for space operations. |
| Conjunction analysis | Assessment of encounters between orbiting objects, including uncertainty in their positions and separation. |
| Clinical decision support | Methods supplying information to a clinician's decision process. Model evaluation does not establish clinical effectiveness. |
| AI for Clinical Decision Support and Health Services | The application topic covering clinical information extraction, decision support, referral networks, healthcare-demand forecasting and population health risk prediction. Related methods papers are identified as such. |
| Funded project | An awarded research project or computing allocation with an identifiable grant or award reference. Completed projects are included when their activity overlaps 2021 or later. |
| Local PI | Principal investigator for the participation at the local institution. Use this role for Artificial Intelligence Fights Space Debris. |
| Preprint | A publicly available manuscript without an established publication claim in the evidence used here. Related manuscripts may develop earlier work and are not counted as independent journal or conference publications. |
| Research direction | A line of work described through its scientific questions and methods. Its description does not establish a completed result, implementation or funding award. |

## Evidence boundaries

- Public pages describe lines of work through scientific questions and methods.
  Omit funding application names and submission status, as requested by the
  user on 20 October 2026.
- Preserve the distinction between CLASP's established bounds and research
  questions about bounds under component substitutions.
- STEmo is described in a manuscript under review. Integration of facial-motion
  generation into Unreal Engine workflows is a research direction.
- The healthcare page uses the documented HyCARE research scope.
- Publication metadata and links use the existing `_publications` collection.
  Topic assignments and additional papers are maintained in
  `_data/research_coverage.yml`, so regenerating publications does not erase them.
- Coverage includes all 51 existing publication records, 28 additional papers
  and public manuscripts, and 11 funded project records. Use 2021 as the
  calendar-year boundary. Keep older work accessible separately.
- AI4Europe is the name confirmed by the user for grant 101070000. BIGMATH's
  role is National PI; the University of Milan coordinated the consortium.
- AI4Europe is shared research infrastructure. Sustainable Stone by Portugal
  is a related industrial programme. Their placement under
  the methods topic does not assert that every activity uses online learning.
- User corrections on 20 October 2026 take precedence over the earlier database
  records: exclude Drivolution because Cláudia did not participate; list her as
  Local PI for Artificial Intelligence Fights Space Debris; list the
  cortico-cerebellar motor-learning paper as accepted at EPIA 2026.
- See `_audits/research-coverage-2026-10-19.md` for sources and coverage limits.
