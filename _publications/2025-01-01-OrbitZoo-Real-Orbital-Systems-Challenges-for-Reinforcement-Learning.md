---
title: "OrbitZoo: Real Orbital Systems Challenges for Reinforcement Learning"
collection: publications
permalink: /publication/2025-01-01-OrbitZoo-Real-Orbital-Systems-Challenges-for-Reinforcement-Learning
excerpt: 'The increasing number of satellites and orbital debris has made space congestion a critical issue, threatening satellite safety and sustainability. Challenges such as collision avoidance, station-keeping, and orbital maneuvering require advanced techniques to handle dynamic uncertainties and multi-agent interactions. Reinforcement learning (RL) has shown promise in this domain, enabling adaptive, autonomous policies for space operations; however, many existing RL frameworks rely on custom-built environments developed.'
date: 2025-01-01
venue: 'NeurIPS 2025 poster'
paperurl: 'https://openreview.net/forum?id=oElWLpkOux'
citation: 'Alexandre Oliveira, Katarina Dyreby, Francisco Miguel Caldas, Claudia Soares, "OrbitZoo: Real Orbital Systems Challenges for Reinforcement Learning." NeurIPS 2025 poster, 2025.'
---

The increasing number of satellites and orbital debris has made space congestion a critical issue, threatening satellite safety and sustainability. Challenges such as collision avoidance, station-keeping, and orbital maneuvering require advanced techniques to handle dynamic uncertainties and multi-agent interactions. Reinforcement learning (RL) has shown promise in this domain, enabling adaptive, autonomous policies for space operations; however, many existing RL frameworks rely on custom-built environments developed from scratch, which often use simplified models and require significant time to implement and validate the orbital dynamics, limiting their ability to fully capture real-world complexities. To address this, we introduce OrbitZoo, a versatile multi-agent RL environment built on a high-fidelity industry standard library, that enables realistic data generation, supports scenarios like collision avoidance and cooperative maneuvers, and ensures robust and accurate orbital dynamics. The environment is validated against various real satellite constellations, including Starlink, achieving a Mean Absolute Percentage Error (MAPE) of 0.16% compared to real-world data. This validation ensures reliability for generating high-fidelity simulations and enabling autonomous and independent satellite operations. This project is open source and has a dedicated project page.

[Access paper here](https://openreview.net/forum?id=oElWLpkOux){:target="_blank"}

Bibtex:

<pre><code>@inproceedings{Oliveira2025orbitzoo-real-orbital,
    author = &quot;Oliveira, Alexandre and Dyreby, Katarina and Caldas, Francisco Miguel and Soares, Claudia&quot;,
    title = &quot;OrbitZoo: Real Orbital Systems Challenges for Reinforcement Learning&quot;,
    booktitle = &quot;NeurIPS 2025 poster&quot;,
    url = &quot;https://openreview.net/forum?id=oElWLpkOux&quot;,
    year = &quot;2025&quot;,
    eprint = &quot;https://openreview.net/pdf?id=oliveira|orbitzoo\\_real\\_orbital\\_systems\\_challenges\\_for\\_reinforcement\\_learning&quot;,
    organization = &quot;NeurIPS.cc/2025/Conference&quot;,
    abstract = &quot;The increasing number of satellites and orbital debris has made space congestion a critical issue, threatening satellite safety and sustainability. Challenges such as collision avoidance, station-keeping, and orbital maneuvering require advanced techniques to handle dynamic uncertainties and multi-agent interactions. Reinforcement learning (RL) has shown promise in this domain, enabling adaptive, autonomous policies for space operations; however, many existing RL frameworks rely on custom-built environments developed from scratch, which often use simplified models and require significant time to implement and validate the orbital dynamics, limiting their ability to fully capture real-world complexities. To address this, we introduce OrbitZoo, a versatile multi-agent RL environment built on a high-fidelity industry standard library, that enables realistic data generation, supports scenarios like collision avoidance and cooperative maneuvers, and ensures robust and accurate orbital dynamics. The environment is validated against various real satellite constellations, including Starlink, achieving a Mean Absolute Percentage Error (MAPE) of 0.16\\% compared to real-world data. This validation ensures reliability for generating high-fidelity simulations and enabling autonomous and independent satellite operations. This project is open source and has a dedicated project page.&quot;
}</code></pre>
