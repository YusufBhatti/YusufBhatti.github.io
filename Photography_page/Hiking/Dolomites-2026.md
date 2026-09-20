---
layout: page
title: Dolomites Huts 2026
permalink: /photography/hiking-trips/Dolomites-2026
---

<div class="page-nav-sticky">
  <a class="back-link" href="{{ '/photography/hiking-trips' | relative_url }}">&larr; Back to Hiking Trips</a>
  <span class="page-nav-title">{{ page.title }}</span>
</div>

Dolomites Huts 2026 (3 days)

{% assign dolomites_files = site.static_files | where_exp: "f", "f.path contains '/assets/Hiking_Trips/Dolomites_2026/'" | sort: "path" %}

<div class="gallery">
{% for f in dolomites_files %}
  {% assign ext = f.extname | downcase %}
  {% if ext == ".jpg" or ext == ".jpeg" or ext == ".png" %}
  <a href="{{ f.path | relative_url }}" data-lightbox="dolomites-2026" data-title="Dolomites Huts 2026">
    <img src="{{ f.path | relative_url }}" alt="Dolomites Huts 2026">
  </a>
  {% endif %}
{% endfor %}
</div>

<!-- <h3>Video Clips</h3>
<p class="video-note">Recorded on iPhone; playback depends on your browser's codec support (works in Safari and most modern Chrome/Edge/Firefox).</p>
<div class="video-gallery">
{% for f in dolomites_files %}
  {% assign ext = f.extname | downcase %}
  {% if ext == ".mov" or ext == ".mp4" %}
  <video controls preload="metadata" src="{{ f.path | relative_url }}"></video>
  {% endif %}
{% endfor %}
</div>
 -->
<style>
.video-gallery {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}
.video-gallery video {
  width: 320px;
  max-width: 100%;
  border-radius: 8px;
}
.video-note {
  font-size: 0.85em;
  color: #777;
}
.gallery-note {
  font-size: 0.85em;
  color: #999;
  margin-top: 1.5em;
}
body {
  background-color: #e6f4fb; /* Soft sky blue */
}
</style>
