---
layout: page
title: "Research"
permalink: /research/
main_nav: true
---
To see my past publications I have led, see <a href="#past-publications">my Past Lead Author Publications and Research</a>, below.

Also to see the research I have co-authored, see <a href="https://scholar.google.com/citations?user=G7Si4kEAAAAJ&hl=en">my google scholar</a>.

See <a href="Coding-Development.md">Coding Development</a> for model development, software development, and other projects involved in doing these publications.

<h3>Current Research</h3>



<div class="research-item">
<h3>Constraining aerosol-cloud uncertainties in climate models using machine learning applications and the new NASA PACE and ESA EarthCARE satellite.</h3>

  <img src="/assets/Main_page/PACE_mission.jpg" alt="Aerosol-cloud interactions" class="research-image">
  <p> </p>
  <ul>
  <li><strong>Aim:</strong> Reduce uncertainties in aerosol-cloud interactions using machine learning and next-generation satellite data.</li>
  <li><strong>Methods:</strong> Leverage NASA PACE and ESA EarthCARE satellite observations to train machine learning models for improved climate simulations.</li>
  </ul>
  <!-- <p><em>Status: In preparation</em></p> -->
</div>

<a id="past-publications"></a>

<h3 id="past-publications">Past Lead Author Publications and Research</h3>

<div class="research-list">


  <!-- Aerosol-cloud interactions -->
  <div class="research-item">
  <h3>Quantifying aerosol-cloud interactions using machine learning applications to climate models</h3>

    <img src="/assets/Main_page/PPE_Observation_Comparison_2010.png" alt="Aerosol-cloud interactions" class="research-image">
    <ul>
    <li><strong>Aim:</strong> Quantify uncertainties in aerosol-cloud interactions and their impact on radiative forcing.</li>
    <li><strong>Methods:</strong> Developed a perturbed parameter ensemble (PPE) of 221 simulations in ECHAM6.3-HAM2.3, varying 25 key parameters.</li>
    <li>Regional uncertainties in aerosol parameters contribute to regional uncertainties in aerosol radiative effects.</li>
    </ul>
    <a href="https://doi.org/10.5194/egusphere-2025-2848" class="research-link">Read Manuscript</a>
  </div>

  <!-- UKESM1 chemistry -->
  <div class="research-item">
    <h3>Aerosol and Dimethyl Sulfide Sensitivity to Sulfate Chemistry Schemes
    <img src="/assets/Main_page/Paper_3.png" alt="chemistry" class="research-image">

</h3>
    <ul>
    <li><strong>Aim:</strong> Evaluate the sensitivity of sulfate aerosol to DMS oxidation pathways in CMIP6 models.</li>
    <li><strong>Methods:</strong> Implemented seven DMS and sulfate chemistry schemes in an atmosphere-only Earth system model.</li>
    <li>The simulated spread in aerosol optical depth and cloud droplet number concentration is more than twice as large as the change from pre-industrial to present-day.</li>
    <li>Constraining the chemistry of atmospheric sulfur is critical to constrain aerosol-cloud interactions.</li>
    </ul>
    <a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2023JD040635" class="research-link">Read Manuscript</a>
  </div>


  <!-- UKESM1 model development -->
  <div class="research-item">
  <h3>The sensitivity of Southern Ocean atmospheric dimethyl sulfide (DMS) to modeled oceanic DMS concentrations and emissions

    <img src="/assets/Main_Page/Paper_2.png" alt="ccn" class="research-image">

</h3>
<ul>
<li><strong>Aim:</strong> Assess the sensitivity of atmospheric DMS to oceanic DMS datasets and transfer velocity parameterizations.</li>
<li><strong>Methods:</strong> Conducted eight 10-year simulations using UKESM1-AMIP, testing four oceanic DMS datasets and three transfer velocity parameterizations.</li>
<li>The choice of oceanic DMS dataset has a larger influence on atmospheric DMS than the choice of DMS transfer velocity.</li>
<li>Capturing large-scale spatial variability can be more important than large-scale interannual variability.</li>
</ul>
<a href="https://acp.copernicus.org/articles/23/15181/2023/" class="research-link">Read Manuscript</a>

</div>
  <!-- Ozone -->
  <div class="research-item">
    <h3>Influences of Antarctic Ozone Depletion on Southern Ocean Aerosols</h3>
    <img src="/assets/Main_page/Paper_1.png" alt="Ozone_Depletion" class="research-image">

    <ul>
    <li><strong>Aim:</strong> Investigate the impact of Antarctic ozone depletion on Southern Ocean aerosols.</li>
    <li><strong>Methods:</strong> Analyzed state-of-the-art Earth System Models to evaluate changes in aerosol fluxes and marine biogeochemical activity.</li>
    <li>Wind-driven Southern Ocean aerosol fluxes are influenced by the ozone hole during austral summer.</li>
    <li>Indirect influences of ozone losses mean Southern Ocean aerosols cannot be considered to be representative of pristine conditions.</li>
    </ul>
    <a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2022JD037199" class="research-link">Read Manuscript</a>
  </div>
</div>

  <!-- Ozone -->
  <div class="research-item">
    <h3>PhD Thesis in Physics: Southern Ocean dimethyl sulfide and marine aerosol production simulated with an earth system model</h3>
    <img src="/assets/Main_page/Schematic.png" alt="Ozone_Depletion" class="research-image">

    <ul>
      <li><strong>Aim:</strong> Simulate Southern Ocean DMS and marine aerosol production using an Earth System Model.</li>
      <li><strong>Methods:</strong> Developed and validated a model framework to simulate DMS emissions and their impact on marine aerosols.</li>
    </ul>
    <a href="https://libcat.canterbury.ac.nz/Record/in1360920" class="research-link">Read PhD Thesis</a>
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
      width: 120%; /* Adjust this value as needed */
      max-width: auto; /* Ensures images don't get too large */
      height: auto;
      object-fit: cover;
      <!-- border-radius: 8px;
      margin-bottom: 15px; -->
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
