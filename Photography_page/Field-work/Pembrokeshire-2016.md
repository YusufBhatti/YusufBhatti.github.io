---
layout: page
title: Pembrokeshire Geology 2016
permalink: /photography/field-work/Pembrokeshire-2016
---

<div class="page-nav-sticky">
  <a class="back-link" href="{{ '/photography/field-work' | relative_url }}">&larr; Back to Field Work</a>
  <span class="page-nav-title">{{ page.title }}</span>
</div>

Pembrokeshire, Wales &mdash; Geology (2016)

{% assign trip_files = site.static_files | where_exp: "f", "f.path contains '/assets/Field-work/UK/Pembrokeshire/'" | sort: "path" %}

<div class="gallery">
{% for f in trip_files %}
  {% assign ext = f.extname | downcase %}
  {% if ext == ".jpg" or ext == ".jpeg" or ext == ".png" %}
  <a href="{{ f.path | relative_url }}" data-lightbox="pembrokeshire-2016" data-title="Pembrokeshire Geology 2016">
    <img src="{{ f.path | relative_url }}" alt="Pembrokeshire Geology 2016">
  </a>
  {% endif %}
{% endfor %}
</div>

<style>
body {
  background-color: #e6f4fb; /* Soft sky blue */
}
</style>
