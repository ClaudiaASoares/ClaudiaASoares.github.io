---
title: "Identification of the Gravitational Constant from Satellite Trajectories Using Neural Ordinary Differential Equations"
collection: publications
permalink: /publication/2026-10-21-Identification-of-the-Gravitational-Constant-from-Satellite-Trajectories-Using-Neural-Ordinary-Differential-Equations
excerpt_separator: ""
description: 'The rapid growth of satellite constellations in low Earth orbit has increased the probability of collisions involving satellites and debris, making accurate orbit propagation increasingly important.'
excerpt: 'The rapid growth of satellite constellations in low Earth orbit has increased the probability of collisions involving satellites and debris, making accurate orbit propagation increasingly important. However, accurate orbit prediction remains challenging. Propagators depend on spacecraft properties, environmental parameters, and non-conservative forces that are often uncertain, causing propagation errors to accumulate over time. Estimating these values directly from orbital data offers a solution that could…'
excerpt_truncated: true
date: 2026-10-21
venue: 'SPAICE 2026'
citation_authors: ["Katarina Dyreby", "Claudia Soares"]
citation_year: '2026'
citation_conference: "SPAICE 2026"
paperurl: 'https://openreview.net/forum?id=Gf8ij9SHjP'
citation: 'Katarina Dyreby, Claudia Soares, "Identification of the Gravitational Constant from Satellite Trajectories Using Neural Ordinary Differential Equations." SPAICE 2026, 2026.'
---


<p class="publication-authors">Katarina Dyreby, Claudia Soares</p>

{% raw %}

## Abstract

<div class="publication-abstract"><p>The rapid growth of satellite constellations in low Earth orbit has increased the probability of collisions involving satellites and debris, making accurate orbit propagation increasingly important. However, accurate orbit prediction remains challenging. Propagators depend on spacecraft properties, environmental parameters, and non-conservative forces that are often uncertain, causing propagation errors to accumulate over time. Estimating these values directly from orbital data offers a solution that could improve propagation accuracy. This work investigates whether a global physical constant can be identified directly from real orbital data using Neural Ordinary Differential Equations (Neural ODEs). A hybrid Neural ODE model is developed in which the equations of motion of satellites are split into two parts: known gravitational dynamics, with the gravitational constant treated as a trainable parameter, and a Neural Network that learns the residual accelerations representing the unmodelled forces. Using different initial biases, the model successfully recovers the gravitational constant for relative errors of up to 150%. Increasing the initialization error primarily increases the number of training epochs required for convergence, as the final relative errors achieved are below 0.02% for all different initial biases used. At higher initial errors, the Neural Network instead compensates for the incorrect gravitational term by learning residual accelerations several orders of magnitude larger than physically expected, preventing recovery of the gravitational constant. These results show that Neural ODEs can recover physical parameters from real orbital data, while also revealing the limits of parameter identifiability when unknown dynamics are learned simultaneously.</p></div>

[Access paper here](https://openreview.net/forum?id=Gf8ij9SHjP){:target="_blank"}

## BibTeX

<pre><code>@inproceedings{spaice2026Gf8ij9SHjP,
    author = &quot;Dyreby, Katarina and Soares, Claudia&quot;,
    title = &quot;Identification of the Gravitational Constant from Satellite Trajectories Using Neural Ordinary Differential Equations&quot;,
    booktitle = &quot;SPAICE 2026&quot;,
    year = &quot;2026&quot;,
    month = &quot;oct&quot;,
    day = &quot;21&quot;,
    url = &quot;https://openreview.net/forum?id=Gf8ij9SHjP&quot;,
    abstract = &quot;The rapid growth of satellite constellations in low Earth orbit has increased the probability of collisions involving satellites and debris, making accurate orbit propagation increasingly important. However, accurate orbit prediction remains challenging. Propagators depend on spacecraft properties, environmental parameters, and non-conservative forces that are often uncertain, causing propagation errors to accumulate over time. Estimating these values directly from orbital data offers a solution that could improve propagation accuracy. This work investigates whether a global physical constant can be identified directly from real orbital data using Neural Ordinary Differential Equations (Neural ODEs). A hybrid Neural ODE model is developed in which the equations of motion of satellites are split into two parts: known gravitational dynamics, with the gravitational constant treated as a trainable parameter, and a Neural Network that learns the residual accelerations representing the unmodelled forces. Using different initial biases, the model successfully recovers the gravitational constant for relative errors of up to 150\\%. Increasing the initialization error primarily increases the number of training epochs required for convergence, as the final relative errors achieved are below 0.02\\% for all different initial biases used. At higher initial errors, the Neural Network instead compensates for the incorrect gravitational term by learning residual accelerations several orders of magnitude larger than physically expected, preventing recovery of the gravitational constant. These results show that Neural ODEs can recover physical parameters from real orbital data, while also revealing the limits of parameter identifiability when unknown dynamics are learned simultaneously.&quot;,
    note = &quot;Accepted for oral presentation&quot;
}</code></pre>
{% endraw %}
