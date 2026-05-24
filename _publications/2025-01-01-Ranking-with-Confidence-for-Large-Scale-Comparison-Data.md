---
title: "Ranking with Confidence for Large Scale Comparison Data"
collection: publications
permalink: /publication/2025-01-01-Ranking-with-Confidence-for-Large-Scale-Comparison-Data
excerpt: 'In this work, we leverage a generative data model considering comparison noise to develop a fast, precise, and informative ranking algorithm from pairwise comparisons that produces a measure of confidence on each comparison. The problem of ranking a large number of items from noisy and sparse pairwise comparison data arises in diverse applications, like ranking players in online games, document retrieval or ranking human perceptions.'
date: 2025-01-01
venue: 'Proceedings of the 2025 SIAM International Conference on Data Mining (SDM)'
paperurl: 'http://dx.doi.org/10.1137/1.9781611978520.21'
citation: 'Filipa Valdeira, Cláudia Soares, "Ranking with Confidence for Large Scale Comparison Data." Proceedings of the 2025 SIAM International Conference on Data Mining (SDM), 2025.'
---

In this work, we leverage a generative data model considering comparison noise to develop a fast, precise, and informative ranking algorithm from pairwise comparisons that produces a measure of confidence on each comparison. The problem of ranking a large number of items from noisy and sparse pairwise comparison data arises in diverse applications, like ranking players in online games, document retrieval or ranking human perceptions. Although different algorithms are available, we need fast, large-scale algorithms whose accuracy degrades gracefully when the number of comparisons is too small. Fitting our proposed model entails solving a non-convex optimization problem, which we tightly approximate by a sum of quasi-convex functions and a regularization term. Resorting to an iterative reweighted minimization and the Primal-Dual Hybrid Gradient method, we obtain PD-Rank, achieving a better Kendall tau than comparing methods, even for 10% of wrong comparisons in simulated data matching our data model and without the assumption of strong connectivity. In real data, PD-Rank requires less computational time to achieve the same Kendall tau than active learning methods.

[Access paper here](http://dx.doi.org/10.1137/1.9781611978520.21){:target="_blank"}

Bibtex:

<pre><code>@inbook{Valdeira_2025-2,
    author = &quot;Valdeira, Filipa and Soares, Cláudia&quot;,
    title = &quot;Ranking with Confidence for Large Scale Comparison Data&quot;,
    ISBN = &quot;9781611978520&quot;,
    url = &quot;http://dx.doi.org/10.1137/1.9781611978520.21&quot;,
    DOI = &quot;10.1137/1.9781611978520.21&quot;,
    booktitle = &quot;Proceedings of the 2025 SIAM International Conference on Data Mining (SDM)&quot;,
    publisher = &quot;Society for Industrial and Applied Mathematics&quot;,
    year = &quot;2025&quot;,
    month = &quot;Jan&quot;,
    pages = &quot;223-232&quot;,
    abstract = &quot;In this work, we leverage a generative data model considering comparison noise to develop a fast, precise, and informative ranking algorithm from pairwise comparisons that produces a measure of confidence on each comparison. The problem of ranking a large number of items from noisy and sparse pairwise comparison data arises in diverse applications, like ranking players in online games, document retrieval or ranking human perceptions. Although different algorithms are available, we need fast, large-scale algorithms whose accuracy degrades gracefully when the number of comparisons is too small. Fitting our proposed model entails solving a non-convex optimization problem, which we tightly approximate by a sum of quasi-convex functions and a regularization term. Resorting to an iterative reweighted minimization and the Primal-Dual Hybrid Gradient method, we obtain PD-Rank, achieving a better Kendall tau than comparing methods, even for 10\\% of wrong comparisons in simulated data matching our data model and without the assumption of strong connectivity. In real data, PD-Rank requires less computational time to achieve the same Kendall tau than active learning methods.&quot;
}</code></pre>
