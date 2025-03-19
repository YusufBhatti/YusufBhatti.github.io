---
layout: page
title: "Research"
permalink: /research/
main_nav: true
---
See <a href="Coding-Development.md">Coding Development</a> for model development, software development, and other projects involved in doing these publications.

<h3>Current Research</h3>



<div class="research-item">
<h3>Constraining aerosol-cloud uncertainties in climate models using machine learning applications and the new NASA PACE and ESA EarthCARE satellite.</h3>

  <img src="/assets/Main_Page/.png" alt="Aerosol-cloud interactions" class="research-image">
  <p> </p>
  <ul>
    <!-- <li>Developed a PPE for ECHAM6-HAM to quantify uncertainties in aerosol-cloud interactions.</li>
    <li> Regional uncertainties in aerosol parameters contribute to regional
    uncertainties in aerosol radiative effects. </li> -->
  </ul>
  <p><em>Status: In preparation</em></p>
</div>


<h3>Past Publications and Research</h3>

<div class="research-list">


  <!-- Aerosol-cloud interactions -->
  <div class="research-item">
  <h3>Quantifying aerosol-cloud interactions using machine learning applications to climate models</h3>

    <img src="/assets/Main_Page/PPE_Observation_Comparison_2010.png" alt="Aerosol-cloud interactions" class="research-image">
    <p>Aerosol–cloud interactions remain one of the largest uncertainties to effective radiative forcing (ERF) estimates, limiting the
accuracy of climate projections. This study quantifies parametric aerosol and cloud uncertainties in the ECHAM6.3-HAM2.3
climate model using a perturbed parameter ensemble (PPE) of 221 simulations, varying 25 key parameters. The resulting global
mean aerosol ERF is -1.62 W m−2 (95% credible range: -2.22 to -1.08 W m−2), with the cloud droplet number concentration
parameter (CDNC_min) contributing 19% of total uncertainty. Sulfate and black carbon emissions also play a major role,
particularly in regions with high biomass burning activity.
Comparison with satellite observations from POLDER (PARASOL) reveals model biases in aerosol optical depth (AOD),
Ångström exponent (AE), and single scattering albedo (SSA), primarily due to coarse-mode aerosol underestimation and
biases in natural aerosol emissions. Coarse-mode sea salt, dust, and carbonaceous aerosols are insufficiently represented, likely
due to excessive removal before coagulation and growth. Regional uncertainties in aerosol parameters contribute to regional
uncertainties in aerosol radiative effects. Oceans generally demonstrate a higher uncertainty for present-day aerosol than over land. We find that areas of highest model AOD uncertainty correspond to areas that are different with observations. </p>
    <ul>
      <li>Developed a PPE for ECHAM6-HAM to quantify uncertainties in aerosol-cloud interactions.</li>
      <li> Regional uncertainties in aerosol parameters contribute to regional
      uncertainties in aerosol radiative effects. </li>
    </ul>
    <p><em>Status: In preparation</em></p>
  </div>

  <!-- UKESM1 chemistry -->
  <div class="research-item">
    <h3>Aerosol and Dimethyl Sulfide Sensitivity to Sulfate Chemistry Schemes
    <img src="/assets/Main_page/Paper_3.png" alt="chemistry" class="research-image">

</h3>
    <p>
    Dimethyl sulfide (DMS) is the largest source of natural sulfur in the atmosphere and undergoes oxidation reactions resulting in gas-to-particle conversion to form sulfate aerosol. Climate models typically use independent chemical schemes to simulate these processes, however, the sensitivity of sulfate aerosol to the schemes used by CMIP6 models has not been evaluated. Current climate models offer oversimplified DMS oxidation pathways, adding to the ambiguity surrounding the global sulfur burden. Here, we implemented seven DMS and sulfate chemistry schemes, six of which are from CMIP6 models, in an atmosphere-only Earth system model. A large spread in aerosol optical depth (AOD) is simulated (0.077), almost twice the magnitude of the pre-industrial to present-day increase in AOD. Differences are largely driven by the inclusion of the nighttime DMS oxidation reaction with NO3, and in the number of aqueous phase sulfate reactions. Our analysis identifies the importance of DMS-sulfate chemistry for simulating aerosols. We suggest that optimizing DMS/sulfur chemistry schemes is crucial for the accurate simulation of sulfate aerosols.

    </p>
    <ul>
      <li>The simulated spread in aerosol optical depth and cloud droplet number concentration is more than twice as large as the change from pre-industrial to present-day.</li>
      <li>Constraining the chemistry of atmospheric sulfur is critical to constrain aerosol-cloud interactions.
