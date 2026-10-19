---
title: "ISEE.U: Distributed online estimation and control for improved target localization accuracy"
collection: publications
permalink: /publication/2021-01-01-ISEEU-Distributed-online-estimation-and-control-for-improved-target-localization-accuracy
excerpt_separator: ""
description: 'This paper addresses target localization with an online active learning algorithm defined by distributed, simple and fast computations at each node, with no parameters to tune and where the estimate of the target position at each agent is asymptotically equal in expectation to the centralized maximum-likelihood estimator.'
excerpt: 'This paper addresses target localization with an online active learning algorithm defined by distributed, simple and fast computations at each node, with no parameters to tune and where the estimate of the target position at each agent is asymptotically equal in expectation to the centralized maximum-likelihood estimator. ISEE.U takes noisy distances at each agent and finds a control that maximizes localization accuracy. We do not…'
excerpt_truncated: true
date: 2021-01-01
venue: 'Publication'
citation_authors: ["Claudia Soares", "Miguel Vasques", "Joao Gomes"]
citation_year: '2021'
preprinturl: 'https://arxiv.org/abs/2210.09107'
citation: 'Claudia Soares, Miguel Vasques, Joao Gomes, "ISEE.U: Distributed online estimation and control for improved target localization accuracy." Publication, 2021.'
---


<p class="publication-authors">Claudia Soares, Miguel Vasques, Joao Gomes</p>

{% raw %}

## Abstract

<div class="publication-abstract"><p>This paper addresses target localization with an online active learning algorithm defined by distributed, simple and fast computations at each node, with no parameters to tune and where the estimate of the target position at each agent is asymptotically equal in expectation to the centralized maximum-likelihood estimator. ISEE.U takes noisy distances at each agent and finds a control that maximizes localization accuracy. We do not assume specific target dynamics and, thus, our method is robust when facing unpredictable targets. Each agent computes the control that maximizes overall target position accuracy via a local estimate of the Fisher Information Matrix. We compared the proposed method with a state of the art algorithm outperforming it when the target movements do not follow a prescribed trajectory, with x100 less computation time, even when our method is running in one central CPU.</p></div>

[Abstract from the later author preprint (2022)](https://arxiv.org/abs/2210.09107).

[Download paper here](https://arxiv.org/abs/2210.09107){:target="_blank"}

## BibTeX

<pre><code>@unpublished{SoaresVasques2019,
    author = &quot;Soares, Claudia and Vasques, Miguel and Gomes, Joao&quot;,
    title = &quot;ISEE.U: Distributed online estimation and control for improved target localization accuracy&quot;,
    year = &quot;2021&quot;,
    abstract = &quot;This paper addresses target localization with an online active learning algorithm defined by distributed, simple and fast computations at each node, with no parameters to tune and where the estimate of the target position at each agent is asymptotically equal in expectation to the centralized maximum-likelihood estimator. ISEE.U takes noisy distances at each agent and finds a control that maximizes localization accuracy. We do not assume specific target dynamics and, thus, our method is robust when facing unpredictable targets. Each agent computes the control that maximizes overall target position accuracy via a local estimate of the Fisher Information Matrix. We compared the proposed method with a state of the art algorithm outperforming it when the target movements do not follow a prescribed trajectory, with x100 less computation time, even when our method is running in one central CPU.&quot;,
    abstractsource = &quot;https://arxiv.org/abs/2210.09107&quot;,
    abstractsourcelabel = &quot;Abstract from the later author preprint (2022)&quot;,
    preprinturl = &quot;https://arxiv.org/abs/2210.09107&quot;
}</code></pre>
{% endraw %}
