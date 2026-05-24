---
title: "LocDyn: Robust Distributed Localization for Mobile Underwater Networks"
collection: publications
permalink: /publication/2017-10-01-LocDyn-Robust-Distributed-Localization-for-Mobile-Underwater-Networks
excerpt: 'How do we self-localize large teams of underwater nodes using only noisy range measurements? How do we do it in a distributed way, and incorporating dynamics into the problem? How do we reject outliers and produce trustworthy position estimates? And what if some of the vehicles can measure angular information? The stringent acoustic communication constraints and accuracy needs of our geophysical survey application demand fast.'
date: 2017-10-01
venue: 'IEEE Journal of Oceanic Engineering'
paperurl: 'http://dx.doi.org/10.1109/joe.2017.2736951'
citation: 'Claudia Soares, Joao Gomes, Beatriz Quintino Ferreira, Joao Paulo Costeira, "LocDyn: Robust Distributed Localization for Mobile Underwater Networks." IEEE Journal of Oceanic Engineering, 2017.'
---

How do we self-localize large teams of underwater nodes using only noisy range measurements? How do we do it in a distributed way, and incorporating dynamics into the problem? How do we reject outliers and produce trustworthy position estimates? And what if some of the vehicles can measure angular information? The stringent acoustic communication constraints and accuracy needs of our geophysical survey application demand fast and very accurate localization methods. We address dynamic localization as a MAP estimation problem where the prior encodes kinematic information, and we apply a convex relaxation method that takes advantage of previous estimates at each measurement acquisition step. The resulting LocDyn algorithm is fast: It converges at an optimal rate for first order methods. LocDyn is distributed: There is no fusion center responsible for processing acquired data and the same simple computations are performed at each node. LocDyn is accurate: Numerical experiments attest to about 30% smaller positioning error than a comparable Kalman filter. LocDyn is robust: It rejects outlier noise, while benchmarking methods succumb in terms of positioning error.

[Access paper here](http://dx.doi.org/10.1109/joe.2017.2736951){:target="_blank"}

Bibtex:

<pre><code>@article{Soares_2017,
    author = &quot;Soares, Claudia and Gomes, Joao and Ferreira, Beatriz Quintino and Costeira, Joao Paulo&quot;,
    title = &quot;LocDyn: Robust Distributed Localization for Mobile Underwater Networks&quot;,
    volume = &quot;42&quot;,
    ISSN = &quot;2373-7786&quot;,
    url = &quot;http://dx.doi.org/10.1109/joe.2017.2736951&quot;,
    DOI = &quot;10.1109/joe.2017.2736951&quot;,
    number = &quot;4&quot;,
    journal = &quot;IEEE Journal of Oceanic Engineering&quot;,
    publisher = &quot;Institute of Electrical and Electronics Engineers (IEEE)&quot;,
    year = &quot;2017&quot;,
    month = &quot;Oct&quot;,
    pages = &quot;1063-1074&quot;,
    abstract = &quot;How do we self-localize large teams of underwater nodes using only noisy range measurements? How do we do it in a distributed way, and incorporating dynamics into the problem? How do we reject outliers and produce trustworthy position estimates? And what if some of the vehicles can measure angular information? The stringent acoustic communication constraints and accuracy needs of our geophysical survey application demand fast and very accurate localization methods. We address dynamic localization as a MAP estimation problem where the prior encodes kinematic information, and we apply a convex relaxation method that takes advantage of previous estimates at each measurement acquisition step. The resulting LocDyn algorithm is fast: It converges at an optimal rate for first order methods. LocDyn is distributed: There is no fusion center responsible for processing acquired data and the same simple computations are performed at each node. LocDyn is accurate: Numerical experiments attest to about 30\\% smaller positioning error than a comparable Kalman filter. LocDyn is robust: It rejects outlier noise, while benchmarking methods succumb in terms of positioning error.&quot;
}</code></pre>
