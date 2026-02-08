---
layout: default
title: "Pace Calculator"
permalink: /pace-calculator/
---

<!-- markdownlint-disable MD033 -->
<style>
  /* Theme tokens — single source of truth for app-specific values not inherited */
  .pace-calc {
    --muted: #909498;
    --accent: #bf616a;
    --input-bg: #2d3033;
    --border: #444;
  }

  .calc-title {
    font-size: 1.6rem;
    font-weight: 400;
    margin: 1.5rem 0 1rem;
  }

  /* Unit toggle */
  .unit-toggle {
    display: flex;
    margin-bottom: 1.5rem;
  }

  .unit-toggle button {
    flex: 1;
    padding: 0.5rem 1rem;
    border: 1px solid var(--muted);
    background: transparent;
    color: var(--muted);
    font: inherit;
    font-size: 0.9rem;
    cursor: pointer;
    transition: all 0.2s ease-out;
  }

  .unit-toggle button:first-child { border-radius: 4px 0 0 4px; }
  .unit-toggle button:last-child { border-radius: 0 4px 4px 0; }

  .unit-toggle button.active {
    background: var(--accent);
    border-color: var(--accent);
    color: inherit;
  }

  /* Field groups */
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
  }

  .field-group input:focus {
    outline: none;
    border-color: var(--accent);
  }

  .field-group .time-inputs {
    display: flex;
    align-items: center;
    gap: 0.3rem;
    width: 100%;
  }

  .field-group .time-inputs input { width: 76px; text-align: center; }
  .field-group .time-inputs .sep { color: var(--muted); font-size: 1.2rem; }

  .field-group .unit-label {
    color: var(--muted);
    font-size: 0.85rem;
    white-space: nowrap;
    min-width: 3rem;
  }

  /* Presets */
  .presets {
    display: flex;
    gap: 0.5rem;
    margin: 1.2rem 0;
    flex-wrap: wrap;
  }

  .presets button {
    padding: 0.4rem 0.9rem;
    border: 1px solid var(--muted);
    border-radius: 4px;
    background: transparent;
    color: var(--muted);
    font: inherit;
    font-size: 0.85rem;
    cursor: pointer;
    transition: all 0.2s ease-out;
  }

  .presets button:hover,
  .presets button.selected {
    border-color: var(--accent);
    color: var(--accent);
  }

  /* Action buttons */
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

  /* Results */
  .result {
    border-top: 1px solid var(--border);
    padding-top: 1rem;
    margin-top: 0.5rem;
    display: none;
  }

  .result .result-row {
    display: flex;
    justify-content: space-between;
    padding: 0.4rem 0;
  }

  .result .result-label { color: var(--muted); }
  .result .result-value { font-weight: 500; }
  .result .result-value.computed { color: var(--accent); }

  .error-msg {
    color: var(--accent);
    font-size: 0.85rem;
    margin-top: 0.5rem;
    display: none;
  }
</style>

<div class="pace-calc">
<h1 class="calc-title">Pace Calculator</h1>
<p style="color: var(--muted); font-size: 0.9rem; margin: 0 0 1.5rem;">Enter any 2 fields and the 3rd will be calculated.</p>

<div class="unit-toggle">
  <button id="btn-mi" class="active" onclick="setUnit('mi')">Miles</button>
  <button id="btn-km" onclick="setUnit('km')">Kilometers</button>
</div>

<div class="field-group">
  <label>Pace</label>
  <div class="inputs">
    <div class="time-inputs">
      <input type="number" id="pace-min" min="0" max="59" placeholder="min">
      <span class="sep">:</span>
      <input type="number" id="pace-sec" min="0" max="59" placeholder="sec">
    </div>
    <span class="unit-label" id="pace-unit">/ mi</span>
  </div>
</div>

<div class="field-group">
  <label>Time</label>
  <div class="inputs">
    <div class="time-inputs">
      <input type="number" id="time-hr" min="0" placeholder="hr">
      <span class="sep">:</span>
      <input type="number" id="time-min" min="0" max="59" placeholder="min">
      <span class="sep">:</span>
      <input type="number" id="time-sec" min="0" max="59" placeholder="sec">
    </div>
  </div>
</div>

<div class="field-group">
  <label>Distance</label>
  <div class="inputs">
    <input type="number" id="distance" min="0" step="any" placeholder="0.00">
    <span class="unit-label" id="dist-unit">mi</span>
  </div>
</div>

<div class="presets">
  <button onclick="setPreset(5, '5K')">5K</button>
  <button onclick="setPreset(10, '10K')">10K</button>
  <button onclick="setPreset(21.0975, 'Half')">Half</button>
  <button onclick="setPreset(42.195, 'Marathon')">Marathon</button>
</div>

<div class="actions">
  <button class="btn-calc" onclick="calculate()">Calculate</button>
  <button class="btn-clear" onclick="clearAll()">Clear</button>
</div>

<div class="error-msg" id="error"></div>

<div class="result" id="result">
  <div class="result-row">
    <span class="result-label">Pace</span>
    <span class="result-value" id="res-pace"></span>
  </div>
  <div class="result-row">
    <span class="result-label">Time</span>
    <span class="result-value" id="res-time"></span>
  </div>
  <div class="result-row">
    <span class="result-label">Distance</span>
    <span class="result-value" id="res-dist"></span>
  </div>
</div>
</div>

