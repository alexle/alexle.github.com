---
layout: app
title: "Regex Lab"
permalink: /regex/
---

<!-- markdownlint-disable MD033 -->
<style>
  .regex-app {
    --muted: #909498;
    --accent: #bf616a;
    --input-bg: #2d3033;
    --border: #444;
    --gold: #d4a843;
    --match-bg: rgba(212, 168, 67, 0.3);
  }

  .cheat-wrapper {
    margin: 0 0 2rem;
  }

  .field-group { margin-bottom: 1rem; }

  .field-group label {
    display: block;
    font-size: 0.85rem;
    color: var(--muted);
    margin-bottom: 0.3rem;
  }

  .field-group input,
  .field-group textarea {
    background: var(--input-bg);
    border: 1px solid var(--border);
    border-radius: 4px;
    color: inherit;
    font: inherit;
    font-size: 1rem;
    padding: 0.5rem 0.6rem;
    width: 100%;
    box-sizing: border-box;
  }

  .field-group input:focus,
  .field-group textarea:focus {
    outline: none;
    border-color: var(--accent);
  }

  .field-group textarea {
    resize: vertical;
    min-height: 100px;
    line-height: 1.4;
  }

  .pattern-row {
    display: flex;
    gap: 0.4rem;
    align-items: center;
  }

  .pattern-row input { flex: 1; font-family: monospace; }

  .flags {
    display: flex;
    gap: 0.2rem;
  }

  .flags button {
    width: 32px;
    height: 34px;
    border: 1px solid var(--border);
    border-radius: 4px;
    background: transparent;
    color: var(--muted);
    font: inherit;
    font-size: 0.85rem;
    cursor: pointer;
    transition: all 0.2s ease-out;
  }

  .flags button.active {
    background: var(--accent);
    border-color: var(--accent);
    color: inherit;
  }

  .error-msg {
    color: var(--accent);
    font-size: 0.85rem;
    margin-top: 0.5rem;
    min-height: 1.2em;
  }

  /* Results */
  .results-section {
    border-top: 1px solid var(--border);
    padding-top: 1rem;
    margin-top: 0.5rem;
    display: none;
  }

  .section-heading {
    font-size: 0.85rem;
    color: var(--muted);
    margin-bottom: 0.5rem;
  }

  .highlighted-text {
    font-family: monospace;
    font-size: 0.95rem;
    line-height: 1.4;
    white-space: pre-wrap;
    word-break: break-all;
    padding: 0.75rem;
    background: var(--input-bg);
    border-radius: 4px;
    margin-bottom: 1.5rem;
  }

  .highlighted-text mark {
    background: var(--match-bg);
    color: var(--gold);
    border-radius: 2px;
    padding: 0 1px;
  }

  .match-count {
    font-size: 0.85rem;
    color: var(--muted);
    margin-bottom: 1rem;
  }

  .match-count strong { color: var(--gold); }

  .match-list { margin-bottom: 1.5rem; }

  .match-item {
    font-family: monospace;
    font-size: 0.85rem;
    padding: 0.3rem 0;
    border-bottom: 1px solid var(--border);
    display: flex;
    gap: 0.75rem;
  }

  .match-item:last-child { border-bottom: none; }

  .match-idx {
    color: var(--muted);
    min-width: 2rem;
  }

  .match-val { color: var(--gold); }

  .match-groups {
    color: var(--muted);
    font-size: 0.8rem;
  }

  /* Cheat sheet */
  .cheat-toggle {
    font-size: 0.85rem;
    color: var(--muted);
    cursor: pointer;
    border: none;
    background: none;
    font: inherit;
    padding: 0;
    transition: color 0.2s;
  }

  .cheat-toggle:hover { color: inherit; }

  .cheat-toggle::before {
    content: '\25B6';
    display: inline-block;
    margin-right: 0.4rem;
    font-size: 0.7rem;
    transition: transform 0.2s;
  }

  .cheat-toggle.open::before { transform: rotate(90deg); }

  .cheat-sheet {
    display: none;
    margin-top: 0.75rem;
    font-size: 0.85rem;
  }

  .cheat-sheet table {
    width: 100%;
    border-collapse: collapse;
  }

  .cheat-sheet th {
    text-align: left;
    color: var(--muted);
    font-weight: 400;
    padding: 0.3rem 0.5rem;
    border-bottom: 1px solid var(--border);
  }

  .cheat-sheet td {
    padding: 0.3rem 0.5rem;
    border-bottom: 1px solid var(--border);
  }

  .cheat-sheet td:first-child {
    font-family: monospace;
    color: var(--gold);
    white-space: nowrap;
    width: 6rem;
  }

  .cheat-sheet td:last-child { color: var(--muted); }
</style>

<div class="regex-app">
<p style="color: var(--muted); font-size: 0.9rem; margin: 0 0 1.5rem;">Test regular expressions with live matching.</p>

<div class="regex-inputs">
<div class="field-group">
  <label>Pattern</label>
  <div class="pattern-row">
    <input type="text" id="pattern" placeholder="[a-z]+@[a-z]+\.[a-z]+" spellcheck="false" autocomplete="off">
    <div class="flags">
      <button id="flag-g" class="active" onclick="toggleFlag('g')">g</button>
      <button id="flag-i" onclick="toggleFlag('i')">i</button>
      <button id="flag-m" onclick="toggleFlag('m')">m</button>
    </div>
  </div>
</div>

<div class="field-group">
  <label>Test String</label>
  <textarea id="test-string" placeholder="Type or paste text to test against..."></textarea>
</div>

