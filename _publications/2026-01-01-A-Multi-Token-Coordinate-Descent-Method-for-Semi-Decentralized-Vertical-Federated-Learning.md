---
title: "A Multi-Token Coordinate Descent Method for Semi-Decentralized Vertical Federated Learning"
collection: publications
permalink: /publication/2026-01-01-A-Multi-Token-Coordinate-Descent-Method-for-Semi-Decentralized-Vertical-Federated-Learning
excerpt_separator: ""
description: 'Most federated learning (FL) methods use a client-server scheme, where clients communicate only with a central server.'
excerpt: 'Most federated learning (FL) methods use a client-server scheme, where clients communicate only with a central server. However, this scheme is prone to bandwidth bottlenecks at the server and has a single point of failure. In contrast, in a (fully) decentralized approach, clients communicate directly with each other, dispensing with the server and mitigating these issues. Yet, as the client network grows larger and sparser.'
date: 2026-01-01
venue: 'IEEE Transactions on Signal Processing'
citation_authors: ["Pedro Valdeira", "Yuejie Chi", "Cláudia Soares", "João Xavier"]
citation_year: '2026'
citation_journal: "IEEE Transactions on Signal Processing"
citation_doi: "10.1109/tsp.2026.3652487"
citation_volume: "74"
citation_issn: "1941-0476"
citation_firstpage: '293'
citation_lastpage: '308'
mathjax: true
paperurl: 'http://dx.doi.org/10.1109/tsp.2026.3652487'
preprinturl: 'https://arxiv.org/abs/2309.09977'
citation: 'Pedro Valdeira, Yuejie Chi, Cláudia Soares, João Xavier, "A Multi-Token Coordinate Descent Method for Semi-Decentralized Vertical Federated Learning." IEEE Transactions on Signal Processing, 2026.'
---


<p class="publication-authors">Pedro Valdeira, Yuejie Chi, Cláudia Soares, João Xavier</p>

{% raw %}

## Abstract

<div class="publication-abstract"><p>Most federated learning (FL) methods use a client-server scheme, where clients communicate only with a central server. However, this scheme is prone to bandwidth bottlenecks at the server and has a single point of failure. In contrast, in a (fully) decentralized approach, clients communicate directly with each other, dispensing with the server and mitigating these issues. Yet, as the client network grows larger and sparser, the convergence of decentralized methods slows down, even failing to converge if the network is disconnected. This work addresses this gap between client-server and decentralized schemes, focusing on the vertical FL setup, where clients hold different features of the same samples. We propose multi-token coordinate descent (MTCD), a flexible semi-decentralized method for vertical FL that can exploit both client-server and client-client links. By selecting appropriate hyperparameters, MTCD recovers the client-sever and decentralized schemes as special cases. In fact, its decentralized instance is itself a novel method of independent interest. Yet, by controlling the degree of dependency on client-server links, MTCD can also explore a spectrum of schemes ranging from client-server to decentralized. We prove that, for sufficiently large batch sizes, MTCD converges at an $\mathcal{O}(1/T)$ rate for nonconvex objectives when the tokens roam across disjoint subsets of clients. To capture the aforementioned drawbacks of the client-server scheme succinctly, we model the relative impact of using client-server versus client-client links as the ratio of their &quot;costs&quot;, which depends on the application. This allows us to demonstrate, both analytically and empirically, that by tuning the degree of dependency on the server, the semi-decentralized instances of MTCD can outperform both client-server and decentralized approaches across a range of applications.</p></div>

[Author preprint abstract](https://arxiv.org/abs/2309.09977).

[Download paper here](https://arxiv.org/abs/2309.09977){:target="_blank"}

## BibTeX

<pre><code>@article{Valdeira_2026,
    author = &quot;Valdeira, Pedro and Chi, Yuejie and Soares, Cláudia and Xavier, João&quot;,
    title = &quot;A Multi-Token Coordinate Descent Method for Semi-Decentralized Vertical Federated Learning&quot;,
    volume = &quot;74&quot;,
    ISSN = &quot;1941-0476&quot;,
    url = &quot;http://dx.doi.org/10.1109/tsp.2026.3652487&quot;,
    DOI = &quot;10.1109/tsp.2026.3652487&quot;,
    journal = &quot;IEEE Transactions on Signal Processing&quot;,
    publisher = &quot;Institute of Electrical and Electronics Engineers (IEEE)&quot;,
    year = &quot;2026&quot;,
    pages = &quot;293-308&quot;,
    abstract = {Most federated learning (FL) methods use a client-server scheme, where clients communicate only with a central server. However, this scheme is prone to bandwidth bottlenecks at the server and has a single point of failure. In contrast, in a (fully) decentralized approach, clients communicate directly with each other, dispensing with the server and mitigating these issues. Yet, as the client network grows larger and sparser, the convergence of decentralized methods slows down, even failing to converge if the network is disconnected. This work addresses this gap between client-server and decentralized schemes, focusing on the vertical FL setup, where clients hold different features of the same samples. We propose multi-token coordinate descent (MTCD), a flexible semi-decentralized method for vertical FL that can exploit both client-server and client-client links. By selecting appropriate hyperparameters, MTCD recovers the client-sever and decentralized schemes as special cases. In fact, its decentralized instance is itself a novel method of independent interest. Yet, by controlling the degree of dependency on client-server links, MTCD can also explore a spectrum of schemes ranging from client-server to decentralized. We prove that, for sufficiently large batch sizes, MTCD converges at an $\mathcal{O}(1/T)$ rate for nonconvex objectives when the tokens roam across disjoint subsets of clients. To capture the aforementioned drawbacks of the client-server scheme succinctly, we model the relative impact of using client-server versus client-client links as the ratio of their &quot;costs&quot;, which depends on the application. This allows us to demonstrate, both analytically and empirically, that by tuning the degree of dependency on the server, the semi-decentralized instances of MTCD can outperform both client-server and decentralized approaches across a range of applications.},
    abstractsource = &quot;https://arxiv.org/abs/2309.09977&quot;,
    abstractsourcelabel = &quot;Author preprint abstract&quot;,
    preprinturl = &quot;https://arxiv.org/abs/2309.09977&quot;
}</code></pre>
{% endraw %}
