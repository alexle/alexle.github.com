---
layout: default
title: "GitHub Stats"
permalink: /github-stats/
---

<!-- markdownlint-disable MD033 -->
<style>
  .gh-stats {
    --muted: #909498;
    --accent: #bf616a;
    --input-bg: #2d3033;
    --border: #444;
    --gold: #d4a843;
  }

  .gh-inputs { max-width: 480px; }

  .calc-title {
    font-size: 1.6rem;
    font-weight: 400;
    margin: 1.5rem 0 1rem;
  }

  .field-group { margin-bottom: 1rem; }

  .field-group label {
    display: block;
    font-size: 0.85rem;
    color: var(--muted);
    margin-bottom: 0.3rem;
  }

  .field-group .inputs {
    display: flex;
    align-items: center;
    gap: 0.3rem;
  }

  .field-group input {
    background: var(--input-bg);
    border: 1px solid var(--border);
    border-radius: 4px;
    color: inherit;
    font: inherit;
    font-size: 1rem;
    padding: 0.5rem 0.6rem;
    width: 100%;
    -moz-appearance: textfield;
  }

  .field-group input:focus {
    outline: none;
    border-color: var(--accent);
  }

  .actions {
    display: flex;
    gap: 0.5rem;
    margin: 1.5rem 0;
  }

  .actions button {
    padding: 0.55rem 1.5rem;
    border: none;
    border-radius: 4px;
    font: inherit;
    font-size: 0.95rem;
    cursor: pointer;
    transition: all 0.2s ease-out;
  }

  .btn-calc { background: var(--accent); color: inherit; }
  .btn-calc:hover { opacity: 0.85; }

  .btn-clear {
    background: transparent;
    border: 1px solid var(--muted) !important;
    color: var(--muted);
  }

  .btn-clear:hover {
    border-color: inherit !important;
    color: inherit;
  }

  .error-msg {
    color: var(--accent);
    font-size: 0.85rem;
    margin-top: 0.5rem;
    display: none;
  }

  .loading {
    color: var(--muted);
    font-size: 0.9rem;
    display: none;
  }

  /* Results */
  .results-section {
    border-top: 1px solid var(--border);
    padding-top: 1.5rem;
    margin-top: 0.5rem;
    display: none;
  }

  /* Profile card */
  .profile-card {
    display: flex;
    gap: 1.2rem;
    align-items: flex-start;
    margin-bottom: 1rem;
    text-decoration: none;
    color: inherit;
    border-radius: 8px;
    padding: 1rem;
    margin-left: -1rem;
    margin-right: -1rem;
    transition: background 0.2s ease-out;
  }

  .profile-card:hover { background: var(--input-bg); }

  .profile-card img {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    border: 2px solid var(--border);
  }

  .profile-info { flex: 1; }

  .profile-name {
    font-size: 1.2rem;
    font-weight: 500;
    margin: 0 0 0.1rem;
  }

  .profile-login {
    color: var(--muted);
    font-size: 0.9rem;
    margin: 0 0 0.4rem;
    text-decoration: none;
    display: block;
  }

  .profile-login:hover { text-decoration: underline; }

  .profile-bio {
    font-size: 0.9rem;
    color: var(--muted);
    margin: 0 0 0.5rem;
    line-height: 1.4;
  }

  .profile-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    font-size: 0.8rem;
    color: var(--muted);
  }

  .profile-meta span strong {
    color: inherit;
    font-weight: 600;
    color: #E1E3E6;
  }

  /* Commit activity */
  .commit-section {
    margin-bottom: 2rem;
    display: none;
  }

  .commit-stats {
    display: flex;
    gap: 2rem;
  }

  .commit-stat {
    display: flex;
    flex-direction: column;
  }

  .commit-number {
    font-size: 1.4rem;
    font-weight: 600;
    color: #E1E3E6;
  }

  .commit-label {
    font-size: 0.8rem;
    color: var(--muted);
  }

  .commit-note {
    font-size: 0.75rem;
    color: var(--muted);
    margin-top: 0.5rem;
    font-style: italic;
  }

  /* Language chart */
  .lang-section {
    margin-bottom: 2rem;
  }

  .section-heading {
    font-size: 0.85rem;
    color: var(--muted);
    margin-bottom: 0.75rem;
  }

  .lang-bar {
    display: flex;
    height: 10px;
    border-radius: 5px;
    overflow: hidden;
    margin-bottom: 0.75rem;
  }

  .lang-legend {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem 1.2rem;
    font-size: 0.8rem;
    color: var(--muted);
  }

  .lang-legend-item {
    display: flex;
    align-items: center;
    gap: 0.35rem;
  }

  .lang-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    display: inline-block;
  }

  /* Repo list */
  .repo-section { margin-bottom: 1rem; }

  .repo-card {
    padding: 0.75rem 0;
    border-bottom: 1px solid var(--border);
  }

  .repo-card:last-child { border-bottom: none; }

  .repo-name {
    font-weight: 500;
    color: var(--accent);
    text-decoration: none;
    font-size: 0.95rem;
  }

  .repo-name:hover { text-decoration: underline; }

  .repo-desc {
    font-size: 0.85rem;
    color: var(--muted);
    margin: 0.2rem 0 0.4rem;
    line-height: 1.4;
  }

  .repo-meta {
    display: flex;
    gap: 1rem;
    font-size: 0.8rem;
    color: var(--muted);
  }

  .repo-meta-item {
    display: flex;
    align-items: center;
    gap: 0.3rem;
  }
