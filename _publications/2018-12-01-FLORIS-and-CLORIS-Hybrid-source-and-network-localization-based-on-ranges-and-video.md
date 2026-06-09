---
title: "FLORIS and CLORIS: Hybrid source and network localization based on ranges and video"
collection: publications
permalink: /publication/2018-12-01-FLORIS-and-CLORIS-Hybrid-source-and-network-localization-based-on-ranges-and-video
excerpt: 'We propose hybrid methods for localization in wireless sensor networks fusing noisy range measurements with angular information (extracted from video). Compared with conventional methods that rely on a single sensed variable, this may pave the way for improved localization accuracy and robustness. We address both the single-source and network (i.e., cooperative multiple-source) localization paradigms, solving them via optimization of a convex surrogate. The formulations for.'
date: 2018-12-01
venue: 'Signal Processing'
paperurl: 'http://dx.doi.org/10.1016/j.sigpro.2018.08.003'
citation: 'Beatriz Quintino Ferreira, João Gomes, Cláudia Soares, João P. Costeira, "FLORIS and CLORIS: Hybrid source and network localization based on ranges and video." Signal Processing, 2018.'
---

We propose hybrid methods for localization in wireless sensor networks fusing noisy range measurements with angular information (extracted from video). Compared with conventional methods that rely on a single sensed variable, this may pave the way for improved localization accuracy and robustness. We address both the single-source and network (i.e., cooperative multiple-source) localization paradigms, solving them via optimization of a convex surrogate. The formulations for hybrid localization are unified in the sense that we propose a single nonlinear least-squares cost function, fusing both angular and range measurements. We then relax the problem to obtain an estimate of the optimal positions. This contrasts with other hybrid approaches that alternate the execution of localization algorithms for each type of measurement separately, to progressively refine the position estimates. Single-source localization uses a semidefinite relaxation to obtain a one-shot matrix solution from which the source position is derived through factorization. Network localization uses a different approach where sensor coordinates are retained as optimization variables, and the relaxed cost function is efficiently minimized using fast iterations based on Nesterov’s optimal method. Further, an automated calibration procedure is developed to express range and angular information, obtained through different devices, possibly deployed at different locations, in a single consistent coordinate system. This drastically reduces the need for manual calibration that would otherwise negatively impact the practical usability of hybrid range/video localization systems. We develop and test, both in simulation and experimentally, the new hybrid localization algorithms, which not only overcome the limitations of previous fusing approaches, but also compare favourably to state-of-the-art methods, even outperforming them in some scenarios.

[Access paper here](http://dx.doi.org/10.1016/j.sigpro.2018.08.003){:target="_blank"}

Bibtex:

<pre><code>@article{Ferreira_2018,
    author = &quot;Ferreira, Beatriz Quintino and Gomes, João and Soares, Cláudia and Costeira, João P.&quot;,
    title = &quot;FLORIS and CLORIS: Hybrid source and network localization based on ranges and video&quot;,
    volume = &quot;153&quot;,
    ISSN = &quot;0165-1684&quot;,
    url = &quot;http://dx.doi.org/10.1016/j.sigpro.2018.08.003&quot;,
    DOI = &quot;10.1016/j.sigpro.2018.08.003&quot;,
    journal = &quot;Signal Processing&quot;,
    publisher = &quot;Elsevier BV&quot;,
    year = &quot;2018&quot;,
    month = &quot;Dec&quot;,
    pages = &quot;355-367&quot;,
    keywords = &quot;Hybrid single-source and cooperative localization, Convex relaxation, Ranges, Orientation, Vision, Wireless sensor networks&quot;,
    abstract = &quot;We propose hybrid methods for localization in wireless sensor networks fusing noisy range measurements with angular information (extracted from video). Compared with conventional methods that rely on a single sensed variable, this may pave the way for improved localization accuracy and robustness. We address both the single-source and network (i.e., cooperative multiple-source) localization paradigms, solving them via optimization of a convex surrogate. The formulations for hybrid localization are unified in the sense that we propose a single nonlinear least-squares cost function, fusing both angular and range measurements. We then relax the problem to obtain an estimate of the optimal positions. This contrasts with other hybrid approaches that alternate the execution of localization algorithms for each type of measurement separately, to progressively refine the position estimates. Single-source localization uses a semidefinite relaxation to obtain a one-shot matrix solution from which the source position is derived through factorization. Network localization uses a different approach where sensor coordinates are retained as optimization variables, and the relaxed cost function is efficiently minimized using fast iterations based on Nesterov’s optimal method. Further, an automated calibration procedure is developed to express range and angular information, obtained through different devices, possibly deployed at different locations, in a single consistent coordinate system. This drastically reduces the need for manual calibration that would otherwise negatively impact the practical usability of hybrid range/video localization systems. We develop and test, both in simulation and experimentally, the new hybrid localization algorithms, which not only overcome the limitations of previous fusing approaches, but also compare favourably to state-of-the-art methods, even outperforming them in some scenarios.&quot;
}</code></pre>
