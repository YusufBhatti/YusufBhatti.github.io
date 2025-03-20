---
layout: page
title: Photography
permalink: /photography/
main_nav: true
---


  <div class="photography">
    <!-- <h1>Photography</h1> -->
    <p>Explore my photography albums from different activities. This section is still being worked on</p>

    <div class="project-grid">
      <!-- Hiking Trips Album -->
      <div class="project-item">
        <a href="{{ '/photography/hiking-trips' | relative_url }}">
          <img src="{{ '/assets/New_Zealand/cover.jpg' | relative_url }}" alt="Hiking Trips">
          <h3>Hiking Trips</h3>
        </a>
      </div>

      <!-- Field Work Album -->
      <div class="project-item">
        <a href="{{ '/photography/field-work' | relative_url }}">
          <img src="{{ '/assets/Field-work/Italy/Etna/cover.jpg' | relative_url }}" alt="Field Work">
          <h3>Field Work</h3>
        </a>
      </div>

      <!-- Travelling Album -->
      <div class="project-item">
        <a href="{{ '/photography/travelling' | relative_url }}">
          <img src="{{ '/assets/Travelling/Australia/IMG_9823.jpeg' | relative_url }}" alt="Travelling">
          <h3>Travelling</h3>
        </a>
      </div>
    </div>
  </div>

  <style>
    /* CSS for the photography section */
    .photography {
      text-align: center;
      padding: 20px;
    }

    .photography h1 {
      font-size: 2.5em;
      margin-bottom: 10px;
    }

    .photography p {
      font-size: 1.2em;
      margin-bottom: 30px;
      color: #666;
    }

    .project-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      justify-content: center;
    }

    .project-item {
      flex: 1 1 calc(33.333% - 40px); /* Three items per row with gap */
      max-width: 300px; /* Limit the maximum width of each item */
      text-align: center;
      border: 5px solid #87CEEB; /* Sky blue border */
      border-radius: 10px; /* Rounded corners */
      overflow: hidden; /* Ensure the image doesn't overflow */
      transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth hover effect */
    }

    .project-item:hover {
      transform: scale(1.05); /* Slightly enlarge on hover */
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); /* Add shadow on hover */
    }

    .project-item img {
      width: 100%;
      height: 200px; /* Fixed height for all images */
      object-fit: cover; /* Ensure the image covers the area without distortion */
    }

    .project-item h3 {
      margin: 15px 0;
      font-size: 1.5em;
      color: #333;
    }

    .project-item a {
      text-decoration: none; /* Remove underline from links */
      color: inherit; /* Inherit text color */
    }
  </style>
