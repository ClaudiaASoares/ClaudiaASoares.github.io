---
title: "Refined Inverse Rigging: A Balanced Approach to High-fidelity Blendshape Animation"
collection: publications
permalink: /publication/2024-12-01-Refined-Inverse-Rigging-A-Balanced-Approach-to-High-fidelity-Blendshape-Animation
excerpt_separator: ""
description: 'In this paper, we present an advanced approach to solving the inverse rig problem in blendshape animation, using high-quality corrective blendshapes.'
excerpt: 'In this paper, we present an advanced approach to solving the inverse rig problem in blendshape animation, using high-quality corrective blendshapes. Our algorithm focuses on three key areas: ensuring high data fidelity in reconstructed meshes, achieving greater sparsity in weight distributions, and facilitating smoother frame-to-frame transitions. While the incorporation of corrective terms is a known practice, our method differentiates itself by employing a unique combination…'
excerpt_truncated: true
date: 2024-12-01
venue: 'SIGGRAPH Asia 2024 Conference Papers'
citation_authors: ["Stevo Racković", "Dušan Jakovetić", "Cláudia Soares"]
citation_year: '2024'
citation_conference: "SIGGRAPH Asia 2024 Conference Papers"
citation_doi: "10.1145/3680528.3687670"
citation_firstpage: '1'
citation_lastpage: '9'
paperurl: 'http://dx.doi.org/10.1145/3680528.3687670'
citation: 'Stevo Racković, Dušan Jakovetić, Cláudia Soares, "Refined Inverse Rigging: A Balanced Approach to High-fidelity Blendshape Animation." SIGGRAPH Asia 2024 Conference Papers, 2024.'
---


<p class="publication-authors">Stevo Racković, Dušan Jakovetić, Cláudia Soares</p>

{% raw %}

## Abstract

<div class="publication-abstract"><p>In this paper, we present an advanced approach to solving the inverse rig problem in blendshape animation, using high-quality corrective blendshapes. Our algorithm focuses on three key areas: ensuring high data fidelity in reconstructed meshes, achieving greater sparsity in weight distributions, and facilitating smoother frame-to-frame transitions. While the incorporation of corrective terms is a known practice, our method differentiates itself by employing a unique combination of l1 norm regularization for sparsity and a temporal smoothness constraint through roughness penalty, focusing on the sum of second differences in consecutive frame weights. A significant innovation in our approach is the temporal decoupling of blendshapes, which permits simultaneous optimization across entire animation sequences. This feature sets our work apart from existing methods and contributes to a more efficient and effective solution. Our algorithm exhibits a marked improvement in maintaining data fidelity and ensuring smooth frame transitions when compared to prior approaches that either lack smoothness regularization or rely solely on linear blendshape models. In addition to superior mesh resemblance and smoothness, our method offers practical benefits, including reduced computational complexity and execution time, achieved through a novel parallelization strategy using clustering methods. Our results not only advance the state-of-the-art in terms of fidelity, sparsity, and smoothness in inverse rigging but also introduce significant efficiency improvements.</p></div>

[Published abstract source](https://researchportal.ulisboa.pt/pt/publications/refined-inverse-rigging-a-balanced-approach-to-high-fidelity-blen/).

[Access paper here](http://dx.doi.org/10.1145/3680528.3687670){:target="_blank"}

## BibTeX

<pre><code>@inproceedings{Rackovi__2024,
    author = &quot;Racković, Stevo and Jakovetić, Dušan and Soares, Cláudia&quot;,
    series = &quot;SA ’24&quot;,
    title = &quot;Refined Inverse Rigging: A Balanced Approach to High-fidelity Blendshape Animation&quot;,
    url = &quot;http://dx.doi.org/10.1145/3680528.3687670&quot;,
    DOI = &quot;10.1145/3680528.3687670&quot;,
    booktitle = &quot;SIGGRAPH Asia 2024 Conference Papers&quot;,
    publisher = &quot;ACM&quot;,
    year = &quot;2024&quot;,
    month = &quot;Dec&quot;,
    pages = &quot;1-9&quot;,
    collection = &quot;SA ’24&quot;,
    abstract = &quot;In this paper, we present an advanced approach to solving the inverse rig problem in blendshape animation, using high-quality corrective blendshapes. Our algorithm focuses on three key areas: ensuring high data fidelity in reconstructed meshes, achieving greater sparsity in weight distributions, and facilitating smoother frame-to-frame transitions. While the incorporation of corrective terms is a known practice, our method differentiates itself by employing a unique combination of l1 norm regularization for sparsity and a temporal smoothness constraint through roughness penalty, focusing on the sum of second differences in consecutive frame weights. A significant innovation in our approach is the temporal decoupling of blendshapes, which permits simultaneous optimization across entire animation sequences. This feature sets our work apart from existing methods and contributes to a more efficient and effective solution. Our algorithm exhibits a marked improvement in maintaining data fidelity and ensuring smooth frame transitions when compared to prior approaches that either lack smoothness regularization or rely solely on linear blendshape models. In addition to superior mesh resemblance and smoothness, our method offers practical benefits, including reduced computational complexity and execution time, achieved through a novel parallelization strategy using clustering methods. Our results not only advance the state-of-the-art in terms of fidelity, sparsity, and smoothness in inverse rigging but also introduce significant efficiency improvements.&quot;,
    abstractsource = &quot;https://researchportal.ulisboa.pt/pt/publications/refined-inverse-rigging-a-balanced-approach-to-high-fidelity-blen/&quot;,
    abstractsourcelabel = &quot;Published abstract source&quot;
}</code></pre>
{% endraw %}
