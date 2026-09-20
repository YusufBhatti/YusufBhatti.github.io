---
layout: page
title: New Zealand Waipara 2021
permalink: /photography/field-work/Waipara-2021
---

<div class="page-nav-sticky">
  <a class="back-link" href="{{ '/photography/field-work' | relative_url }}">&larr; Back to Field Work</a>
  <span class="page-nav-title">{{ page.title }}</span>
</div>

New Zealand &mdash; Waipara (2021)

{% assign trip_files = site.static_files | where_exp: "f", "f.path contains '/assets/Field-work/New_Zealand/Waipara/'" | sort: "path" %}

<div class="gallery">
{% for f in trip_files %}
  {% assign ext = f.extname | downcase %}
  {% if ext == ".jpg" or ext == ".jpeg" or ext == ".png" %}
  <a href="{{ f.path | relative_url }}" data-lightbox="waipara-2021" data-title="New Zealand Waipara 2021">
    <img src="{{ f.path | relative_url }}" alt="New Zealand Waipara 2021">
  </a>
  {% endif %}
{% endfor %}
</div>

<style>
body {
  background-color: #e6f4fb; /* Soft sky blue */
}
</style>
