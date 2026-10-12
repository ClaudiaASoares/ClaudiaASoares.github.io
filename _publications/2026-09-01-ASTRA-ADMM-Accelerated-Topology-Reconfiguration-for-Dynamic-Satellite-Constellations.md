---
title: "ASTRA: ADMM-Accelerated Topology Reconfiguration for Dynamic Satellite Constellations"
collection: publications
permalink: /publication/2026-09-01-ASTRA-ADMM-Accelerated-Topology-Reconfiguration-for-Dynamic-Satellite-Constellations
excerpt_separator: ""
description: 'Dynamic topology reconfiguration is central to the reliability and efficiency of large satellite constellations, yet many existing approaches rely on idealized assumptions such as full constellation deployment or uniform orbital spacing.'
excerpt: 'Dynamic topology reconfiguration is central to the reliability and efficiency of large satellite constellations, yet many existing approaches rely on idealized assumptions such as full constellation deployment or uniform orbital spacing. We present Adaptive Satellite Topology via Regret-Aware learning (ASTRA), a theoretically-grounded framework for dynamic satellite topology reconfiguration that builds on an online learning formulation and makes it computationally practical. ASTRA combines an ADMM-based offline.'
date: 2026-09-01
venue: 'NeurIPS 2026'
citation_authors: ["João Norberto", "Ricardo Ferreira", "Cláudia Soares"]
citation_year: '2026'
citation_conference: "NeurIPS 2026"
preprinturl: 'https://arxiv.org/pdf/2609.33993.pdf'
citation: 'João Norberto, Ricardo Ferreira, Cláudia Soares, "ASTRA: ADMM-Accelerated Topology Reconfiguration for Dynamic Satellite Constellations." NeurIPS 2026, 2026.'
---


<p class="publication-authors">João Norberto, Ricardo Ferreira, Cláudia Soares</p>

{% raw %}

## Abstract

<div class="publication-abstract"><p>Dynamic topology reconfiguration is central to the reliability and efficiency of large satellite constellations, yet many existing approaches rely on idealized assumptions such as full constellation deployment or uniform orbital spacing. We present Adaptive Satellite Topology via Regret-Aware learning (ASTRA), a theoretically-grounded framework for dynamic satellite topology reconfiguration that builds on an online learning formulation and makes it computationally practical. ASTRA combines an ADMM-based offline solver with efficient online updates for both online gradient descent and online conditional gradient, yielding markedly cheaper constrained updates than generic optimization pipelines. On the theory side, we show that for a relevant class of entry-wise nonzero utility matrices, the objective is strongly convex, which yields logarithmic static regret for online gradient descent, and we further instantiate known dynamic-regret guarantees under inexact ADMM inner loops. Empirically, ASTRA matches or improves topology quality, presenting a good trade-off with computational time on synthetic constellations, and it remains effective on real Starlink data under partial deployment and non-uniform spacing, where idealized structural assumptions break down. These results position ASTRA as an efficient and theoretically grounded approach to topology reconfiguration in realistic Low Earth Orbit networks.</p></div>

[Author preprint abstract](https://arxiv.org/abs/2609.33993).

[Download paper here](https://arxiv.org/pdf/2609.33993.pdf){:target="_blank"}

## BibTeX

<pre><code>@inproceedings{Norberto_2026_ASTRA,
    author = &quot;Norberto, João and Ferreira, Ricardo and Soares, Cláudia&quot;,
    title = &quot;{ASTRA}: {ADMM}-Accelerated Topology Reconfiguration for Dynamic Satellite Constellations&quot;,
    booktitle = &quot;NeurIPS 2026&quot;,
    year = &quot;2026&quot;,
    month = &quot;September&quot;,
    note = &quot;Accepted at NeurIPS 2026&quot;,
    preprinturl = &quot;https://arxiv.org/abs/2609.33993&quot;,
    abstract = &quot;Dynamic topology reconfiguration is central to the reliability and efficiency of large satellite constellations, yet many existing approaches rely on idealized assumptions such as full constellation deployment or uniform orbital spacing. We present Adaptive Satellite Topology via Regret-Aware learning (ASTRA), a theoretically-grounded framework for dynamic satellite topology reconfiguration that builds on an online learning formulation and makes it computationally practical. ASTRA combines an ADMM-based offline solver with efficient online updates for both online gradient descent and online conditional gradient, yielding markedly cheaper constrained updates than generic optimization pipelines. On the theory side, we show that for a relevant class of entry-wise nonzero utility matrices, the objective is strongly convex, which yields logarithmic static regret for online gradient descent, and we further instantiate known dynamic-regret guarantees under inexact ADMM inner loops. Empirically, ASTRA matches or improves topology quality, presenting a good trade-off with computational time on synthetic constellations, and it remains effective on real Starlink data under partial deployment and non-uniform spacing, where idealized structural assumptions break down. These results position ASTRA as an efficient and theoretically grounded approach to topology reconfiguration in realistic Low Earth Orbit networks.&quot;,
    abstractsource = &quot;https://arxiv.org/abs/2609.33993&quot;,
    abstractsourcelabel = &quot;Author preprint abstract&quot;
}</code></pre>
{% endraw %}