</style>

<div class="gh-stats">
<h1 class="calc-title">GitHub Stats</h1>
<p style="color: var(--muted); font-size: 0.9rem; margin: 0 0 1.5rem;">Look up any GitHub user's public profile and repos.</p>

<div class="gh-inputs">
<div class="field-group">
  <label>GitHub Username</label>
  <div class="inputs">
    <input type="text" id="username" placeholder="username" autocomplete="off" spellcheck="false">
  </div>
</div>

<div class="actions">
  <button class="btn-calc" onclick="lookup()">Look Up</button>
  <button class="btn-clear" onclick="clearResults()">Clear</button>
</div>

<div class="error-msg" id="error"></div>
<div class="loading" id="loading">Fetching from GitHub...</div>
</div>

<div class="results-section" id="results-section">
  <a class="profile-card" id="profile-link" target="_blank" rel="noopener">
    <img id="avatar" src="" alt="">
    <div class="profile-info">
      <div class="profile-name" id="name"></div>
      <div class="profile-login" id="login"></div>
      <div class="profile-bio" id="bio"></div>
      <div class="profile-meta" id="meta"></div>
    </div>
  </a>

  <div class="commit-section" id="commit-section">
    <div class="section-heading">Commit Activity</div>
    <div class="loading" id="commit-loading">Loading commit activity...</div>
    <div class="commit-stats" id="commit-stats">
      <div class="commit-stat">
        <span class="commit-number" id="commits-month">—</span>
        <span class="commit-label">past 30 days</span>
      </div>
      <div class="commit-stat">
        <span class="commit-number" id="commits-year">—</span>
        <span class="commit-label">past year</span>
      </div>
    </div>
    <div class="commit-note" id="commit-note"></div>
  </div>

  <div class="lang-section" id="lang-section">
    <div class="section-heading">Languages</div>
    <div class="lang-bar" id="lang-bar"></div>
    <div class="lang-legend" id="lang-legend"></div>
  </div>

  <div class="repo-section">
    <div class="section-heading">Top Repositories</div>
    <div id="repo-list"></div>
  </div>
</div>
</div>

