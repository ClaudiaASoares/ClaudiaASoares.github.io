---
title: "SCENE-Net: Geometric induction for interpretable and low-resource 3D pole detection with Group-Equivariant Non-Expansive Operators"
collection: publications
permalink: /publication/2025-12-01-SCENE-Net-Geometric-induction-for-interpretable-and-low-resource-3D-pole-detection-with-Group-Equivariant-Non-Expansive-Operators
excerpt: 'This paper introduces SCENE-Net, a novel low-resource, white-box model that serves as a compelling proof-of-concept for 3D point cloud segmentation. At its core, SCENE-Net employs Group Equivariant Non-Expansive Operators (GENEOs), a mechanism that leverages geometric priors for enhanced object identification. Our contribution extends the theoretical landscape of geometric learning, highlighting the utility of geometric observers as intrinsic biases in analyzing 3D environments. Through empirical testing.'
date: 2025-12-01
venue: 'Computer Vision and Image Understanding'
paperurl: 'http://dx.doi.org/10.1016/j.cviu.2025.104531'
citation: 'Diogo Lavado, Alessandra Micheletti, Giovanni Bocchi, Patrizio Frosini, Cláudia Soares, "SCENE-Net: Geometric induction for interpretable and low-resource 3D pole detection with Group-Equivariant Non-Expansive Operators." Computer Vision and Image Understanding, 2025.'
---

This paper introduces SCENE-Net, a novel low-resource, white-box model that serves as a compelling proof-of-concept for 3D point cloud segmentation. At its core, SCENE-Net employs Group Equivariant Non-Expansive Operators (GENEOs), a mechanism that leverages geometric priors for enhanced object identification. Our contribution extends the theoretical landscape of geometric learning, highlighting the utility of geometric observers as intrinsic biases in analyzing 3D environments. Through empirical testing and efficiency analysis, we demonstrate the performance of SCENE-Net in detecting power line supporting towers, a key application in forest fire prevention. Our results showcase the superior accuracy and resilience of our model to label noise, achieved with minimal computational resources—this instantiation of SCENE-Net has only eleven trainable parameters—thereby marking a significant step forward in trustworthy machine learning applied to 3D scene understanding. Our code is available in: https://github.com/dlavado/scene-net . • We introduce SCENE-Net, the first white-box model for 3D point cloud segmentation that incorporates interpretable Group Equivariant Non-Expansive Operators (GENEOs) to extract geometric features with minimal supervision. • SCENE-Net achieves high-precision pole detection using only 11 trainable parameters, outperforming black-box baselines on the TS40K dataset and generalizing effectively to SemanticKITTI with state-of-the-art parameter efficiency. • Our approach embeds geometric priors as inductive biases, providing robustness to label noise, input sparsity, and occlusion.

[Access paper here](http://dx.doi.org/10.1016/j.cviu.2025.104531){:target="_blank"}

Bibtex:

<pre><code>@article{Lavado_2025,
    author = &quot;Lavado, Diogo and Micheletti, Alessandra and Bocchi, Giovanni and Frosini, Patrizio and Soares, Cláudia&quot;,
    title = &quot;SCENE-Net: Geometric induction for interpretable and low-resource 3D pole detection with Group-Equivariant Non-Expansive Operators&quot;,
    volume = &quot;262&quot;,
    ISSN = &quot;1077-3142&quot;,
    url = &quot;http://dx.doi.org/10.1016/j.cviu.2025.104531&quot;,
    DOI = &quot;10.1016/j.cviu.2025.104531&quot;,
    journal = &quot;Computer Vision and Image Understanding&quot;,
    publisher = &quot;Elsevier BV&quot;,
    year = &quot;2025&quot;,
    month = &quot;Dec&quot;,
    pages = &quot;104531&quot;,
    abstract = &quot;This paper introduces SCENE-Net, a novel low-resource, white-box model that serves as a compelling proof-of-concept for 3D point cloud segmentation. At its core, SCENE-Net employs Group Equivariant Non-Expansive Operators (GENEOs), a mechanism that leverages geometric priors for enhanced object identification. Our contribution extends the theoretical landscape of geometric learning, highlighting the utility of geometric observers as intrinsic biases in analyzing 3D environments. Through empirical testing and efficiency analysis, we demonstrate the performance of SCENE-Net in detecting power line supporting towers, a key application in forest fire prevention. Our results showcase the superior accuracy and resilience of our model to label noise, achieved with minimal computational resources—this instantiation of SCENE-Net has only eleven trainable parameters—thereby marking a significant step forward in trustworthy machine learning applied to 3D scene understanding. Our code is available in: https://github.com/dlavado/scene-net . • We introduce SCENE-Net, the first white-box model for 3D point cloud segmentation that incorporates interpretable Group Equivariant Non-Expansive Operators (GENEOs) to extract geometric features with minimal supervision. • SCENE-Net achieves high-precision pole detection using only 11 trainable parameters, outperforming black-box baselines on the TS40K dataset and generalizing effectively to SemanticKITTI with state-of-the-art parameter efficiency. • Our approach embeds geometric priors as inductive biases, providing robustness to label noise, input sparsity, and occlusion.&quot;
}</code></pre>
