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
them, spanning model development (ECHAM6-HAM, ICON-HAM, UKESM1), perturbed-parameter ensembles,
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
    <h4>Aerosol-Cloud Interactions</h4>
    <p>Quantifying how aerosols influence cloud properties and Earth's radiation budget, and constraining
    the resulting uncertainty in climate projections.</p>
  </div>
  <div class="interest-item">
    <h4>Machine Learning Emulation</h4>
    <p>Develop and train Gaussian process emulators on large perturbed-parameter
    ensembles.</p>
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
  <li><strong>Aim:</strong> Constrain aerosol Effective Radiative Forcing (ERF) uncertainty in climate models - one of the largest remaining uncertainties in future climate projections.</li>
  <li><strong>Methods:</strong> Use PACE and EarthCARE satellite observations of aerosol amount, size, absorption, and vertical distribution, together with cloud droplet number concentration, to constrain a perturbed parameter ensemble of aerosol-climate model simulations.</li>
  <li><strong>Results:</strong> Combining these observations reduces aerosol ERF parametric uncertainty by 34%, narrowing the ERFari and ERFaci credible interval ranges by 66% and 32% respectively.</li>
  <li>The resulting observation-consistent ERF estimate of -1.52 W/m&sup2; [-2.0 to -1.1 W/m&sup2;] suggests stronger aerosol cooling than the current IPCC estimate of -1.3 [-2.0 to -0.6] W/m&sup2;.</li>
  </ul>
</div>

<h3 id="research-highlights">Research Highlights</h3>

<div class="research-item">
  <h3>Quantifying aerosol uncertainties using machine learning applications (perturbed parameter ensemble) to climate models</h3>
  <img src="/assets/Main_page/PPE_Observation_Comparison_2010.png" alt="Aerosol-cloud interactions" class="research-image">
  <p class="citation">
  <strong>Bhatti, YA.,</strong> Watson-Parris, D., Regayre, L., Jia, H., Neubauer, D., Im, U., Svenhag, C., Schutgens, N., Tsikerdekis, A., Nenes, A., Muhammed, I., van Diedenhoven, B., Arifi, A., Fu, G., Hasekamp, O. (2026).
  <a href="https://doi.org/10.5194/acp-26-269-2026">
    Uncertainty in aerosol effective radiative forcing from anthropogenic and natural aerosol parameters in ECHAM6.3-HAM2.3.</a> <em>Atmospheric Chemistry and Physics</em>, 26(1), 269-293.
  </p>
  <ul>
  <li><strong>Aim:</strong> Quantify parametric uncertainty in aerosol effective radiative forcing (ERF) from aerosol-cloud and aerosol-radiation interactions.</li>
  <li><strong>Methods:</strong> Developed a perturbed parameter ensemble (PPE) of 221 simulations in ECHAM6.3-HAM2.3, varying 23 parameters controlling aerosol emissions, removal, chemistry, and microphysics.</li>
  <li><strong>Results:</strong> Global uncertainty is dominated by sulfate-related processes, biomass burning, aerosol size, and natural emissions.</li>
  <li>Sulfate chemistry and dry deposition most strongly influence aerosol-radiation interactions, while DMS and biomass burning emissions dominate aerosol-cloud interactions.</li>
  <li>Comparison with POLDER-3/PARASOL satellite retrievals reveals persistent model biases in aerosol optical depth, &Aring;ngstr&ouml;m exponent, and single-scattering albedo - sulfate-related processes alone account for over 40% of AOD uncertainty.</li>
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
  <li><strong>Results:</strong> The choice of oceanic DMS dataset has a larger influence on atmospheric DMS than the choice of DMS transfer velocity.</li>
  <li>Capturing large-scale spatial variability can be more important than large-scale interannual variability.</li>
  </ul>
  <a href="https://acp.copernicus.org/articles/23/15181/2023/" class="research-link">Read Manuscript</a>
</div>

<div class="research-item">
  <h3>Aerosol and Dimethyl Sulfide Sensitivity to Sulfate Chemistry Schemes</h3>
  <img src="/assets/Main_page/Paper_3.png" alt="chemistry" class="research-image">
  <p class="citation">
    <strong>Bhatti, YA.</strong>, Revell, LE., McDonald, AJ., Archibald, AT., Schuddeboom, AJ., Williams, J., Hardacre, C., Mulcahy, J., Lin, D. (2024).
    <a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2023JD040635">Aerosol and dimethyl sulfide sensitivity to sulfate chemistry schemes.</a>
    <em>Journal of Geophysical Research: Atmospheres</em>, 129(12), e2023JD040635.
  </p>
  <ul>
  <li><strong>Aim:</strong> Evaluate the sensitivity of sulfate aerosol to DMS oxidation pathways in CMIP6 models.</li>
  <li><strong>Methods:</strong> Implemented seven DMS and sulfate chemistry schemes in an atmosphere-only Earth system model.</li>
  <li><strong>Results:</strong> The simulated spread in aerosol optical depth and cloud droplet number concentration is more than twice as large as the change from pre-industrial to present-day.</li>
  <li>Constraining the chemistry of atmospheric sulfur is critical to constrain aerosol-cloud interactions.</li>
  </ul>
  <a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2023JD040635" class="research-link">Read Manuscript</a>
</div>

<div class="research-item">
  <h3>Influences of Antarctic Ozone Depletion on Southern Ocean Aerosols</h3>
  <img src="/assets/Main_page/Paper_1.png" alt="Ozone_Depletion" class="research-image">
  <p class="citation">
    <strong>Bhatti, YA.</strong>, Revell, LE., McDonald, AJ. (2022).
    <a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2022JD037199">Influences of Antarctic ozone depletion on southern ocean aerosols.</a>
    <em>Journal of Geophysical Research: Atmospheres</em>, 127(18), e2022JD037199.
  </p>
  <ul>
  <li><strong>Aim:</strong> Investigate the impact of Antarctic ozone depletion on Southern Ocean aerosols.</li>
  <li><strong>Methods:</strong> Analyzed state-of-the-art Earth System Models to evaluate changes in aerosol fluxes and marine biogeochemical activity.</li>
  <li><strong>Results:</strong> Indirect influences of ozone losses mean Southern Ocean aerosols cannot be considered to be representative of pristine conditions.</li>
<li> Wind-driven Southern Ocean aerosol fluxes are influenced by the ozone hole during austral summer.</li>
  </ul>
  <a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2022JD037199" class="research-link">Read Manuscript</a>
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
