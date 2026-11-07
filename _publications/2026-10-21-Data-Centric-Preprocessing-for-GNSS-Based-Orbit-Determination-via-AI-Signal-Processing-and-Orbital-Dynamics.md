---
title: "Data-Centric Preprocessing for GNSS-Based Orbit Determination via AI, Signal Processing, and Orbital Dynamics"
collection: publications
permalink: /publication/2026-10-21-Data-Centric-Preprocessing-for-GNSS-Based-Orbit-Determination-via-AI-Signal-Processing-and-Orbital-Dynamics
excerpt_separator: ""
description: 'GNSS-based orbit determination relies on input measurements whose quality can vary significantly across mission phases and operating conditions.'
excerpt: 'GNSS-based orbit determination relies on input measurements whose quality can vary significantly across mission phases and operating conditions. In such settings, inappropriate data conditioning may either improve estimation robustness or, if misapplied, degrade convergence and numerical stability. This work proposes a data-centric preprocessing pipeline designed to operate safely under heterogeneous data quality conditions. The method combines lightweight physical sanity checks with a structure-aware ML classifier…'
excerpt_truncated: true
date: 2026-10-21
venue: 'SPAICE 2026'
citation_authors: ["Marta Guimaraes", "Robert Arthur", "Claudia Soares", "Chiara Manfletti", "Gerarda De Pasquale"]
citation_year: '2026'
citation_conference: "SPAICE 2026"
paperurl: 'https://openreview.net/forum?id=N21P2fboTE'
citation: 'Marta Guimaraes, Robert Arthur, Claudia Soares, Chiara Manfletti, Gerarda De Pasquale, "Data-Centric Preprocessing for GNSS-Based Orbit Determination via AI, Signal Processing, and Orbital Dynamics." SPAICE 2026, 2026.'
---


<p class="publication-authors">Marta Guimaraes, Robert Arthur, Claudia Soares, Chiara Manfletti, Gerarda De Pasquale</p>

{% raw %}

## Abstract

<div class="publication-abstract"><p>GNSS-based orbit determination relies on input measurements whose quality can vary significantly across mission phases and operating conditions. In such settings, inappropriate data conditioning may either improve estimation robustness or, if misapplied, degrade convergence and numerical stability. This work proposes a data-centric preprocessing pipeline designed to operate safely under heterogeneous data quality conditions. The method combines lightweight physical sanity checks with a structure-aware ML classifier that gates increasingly assumption-dependent signal-processing-based cleaning stages. The pipeline targets localised measurement irregularities across multiple orbital representations while explicitly avoiding over-cleaning in weakly structured segments. In representative scenarios, it agrees with a baseline batch least-squares estimator on obvious outliers and additionally identifies dynamically inconsistent samples that remain invisible to position-only residual analysis. The results show that data-centric AI preprocessing reduces residual dispersion and improves convergence behaviour, resulting in a more stable and statistically consistent orbit determination without modifying the underlying dynamical model.</p></div>

[Access paper here](https://openreview.net/forum?id=N21P2fboTE){:target="_blank"}

## BibTeX

<pre><code>@inproceedings{spaice2026N21P2fboTE,
    author = &quot;Guimaraes, Marta and Arthur, Robert and Soares, Claudia and Manfletti, Chiara and Pasquale, Gerarda De&quot;,
    title = &quot;Data-Centric Preprocessing for GNSS-Based Orbit Determination via AI, Signal Processing, and Orbital Dynamics&quot;,
    booktitle = &quot;SPAICE 2026&quot;,
    year = &quot;2026&quot;,
    month = &quot;oct&quot;,
    day = &quot;21&quot;,
    url = &quot;https://openreview.net/forum?id=N21P2fboTE&quot;,
    abstract = &quot;GNSS-based orbit determination relies on input measurements whose quality can vary significantly across mission phases and operating conditions. In such settings, inappropriate data conditioning may either improve estimation robustness or, if misapplied, degrade convergence and numerical stability. This work proposes a data-centric preprocessing pipeline designed to operate safely under heterogeneous data quality conditions. The method combines lightweight physical sanity checks with a structure-aware ML classifier that gates increasingly assumption-dependent signal-processing-based cleaning stages. The pipeline targets localised measurement irregularities across multiple orbital representations while explicitly avoiding over-cleaning in weakly structured segments. In representative scenarios, it agrees with a baseline batch least-squares estimator on obvious outliers and additionally identifies dynamically inconsistent samples that remain invisible to position-only residual analysis. The results show that data-centric AI preprocessing reduces residual dispersion and improves convergence behaviour, resulting in a more stable and statistically consistent orbit determination without modifying the underlying dynamical model.&quot;,
    note = &quot;Accepted for oral presentation&quot;
}</code></pre>
{% endraw %}
