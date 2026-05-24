---
title: "A majorization-minimization-based method for nonconvex inverse rig problems in facial animation: algorithm derivation"
collection: publications
permalink: /publication/2023-05-01-A-majorization-minimization-based-method-for-nonconvex-inverse-rig-problems-in-facial-animation-algorithm-derivation
excerpt: 'Abstract Automated methods for facial animation are a necessary tool in the modern industry since the standard blendshape head models consist of hundreds of controllers, and a manual approach is painfully slow. Different solutions have been proposed that produce output in real-time or generalize well for different face topologies. However, all these prior works consider a linear approximation of the blendshape function and hence do.'
date: 2023-05-01
venue: 'Optimization Letters'
paperurl: 'http://dx.doi.org/10.1007/s11590-023-02012-w'
citation: 'Stevo Racković, Cláudia Soares, Dušan Jakovetić, Zoranka Desnica, "A majorization-minimization-based method for nonconvex inverse rig problems in facial animation: algorithm derivation." Optimization Letters, 2023.'
---

Abstract Automated methods for facial animation are a necessary tool in the modern industry since the standard blendshape head models consist of hundreds of controllers, and a manual approach is painfully slow. Different solutions have been proposed that produce output in real-time or generalize well for different face topologies. However, all these prior works consider a linear approximation of the blendshape function and hence do not provide a high-enough level of detail for modern realistic human face reconstruction. A second-order blendshape approximation leads to higher fidelity facial animation but generates a non-linear least squares optimization problem with high dimensionality. We derive a method for solving the inverse rig in blendshape animation using quadratic corrective terms, which increases accuracy. At the same time, due to the proposed construction of the objective function, it yields a sparser estimated weight vector compared to the state-of-the-art methods. The former feature means lower demand for subsequent manual corrections of the solution, while the latter indicates that the manual modifications are also easier to include. Our algorithm is iterative and employs a Majorization-Minimization paradigm to cope with the increased complexity produced by adding corrective terms. The surrogate function is easy to solve and allows for further parallelization on the component level within each iteration. This paper is complementary to an accompanying paper (Racković et al. arxiv preprint. https://arxiv.org/abs/2302.04843 , 2023) where we provide detailed experimental results and discussion, including highly-realistic animation data, and show a clear superiority of the results compared to the state-of-the-art methods.

[Access paper here](http://dx.doi.org/10.1007/s11590-023-02012-w){:target="_blank"}

Bibtex:

<pre><code>@article{Rackovi__2023-2,
    author = &quot;Racković, Stevo and Soares, Cláudia and Jakovetić, Dušan and Desnica, Zoranka&quot;,
    title = &quot;A majorization-minimization-based method for nonconvex inverse rig problems in facial animation: algorithm derivation&quot;,
    volume = &quot;18&quot;,
    ISSN = &quot;1862-4480&quot;,
    url = &quot;http://dx.doi.org/10.1007/s11590-023-02012-w&quot;,
    DOI = &quot;10.1007/s11590-023-02012-w&quot;,
    number = &quot;2&quot;,
    journal = &quot;Optimization Letters&quot;,
    publisher = &quot;Springer Science and Business Media LLC&quot;,
    year = &quot;2023&quot;,
    month = &quot;May&quot;,
    pages = &quot;545-559&quot;,
    abstract = &quot;Abstract Automated methods for facial animation are a necessary tool in the modern industry since the standard blendshape head models consist of hundreds of controllers, and a manual approach is painfully slow. Different solutions have been proposed that produce output in real-time or generalize well for different face topologies. However, all these prior works consider a linear approximation of the blendshape function and hence do not provide a high-enough level of detail for modern realistic human face reconstruction. A second-order blendshape approximation leads to higher fidelity facial animation but generates a non-linear least squares optimization problem with high dimensionality. We derive a method for solving the inverse rig in blendshape animation using quadratic corrective terms, which increases accuracy. At the same time, due to the proposed construction of the objective function, it yields a sparser estimated weight vector compared to the state-of-the-art methods. The former feature means lower demand for subsequent manual corrections of the solution, while the latter indicates that the manual modifications are also easier to include. Our algorithm is iterative and employs a Majorization-Minimization paradigm to cope with the increased complexity produced by adding corrective terms. The surrogate function is easy to solve and allows for further parallelization on the component level within each iteration. This paper is complementary to an accompanying paper (Racković et al. arxiv preprint. https://arxiv.org/abs/2302.04843 , 2023) where we provide detailed experimental results and discussion, including highly-realistic animation data, and show a clear superiority of the results compared to the state-of-the-art methods.&quot;
}</code></pre>
