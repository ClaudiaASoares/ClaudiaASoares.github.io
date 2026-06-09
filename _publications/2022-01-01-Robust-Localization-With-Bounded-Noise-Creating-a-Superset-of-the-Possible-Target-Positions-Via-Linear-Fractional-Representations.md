---
title: "Robust Localization With Bounded Noise: Creating a Superset of the Possible Target Positions via Linear-Fractional Representations"
collection: publications
permalink: /publication/2022-01-01-Robust-Localization-With-Bounded-Noise-Creating-a-Superset-of-the-Possible-Target-Positions-Via-Linear-Fractional-Representations
excerpt: 'Locating a target is key in many applications, namely in high-stakes real-world scenarios, like detecting humans or obstacles in vehicular networks. In scenarios where precise statistics of the measurement noise are unavailable, applications require localization methods that assume minimal knowledge on the noise distribution. We present a scalable algorithm delimiting a tight superset of all possible target locations, assuming range measurements to known landmarks, contaminated.'
date: 2022-01-01
venue: 'IEEE Transactions on Signal Processing'
paperurl: 'http://dx.doi.org/10.1109/tsp.2022.3185899'
citation: 'Joao Domingos, Claudia Soares, Joao Xavier, "Robust Localization With Bounded Noise: Creating a Superset of the Possible Target Positions via Linear-Fractional Representations." IEEE Transactions on Signal Processing, 2022.'
---

Locating a target is key in many applications, namely in high-stakes real-world scenarios, like detecting humans or obstacles in vehicular networks. In scenarios where precise statistics of the measurement noise are unavailable, applications require localization methods that assume minimal knowledge on the noise distribution. We present a scalable algorithm delimiting a tight superset of all possible target locations, assuming range measurements to known landmarks, contaminated with bounded noise and unknown distributions. This superset is of primary interest in robust statistics since it is a tight majorizer of the set of Maximum-Likelihood (ML) estimates parametrized by noise densities respecting two main assumptions: (1) the noise distribution is supported on a ellipsoidal uncertainty region and (2) the measurements are non-negative with probability one. We create the superset through convex relaxations that use Linear Fractional Representations (LFRs), a well-known technique in robust control. For low noise regimes the supersets created by our method double the accuracy of a standard semidefinite relaxation. For moderate to high noise regimes our method still improves the benchmark but the benefit tends to be less significant, as both supersets tend to have the same size (area).

[Access paper here](http://dx.doi.org/10.1109/tsp.2022.3185899){:target="_blank"}

Bibtex:

<pre><code>@article{Domingos_2022,
    author = &quot;Domingos, Joao and Soares, Claudia and Xavier, Joao&quot;,
    title = &quot;Robust Localization With Bounded Noise: Creating a Superset of the Possible Target Positions via Linear-Fractional Representations&quot;,
    volume = &quot;70&quot;,
    ISSN = &quot;1941-0476&quot;,
    url = &quot;http://dx.doi.org/10.1109/tsp.2022.3185899&quot;,
    DOI = &quot;10.1109/tsp.2022.3185899&quot;,
    journal = &quot;IEEE Transactions on Signal Processing&quot;,
    publisher = &quot;Institute of Electrical and Electronics Engineers (IEEE)&quot;,
    year = &quot;2022&quot;,
    pages = &quot;3743-3757&quot;,
    abstract = &quot;Locating a target is key in many applications, namely in high-stakes real-world scenarios, like detecting humans or obstacles in vehicular networks. In scenarios where precise statistics of the measurement noise are unavailable, applications require localization methods that assume minimal knowledge on the noise distribution. We present a scalable algorithm delimiting a tight superset of all possible target locations, assuming range measurements to known landmarks, contaminated with bounded noise and unknown distributions. This superset is of primary interest in robust statistics since it is a tight majorizer of the set of Maximum-Likelihood (ML) estimates parametrized by noise densities respecting two main assumptions: (1) the noise distribution is supported on a ellipsoidal uncertainty region and (2) the measurements are non-negative with probability one. We create the superset through convex relaxations that use Linear Fractional Representations (LFRs), a well-known technique in robust control. For low noise regimes the supersets created by our method double the accuracy of a standard semidefinite relaxation. For moderate to high noise regimes our method still improves the benchmark but the benefit tends to be less significant, as both supersets tend to have the same size (area).&quot;
}</code></pre>
