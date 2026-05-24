---
title: "Distributed Solution of the Blendshape Rig Inversion Problem"
collection: publications
permalink: /publication/2023-11-01-Distributed-Solution-of-the-Blendshape-Rig-Inversion-Problem
excerpt: 'The problem of rig inversion is central in facial animation, but with the increasing complexity of modern blendshape models, execution times increase beyond practically feasible solutions. A possible approach towards a faster solution is clustering, which exploits the spacial nature of the face, leading to a distributed method. In this paper, we go a step further, involving cluster coupling to get more confident estimates of.'
date: 2023-11-01
venue: 'SIGGRAPH Asia 2023 Technical Communications'
paperurl: 'http://dx.doi.org/10.1145/3610543.3626166'
citation: 'Stevo Racković, Cláudia Soares, Dušan Jakovetić, "Distributed Solution of the Blendshape Rig Inversion Problem." SIGGRAPH Asia 2023 Technical Communications, 2023.'
---

The problem of rig inversion is central in facial animation, but with the increasing complexity of modern blendshape models, execution times increase beyond practically feasible solutions. A possible approach towards a faster solution is clustering, which exploits the spacial nature of the face, leading to a distributed method. In this paper, we go a step further, involving cluster coupling to get more confident estimates of the overlapping components. Our algorithm applies the Alternating Direction Method of Multipliers, sharing the overlapping weights between the subproblems and show a clear advantage over the naive clustered approach. The method applies to an arbitrary clustering of the face. We also introduce a novel method for choosing the number of clusters in a data-free manner, resulting in a sparse clustering graph without losing essential information. Finally, we give a new variant of a data-free clustering algorithm that produces good scores with respect to the mentioned strategy for choosing the optimal clustering.

[Access paper here](http://dx.doi.org/10.1145/3610543.3626166){:target="_blank"}

Bibtex:

<pre><code>@inproceedings{Rackovi__2023,
    author = &quot;Racković, Stevo and Soares, Cláudia and Jakovetić, Dušan&quot;,
    series = &quot;SA ’23&quot;,
    title = &quot;Distributed Solution of the Blendshape Rig Inversion Problem&quot;,
    url = &quot;http://dx.doi.org/10.1145/3610543.3626166&quot;,
    DOI = &quot;10.1145/3610543.3626166&quot;,
    booktitle = &quot;SIGGRAPH Asia 2023 Technical Communications&quot;,
    publisher = &quot;ACM&quot;,
    year = &quot;2023&quot;,
    month = &quot;Nov&quot;,
    pages = &quot;1-4&quot;,
    collection = &quot;SA ’23&quot;,
    abstract = &quot;The problem of rig inversion is central in facial animation, but with the increasing complexity of modern blendshape models, execution times increase beyond practically feasible solutions. A possible approach towards a faster solution is clustering, which exploits the spacial nature of the face, leading to a distributed method. In this paper, we go a step further, involving cluster coupling to get more confident estimates of the overlapping components. Our algorithm applies the Alternating Direction Method of Multipliers, sharing the overlapping weights between the subproblems and show a clear advantage over the naive clustered approach. The method applies to an arbitrary clustering of the face. We also introduce a novel method for choosing the number of clusters in a data-free manner, resulting in a sparse clustering graph without losing essential information. Finally, we give a new variant of a data-free clustering algorithm that produces good scores with respect to the mentioned strategy for choosing the optimal clustering.&quot;
}</code></pre>
