---
layout: page
title: "Research"
permalink: /research/
main_nav: true
---

<div class="research-list">

<p class="research-overview">
My research quantifies and reduces uncertainty in how aerosols and clouds interact within the Earth's
climate system. I combine large-scale climate model experiments, satellite observations, and machine
learning to work out where climate models get aerosol-cloud interactions wrong, why, and how to fix
them &mdash; spanning model development (ECHAM6-HAM, ICON-HAM, UKESM1), perturbed-parameter ensembles,
and Gaussian process / neural network emulation.
</p>

<p class="research-links">
See my <a href="https://scholar.google.com/citations?user=G7Si4kEAAAAJ&hl=en">Google Scholar</a> or
<a href="https://orcid.org/0000-0003-1254-9845">ORCID record</a> for the full citation record, or visit
my <a href="/publications">Publications page</a> for the complete list.
</p>

<h3>Research Interests</h3>
<div class="interests-grid">
  <div class="interest-item">
    <h4>Aerosol&ndash;Cloud Interactions</h4>
    <p>Quantifying how aerosols influence cloud properties and Earth's radiation budget, and constraining
    the resulting uncertainty in climate projections.</p>
  </div>
  <div class="interest-item">
    <h4>Machine Learning Emulation</h4>
    <p>Building Gaussian process and neural network emulators trained on large perturbed-parameter
    ensembles, making uncertainty quantification computationally tractable at scale.</p>
  </div>
  <div class="interest-item">
    <h4>Satellite-Constrained Modelling</h4>
    <p>Using observations from NASA PACE, ESA EarthCARE, and other missions to evaluate and constrain
    aerosol and cloud processes in global and regional climate models.</p>
  </div>
</div>

<h3>Current Research</h3>
<div class="research-item">
  <h3>Using machine learning and satellites to constrain climate models' aerosol uncertainty</h3>
  <img src="/assets/Main_page/PACE_mission.jpg" alt="Aerosol-cloud interactions" class="research-image">
  <ul>
  <li><strong>Aim:</strong> Reduce uncertainties in aerosol-cloud interactions using machine learning and next-generation satellite data.</li>
  <li><strong>Methods:</strong> Use NASA PACE and ESA EarthCARE satellite observations to train machine learning models for improved climate simulations.</li>
  </ul>
</div>

<h3 id="research-highlights">Research Highlights</h3>

<div class="research-item">
  <h3>Quantifying aerosol-cloud interactions using machine learning applications to climate models</h3>
  <img src="/assets/Main_page/PPE_Observation_Comparison_2010.png" alt="Aerosol-cloud interactions" class="research-image">
  <p class="citation">
  <strong>Bhatti, YA.,</strong> Watson-Parris, D., Regayre, L., Jia, H., Neubauer, D., Im, U., Svenhag, C., Schutgens, N., Tsikerdekis, A., Nenes, A., Muhammed, I., van Diedenhoven, B., Arifi, A., Fu, G., Hasekamp, O. (2026).
  <a href="https://doi.org/10.5194/acp-26-269-2026">
    Uncertainty in aerosol effective radiative forcing from anthropogenic and natural aerosol parameters in ECHAM6.3-HAM2.3.</a> <em>Atmospheric Chemistry and Physics</em>, 26(1), 269-293.
  </p>
  <ul>
  <li><strong>Aim:</strong> Quantify uncertainties in aerosol-cloud interactions and their impact on radiative forcing.</li>
  <li><strong>Methods:</strong> Developed a perturbed parameter ensemble (PPE) of 221 simulations in ECHAM6.3-HAM2.3, varying 23 key parameters.</li>
  <li>Regional uncertainties in aerosol parameters contribute to regional uncertainties in aerosol radiative effects.</li>
  </ul>
  <a href="https://doi.org/10.5194/egusphere-2025-2848" class="research-link">Read Manuscript</a>
</div>

<div class="research-item">
  <h3>The sensitivity of Southern Ocean atmospheric dimethyl sulfide (DMS) to modeled oceanic DMS concentrations and emissions</h3>
  <img src="/assets/Main_Page/Paper_2.png" alt="ccn" class="research-image">
  <p class="citation">
    <strong>Bhatti, YA.</strong>, Revell, LE., Schuddeboom, AJ., McDonald, AJ., Archibald, AT., Williams, J., Venugopal, AU., Hardacre, C., Behrens, E. (2023).
    <a href="https://acp.copernicus.org/articles/23/15181/2023/">The sensitivity of Southern Ocean atmospheric dimethyl sulfide (DMS) to modeled oceanic DMS concentrations and emissions.</a>
    <em>Atmospheric Chemistry and Physics</em>, 23(24), 15181-15196.
  </p>
  <ul>
  <li><strong>Aim:</strong> Assess the sensitivity of atmospheric DMS to oceanic DMS datasets and transfer velocity parameterizations.</li>
  <li><strong>Methods:</strong> Conducted eight 10-year simulations using UKESM1-AMIP, testing four oceanic DMS datasets and three transfer velocity parameterizations.</li>
  <li>The choice of oceanic DMS dataset has a larger influence on atmospheric DMS than the choice of DMS transfer velocity.</li>
  <li>Capturing large-scale spatial variability can be more important than large-scale interannual variability.</li>
  </ul>
  <a href="https://acp.copernicus.org/articles/23/15181/2023/" class="research-link">Read Manuscript</a>
</div>

<p class="research-links">
See my full <a href="/publications">Publications list</a> for every peer-reviewed article, in-review
manuscript, and my PhD thesis.
</p>

</div>

<style>
body {
  background-color: #e6f4fb; /* Soft sky blue */
}

.research-overview {
  max-width: 800px;
  margin: 0 auto 0.5em;
  font-size: 1.1em;
  line-height: 1.7;
  color: #333;
}

.research-links {
  max-width: 800px;
  margin: 0 auto 2em;
  font-size: 0.95em;
  color: #555;
}

.research-links a {
  color: #1a0dab;
  text-decoration: underline;
}

.interests-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  max-width: 800px;
  margin: 0 auto 2em;
}

.interest-item {
  flex: 1 1 220px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-left: 5px solid #87CEEB;
  border-radius: 8px;
  padding: 14px 18px;
}

.interest-item h4 {
  margin: 0 0 6px;
  font-size: 1.05em;
  color: #222;
}

.interest-item p {
  margin: 0;
  font-size: 0.92em;
  color: #555;
  line-height: 1.5;
}

  /* Styling for the Research List */
  .research-list {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }

  /* Styling for Each Research Item */
  .research-item {
    background-color: #e8f0f4ff;
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
      max-width: auto; /* Ensures images don't get too large */
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
    background-color: rgb(108, 178, 216, 1);
    border-radius: 4px;
    text-decoration: none;
    transition: background-color 0.3s ease;
  }

  .research-link:hover {
    background-color: rgb(88, 158, 196, 1); /* Darker blue on hover (was identical to base color before) */
  }

  .research-item em {
    font-style: italic;
    color: #777;
  }
</style>
