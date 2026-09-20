---
layout: page
title: New Zealand Science Outreach (Weather Balloon)
permalink: /photography/field-work/Science-Outreach-Balloon
---

<div class="page-nav-sticky">
  <a class="back-link" href="{{ '/photography/field-work' | relative_url }}">&larr; Back to Field Work</a>
  <span class="page-nav-title">{{ page.title }}</span>
</div>

New Zealand &mdash; Science Outreach, Weather Balloon Launch

{% assign trip_files = site.static_files | where_exp: "f", "f.path contains '/assets/Field-work/New_Zealand/Science_Outreach_Balloon/'" | sort: "path" %}

<div class="gallery">
{% for f in trip_files %}
  {% assign ext = f.extname | downcase %}
  {% if ext == ".jpg" or ext == ".jpeg" or ext == ".png" %}
  <a href="{{ f.path | relative_url }}" data-lightbox="science-outreach-balloon" data-title="Science Outreach - Weather Balloon">
    <img src="{{ f.path | relative_url }}" alt="Science Outreach - Weather Balloon">
  </a>
  {% endif %}
{% endfor %}
</div>

<style>
body {
  background-color: #e6f4fb; /* Soft sky blue */
}
</style>
