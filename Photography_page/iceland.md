---
layout: page
title: Iceland
permalink: /photography/travelling/iceland/
---

<div class="page-nav-sticky">
  <a class="back-link" href="{{ '/photography/travelling' | relative_url }}">&larr; Back to Travelling</a>
  <span class="page-nav-title">{{ page.title }}</span>
</div>

Iceland

{% assign trip_files = site.static_files | where_exp: "f", "f.path contains '/assets/Travelling/Iceland/'" | sort: "path" %}

{% if trip_files.size > 0 %}
<div class="gallery">
{% for f in trip_files %}
  {% assign ext = f.extname | downcase %}
  {% if ext == ".jpg" or ext == ".jpeg" or ext == ".png" %}
  <a href="{{ f.path | relative_url }}" data-lightbox="iceland" data-title="Iceland">
    <img src="{{ f.path | relative_url }}" alt="Iceland" loading="lazy">
  </a>
  {% endif %}
{% endfor %}
</div>
{% else %}
<p class="coming-soon">Photos coming soon.</p>
{% endif %}

<style>
body {
  background-color: #e6f4fb; /* Soft sky blue */
}
.coming-soon {
  color: #999;
  font-style: italic;
}
</style>
