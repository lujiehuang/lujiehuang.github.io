---
layout: default
title: "Blog"
permalink: /blog
author_profile: true
---

# Blog

Notes on human-AI interaction, educational technology, learning agents, and research methods for evaluating AI-supported learning.

---

{% for post in site.posts %}
<div style="margin-bottom: 2em; padding-bottom: 1.5em; border-bottom: 1px solid #efefef;">
  <h2 style="margin-bottom: 0.3em;"><a href="{{ post.url }}" style="text-decoration: none;">{{ post.title }}</a></h2>
  <p style="color: #888; font-size: 0.9em; margin-bottom: 0.5em;">{{ post.date | date: "%B %d, %Y" }}</p>
  <p>{{ post.content | strip_html | truncatewords: 50 }}</p>
  <a href="{{ post.url }}" style="font-size: 0.9em;">Read more →</a>
</div>
{% endfor %}

{% if site.posts.size == 0 %}
<p>Coming soon — I plan to share short research notes on AI-supported learning, virtual tutors, learner engagement, and behavioral evaluation methods.</p>
{% endif %}
