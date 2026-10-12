---
title: "CLASP: Online learning algorithms for Convex Losses And Squared Penalties"
collection: publications
permalink: /publication/2026-01-01-CLASP-Online-learning-algorithms-for-Convex-Losses-And-Squared-Penalties
excerpt_separator: ""
description: 'Addressing Constrained Online Convex Optimization (COCO), we introduce CLASP (Convex Losses And Squared Penalties), a framework that minimizes cumulative loss together with squared constraint violations.'
excerpt: 'Addressing Constrained Online Convex Optimization (COCO), we introduce CLASP (Convex Losses And Squared Penalties), a framework that minimizes cumulative loss together with squared constraint violations. We propose two variants of CLASP, CLASP-I and CLASP-F, allowing for a joint or separate handling of the static decision set and the time-varying constraints, a decoupling flexibility that affords simpler implementations when projections onto the static decision set are.'
date: 2026-01-01
venue: 'Proceedings of the 43rd International Conference on Machine Learning'
citation_authors: ["Ricardo N. Ferreira", "Joao Xavier", "Cláudia Soares"]
citation_year: '2026'
citation_conference: "Proceedings of the 43rd International Conference on Machine Learning"
citation_volume: "306"
citation_firstpage: '30861'
citation_lastpage: '30878'
mathjax: true
paperurl: 'https://proceedings.mlr.press/v306/ferreira26a.html'
citation: 'Ricardo N. Ferreira, Joao Xavier, Cláudia Soares, "CLASP: Online learning algorithms for Convex Losses And Squared Penalties." Proceedings of the 43rd International Conference on Machine Learning, 2026.'
---


<p class="publication-authors">Ricardo N. Ferreira, Joao Xavier, Cláudia Soares</p>

{% raw %}

## Abstract

<div class="publication-abstract"><p>Addressing Constrained Online Convex Optimization (COCO), we introduce CLASP (Convex Losses And Squared Penalties), a framework that minimizes cumulative loss together with squared constraint violations. We propose two variants of CLASP, CLASP-I and CLASP-F, allowing for a joint or separate handling of the static decision set and the time-varying constraints, a decoupling flexibility that affords simpler implementations when projections onto the static decision set are easy. Our theoretical analysis departs from prior work by fully leveraging the variety of cutter operators, and contraction properties such as the strongly quasi-nonexpansiveness, a proof strategy not previously applied in this setting. For convex losses, both CLASP algorithms achieve regret $O\left(T^{\max{\beta,1-\beta}}\right)$ and cumulative squared penalty $O\left(T^{{1-\beta}}\right)$ for any $\beta \in (0,1)$. Most importantly, for strongly convex problems, we provide the first logarithmic guarantees on both regret and cumulative squared penalty: In the strongly convex case, both CLASP algorithms guarantee that the regret is upper bounded by $O( \log T )$ and the cumulative squared penalty is also upper bounded by $O( \log T )$.</p></div>

[Published abstract source](https://proceedings.mlr.press/v306/ferreira26a.html).

[Access paper here](https://proceedings.mlr.press/v306/ferreira26a.html){:target="_blank"}

## BibTeX

<pre><code>@inproceedings{Ferreira_2026_CLASP,
    author = &quot;Ferreira, Ricardo N. and Xavier, Joao and Soares, Cl{\&#x27;a}udia&quot;,
    title = &quot;{CLASP}: Online learning algorithms for {C}onvex {L}osses {A}nd {S}quared {P}enalties&quot;,
    booktitle = &quot;Proceedings of the 43rd International Conference on Machine Learning&quot;,
    year = &quot;2026&quot;,
    url = &quot;https://proceedings.mlr.press/v306/ferreira26a.html&quot;,
    abstract = &quot;Addressing Constrained Online Convex Optimization (COCO), we introduce CLASP (Convex Losses And Squared Penalties), a framework that minimizes cumulative loss together with squared constraint violations. We propose two variants of CLASP, CLASP-I and CLASP-F, allowing for a joint or separate handling of the static decision set and the time-varying constraints, a decoupling flexibility that affords simpler implementations when projections onto the static decision set are easy. Our theoretical analysis departs from prior work by fully leveraging the variety of cutter operators, and contraction properties such as the strongly quasi-nonexpansiveness, a proof strategy not previously applied in this setting. For convex losses, both CLASP algorithms achieve regret $O\left(T^{\max{\beta,1-\beta}}\right)$ and cumulative squared penalty $O\left(T^{{1-\beta}}\right)$ for any $\beta \in (0,1)$. Most importantly, for strongly convex problems, we provide the first logarithmic guarantees on both regret and cumulative squared penalty: In the strongly convex case, both CLASP algorithms guarantee that the regret is upper bounded by $O( \log T )$ and the cumulative squared penalty is also upper bounded by $O( \log T )$.&quot;,
    abstractsource = &quot;https://proceedings.mlr.press/v306/ferreira26a.html&quot;,
    abstractsourcelabel = &quot;Published abstract source&quot;,
    pages = &quot;30861--30878&quot;,
    volume = &quot;306&quot;,
    publisher = &quot;PMLR&quot;
}</code></pre>
{% endraw %}