<script>
  const API = 'https://api.github.com';
  var commitGeneration = 0;
  const STATS_MAX_RETRIES = 5;
  const RETRY_DELAY_MS = 2000;
  const RECENT_DAYS = 90;
  const MAX_STATS_REPOS = 5;
  const MAX_DISPLAY_REPOS = 8;

  // GitHub-style language colors
  const LANG_COLORS = {
    JavaScript: '#f1e05a', TypeScript: '#3178c6', Python: '#3572A5',
    Go: '#00ADD8', Rust: '#dea584', Java: '#b07219',
    'C++': '#f34b7d', C: '#555555', 'C#': '#178600',
    Ruby: '#701516', PHP: '#4F5D95', Swift: '#F05138',
    Kotlin: '#A97BFF', Dart: '#00B4AB', Shell: '#89e051',
    HTML: '#e34c26', CSS: '#563d7c', SCSS: '#c6538c',
    Lua: '#000080', Vim: '#199f4b', Makefile: '#427819',
    Dockerfile: '#384d54', HCL: '#844FBA', Nix: '#7e7eff'
  };

  function showError(msg) {
    document.getElementById('error').textContent = msg;
    document.getElementById('error').style.display = 'block';
    document.getElementById('loading').style.display = 'none';
    document.getElementById('results-section').style.display = 'none';
  }

  async function lookup() {
    const username = document.getElementById('username').value.trim();
    if (!username) { showError('Please enter a username.'); return; }

    document.getElementById('error').style.display = 'none';
    document.getElementById('results-section').style.display = 'none';
    document.getElementById('commit-section').style.display = 'none';
    document.getElementById('commits-month').textContent = '—';
    document.getElementById('commits-year').textContent = '—';
    document.getElementById('loading').style.display = 'block';

    try {
      var enc = encodeURIComponent(username);
      const [userRes, reposRes] = await Promise.all([
        fetch(API + '/users/' + enc),
        fetch(API + '/users/' + enc + '/repos?per_page=100&sort=stars&direction=desc')
      ]);

      if (userRes.status === 404) { showError('User not found.'); return; }
      if (userRes.status === 403) { showError('API rate limit reached. Try again later.'); return; }
      if (!userRes.ok) { showError('GitHub API error (' + userRes.status + ').'); return; }

      const user = await userRes.json();
      const repos = await reposRes.json();

      document.getElementById('loading').style.display = 'none';
      renderProfile(user);
      renderLanguages(repos);
      renderRepos(repos);
      document.getElementById('results-section').style.display = 'block';
      fetchCommitActivity(repos, user.login);
    } catch (e) {
      showError('Network error. Check your connection.');
    }
  }

  function renderProfile(user) {
    document.getElementById('avatar').src = user.avatar_url;
    document.getElementById('avatar').alt = user.login;
    document.getElementById('name').textContent = user.name || user.login;
    document.getElementById('login').textContent = '@' + user.login;
    document.getElementById('profile-link').href = user.html_url;
    document.getElementById('bio').textContent = user.bio || '';
    document.getElementById('bio').style.display = user.bio ? 'block' : 'none';

    const joined = new Date(user.created_at);
    const memberYears = new Date().getFullYear() - joined.getFullYear();
    const parts = [];
    if (user.location) parts.push(user.location);
    parts.push('<strong>' + user.public_repos + '</strong> repos');
    parts.push('<strong>' + user.followers + '</strong> followers');
    parts.push('Joined ' + joined.getFullYear() + ' (' + memberYears + ' yr' + (memberYears !== 1 ? 's' : '') + ')');
    document.getElementById('meta').innerHTML = parts.map(function(p) { return '<span>' + p + '</span>'; }).join('');
  }

  function renderLanguages(repos) {
    // Count repos per language (exclude forks and null language)
    const counts = {};
    let total = 0;
    repos.forEach(function(r) {
      if (r.fork || !r.language) return;
      counts[r.language] = (counts[r.language] || 0) + 1;
      total++;
    });

    if (total === 0) {
      document.getElementById('lang-section').style.display = 'none';
      return;
    }
    document.getElementById('lang-section').style.display = 'block';

    // Sort by count descending
    const sorted = Object.entries(counts).sort(function(a, b) { return b[1] - a[1]; });

    // Render bar
    const bar = document.getElementById('lang-bar');
    bar.innerHTML = '';
    sorted.forEach(function(entry) {
      var lang = entry[0], count = entry[1];
      var pct = (count / total) * 100;
      var color = LANG_COLORS[lang] || '#8b8b8b';
      var seg = document.createElement('div');
      seg.style.width = pct + '%';
      seg.style.background = color;
      seg.title = lang + ' (' + Math.round(pct) + '%)';
      bar.appendChild(seg);
    });

    // Render legend
    var legend = document.getElementById('lang-legend');
    legend.innerHTML = '';
    sorted.forEach(function(entry) {
      var lang = entry[0], count = entry[1];
      var pct = ((count / total) * 100).toFixed(1);
      var color = LANG_COLORS[lang] || '#8b8b8b';
      var item = document.createElement('div');
      item.className = 'lang-legend-item';
      item.innerHTML = '<span class="lang-dot" style="background:' + color + '"></span>' + lang + ' ' + pct + '%';
      legend.appendChild(item);
    });
  }

  function renderRepos(repos) {
    // Filter out forks, sort by stars then by updated
    var own = repos
      .filter(function(r) { return !r.fork; })
      .sort(function(a, b) {
        if (b.stargazers_count !== a.stargazers_count) return b.stargazers_count - a.stargazers_count;
        return new Date(b.updated_at) - new Date(a.updated_at);
      })
      .slice(0, MAX_DISPLAY_REPOS);

    var list = document.getElementById('repo-list');
    list.innerHTML = '';

    own.forEach(function(r) {
      var card = document.createElement('div');
      card.className = 'repo-card';

      var nameLink = '<a class="repo-name" href="' + r.html_url + '" target="_blank" rel="noopener">' + r.name + '</a>';
      var desc = r.description ? '<div class="repo-desc">' + escapeHtml(r.description) + '</div>' : '';

      var meta = [];
      if (r.language) {
        var color = LANG_COLORS[r.language] || '#8b8b8b';
        meta.push('<span class="repo-meta-item"><span class="lang-dot" style="background:' + color + '"></span>' + r.language + '</span>');
      }
      if (r.stargazers_count > 0) {
        meta.push('<span class="repo-meta-item">\u2605 ' + r.stargazers_count + '</span>');
      }
      if (r.forks_count > 0) {
        meta.push('<span class="repo-meta-item">\u2442 ' + r.forks_count + '</span>');
      }
      var updated = new Date(r.updated_at);
      var monthNames = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
      meta.push('<span class="repo-meta-item">Updated ' + monthNames[updated.getMonth()] + ' ' + updated.getFullYear() + '</span>');

      card.innerHTML = nameLink + desc + '<div class="repo-meta">' + meta.join('') + '</div>';
      list.appendChild(card);
    });
  }

  // Fetch with retry for GitHub's 202 "computing" response
  async function fetchWithRetry(url, retries) {
    for (var i = 0; i <= retries; i++) {
      var res = await fetch(url, { cache: 'no-store' });
      if (res.status !== 202) return res;
      await new Promise(function(r) { setTimeout(r, RETRY_DELAY_MS); });
    }
    return res;
  }

  async function fetchCommitActivity(repos, username) {
    var gen = ++commitGeneration;
    var now = Date.now();
    var ninetyDaysAgo = now - (RECENT_DAYS * 24 * 60 * 60 * 1000);
    var section = document.getElementById('commit-section');

    // Filter to non-fork repos updated in last 90 days, cap at 5
    var recent = repos
      .filter(function(r) { return !r.fork && new Date(r.pushed_at).getTime() > ninetyDaysAgo; })
      .sort(function(a, b) { return new Date(b.pushed_at) - new Date(a.pushed_at); })
      .slice(0, MAX_STATS_REPOS);

    if (recent.length === 0) {
      section.style.display = 'none';
      return;
    }

    // Show section with zeros, update progressively as repos resolve
    section.style.display = 'block';
    document.getElementById('commit-loading').style.display = 'block';
    document.getElementById('commit-stats').style.display = 'flex';
    document.getElementById('commit-note').style.display = 'block';
    document.getElementById('commits-month').textContent = '0';
    document.getElementById('commits-year').textContent = '0';
    document.getElementById('commit-note').textContent =
      'Loading 0 of ' + recent.length + ' repos...';

    var yearTotal = 0;
    var monthTotal = 0;
    var resolved = 0;
    var login = username.toLowerCase();

    function updateDisplay() {
      if (gen !== commitGeneration) return;
      document.getElementById('commits-month').textContent = monthTotal.toLocaleString();
      document.getElementById('commits-year').textContent = yearTotal.toLocaleString();
      var pending = recent.length - resolved;
      if (pending > 0) {
        document.getElementById('commit-note').textContent =
          'Loading ' + resolved + ' of ' + recent.length + ' repos...';
      } else {
        document.getElementById('commit-loading').style.display = 'none';
        document.getElementById('commit-note').textContent =
          'Based on ' + recent.length + ' recently active repo' + (recent.length !== 1 ? 's' : '');
      }
    }

    async function processRepo(repo) {
      try {
        var res = await fetchWithRetry(API + '/repos/' + repo.full_name + '/stats/contributors', STATS_MAX_RETRIES);
        if (!res.ok || res.status === 202) { resolved++; updateDisplay(); return; }
        var contributors = await res.json();
        if (!Array.isArray(contributors)) { resolved++; updateDisplay(); return; }

        var match = contributors.find(function(c) {
          return c.author && c.author.login.toLowerCase() === login;
        });
        if (match) {
          match.weeks.forEach(function(w) { yearTotal += w.c; });
          match.weeks.slice(-4).forEach(function(w) { monthTotal += w.c; });
        }
        resolved++;
        updateDisplay();
      } catch (e) {
        resolved++;
        updateDisplay();
      }
    }

    // Fire all in parallel, update display as each resolves
    recent.forEach(function(r) { processRepo(r); });
  }

  function escapeHtml(str) {
    var div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }

  function clearResults() {
    document.getElementById('results-section').style.display = 'none';
    document.getElementById('error').style.display = 'none';
    document.getElementById('loading').style.display = 'none';
    document.getElementById('commit-section').style.display = 'none';
  }

  document.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') lookup();
  });
</script>
