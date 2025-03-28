---
layout: page
title: "Teaching and Conferences"
permalink: /teaching-conferences/
main_nav: true
---

## Teaching (University of Canterbury)

- **2020 – 2023** Introductory Physics for Physical Sciences and Engineering (PHYS111)  
- **2022** Environmental and Climate Modelling (PHYS330/PHYS430)  
- **2020 – 2022** Planet Earth: An Introduction to Geology (GEOL111)  
- **2020 – 2021** Field Studies A - Mapping (GEOL240)  

---

## Invited Talks and Conference Chairing

- **2023** Invited Talk – Met Office  
- **2022** Invited Talk – Clean Air Society of New Zealand and Australia  
- **2020** New Zealand Meteorological Society Conference Committee Member  
- **2020** Session Chair – New Zealand Meteorological Society Conference  

---

## Grants and Awards

- **2025** Surf/NWO-i HPC CPU and GPU Large Compute Grant (~€60,000)  
- **2024** Surf HPC CPU Small Compute Grant (~€15,000)  
- **2023** UC Foundation Doctoral Publication Prize  
- **2022** UC Foundation Doctoral Publication Prize  
- **2021** Outstanding People's Choice Poster – Antarctica New Zealand Conference, Christchurch  
- **2020** Winner – University of Canterbury Gradfest Competition  
- **2020** Best Poster – New Zealand Meteorological Society Conference, Christchurch  
- **2020** School of Physical and Chemical Sciences PhD Award, Christchurch  
- **2018** Bronze Volunteer Award, Keele  

### Travel Grant
- **2023** School of Physical and Chemical Sciences Travel Grant  
- **2023** New Zealand Meteorological Society International Travel Grant
- **2023** New Zealand Meteorological Society Domestic Travel Grant    
- **2023** Clean Air Society of New Zealand and Australia Travel Grant
- **2019** Aerosol Society Early Career Scientist Travel Award, Leeds  


---

## Talks

- **2025** Presentation – American Meteorological Society, New Orleans  
- **2024** Presentation – Aerocom/Aerosat, Lille  
- **2023** Presentation – New Zealand Meteorological Society Conference, Wellington
- **2023** Presentation – European Geosciences Union (EGU), Vienna   
- **2022** Poster – CATCH, Online Workshop
- **2022** Presentation – Australian Meteorological and Oceanographic Society, Adelaide  
- **2022** Presentation – International Conference on Southern Hemisphere Meteorology and Oceanography (ICSCHMO), Online  
- **2021** Presentation & Poster – New Zealand Meteorological Society Conference, Dunedin  
- **2021** Presentation – European Geosciences Union (EGU), Online  
- **2021** Poster – Antarctica New Zealand Conference, Christchurch  
- **2020** Presentation & Poster – New Zealand Meteorological Society Conference, Christchurch  
- **2019** Poster – European Aerosol Conference, Gothenburg  

---

## Society Memberships

- American Meteorological Society  
- Australian Meteorological and Oceanographic Society  
- Meteorological Society of New Zealand  
- Clean Air Society of Australia & New Zealand  

---

{% for category in site.categories %}
  {% capture cat %}{{ category | first }}{% endcapture %}
  <h2 id="{{cat}}">{{ cat | capitalize }}</h2>
  {% for desc in site.descriptions %}
    {% if desc.cat == cat %}
      <p class="desc"><em>{{ desc.desc }}</em></p>
    {% endif %}
  {% endfor %}
  <ul class="posts-list">
  {% for post in site.categories[cat] %}
    <li>
      <strong>
        <a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
      </strong>
      <span class="post-date">- {{ post.date | date_to_long_string }}</span>
    </li>
  {% endfor %}
  </ul>
  {% if forloop.last == false %}<hr>{% endif %}
{% endfor %}
<br>