<script>
  let unit = 'mi';
  const KM_PER_MI = 1.609344;

  const PRESETS_KM = { '5K': 5, '10K': 10, 'Half': 21.0975, 'Marathon': 42.195 };
  const PRESETS_MI = { '5K': 3.10686, '10K': 6.21371, 'Half': 13.1094, 'Marathon': 26.2188 };

  function setUnit(u) {
    const prevUnit = unit;
    unit = u;
    document.getElementById('btn-mi').classList.toggle('active', u === 'mi');
    document.getElementById('btn-km').classList.toggle('active', u === 'km');
    document.getElementById('pace-unit').textContent = u === 'mi' ? '/ mi' : '/ km';
    document.getElementById('dist-unit').textContent = u;

    // Convert existing distance value
    const distInput = document.getElementById('distance');
    if (distInput.value) {
      const val = parseFloat(distInput.value);
      if (!isNaN(val) && prevUnit !== u) {
        distInput.value = u === 'km' ? (val * KM_PER_MI).toFixed(2) : (val / KM_PER_MI).toFixed(2);
      }
    }

    // Update selected preset highlight
    updatePresetHighlight();
  }

  function setPreset(km, name) {
    const dist = unit === 'km' ? km : km / KM_PER_MI;
    document.getElementById('distance').value = dist.toFixed(2);
    // Highlight selected preset
    document.querySelectorAll('.presets button').forEach(b => {
      b.classList.toggle('selected', b.textContent === name);
    });
  }

  function updatePresetHighlight() {
    const distVal = parseFloat(document.getElementById('distance').value);
    if (isNaN(distVal)) return;
    const presets = unit === 'km' ? PRESETS_KM : PRESETS_MI;
    document.querySelectorAll('.presets button').forEach(b => {
      const presetDist = presets[b.textContent];
      b.classList.toggle('selected', presetDist && Math.abs(distVal - presetDist) < 0.01);
    });
  }

  function getSeconds(id) {
    const val = document.getElementById(id).value;
    return val === '' ? NaN : parseInt(val, 10);
  }

  function hasPace() {
    return document.getElementById('pace-min').value !== '' || document.getElementById('pace-sec').value !== '';
  }

  function hasTime() {
    return document.getElementById('time-hr').value !== '' || document.getElementById('time-min').value !== '' || document.getElementById('time-sec').value !== '';
  }

  function hasDist() {
    return document.getElementById('distance').value !== '';
  }

  function getPaceSec() {
    const m = getSeconds('pace-min');
    const s = getSeconds('pace-sec');
    return (isNaN(m) ? 0 : m) * 60 + (isNaN(s) ? 0 : s);
  }

  function getTimeSec() {
    const h = getSeconds('time-hr');
    const m = getSeconds('time-min');
    const s = getSeconds('time-sec');
    return (isNaN(h) ? 0 : h) * 3600 + (isNaN(m) ? 0 : m) * 60 + (isNaN(s) ? 0 : s);
  }

  function getDist() {
    return parseFloat(document.getElementById('distance').value);
  }

  function fmtPace(totalSec) {
    const m = Math.floor(totalSec / 60);
    const s = Math.round(totalSec % 60);
    return m + ':' + String(s).padStart(2, '0');
  }

  function fmtTime(totalSec) {
    const h = Math.floor(totalSec / 3600);
    const m = Math.floor((totalSec % 3600) / 60);
    const s = Math.round(totalSec % 60);
    if (h > 0) return h + ':' + String(m).padStart(2, '0') + ':' + String(s).padStart(2, '0');
    return m + ':' + String(s).padStart(2, '0');
  }

  function showError(msg) {
    const el = document.getElementById('error');
    el.textContent = msg;
    el.style.display = 'block';
    document.getElementById('result').style.display = 'none';
  }

  function calculate() {
    document.getElementById('error').style.display = 'none';

    const hp = hasPace(), ht = hasTime(), hd = hasDist();
    const filled = [hp, ht, hd].filter(Boolean).length;

    if (filled < 2) {
      showError('Enter any 2 fields to calculate the 3rd.');
      return;
    }
    if (filled === 3) {
      showError('Leave one field blank to calculate it.');
      return;
    }

    let paceSec, timeSec, dist, computed;

    if (!hp) {
      // Calculate pace
      timeSec = getTimeSec();
      dist = getDist();
      if (dist <= 0) { showError('Distance must be greater than 0.'); return; }
      paceSec = timeSec / dist;
      computed = 'pace';
    } else if (!ht) {
      // Calculate time
      paceSec = getPaceSec();
      dist = getDist();
      if (dist <= 0) { showError('Distance must be greater than 0.'); return; }
      timeSec = paceSec * dist;
      computed = 'time';
    } else {
      // Calculate distance
      paceSec = getPaceSec();
      timeSec = getTimeSec();
      if (paceSec <= 0) { showError('Pace must be greater than 0.'); return; }
      dist = timeSec / paceSec;
      computed = 'distance';
    }

    // Display results
    const resPace = document.getElementById('res-pace');
    const resTime = document.getElementById('res-time');
    const resDist = document.getElementById('res-dist');

    resPace.textContent = fmtPace(paceSec) + ' ' + (unit === 'mi' ? '/mi' : '/km');
    resTime.textContent = fmtTime(timeSec);
    resDist.textContent = dist.toFixed(2) + ' ' + unit;

    // Highlight computed value
    resPace.classList.toggle('computed', computed === 'pace');
    resTime.classList.toggle('computed', computed === 'time');
    resDist.classList.toggle('computed', computed === 'distance');

    document.getElementById('result').style.display = 'block';
  }

  function clearAll() {
    document.getElementById('pace-min').value = '';
    document.getElementById('pace-sec').value = '';
    document.getElementById('time-hr').value = '';
    document.getElementById('time-min').value = '';
    document.getElementById('time-sec').value = '';
    document.getElementById('distance').value = '';
    document.getElementById('result').style.display = 'none';
    document.getElementById('error').style.display = 'none';
    document.querySelectorAll('.presets button').forEach(b => b.classList.remove('selected'));
  }

  // Allow Enter key to trigger calculation
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') calculate();
  });
</script>
