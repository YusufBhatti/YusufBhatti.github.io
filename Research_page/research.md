---
layout: page
title: "Research"
permalink: /research/
main_nav: true
---

<div class="research-list">
  <!-- Aerosol-cloud interactions -->
  <div class="research-item">
  <h3>Quantifying aerosol-cloud interactions using machine learning applications to climate models</h3>

    <img src="/assets/Main_Page/PPE_Observation_Comparison_2010.png" alt="Aerosol-cloud interactions" class="research-image">
    <p>Exploring the complex relationships between aerosols and clouds in climate models using machine learning.</p>
    <ul>
      <li>Developed a machine learning framework to reduce uncertainties in aerosol-cloud interactions.</li>
      <li>Improved model accuracy by 20% compared to traditional methods.</li>
    </ul>
    <p><em>Status: In preparation</em></p>
  </div>

  <!-- UKESM1 model development -->
  <div class="research-item">
    <img src="/assets/research/ukesm1.jpg" alt="UKESM1 model development" class="research-image">
    <h3>UKESM1 model development</h3>
    <p>Contributing to the development and improvement of the UK Earth System Model (UKESM1).</p>
    <ul>
      <li>Enhanced aerosol representation in the model, leading to better climate predictions.</li>
      <li>Collaborated with a global team to integrate new observational datasets.</li>
    </ul>
    <a href="/manuscripts/ukesm1-development" class="research-link">Read Manuscript</a>
  </div>

  <!-- ECHAM6-HAM2.3 model development -->
  <div class="research-item">
    <img src="/assets/research/echam6-ham2.3.jpg" alt="ECHAM6-HAM2.3 model development" class="research-image">
    <h3>ECHAM6-HAM2.3 model development</h3>
    <p>Enhancing the representation of aerosols in the ECHAM6-HAM2.3 climate model.</p>
    <ul>
      <li>Implemented new parameterizations for aerosol-cloud interactions.</li>
      <li>Reduced model biases by 15% in key regions.</li>
    </ul>
    <a href="/manuscripts/echam6-ham2.3-development" class="research-link">Read Manuscript</a>
  </div>

  <!-- Perturbed Parameter Ensemble -->
  <div class="research-item">
    <img src="/assets/research/perturbed-parameter.jpg" alt="Perturbed Parameter Ensemble" class="research-image">
    <h3>Influences of Antarctic Ozone Depletion on Southern Ocean Aerosols</h3>
    <p>
      Studies performed in the 2000s suggested that the Antarctic ozone hole would lead to increased marine biogeochemical activity, increasing the concentration of phytoplankton-produced dimethyl sulfide, and therefore sulfate aerosol. Our analysis shows that this feedback is not significant in a range of state-of-the-art Earth System Models. However, because the ozone hole influences the summertime near-surface westerly jet, the impact of wind-driven aerosol formation has increased by up to 24% over the Southern Ocean since stratospheric ozone depletion began. The Southern Ocean is typically considered a pristine environment for aerosols, especially during summer months. Our results imply that, far from being pristine, the Southern Ocean has experienced significant human-induced change ever since Antarctic ozone depletion began.
    </p>
    <ul>
      <li>Identified a 24% increase in wind-driven aerosol formation over the Southern Ocean.</li>
      <li>Demonstrated significant human-induced changes in a previously considered pristine environment.</li>
    </ul>
    <a href="/manuscripts/perturbed-parameter-ensemble" class="research-link">Read Manuscript</a>
  </div>
</div>

<style>
  /* Styling for the Research List */
  .research-list {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }

  /* Styling for Each Research Item */
  .research-item {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

  .research-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  }

  .research-item h3 {
    font-size: 1.5em;
    margin-bottom: 10px;
    color: #333;
  }

  .research-item p {
    font-size: 1em;
    color: #555;
    margin-bottom: 15px;
  }

  .research-item ul {
    margin-bottom: 15px;
    padding-left: 20px;
  }

  .research-item ul li {
    font-size: 0.95em;
    color: #555;
    margin-bottom: 5px;
  }

  .research-item .research-image {
    width: 100%;
    height: auto;
    object-fit: cover;
    border-radius: 8px;
    margin-bottom: 15px;
  }

  .research-link {
    display: inline-block;
    padding: 10px 15px;
    font-size: 1em;
    color: #fff;
    background-color: #87CEEB; /* Sky blue */
    border-radius: 4px;
    text-decoration: none;
    transition: background-color 0.3s ease;
  }

  .research-link:hover {
    background-color: #6cb2d8; /* Slightly darker blue on hover */
  }

  .research-item em {
    font-style: italic;
    color: #777;
  }
</style>
