---
layout: post
title: "Search"
author: "Alex Le"
permalink: /search/
---

<div class="search-wrapper">
  <input type="text" id="search-input" placeholder="Search ↵" autofocus>
  <ul id="results-container"></ul>
</div>

<script src="https://unpkg.com/simple-jekyll-search@latest/dest/simple-jekyll-search.min.js"></script>
<script>
  SimpleJekyllSearch({
    searchInput: document.getElementById('search-input'),
    resultsContainer: document.getElementById('results-container'),
    json: '/search.json',
    searchResultTemplate: '<li><a href="{url}">{title}</a></li>',
    noResultsText: 'No results found'
  })
</script>
