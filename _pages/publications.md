---
title: "Vermaas Lab - Publications"
layout: gridlay
excerpt: "Vermaas Lab -- Publications."
sitemap: false
permalink: /publications/
---


# Publications

(For a full list of Josh's publications, including those prior to his time at MSU, go to [Google Scholar](https://scholar.google.com/citations?user=WSWCJ-gAAAAJ), [ORCID](https://orcid.org/0000-0003-3139-6469))

## Highlights

<style>
.pub-highlights ol.bibliography,
.pub-fulllist ol.bibliography {
  list-style: none;
  padding-left: 0;
}
.pub-highlights ol.bibliography {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1.5rem;
}
@media (max-width: 768px) {
  .pub-highlights ol.bibliography {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="pub-highlights">
{% bibliography -q @*[highlight=1] -T highlight %}
</div>

<p> &nbsp; </p>
## Full List

<div class="pub-fulllist">
{% bibliography -T full %}
</div>
