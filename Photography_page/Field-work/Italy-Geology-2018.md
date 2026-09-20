---
layout: page
title: Italy Geology 2018
permalink: /photography/field-work/Italy-Geology-2018
---

<div class="page-nav-sticky">
  <a class="back-link" href="{{ '/photography/field-work' | relative_url }}">&larr; Back to Field Work</a>
  <span class="page-nav-title">{{ page.title }}</span>
</div>

Italy Geology (2018)

{% assign trip_files = site.static_files | where_exp: "f", "f.path contains '/assets/Field-work/Italy/GEOL3_vol/'" | sort: "path" %}

<div class="gallery">
{% for f in trip_files %}
  {% assign ext = f.extname | downcase %}
  {% if ext == ".jpg" or ext == ".jpeg" or ext == ".png" %}
  <a href="{{ f.path | relative_url }}" data-lightbox="italy-geology-2018" data-title="Italy Geology 2018">
    <img src="{{ f.path | relative_url }}" alt="Italy Geology 2018">
  </a>
  {% endif %}
{% endfor %}
</div>

<style>
body {
  background-color: #e6f4fb; /* Soft sky blue */
}
</style>
