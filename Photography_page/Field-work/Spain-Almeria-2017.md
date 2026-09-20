---
layout: page
title: Spain Almeria 2017
permalink: /photography/field-work/Spain-Almeria-2017
---

<div class="page-nav-sticky">
  <a class="back-link" href="{{ '/photography/field-work' | relative_url }}">&larr; Back to Field Work</a>
  <span class="page-nav-title">{{ page.title }}</span>
</div>

Almeria, Spain (2017)

{% assign trip_files = site.static_files | where_exp: "f", "f.path contains '/assets/Field-work/Spain/'" | sort: "path" %}

<div class="gallery">
{% for f in trip_files %}
  {% assign ext = f.extname | downcase %}
  {% if ext == ".jpg" or ext == ".jpeg" or ext == ".png" %}
  <a href="{{ f.path | relative_url }}" data-lightbox="spain-almeria-2017" data-title="Spain Almeria 2017">
    <img src="{{ f.path | relative_url }}" alt="Spain Almeria 2017">
  </a>
  {% endif %}
{% endfor %}
</div>

<style>
body {
  background-color: #e6f4fb; /* Soft sky blue */
}
</style>
