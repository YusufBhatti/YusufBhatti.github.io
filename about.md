---
layout: page
title: About Me
permalink: /about/
main_nav: true
---

![alt text]({{ site.baseurl }}/assets/Yusuf_Headshot-web.jpg){:.profile}

<div class="about-section">
  <h1></h1>
  <p>

  I am an atmospheric scientist specializing in climate model development and reducing uncertainties from clouds and aerosol. Currently, I work as a research scientist at the <strong>SRON Space Research Organization Netherlands</strong>, funded through the <a href="https://projects.au.dk/cleancloud/cleancloud-project">EU Horizon CleanCloud</a>, with <strong>Otto Hasekamp</strong>. My expertise includes improving aerosol-cloud interactions within climate models and applying machine learning and AI techniques. 

  </p>
  <p>
I am involved in the development of the ECHAM6-HAM2.3 and ICON-HAM climate models. Much of my research focuses on improving the representation of aerosols in climate models through observations from satellites, ships, aircraft, and ground stations. During my PhD, I was code owner and core developer of the UKESM1 model, up to version 13.2 of the Unified Model.

In 2023, I completed my PhD in atmospheric physics and chemistry at the <strong>University of Canterbury</strong> in New Zealand, under the supervision of <strong>Laura Revell</strong> and <strong>Adrian McDonald</strong>. My Master’s project (MRes; Master of Research) was conducted under the guidance of <strong> Graham Mann </strong> at the <strong> University of Leeds</strong>, where I modeled stratospheric sulfate aerosol injections.

  </p>
  <p>
Having lived in four countries, I have embraced a culturally immersive and enjoyable lifestyle. I've been capturing these experiences through photography, some of which can be found in my <a href="/photography">photography</a> section.
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
    color: #000080; /* Navy blue */
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
  <h1>Research Experience</h1>
  <div class="experience-item">
    <h3> 2024 – Present</h3>
    <h4>Research Scientist</h4>
    <h4>SRON Space Research Organization Netherlands (The Netherlands)</h4>
<p>
Climate models, such as ECHAM6-HAM and ICON-HAM, are essential tools for understanding past and future climate change. However, significant uncertainties remain, particularly in the representation of aerosols and clouds. My work focuses on reducing these uncertainties by combining advanced climate modelling, perturbed parameter ensembles (PPEs), machine learning, and new satellite observations from missions including NASA/SRON's PACE and ESA's EarthCARE.
</p>
<p>
To achieve this, I develop perturbed parameter ensembles consisting of hundreds of climate model simulations with systematic variations in model parameters. Using these PPEs as training sets, I apply machine learning techniques to emulate millions of additional model configurations efficiently. This approach enables us to identify the sources of uncertainty within climate models, evaluate model outputs against satellite observations, and constrain the representation of aerosol-cloud interactions and their impact on climate forcing.
</p>
<p>
I also co-coordinate an international, multi-model perturbed-parameter ensemble inter-comparison (PPE-ACI MIP) spanning ECHAM6-HAM, ICON-HAM, UKESM1/HadGEM, CAM6, and other climate models. My responsibilities include developing and maintaining automated Python and Bash pipelines for processing more than 100 TB of climate model and satellite NetCDF data, with version-controlled workflows using Git. I also mentor students in climate model development, scientific computing, and data analysis at SRON, alongside international collaborators.
</p>
<p>
By combining satellite observations, climate modelling, and advanced machine learning, my research aims to reduce uncertainties in climate projections and improve our understanding of aerosol and cloud processes and their impacts on the Earth's climate system.
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
    <h3>University of Leeds (United Kingdom)</h3>
    <h4>Master of Research in Climate and Atmospheric Chemistry and Physics</h4>
    <h5>Sept 2016 - Sept 2017</h5>
    <p>
    Grade: Distinction (A+) <br>

      Research project on ‘The global distribution of volcanic aerosol from a notional December 2017 major eruption’. Supervised by Graham Mann and Ryan Neely III
    </p>
  </div>

  <div class="education-item">
    <h3>University of Keele (United Kingdom)</h3>
    <h4>BSc(Hons) Geology with Physical Geography</h4>
    <h5>Sept 2015 - Sept 2018</h5>
    <p>
    Grade: Upper Second Class Honours (2:1)

    </p>
  </div>

  <div class="education-item">
    <h3>University of Utah (United States of America)</h3>
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