</li>
    </ul>
    <a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2023JD040635" class="research-link">Read Manuscript</a>
  </div>


  <!-- UKESM1 model development -->
  <div class="research-item">
  <h3>The sensitivity of Southern Ocean atmospheric dimethyl sulfide (DMS) to modeled oceanic DMS concentrations and emissions

    <img src="/assets/Main_Page/Paper_2.png" alt="ccn" class="research-image">

</h3>
<p>
The biogeochemical formation of dimethyl sulfide (DMS) from the Southern Ocean is complex, dynamic, and driven by physical, chemical, and biological processes. Such processes, produced by marine biogenic activity, are the dominant source of sulfate aerosol over the Southern Ocean. Using an atmosphere-only configuration of the United Kingdom Earth System Model (UKESM1-AMIP), we performed eight 10-year simulations for the recent past (2009–2018) during austral summer. We tested the sensitivity of atmospheric DMS to four oceanic DMS datasets and three DMS transfer velocity parameterizations. One oceanic DMS dataset was developed here from satellite chlorophyll a. We find that the choice of oceanic DMS dataset has a larger influence on atmospheric DMS than the choice of DMS transfer velocity. Simulations with linear transfer velocity parameterizations show a more accurate representation of atmospheric DMS concentration than those using quadratic relationships. This work highlights that the oceanic DMS and DMS transfer velocity parameterizations currently used in climate models are poorly constrained for the Southern Ocean region. Simulations using oceanic DMS derived from satellite chlorophyll a data, and when combined with a recently developed linear transfer velocity parameterization for DMS, show better spatial variability than the UKESM1 configuration. We also demonstrate that capturing large-scale spatial variability can be more important than large-scale interannual variability. We recommend that models use a DMS transfer velocity parameterization that was developed specifically for DMS and improvements to oceanic DMS spatial variability. Such improvements may provide a more accurate process-based representation of oceanic and atmospheric DMS, and therefore sulfate aerosol, in the Southern Ocean region.

</p>
<ul>
  <li>The choice of oceanic DMS dataset has a larger influence on atmospheric DMS than the choice of DMS transfer velocity.</li>
  <li>Capturing large-scale spatial variability can be more important than large-scale interannual variability.
</li>
</ul>
<a href="https://acp.copernicus.org/articles/23/15181/2023/" class="research-link">Read Manuscript</a>

</div>
  <!-- Ozone -->
  <div class="research-item">
    <h3>Influences of Antarctic Ozone Depletion on Southern Ocean Aerosols</h3>
    <img src="/assets/Main_page/Paper_1.png" alt="Ozone_Depletion" class="research-image">

    <p>
      Studies performed in the 2000s suggested that the Antarctic ozone hole would lead to increased marine biogeochemical activity, increasing the concentration of phytoplankton-produced dimethyl sulfide, and therefore sulfate aerosol. Our analysis shows that this feedback is not significant in a range of state-of-the-art Earth System Models. However, because the ozone hole influences the summertime near-surface westerly jet, the impact of wind-driven aerosol formation has increased by up to 24% over the Southern Ocean since stratospheric ozone depletion began. The Southern Ocean is typically considered a pristine environment for aerosols, especially during summer months. Our results imply that, far from being pristine, the Southern Ocean has experienced significant human-induced change ever since Antarctic ozone depletion began.
    </p>
    <ul>
      <li>Wind-driven Southern Ocean aerosol fluxes are influenced by the ozone hole during austral summer.</li>
      <li>Indirect influences of ozone losses mean Southern Ocean aerosols cannot be considered to be representative of pristine conditions.
.</li>
    </ul>
    <a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2022JD037199" class="research-link">Read Manuscript</a>
  </div>
</div>

  <!-- Ozone -->
  <div class="research-item">
    <h3>PhD Thesis in Physics: Southern Ocean dimethyl sulfide and marine aerosol production simulated with an earth system model</h3>
    <img src="/assets/Main_page/Paper_1." alt="Ozone_Depletion" class="research-image">

    <p>
    </p>
    <ul>
      <!-- <li>Wind-driven Southern Ocean aerosol fluxes are influenced by the ozone hole during austral summer.</li>
      <li>Indirect influences of ozone losses mean Southern Ocean aerosols cannot be considered to be representative of pristine conditions. -->
<!-- .</li> -->
    </ul>
    <a href="https://libcat.canterbury.ac.nz/Record/in1360920" class="research-link">Read PhD Thesis</a>
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
