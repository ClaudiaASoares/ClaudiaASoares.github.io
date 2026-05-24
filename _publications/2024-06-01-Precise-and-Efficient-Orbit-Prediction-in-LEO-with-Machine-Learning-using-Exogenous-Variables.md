---
title: "Precise and Efficient Orbit Prediction in LEO with Machine Learning using Exogenous Variables"
collection: publications
permalink: /publication/2024-06-01-Precise-and-Efficient-Orbit-Prediction-in-LEO-with-Machine-Learning-using-Exogenous-Variables
excerpt: 'The increasing volume of space objects in Earth&apos;s orbit presents a significant challenge for Space Situational Awareness (SSA). And in particular, accurate orbit prediction is crucial to anticipate the position and velocity of space objects, for collision avoidance and space debris mitigation. When performing Orbit Prediction (OP), it is necessary to consider the impact of non-conservative forces, such as atmospheric drag and gravitational perturbations, that.'
date: 2024-06-01
venue: '2024 IEEE Congress on Evolutionary Computation (CEC)'
paperurl: 'http://dx.doi.org/10.1109/cec60901.2024.10611996'
citation: 'Francisco Caldas, Cláudia Soares, "Precise and Efficient Orbit Prediction in LEO with Machine Learning using Exogenous Variables." 2024 IEEE Congress on Evolutionary Computation (CEC), 2024.'
---

The increasing volume of space objects in Earth&apos;s orbit presents a significant challenge for Space Situational Awareness (SSA). And in particular, accurate orbit prediction is crucial to anticipate the position and velocity of space objects, for collision avoidance and space debris mitigation. When performing Orbit Prediction (OP), it is necessary to consider the impact of non-conservative forces, such as atmospheric drag and gravitational perturbations, that contribute to uncertainty around the future position of spacecraft and space debris alike. Conventional propagator methods like the SGP4 inadequately account for these forces, while numerical propagators are able to model the forces at a high computational cost. To address these limitations, we propose an orbit prediction algorithm utilizing machine learning. This algorithm forecasts state vectors on a spacecraft using past positions and environmental variables like atmospheric density from external sources. The orbital data used in the paper is gathered from precision ephemeris data from the International Laser Ranging Service (ILRS), for the period of almost a year. We show how the use of machine learning and time-series techniques can produce low positioning errors at a very low computational cost, thus significantly improving SSA capabilities by providing faster and reliable orbit determination for an ever increasing number of space objects.

[Access paper here](http://dx.doi.org/10.1109/cec60901.2024.10611996){:target="_blank"}

Bibtex:

<pre><code>@inproceedings{Caldas_2024-2,
    author = &quot;Caldas, Francisco and Soares, Cláudia&quot;,
    title = &quot;Precise and Efficient Orbit Prediction in LEO with Machine Learning using Exogenous Variables&quot;,
    url = &quot;http://dx.doi.org/10.1109/cec60901.2024.10611996&quot;,
    DOI = &quot;10.1109/cec60901.2024.10611996&quot;,
    booktitle = &quot;2024 IEEE Congress on Evolutionary Computation (CEC)&quot;,
    publisher = &quot;IEEE&quot;,
    year = &quot;2024&quot;,
    month = &quot;June&quot;,
    pages = &quot;1-8&quot;,
    abstract = &quot;The increasing volume of space objects in Earth&#x27;s orbit presents a significant challenge for Space Situational Awareness (SSA). And in particular, accurate orbit prediction is crucial to anticipate the position and velocity of space objects, for collision avoidance and space debris mitigation. When performing Orbit Prediction (OP), it is necessary to consider the impact of non-conservative forces, such as atmospheric drag and gravitational perturbations, that contribute to uncertainty around the future position of spacecraft and space debris alike. Conventional propagator methods like the SGP4 inadequately account for these forces, while numerical propagators are able to model the forces at a high computational cost. To address these limitations, we propose an orbit prediction algorithm utilizing machine learning. This algorithm forecasts state vectors on a spacecraft using past positions and environmental variables like atmospheric density from external sources. The orbital data used in the paper is gathered from precision ephemeris data from the International Laser Ranging Service (ILRS), for the period of almost a year. We show how the use of machine learning and time-series techniques can produce low positioning errors at a very low computational cost, thus significantly improving SSA capabilities by providing faster and reliable orbit determination for an ever increasing number of space objects.&quot;
}</code></pre>
