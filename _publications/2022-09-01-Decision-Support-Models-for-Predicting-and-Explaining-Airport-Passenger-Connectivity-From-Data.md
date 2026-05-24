---
title: "Decision Support Models for Predicting and Explaining Airport Passenger Connectivity From Data"
collection: publications
permalink: /publication/2022-09-01-Decision-Support-Models-for-Predicting-and-Explaining-Airport-Passenger-Connectivity-From-Data
excerpt: 'Predicting if passengers in a connecting flight will lose their connection is paramount for airline profitability. We present novel machine learning-based decision support models for the different stages of connection flight management, namely for strategic, pre-tactical, tactical and post-operations. We predict missed flight connections in an airline’s hub airport using historical data on flights and passengers, and analyse the factors that contribute additively to the.'
date: 2022-09-01
venue: 'IEEE Transactions on Intelligent Transportation Systems'
paperurl: 'http://dx.doi.org/10.1109/tits.2022.3147155'
citation: 'Marta Guimaraes, Claudia Soares, Rodrigo Ventura, "Decision Support Models for Predicting and Explaining Airport Passenger Connectivity From Data." IEEE Transactions on Intelligent Transportation Systems, 2022.'
---

Predicting if passengers in a connecting flight will lose their connection is paramount for airline profitability. We present novel machine learning-based decision support models for the different stages of connection flight management, namely for strategic, pre-tactical, tactical and post-operations. We predict missed flight connections in an airline’s hub airport using historical data on flights and passengers, and analyse the factors that contribute additively to the predicted outcome for each decision horizon. Our data is high-dimensional, heterogeneous, imbalanced and noisy, and does not inform about passenger arrival/departure transit time. We employ probabilistic encoding of categorical classes, data balancing with Gaussian Mixture Models, and boosting. For all planning horizons, our models attain an area under the curve (AUC) of the receiver operating characteristic (ROC) higher than 0.93. SHAP value explanations of our models indicate that scheduled/perceived connection times contribute the most to the prediction, followed by passenger age and whether border controls are required.

[Access paper here](http://dx.doi.org/10.1109/tits.2022.3147155){:target="_blank"}

Bibtex:

<pre><code>@article{Guimaraes_2022,
    author = &quot;Guimaraes, Marta and Soares, Claudia and Ventura, Rodrigo&quot;,
    title = &quot;Decision Support Models for Predicting and Explaining Airport Passenger Connectivity From Data&quot;,
    volume = &quot;23&quot;,
    ISSN = &quot;1558-0016&quot;,
    url = &quot;http://dx.doi.org/10.1109/tits.2022.3147155&quot;,
    DOI = &quot;10.1109/tits.2022.3147155&quot;,
    number = &quot;9&quot;,
    journal = &quot;IEEE Transactions on Intelligent Transportation Systems&quot;,
    publisher = &quot;Institute of Electrical and Electronics Engineers (IEEE)&quot;,
    year = &quot;2022&quot;,
    month = &quot;Sept&quot;,
    pages = &quot;16005-16015&quot;,
    abstract = &quot;Predicting if passengers in a connecting flight will lose their connection is paramount for airline profitability. We present novel machine learning-based decision support models for the different stages of connection flight management, namely for strategic, pre-tactical, tactical and post-operations. We predict missed flight connections in an airline’s hub airport using historical data on flights and passengers, and analyse the factors that contribute additively to the predicted outcome for each decision horizon. Our data is high-dimensional, heterogeneous, imbalanced and noisy, and does not inform about passenger arrival/departure transit time. We employ probabilistic encoding of categorical classes, data balancing with Gaussian Mixture Models, and boosting. For all planning horizons, our models attain an area under the curve (AUC) of the receiver operating characteristic (ROC) higher than 0.93. SHAP value explanations of our models indicate that scheduled/perceived connection times contribute the most to the prediction, followed by passenger age and whether border controls are required.&quot;
}</code></pre>
