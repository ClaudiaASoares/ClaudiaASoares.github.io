---
title: "Communication-Efficient Vertical Federated Learning via Compressed Error Feedback"
collection: publications
permalink: /publication/2025-01-01-Communication-Efficient-Vertical-Federated-Learning-via-Compressed-Error-Feedback
excerpt_separator: ""
description: 'Communication overhead is a known bottleneck in federated learning (FL).'
excerpt: 'Communication overhead is a known bottleneck in federated learning (FL). To address this, lossy compression is commonly used on the information communicated between the server and clients during training. In horizontal FL, where each client holds a subset of the samples, such communication-compressed training methods have recently seen significant progress. However, in their vertical FL counterparts, where each client holds a subset of the features…'
excerpt_truncated: true
date: 2025-01-01
venue: 'IEEE Transactions on Signal Processing'
citation_authors: ["Pedro Valdeira", "João Xavier", "Cláudia Soares", "Yuejie Chi"]
citation_year: '2025'
citation_journal: "IEEE Transactions on Signal Processing"
citation_doi: "10.1109/tsp.2025.3540655"
citation_volume: "73"
citation_issn: "1941-0476"
citation_firstpage: '1065'
citation_lastpage: '1080'
mathjax: true
paperurl: 'http://dx.doi.org/10.1109/tsp.2025.3540655'
citation: 'Pedro Valdeira, João Xavier, Cláudia Soares, Yuejie Chi, "Communication-Efficient Vertical Federated Learning via Compressed Error Feedback." IEEE Transactions on Signal Processing, 2025.'
---


<p class="publication-authors">Pedro Valdeira, João Xavier, Cláudia Soares, Yuejie Chi</p>

{% raw %}

## Abstract

<div class="publication-abstract"><p>Communication overhead is a known bottleneck in federated learning (FL). To address this, lossy compression is commonly used on the information communicated between the server and clients during training. In horizontal FL, where each client holds a subset of the samples, such communication-compressed training methods have recently seen significant progress. However, in their vertical FL counterparts, where each client holds a subset of the features, our understanding remains limited. To address this, we propose an error feedback compressed vertical federated learning (EF-VFL) method to train split neural networks. In contrast to previous communication-compressed methods for vertical FL, EF-VFL does not require a vanishing compression error for the gradient norm to converge to zero for smooth nonconvex problems. By leveraging error feedback, our method can achieve a $\mathcal{O}({1}/{T})$ convergence rate for a sufficiently large batch size, improving over the state-of-the-art $\mathcal{O}({1}/{\sqrt{T}})$ rate under $\mathcal{O}({1}/{\sqrt{T}})$ compression error, and matching the rate of uncompressed methods. Further, when the objective function satisfies the Polyak-Łojasiewicz inequality, our method converges linearly. In addition to improving convergence, our method also supports the use of private labels. Numerical experiments show that EF-VFL significantly improves over the prior art, confirming our theoretical results.</p></div>

[Access paper here](http://dx.doi.org/10.1109/tsp.2025.3540655){:target="_blank"}

## BibTeX

<pre><code>@article{Valdeira_2025,
    author = &quot;Valdeira, Pedro and Xavier, João and Soares, Cláudia and Chi, Yuejie&quot;,
    title = &quot;Communication-Efficient Vertical Federated Learning via Compressed Error Feedback&quot;,
    volume = &quot;73&quot;,
    ISSN = &quot;1941-0476&quot;,
    url = &quot;http://dx.doi.org/10.1109/tsp.2025.3540655&quot;,
    DOI = &quot;10.1109/tsp.2025.3540655&quot;,
    journal = &quot;IEEE Transactions on Signal Processing&quot;,
    publisher = &quot;Institute of Electrical and Electronics Engineers (IEEE)&quot;,
    year = &quot;2025&quot;,
    pages = &quot;1065-1080&quot;,
    abstract = {Communication overhead is a known bottleneck in federated learning (FL). To address this, lossy compression is commonly used on the information communicated between the server and clients during training. In horizontal FL, where each client holds a subset of the samples, such communication-compressed training methods have recently seen significant progress. However, in their vertical FL counterparts, where each client holds a subset of the features, our understanding remains limited. To address this, we propose an error feedback compressed vertical federated learning (&lt;monospace xmlns:mml=&quot;http://www.w3.org/1998/Math/MathML&quot; xmlns:xlink=&quot;http://www.w3.org/1999/xlink&quot;&gt;EF-VFL&lt;/monospace&gt;) method to train split neural networks. In contrast to previous communication-compressed methods for vertical FL, &lt;monospace xmlns:mml=&quot;http://www.w3.org/1998/Math/MathML&quot; xmlns:xlink=&quot;http://www.w3.org/1999/xlink&quot;&gt;EF-VFL&lt;/monospace&gt; does not require a vanishing compression error for the gradient norm to converge to zero for smooth nonconvex problems. By leveraging error feedback, our method can achieve a &lt;inline-formula xmlns:mml=&quot;http://www.w3.org/1998/Math/MathML&quot; xmlns:xlink=&quot;http://www.w3.org/1999/xlink&quot;&gt;&lt;tex-math notation=&quot;LaTeX&quot;&gt;$\mathcal{O}({1}/{T})$&lt;/tex-math&gt;&lt;/inline-formula&gt; convergence rate for a sufficiently large batch size, improving over the state-of-the-art &lt;inline-formula xmlns:mml=&quot;http://www.w3.org/1998/Math/MathML&quot; xmlns:xlink=&quot;http://www.w3.org/1999/xlink&quot;&gt;&lt;tex-math notation=&quot;LaTeX&quot;&gt;$\mathcal{O}({1}/{\sqrt{T}})$&lt;/tex-math&gt;&lt;/inline-formula&gt; rate under &lt;inline-formula xmlns:mml=&quot;http://www.w3.org/1998/Math/MathML&quot; xmlns:xlink=&quot;http://www.w3.org/1999/xlink&quot;&gt;&lt;tex-math notation=&quot;LaTeX&quot;&gt;$\mathcal{O}({1}/{\sqrt{T}})$&lt;/tex-math&gt;&lt;/inline-formula&gt; compression error, and matching the rate of uncompressed methods. Further, when the objective function satisfies the Polyak-Łojasiewicz inequality, our method converges linearly. In addition to improving convergence, our method also supports the use of private labels. Numerical experiments show that &lt;monospace xmlns:mml=&quot;http://www.w3.org/1998/Math/MathML&quot; xmlns:xlink=&quot;http://www.w3.org/1999/xlink&quot;&gt;EF-VFL&lt;/monospace&gt; significantly improves over the prior art, confirming our theoretical results.}
}</code></pre>
{% endraw %}
