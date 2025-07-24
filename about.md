---
layout: page
title: About Me
permalink: /about/
main_nav: true
---

![alt text]({{ site.baseurl }}/assets/Yusuf_Headshot.jpg){:.profile}

<div class="about-section">
  <h1></h1>
  <p>
    I'm an atmospheric physicist specializing in developing <a href="/publications">aerosol-cloud interactions</a> in climate models. Currently, I work as a research scientist at <strong>SRON Space Research Organization Netherlands</strong>, funded through <a href="https://projects.au.dk/cleancloud/cleancloud-project">EU Horizon CleanCloud</a>, with <strong>Otto Hasekamp</strong>. My expertise lies in developing aerosol-cloud interactions within climate models and the application of machine learning/AI in climate modeling.
  </p>
  <p>
    My research focuses on improving the representation of aerosols in climate models through observations from satellites, ships, aircraft, and ground stations. I completed my PhD in atmospheric physics and chemistry at the <strong>University of Canterbury</strong> (New Zealand), under the supervision of <strong>Laura Revell</strong> and <strong>Adrian McDonald</strong>.
  </p>
  <p>
    Having lived in four countries, I've embraced a culturally immersive and adaptive lifestyle. I enjoy capturing these experiences through photography, and some of my work can be found in my <a href="/photography">photography</a> section.
  </p>
</div>

<style>
  /* Styling for the About Me Section */
  .about-section {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: Arial, sans-serif;
    line-height: 1.8;
    color: #333;
  }

  .about-section h1 {
    font-size: 2.5em;
    margin-bottom: 20px;
    color: #222;
    text-align: center;
  }

  .about-section p {
    font-size: 1.1em;
    margin-bottom: 20px;
    color: #444;
  }

  .about-section a {
    color: #87CEEB; /* Sky blue */
    text-decoration: none;
    font-weight: bold;
  }

  .about-section a:hover {
    text-decoration: underline;
  }

  .about-section strong {
    color: #222;
    font-weight: bold;
  }
</style>
<div class="experience-section">
  <h1>Work Experience</h1>
  <div class="experience-item">
    <h3> 2024 – Present</h3>
    <h4>SRON Space Research Organization Netherlands (The Netherlands)</h4>
    <h5>Research Scientist</h5>
    <p>
    Climate models, such as ECHAM6-HAM and ICON-HAM, are essential for understanding past and future climate changes. However, significant uncertainties remain, particularly regarding aerosols and clouds. My work focuses on mitigating these uncertainties by integrating new satellite observations from missions like PACE and Earth-Care.
To achieve this, I developed a perturbed parameter ensemble (PPE) consisting of over 221 simulations with slight variations in parameter configurations. Using this PPE as a training set, I apply machine learning techniques to emulate millions of additional simulations efficiently. This approach enables us to pinpoint sources of uncertainty, validate model outputs against observations, and refine the representation of aerosol-cloud interactions in climate models.
By combining satellite data and advanced machine learning, my research aims to enhance the accuracy and reliability of climate projections, contributing to a deeper understanding of aerosol and cloud impacts on the Earth's climate system.

</p>


  </div>

<div class="education-section">
  <h1>Education</h1>
  <div class="education-item">
    <h3>University of Canterbury (New Zealand)</h3>
    <h4>PhD in Physics</h4>
    <h5>Feb 2020 - Dec 2023</h5>

    <p>
      <a href="https://ir.canterbury.ac.nz/items/c6b82640-5663-46d8-8a60-cc3ebbe4e7a6">'Southern Ocean dimethyl sulfide and marine aerosol production simulated with an Earth system model’</a>. Supervised by Laura Revell and Adrian McDonald
    </p>
  </div>
  <div class="education-item">
    <h3>University of Leeds (UK)</h3>
    <h4>Master of Research in Climate and Atmospheric Chemistry and Physics</h4>
    <h5>Sept 2016 - Sept 2017</h5>
    <p>
    Grade: Distinction (A+) <br>

      Research project on ‘The global distribution of volcanic aerosol from a notional December 2017 major eruption’. Supervised by Graham Mann and Ryan Neely III
    </p>
  </div>

  <div class="education-item">
    <h3>University of Keele (UK)</h3>
    <h4>BSc(Hons) Geology with Physical Geography</h4>
    <h5>Sept 2015 - Sept 2018</h5>
    <p>
    Grade: Upper Second Class Honours (2:1)

    </p>
  </div>

  <div class="education-item">
    <h3>University of Utah (USA)</h3>
    <h4>Exchange Student</h4>

    <h5>Aug 2016 - Jan 2017</h5>
    <p>

    </p>
  </div>

</div>

<style>
body {
  background-color: #e6f4fb; /* Soft sky blue */
}

  /* General Styles */
  .profile {
    width: auto;
    height: auto;
    border-radius: 10%;
    display: block;
    margin: 0 auto 0px;
  }

  .about-section,
  .experience-section,
  .education-section {
    margin-bottom: 40px;
  }

  h1 {
    font-size: 2.5em;
    margin-bottom: 20px;
    color: #333;
  }

  h3 {
    font-size: 1.5em;
    margin-bottom: 5px;
    color: #555;
  }

  h4 {
    font-size: 1.2em;
    margin-bottom: 5px;
    color: #777;
  }

  h5 {
    font-size: 1em;
    margin-bottom: 10px;
    color: #999;
  }

  p {
    font-size: 1em;
    line-height: 1.6;
    color: #666;
  }

  .experience-item,
  .education-item {
    margin-bottom: 30px;
    padding: 20px;
    border-left: 5px solid #87CEEB; /* Sky blue accent */
    background-color: #f9f9f9; /* Light background */
    border-radius: 5px;
  }

  .experience-item:hover,
  .education-item:hover {
    background-color: #f1f1f1; /* Slightly darker on hover */
    transition: background-color 0.3s ease;
  }
</style>
