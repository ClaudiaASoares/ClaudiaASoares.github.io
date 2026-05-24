---
title: "Maximum likelihood localization of a network of moving agents from ranges, bearings and velocity measurements"
collection: publications
permalink: /publication/2024-08-01-Maximum-likelihood-localization-of-a-network-of-moving-agents-from-ranges-bearings-and-velocity-measurements
excerpt: 'Localization is a fundamental enabler technology for many applications, like vehicular networks, IoT, and even medicine. While Global Navigation Satellite Systems solutions offer great performance, they are unavailable in scenarios like indoor or underwater environments, and, for large networks, the instrumentation cost is prohibitive. We develop a localization algorithm from ranges and bearings, suitable for generic mobile networks. Our algorithm is built on a tight.'
date: 2024-08-01
venue: 'Signal Processing'
paperurl: 'http://dx.doi.org/10.1016/j.sigpro.2024.109471'
citation: 'Filipa Valdeira, Cláudia Soares, João Gomes, "Maximum likelihood localization of a network of moving agents from ranges, bearings and velocity measurements." Signal Processing, 2024.'
---

Localization is a fundamental enabler technology for many applications, like vehicular networks, IoT, and even medicine. While Global Navigation Satellite Systems solutions offer great performance, they are unavailable in scenarios like indoor or underwater environments, and, for large networks, the instrumentation cost is prohibitive. We develop a localization algorithm from ranges and bearings, suitable for generic mobile networks. Our algorithm is built on a tight convex relaxation of the Maximum Likelihood position estimator. To serve positioning to mobile agents, a horizon-based version is developed accounting for velocity measurements at each agent. To solve the convex problem, a distributed gradient-based method is provided. This constitutes an advantage over centralized approaches, which usually exhibit high latency for large networks and present a single point of failure. Additionally, the algorithm estimates all required parameters and effectively becomes parameter-free. Our solution to the dynamic network localization problem is theoretically well-founded and still easy to understand. We obtain a parameter-free, outlier-robust and trajectory-agnostic algorithm, with nearly constant positioning error regardless of the trajectories of agents and anchors, achieving better or comparable performance to state-of-the-art methods, as our simulations show. Furthermore, the method is distributed, convex and does not require any particular anchor configuration. • Cooperative localization for mobile networks from range, bearing and velocity measurements. • Maximum Likelihood formulation followed by a convex relaxation maintains performance despite of initialization. • Distributed implementation makes the algorithm scalable for large networks. • Parameter estimation step avoids the need for a priori knowledge of noise terms. • The method does not rely on a dynamical model of the system.

[Access paper here](http://dx.doi.org/10.1016/j.sigpro.2024.109471){:target="_blank"}

Bibtex:

<pre><code>@article{Valdeira_2024,
    author = &quot;Valdeira, Filipa and Soares, Cláudia and Gomes, João&quot;,
    title = &quot;Maximum likelihood localization of a network of moving agents from ranges, bearings and velocity measurements&quot;,
    volume = &quot;221&quot;,
    ISSN = &quot;0165-1684&quot;,
    url = &quot;http://dx.doi.org/10.1016/j.sigpro.2024.109471&quot;,
    DOI = &quot;10.1016/j.sigpro.2024.109471&quot;,
    journal = &quot;Signal Processing&quot;,
    publisher = &quot;Elsevier BV&quot;,
    year = &quot;2024&quot;,
    month = &quot;Aug&quot;,
    pages = &quot;109471&quot;,
    abstract = &quot;Localization is a fundamental enabler technology for many applications, like vehicular networks, IoT, and even medicine. While Global Navigation Satellite Systems solutions offer great performance, they are unavailable in scenarios like indoor or underwater environments, and, for large networks, the instrumentation cost is prohibitive. We develop a localization algorithm from ranges and bearings, suitable for generic mobile networks. Our algorithm is built on a tight convex relaxation of the Maximum Likelihood position estimator. To serve positioning to mobile agents, a horizon-based version is developed accounting for velocity measurements at each agent. To solve the convex problem, a distributed gradient-based method is provided. This constitutes an advantage over centralized approaches, which usually exhibit high latency for large networks and present a single point of failure. Additionally, the algorithm estimates all required parameters and effectively becomes parameter-free. Our solution to the dynamic network localization problem is theoretically well-founded and still easy to understand. We obtain a parameter-free, outlier-robust and trajectory-agnostic algorithm, with nearly constant positioning error regardless of the trajectories of agents and anchors, achieving better or comparable performance to state-of-the-art methods, as our simulations show. Furthermore, the method is distributed, convex and does not require any particular anchor configuration. • Cooperative localization for mobile networks from range, bearing and velocity measurements. • Maximum Likelihood formulation followed by a convex relaxation maintains performance despite of initialization. • Distributed implementation makes the algorithm scalable for large networks. • Parameter estimation step avoids the need for a priori knowledge of noise terms. • The method does not rely on a dynamical model of the system.&quot;
}</code></pre>
