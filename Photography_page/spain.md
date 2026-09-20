---
layout: page
title: Spain
permalink: /photography/travelling/spain/
---

<div class="page-nav-sticky">
  <a class="back-link" href="{{ '/photography/travelling' | relative_url }}">&larr; Back to Travelling</a>
  <span class="page-nav-title">{{ page.title }}</span>
</div>

Spain

{% assign trip_files = site.static_files | where_exp: "f", "f.path contains '/assets/Travelling/Spain/'" | sort: "path" %}

<div class="gallery">
{% for f in trip_files %}
  {% assign ext = f.extname | downcase %}
  {% if ext == ".jpg" or ext == ".jpeg" or ext == ".png" %}
  <a href="{{ f.path | relative_url }}" data-lightbox="spain" data-title="Spain">
    <img src="{{ f.path | relative_url }}" alt="Spain" loading="lazy">
  </a>
  {% endif %}
{% endfor %}
</div>

<style>
body {
  background-color: #e6f4fb; /* Soft sky blue */
}
</style>
