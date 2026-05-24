---
title: "STRONG: Synchronous and asynchronous robust network localization, under non-Gaussian noise"
collection: publications
permalink: /publication/2021-01-01-STRONG-Synchronous-and-asynchronous-robust-network-localization-under-non-Gaussian-noise
excerpt: 'Real-world network applications must cope with failing nodes, malicious attacks, or nodes facing corrupted data — data classified as outliers. Our work addresses these concerns in the scope of the sensor network localization problem where, despite the abundance of technical literature, prior research seldom considered outlier data. We propose robust, fast, and distributed network localization algorithms, resilient to high-power noise, but also precise under regular.'
date: 2021-01-01
venue: 'Signal Processing'
paperurl: 'https://www.sciencedirect.com/science/article/pii/S0165168421001043'
citation: 'Cláudia Soares, João Gomes, "STRONG: Synchronous and asynchronous robust network localization, under non-Gaussian noise." Signal Processing, 2021.'
---

Real-world network applications must cope with failing nodes, malicious attacks, or nodes facing corrupted data — data classified as outliers. Our work addresses these concerns in the scope of the sensor network localization problem where, despite the abundance of technical literature, prior research seldom considered outlier data. We propose robust, fast, and distributed network localization algorithms, resilient to high-power noise, but also precise under regular Gaussian noise. We use a Huber M-estimator, thus obtaining a robust (but nonconvex) optimization problem. We convexify and change the problem representation, to allow for distributed robust localization algorithms: a synchronous distributed method that has optimal convergence rate and an asynchronous one with proven convergence guarantees. A major highlight of our contribution lies on the fact that we pay no price for provable distributed computation neither in accuracy, nor in communication cost or convergence speed. Simulations showcase the superior performance of our algorithms, both in the presence of outliers and under regular Gaussian noise: our method exceeds the accuracy of alternative approaches, distributed and centralized, even under heavy additive and multiplicative outlier noise.

[Access paper here](https://www.sciencedirect.com/science/article/pii/S0165168421001043){:target="_blank"}

Bibtex:

<pre><code>@article{Strong21,
    author = &quot;Soares, Cláudia and Gomes, João&quot;,
    title = &quot;STRONG: Synchronous and asynchronous robust network localization, under non-Gaussian noise&quot;,
    journal = &quot;Signal Processing&quot;,
    volume = &quot;185&quot;,
    pages = &quot;108066&quot;,
    year = &quot;2021&quot;,
    issn = &quot;0165-1684&quot;,
    doi = &quot;https://doi.org/10.1016/j.sigpro.2021.108066&quot;,
    url = &quot;https://www.sciencedirect.com/science/article/pii/S0165168421001043&quot;,
    keywords = &quot;Distributed localization algorithms, Robust estimation, Huber function, Convex relaxation, Nonconvex optimization, Distributed iterative network localization, Sensor networks&quot;,
    abstract = &quot;Real-world network applications must cope with failing nodes, malicious attacks, or nodes facing corrupted data — data classified as outliers. Our work addresses these concerns in the scope of the sensor network localization problem where, despite the abundance of technical literature, prior research seldom considered outlier data. We propose robust, fast, and distributed network localization algorithms, resilient to high-power noise, but also precise under regular Gaussian noise. We use a Huber M-estimator, thus obtaining a robust (but nonconvex) optimization problem. We convexify and change the problem representation, to allow for distributed robust localization algorithms: a synchronous distributed method that has optimal convergence rate and an asynchronous one with proven convergence guarantees. A major highlight of our contribution lies on the fact that we pay no price for provable distributed computation neither in accuracy, nor in communication cost or convergence speed. Simulations showcase the superior performance of our algorithms, both in the presence of outliers and under regular Gaussian noise: our method exceeds the accuracy of alternative approaches, distributed and centralized, even under heavy additive and multiplicative outlier noise.&quot;
}</code></pre>
