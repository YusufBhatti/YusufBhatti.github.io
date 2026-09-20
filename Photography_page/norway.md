---
layout: page
title: Norway
permalink: /photography/travelling/norway/
---

<div class="page-nav-sticky">
  <a class="back-link" href="{{ '/photography/travelling' | relative_url }}">&larr; Back to Travelling</a>
  <span class="page-nav-title">{{ page.title }}</span>
</div>

Norway

{% assign trip_files = site.static_files | where_exp: "f", "f.path contains '/assets/Travelling/Norway/'" | sort: "path" %}

<div class="gallery">
{% for f in trip_files %}
  {% assign ext = f.extname | downcase %}
  {% if ext == ".jpg" or ext == ".jpeg" or ext == ".png" %}
  <a href="{{ f.path | relative_url }}" data-lightbox="norway" data-title="Norway">
    <img src="{{ f.path | relative_url }}" alt="Norway" loading="lazy">
  </a>
  {% endif %}
{% endfor %}
</div>

<style>
body {
  background-color: #e6f4fb; /* Soft sky blue */
}
</style>