<div class="error-msg" id="error">&nbsp;</div>
</div>

<div class="results-section" id="results-section">
  <div class="section-heading">Matches</div>
  <div class="match-count" id="match-count"></div>
  <div class="highlighted-text" id="highlighted"></div>
  <div class="match-list" id="match-list"></div>
</div>

<div class="cheat-wrapper">
  <button class="cheat-toggle" id="cheat-toggle" onclick="toggleCheat()">Regex Reference</button>
  <div class="cheat-sheet" id="cheat-sheet">
    <table>
      <tr><th>Pattern</th><th>Description</th></tr>
      <tr><td>.</td><td>Any character except newline</td></tr>
      <tr><td>\d</td><td>Digit (0-9)</td></tr>
      <tr><td>\D</td><td>Not a digit</td></tr>
      <tr><td>\w</td><td>Word character (a-z, A-Z, 0-9, _)</td></tr>
      <tr><td>\W</td><td>Not a word character</td></tr>
      <tr><td>\s</td><td>Whitespace (space, tab, newline)</td></tr>
      <tr><td>\S</td><td>Not whitespace</td></tr>
      <tr><td>\b</td><td>Word boundary</td></tr>
      <tr><td>^</td><td>Start of string (or line with m flag)</td></tr>
      <tr><td>$</td><td>End of string (or line with m flag)</td></tr>
      <tr><td>*</td><td>0 or more</td></tr>
      <tr><td>+</td><td>1 or more</td></tr>
      <tr><td>?</td><td>0 or 1 (optional)</td></tr>
      <tr><td>{n}</td><td>Exactly n times</td></tr>
      <tr><td>{n,m}</td><td>Between n and m times</td></tr>
      <tr><td>[abc]</td><td>Character class (a, b, or c)</td></tr>
      <tr><td>[^abc]</td><td>Not a, b, or c</td></tr>
      <tr><td>(abc)</td><td>Capture group</td></tr>
      <tr><td>(?:abc)</td><td>Non-capturing group</td></tr>
      <tr><td>(?=abc)</td><td>Lookahead</td></tr>
      <tr><td>(?!abc)</td><td>Negative lookahead</td></tr>
      <tr><td>a|b</td><td>a or b</td></tr>
    </table>
  </div>
</div>
</div>

<script>
  var flags = { g: true, i: false, m: false };

  function toggleFlag(f) {
    flags[f] = !flags[f];
    document.getElementById('flag-' + f).classList.toggle('active', flags[f]);
    runMatch();
  }

  function toggleCheat() {
    var sheet = document.getElementById('cheat-sheet');
    var toggle = document.getElementById('cheat-toggle');
    var open = sheet.style.display === 'block';
    sheet.style.display = open ? 'none' : 'block';
    toggle.classList.toggle('open', !open);
  }

  function escapeHtml(str) {
    var div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }

  function getFlags() {
    var f = '';
    if (flags.g) f += 'g';
    if (flags.i) f += 'i';
    if (flags.m) f += 'm';
    return f;
  }

  function runMatch() {
    var patternStr = document.getElementById('pattern').value;
    var testStr = document.getElementById('test-string').value;
    var errorEl = document.getElementById('error');
    var resultsEl = document.getElementById('results-section');

    errorEl.innerHTML = '&nbsp;';

    if (!patternStr || !testStr) {
      resultsEl.style.display = 'none';
      return;
    }

    var regex;
    try {
      regex = new RegExp(patternStr, getFlags());
    } catch (e) {
      errorEl.textContent = e.message.replace(/^Invalid regular expression: /, '');
      resultsEl.style.display = 'none';
      return;
    }

    // Collect matches
    var matches = [];
    if (flags.g) {
      var m;
      var safety = 0;
      while ((m = regex.exec(testStr)) !== null && safety < 1000) {
        matches.push({ index: m.index, value: m[0], groups: m.slice(1) });
        if (m[0].length === 0) { regex.lastIndex++; }
        safety++;
      }
    } else {
      var m = regex.exec(testStr);
      if (m) {
        matches.push({ index: m.index, value: m[0], groups: m.slice(1) });
      }
    }

    // Highlight text
    var highlighted = '';
    var lastIdx = 0;
    matches.forEach(function(match) {
      highlighted += escapeHtml(testStr.slice(lastIdx, match.index));
      highlighted += '<mark>' + escapeHtml(match.value) + '</mark>';
      lastIdx = match.index + match.value.length;
    });
    highlighted += escapeHtml(testStr.slice(lastIdx));

    document.getElementById('highlighted').innerHTML = highlighted;
    document.getElementById('match-count').innerHTML = '<strong>' + matches.length + '</strong> match' + (matches.length !== 1 ? 'es' : '');

    // Match list
    var list = document.getElementById('match-list');
    list.innerHTML = '';
    matches.forEach(function(match, i) {
      var item = document.createElement('div');
      item.className = 'match-item';
      var groupsHtml = '';
      if (match.groups.length > 0) {
        groupsHtml = '<span class="match-groups">' +
          match.groups.map(function(g, j) { return 'Group ' + (j + 1) + ': ' + escapeHtml(g || ''); }).join(', ') +
          '</span>';
      }
      item.innerHTML = '<span class="match-idx">' + i + '</span>' +
        '<span class="match-val">"' + escapeHtml(match.value) + '"</span>' +
        groupsHtml;
      list.appendChild(item);
    });

    resultsEl.style.display = 'block';
  }

  // Live matching on input
  document.getElementById('pattern').addEventListener('input', runMatch);
  document.getElementById('test-string').addEventListener('input', runMatch);
</script>
