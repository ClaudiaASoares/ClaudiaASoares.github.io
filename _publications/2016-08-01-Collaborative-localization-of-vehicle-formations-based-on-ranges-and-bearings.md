---
title: "Collaborative localization of vehicle formations based on ranges and bearings"
collection: publications
permalink: /publication/2016-08-01-Collaborative-localization-of-vehicle-formations-based-on-ranges-and-bearings
excerpt: 'We examine the problem of jointly determining the positions of multiple underwater vehicles based on a set of pairwise range and bearing measurements taken over time. This extends prior work on the so-called (static) collaborative localization paradigm where a hybrid approach was proposed for seamless instantaneous fusion (i.e., no time dependence) of range and bearing measurements. To incorporate time we add to the original convexified.'
date: 2016-08-01
venue: '2016 IEEE Third Underwater Communications and Networking Conference (UComms)'
paperurl: 'http://dx.doi.org/10.1109/ucomms.2016.7583426'
citation: 'Beatriz Quintino Ferreira, Joao Gomes, Claudia Soares, Joao P. Costeira, "Collaborative localization of vehicle formations based on ranges and bearings." 2016 IEEE Third Underwater Communications and Networking Conference (UComms), 2016.'
---

We examine the problem of jointly determining the positions of multiple underwater vehicles based on a set of pairwise range and bearing measurements taken over time. This extends prior work on the so-called (static) collaborative localization paradigm where a hybrid approach was proposed for seamless instantaneous fusion (i.e., no time dependence) of range and bearing measurements. To incorporate time we add to the original convexified least-squares cost function a regularizing term that penalizes deviations between predicted and computed vehicle positions at a given instant. The method operates progressively over time, with past estimates used for prediction at the current instant assuming a very simple quasilinear motion model. The method is amenable to parallelization, with simple gradient-like updates. Numerical results demonstrate promising accuracy gains (reduction on the order of 10 % in terms of root-mean-square positioning error) in simulations inspired by an underwater geoacoustic surveying application.

[Access paper here](http://dx.doi.org/10.1109/ucomms.2016.7583426){:target="_blank"}

Bibtex:

<pre><code>@inproceedings{Ferreira_2016,
    author = &quot;Ferreira, Beatriz Quintino and Gomes, Joao and Soares, Claudia and Costeira, Joao P.&quot;,
    title = &quot;Collaborative localization of vehicle formations based on ranges and bearings&quot;,
    url = &quot;http://dx.doi.org/10.1109/ucomms.2016.7583426&quot;,
    DOI = &quot;10.1109/ucomms.2016.7583426&quot;,
    booktitle = &quot;2016 IEEE Third Underwater Communications and Networking Conference (UComms)&quot;,
    publisher = &quot;IEEE&quot;,
    year = &quot;2016&quot;,
    month = &quot;Aug&quot;,
    pages = &quot;1-5&quot;,
    abstract = &quot;We examine the problem of jointly determining the positions of multiple underwater vehicles based on a set of pairwise range and bearing measurements taken over time. This extends prior work on the so-called (static) collaborative localization paradigm where a hybrid approach was proposed for seamless instantaneous fusion (i.e., no time dependence) of range and bearing measurements. To incorporate time we add to the original convexified least-squares cost function a regularizing term that penalizes deviations between predicted and computed vehicle positions at a given instant. The method operates progressively over time, with past estimates used for prediction at the current instant assuming a very simple quasilinear motion model. The method is amenable to parallelization, with simple gradient-like updates. Numerical results demonstrate promising accuracy gains (reduction on the order of 10 \\% in terms of root-mean-square positioning error) in simulations inspired by an underwater geoacoustic surveying application.&quot;,
    keywords = &quot;distance measurement;least squares approximations;mean square error methods;underwater acoustic communication;underwater vehicles;bearing measurements;collaborative localization paradigm;computed vehicle positions;convexified least-squares cost function;multiple underwater vehicle positions;pairwise range measurements;predicted vehicle positions;quasilinear motion;root-mean-square positioning error;seamless instantaneous fusion;simple gradient-like updates;underwater geoacoustic surveying application;vehicle formations;Acoustics;Collaboration;Cost function;Position measurement;Time measurement;Trajectory;Vehicles&quot;
}</code></pre>
