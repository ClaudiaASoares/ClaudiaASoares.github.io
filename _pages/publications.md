---
layout: archive
title: "Publications"
description: "Publications by Cláudia Soares on trustworthy machine learning, including research in healthcare, space, federated learning and online learning."
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can find a more updated record of my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
