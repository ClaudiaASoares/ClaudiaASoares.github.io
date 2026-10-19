---
title: "One-Shot Initial Orbit Determination in Low-Earth Orbit"
collection: publications
permalink: /publication/2024-03-01-One-Shot-Initial-Orbit-Determination-in-Low-Earth-Orbit
excerpt_separator: ""
description: 'Due to the importance of satellites for society and the exponential increase in the number of objects in orbit, it is important to accurately determine the state (e.g., position and velocity) of these Resident Space Objects (RSOs) at any time and in a timely manner.'
excerpt: 'Due to the importance of satellites for society and the exponential increase in the number of objects in orbit, it is important to accurately determine the state (e.g., position and velocity) of these Resident Space Objects (RSOs) at any time and in a timely manner. State-of-the-art methodologies for initial orbit determination consist of Kalman-type filters that process sequential data over time and return the state…'
excerpt_truncated: true
date: 2024-03-01
venue: 'Accepted at the IEEE Aerospace Conference'
citation_authors: ["Ricardo Ferreira", "Marta Guimarães", "Filipa Valdeira", "Cláudia Soares"]
citation_year: '2024'
citation_conference: "the IEEE Aerospace Conference"
citation_doi: "10.1109/aero58975.2024.10521177"
citation_firstpage: '1'
citation_lastpage: '11'
paperurl: 'http://dx.doi.org/10.1109/aero58975.2024.10521177'
preprinturl: 'https://arxiv.org/abs/2312.13318'
citation: 'Ricardo Ferreira, Marta Guimarães, Filipa Valdeira, Cláudia Soares, "One-Shot Initial Orbit Determination in Low-Earth Orbit." Accepted at the IEEE Aerospace Conference, 2024.'
---


<p class="publication-authors">Ricardo Ferreira, Marta Guimarães, Filipa Valdeira, Cláudia Soares</p>

{% raw %}

## Abstract

<div class="publication-abstract"><p>Due to the importance of satellites for society and the exponential increase in the number of objects in orbit, it is important to accurately determine the state (e.g., position and velocity) of these Resident Space Objects (RSOs) at any time and in a timely manner. State-of-the-art methodologies for initial orbit determination consist of Kalman-type filters that process sequential data over time and return the state and associated uncertainty of the object, as is the case of the Extended Kalman Filter (EKF). However, these methodologies are dependent on a good initial guess for the state vector and usually simplify the physical dynamical model, due to the difficulty of precisely modeling perturbative forces, such as atmospheric drag and solar radiation pressure. Other approaches do not require assumptions about the dynamical system, such as the trilateration method, and require simultaneous measurements, such as three measurements of range and range-rate for the particular case of trilateration. We consider the same setting of simultaneous measurements (one-shot), resorting to time delay and Doppler shift measurements. Based on recent advancements in the problem of moving target localization for sonar multistatic systems, we are able to formulate the problem of initial orbit determination as a Weighted Least Squares. With this approach, we are able to directly obtain the state of the object (position and velocity) and the associated covariance matrix from the Fisher&#x27;s Information Matrix (FIM). We demonstrate that, for small noise, our estimator is able to attain the Cramér-Rao Lower Bound accuracy, i.e., the accuracy attained by the unbiased estimator with minimum variance. We also numerically demonstrate that our estimator is able to attain better accuracy on the state estimation than the trilateration method and returns a smaller uncertainty associated with the estimation.</p></div>

[Author preprint abstract](https://arxiv.org/abs/2312.13318).

[Download paper here](https://arxiv.org/abs/2312.13318){:target="_blank"}

## BibTeX

<pre><code>@inproceedings{Ferreira_2024,
    author = &quot;Ferreira, Ricardo and Guimarães, Marta and Valdeira, Filipa and Soares, Cláudia&quot;,
    title = &quot;One-Shot Initial Orbit Determination in Low-Earth Orbit&quot;,
    url = &quot;http://dx.doi.org/10.1109/aero58975.2024.10521177&quot;,
    DOI = &quot;10.1109/aero58975.2024.10521177&quot;,
    booktitle = &quot;2024 IEEE Aerospace Conference&quot;,
    publisher = &quot;IEEE&quot;,
    year = &quot;2024&quot;,
    month = &quot;Mar&quot;,
    pages = &quot;1-11&quot;,
    abstract = &quot;Due to the importance of satellites for society and the exponential increase in the number of objects in orbit, it is important to accurately determine the state (e.g., position and velocity) of these Resident Space Objects (RSOs) at any time and in a timely manner. State-of-the-art methodologies for initial orbit determination consist of Kalman-type filters that process sequential data over time and return the state and associated uncertainty of the object, as is the case of the Extended Kalman Filter (EKF). However, these methodologies are dependent on a good initial guess for the state vector and usually simplify the physical dynamical model, due to the difficulty of precisely modeling perturbative forces, such as atmospheric drag and solar radiation pressure. Other approaches do not require assumptions about the dynamical system, such as the trilateration method, and require simultaneous measurements, such as three measurements of range and range-rate for the particular case of trilateration. We consider the same setting of simultaneous measurements (one-shot), resorting to time delay and Doppler shift measurements. Based on recent advancements in the problem of moving target localization for sonar multistatic systems, we are able to formulate the problem of initial orbit determination as a Weighted Least Squares. With this approach, we are able to directly obtain the state of the object (position and velocity) and the associated covariance matrix from the Fisher&#x27;s Information Matrix (FIM). We demonstrate that, for small noise, our estimator is able to attain the Cramér-Rao Lower Bound accuracy, i.e., the accuracy attained by the unbiased estimator with minimum variance. We also numerically demonstrate that our estimator is able to attain better accuracy on the state estimation than the trilateration method and returns a smaller uncertainty associated with the estimation.&quot;,
    abstractsource = &quot;https://arxiv.org/abs/2312.13318&quot;,
    abstractsourcelabel = &quot;Author preprint abstract&quot;,
    preprinturl = &quot;https://arxiv.org/abs/2312.13318&quot;,
    journal = &quot;Accepted at the IEEE Aerospace Conference&quot;
}</code></pre>
{% endraw %}
