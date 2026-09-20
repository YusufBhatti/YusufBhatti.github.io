---
layout: page
title: Italy Lipari Geological Mapping 2017
permalink: /photography/field-work/Lipari-Mapping-2017
---

<div class="page-nav-sticky">
  <a class="back-link" href="{{ '/photography/field-work' | relative_url }}">&larr; Back to Field Work</a>
  <span class="page-nav-title">{{ page.title }}</span>
</div>

Lipari, Italy &mdash; Geological Mapping (2017)

{% assign trip_files = site.static_files | where_exp: "f", "f.path contains '/assets/Field-work/Italy/Lipari_Mapping/'" | sort: "path" %}

<div class="gallery">
{% for f in trip_files %}
  {% assign ext = f.extname | downcase %}
  {% if ext == ".jpg" or ext == ".jpeg" or ext == ".png" %}
  <a href="{{ f.path | relative_url }}" data-lightbox="lipari-mapping-2017" data-title="Italy Lipari Geological Mapping 2017">
    <img src="{{ f.path | relative_url }}" alt="Italy Lipari Geological Mapping 2017">
  </a>
  {% endif %}
{% endfor %}
</div>

<style>
body {
  background-color: #e6f4fb; /* Soft sky blue */
}
</style>
