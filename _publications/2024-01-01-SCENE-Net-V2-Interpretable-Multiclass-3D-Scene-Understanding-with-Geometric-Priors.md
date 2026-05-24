---
title: "SCENE-Net V2: Interpretable Multiclass 3D Scene Understanding with Geometric Priors"
collection: publications
permalink: /publication/2024-01-01-SCENE-Net-V2-Interpretable-Multiclass-3D-Scene-Understanding-with-Geometric-Priors
excerpt: 'In this paper, we present SCENE-Net V2, a new resource-efficient, textbfgray-box model for multiclass 3D scene understanding. SCENE-Net V2 leverages Group Equivariant Non-Expansive Operators (GENEOs) to incorporate fundamental geometric priors as inductive biases, offering a more transparent alternative to the prevalent black-box models in the domain. This model addresses the limitations of its white-box predecessor, SCENE-Net, by expanding its applicability from pole-like structures to a.'
date: 2024-01-01
venue: 'ICML 2024 Workshop GRaM'
paperurl: 'https://openreview.net/forum?id=6pKRn6tttu'
citation: 'Diogo Mateus Lavado, Claudia Soares, Alessandra Micheletti, "SCENE-Net V2: Interpretable Multiclass 3D Scene Understanding with Geometric Priors." ICML 2024 Workshop GRaM, 2024.'
---

In this paper, we present SCENE-Net V2, a new resource-efficient, textbfgray-box model for multiclass 3D scene understanding. SCENE-Net V2 leverages Group Equivariant Non-Expansive Operators (GENEOs) to incorporate fundamental geometric priors as inductive biases, offering a more transparent alternative to the prevalent black-box models in the domain. This model addresses the limitations of its white-box predecessor, SCENE-Net, by expanding its applicability from pole-like structures to a wider range of datasets with detailed 3D elements. Our model achieves the sweet-spot between application and transparency: SCENE-Net V2 is a general method for object identification with interpretability guarantees. Our experimental results demonstrate that SCENE-Net V2 achieves competitive performance with a significantly lower parameter count. Furthermore, we propose the use of GENEO-based architectures as a feature extraction tool for black-box models, enabling an increase in performance by adding a minimal number of meaningful parameters. Our code is available in: https://github.com/dlavado/SCENE-Net-V2

[Access paper here](https://openreview.net/forum?id=6pKRn6tttu){:target="_blank"}

Bibtex:

<pre><code>@inproceedings{Lavado2024scene-net-v2,
    author = &quot;Lavado, Diogo Mateus and Soares, Claudia and Micheletti, Alessandra&quot;,
    title = &quot;SCENE-Net V2: Interpretable Multiclass 3D Scene Understanding with Geometric Priors&quot;,
    booktitle = &quot;ICML 2024 Workshop GRaM&quot;,
    url = &quot;https://openreview.net/forum?id=6pKRn6tttu&quot;,
    year = &quot;2024&quot;,
    eprint = &quot;https://openreview.net/pdf?id=lavado|scenenet\\_v2\\_interpretable\\_multiclass\\_3d\\_scene\\_understanding\\_with\\_geometric\\_priors&quot;,
    organization = &quot;ICML.cc/2024/Workshop/GRaM&quot;,
    abstract = &quot;In this paper, we present SCENE-Net V2, a new resource-efficient, \textbf{gray-box model} for multiclass 3D scene understanding. SCENE-Net V2 leverages Group Equivariant Non-Expansive Operators (GENEOs) to incorporate fundamental geometric priors as inductive biases, offering a more transparent alternative to the prevalent black-box models in the domain. This model addresses the limitations of its white-box predecessor, SCENE-Net, by expanding its applicability from pole-like structures to a wider range of datasets with detailed 3D elements. Our model achieves the sweet-spot between application and transparency: SCENE-Net V2 is a general method for object identification with interpretability guarantees. Our experimental results demonstrate that SCENE-Net V2 achieves competitive performance with a significantly lower parameter count. Furthermore, we propose the use of GENEO-based architectures as a feature extraction tool for black-box models, enabling an increase in performance by adding a minimal number of meaningful parameters. Our code is available in: https://github.com/dlavado/SCENE-Net-V2&quot;
}</code></pre>
