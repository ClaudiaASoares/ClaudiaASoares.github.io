---
title: "Optimisation and Sequential Decision-Making"
excerpt: "Optimisation and estimation methods, with constrained online learning, reinforcement learning and operational decision support."
collection: research
topic_id: decisions
order: 1
---

My work in optimisation studies how to compute decisions and estimates under constraints and uncertainty. It includes convex relaxations for localisation, nonconvex optimisation for facial animation, and rank aggregation and learning from pairwise comparisons. Statistical estimation and system identification supply models for control in physical systems.

In sequential decision-making, I study algorithms that act on observations revealed over time. This includes constrained online learning and reinforcement learning for orbital systems, task offloading in computer networks, and distributed energy markets. Further work uses predictive models to support operational decisions in transport and industrial production.

Our ICML 2026 paper CLASP establishes bounds on regret and cumulative squared violation, a metric suitable for control of physical systems. Our NeurIPS 2026 ASTRA combines an ADMM-based solver with online learning for satellite-network decisions. OrbitZoo and PeersimGym provide environments for evaluating sequencial decision-making in challenging physical environments, for example using reinforcement learning.

## Agentic decision-making

My research on agentic decision-making asks when algorithmic guarantees survive substitutions selected by an AI agent during operation. A decision architecture comprises the operator, model class, planning horizon, planning objective and subgoal structure. A substitution replaces one component of that decision architecture.

This line of work examines how computational approximations and changes to the model class affect regret and cumulative squared violation, and under what conditions bounds for individual substitutions extend to a sequence. The physical loss and constraints remain fixed during evaluation.

{% include research-outputs.html %}
