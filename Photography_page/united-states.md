---
layout: page
title: United States
permalink: /photography/travelling/united-states/
---

<div class="page-nav-sticky">
  <a class="back-link" href="{{ '/photography/travelling' | relative_url }}">&larr; Back to Travelling</a>
  <span class="page-nav-title">{{ page.title }}</span>
</div>

United States

{% assign trip_files = site.static_files | where_exp: "f", "f.path contains '/assets/Travelling/United_States/'" | sort: "path" %}

<div class="gallery">
{% for f in trip_files %}
  {% assign ext = f.extname | downcase %}
  {% if ext == ".jpg" or ext == ".jpeg" or ext == ".png" %}
  <a href="{{ f.path | relative_url }}" data-lightbox="united-states" data-title="United States">
    <img src="{{ f.path | relative_url }}" alt="United States" loading="lazy">
  </a>
  {% endif %}
{% endfor %}
</div>

<style>
body {
  background-color: #e6f4fb; /* Soft sky blue */
}
</style>
