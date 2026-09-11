---
layout: app
title: "FIRE Calculator"
permalink: /fire-calculator/
---

<!-- markdownlint-disable MD033 -->
<style>
  .fire-calc {
    --muted: #909498;
    --accent: #bf616a;
    --highlight: #88c0d0;
    --input-bg: #2d3033;
    --border: #444;
  }

  .fire-inputs { max-width: 480px; }

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

  .field-group input::-webkit-outer-spin-button,
  .field-group input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }

  .field-group input:focus {
    outline: none;
    border-color: var(--accent);
  }

  .field-group input.input-error {
    border-color: var(--accent);
    box-shadow: 0 0 0 1px var(--accent);
  }

  .field-group .unit-label {
    color: var(--muted);
    font-size: 0.85rem;
    white-space: nowrap;
    min-width: 1.5rem;
  }

  .optional-fields {
    margin: -0.35rem 0 1rem;
  }

  .optional-fields summary {
    color: var(--muted);
    cursor: pointer;
    font-size: 0.8rem;
    width: fit-content;
  }

  .optional-fields[open] summary { margin-bottom: 0.75rem; }

  .supplemental-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.75rem;
  }

  .supplemental-row .field-group { margin-bottom: 0; }

  @media (max-width: 420px) {
    .supplemental-row { grid-template-columns: 1fr; }
  }

  .section-label {
    font-size: 0.85rem;
    color: var(--muted);
    margin: 1.5rem 0 0.75rem;
    padding-top: 0.75rem;
    border-top: 1px solid var(--border);
  }

  .alloc-row {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 0.5rem;
  }

  .alloc-row .field-group { flex: 1; margin-bottom: 0; }

  .alloc-error {
    color: var(--accent);
    font-size: 0.8rem;
    margin-top: 0.25rem;
    display: none;
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

  .warning-msg {
    color: #e0a458;
    font-size: 0.85rem;
    margin-top: 0.5rem;
    display: none;
  }

  .results-section {
    border-top: 1px solid var(--border);
    padding-top: 1rem;
    margin-top: 0.5rem;
    display: none;
  }

  .fire-headline {
    font-size: 1.1rem;
    font-weight: 400;
    color: var(--muted);
    margin-bottom: 1rem;
    line-height: 1.4;
  }

  .fire-headline strong {
    font-size: 1.4rem;
    color: var(--accent);
  }

  .chart-container {
    position: relative;
    width: 100%;
    margin-bottom: 1rem;
  }

  .chart-container canvas {
    width: 100%;
    height: 280px;
    display: block;
  }

  .chart-legend {
    display: flex;
    gap: 1.2rem;
    font-size: 0.8rem;
    color: var(--muted);
    margin-bottom: 1rem;
  }

  .chart-legend span::before {
    content: '';
    display: inline-block;
    width: 10px;
    height: 10px;
    border-radius: 2px;
    margin-right: 0.4rem;
    vertical-align: middle;
  }

  .legend-working::before { background: var(--accent); opacity: 0.6; }
  .legend-retired::before { background: var(--accent); opacity: 0.27; }
  .legend-fire::before {
    background: none;
    border-top: 2px dashed var(--muted);
    height: 0;
    margin-bottom: 5px;
  }

  .stats-row {
    display: flex;
    justify-content: space-between;
    padding: 0.3rem 0;
    font-size: 0.9rem;
  }

  .stats-row .stat-label { color: var(--muted); }
  .stats-row .stat-value { font-weight: 500; }
  .stats-row .stat-value.milestone-value { color: var(--highlight); }

  .stats-header {
    font-size: 1.1rem;
    color: inherit;
    margin-top: 1rem;
    margin-bottom: 0.25rem;
  }

  .stats-header:first-child { margin-top: 0; }

  .stat-desc {
    font-size: 0.75rem;
    color: var(--muted);
    text-align: right;
  }

  .coast-reached {
    color: #a3d9a5;
    font-size: 0.8rem;
    font-weight: 500;
  }

  .coast-delta {
    color: var(--muted);
    font-size: 0.8rem;
  }

  .stress-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 0.5rem;
    font-size: 0.85rem;
    table-layout: fixed;
  }

  .stress-table th {
    color: var(--muted);
    font-weight: 400;
    text-align: left;
    padding: 0.35rem 0;
    border-bottom: 1px solid var(--border);
  }

  .stress-table th:first-child,
  .stress-table td:first-child {
    width: 30%;
  }

  .stress-table th:not(:first-child),
  .stress-table td:not(:first-child) {
    text-align: right;
  }

  .stress-table td {
    padding: 0.35rem 0;
  }

  .stress-table tr.stress-active td {
    font-weight: 500;
  }

  .gap-negative { color: var(--accent); }
  .gap-positive { color: #a3d9a5; }
</style>

<div class="fire-calc">
<p style="color: var(--muted); font-size: 0.9rem; margin: 0 0 1.5rem;">Project when you can achieve financial independence.</p>
<p style="color: var(--muted); font-size: 0.8rem; margin: -1rem 0 1.5rem;">Financial independence means your investments can cover your living expenses. All amounts are in today's dollars and assume constant real returns; actual results will vary. <a href="https://www.financialplanningassociation.org/sites/default/files/2020-05/7%20Determining%20Withdrawal%20Rates%20Using%20Historical%20Data.pdf">Withdrawal-rate research</a>.</p>

<div class="fire-inputs">
<div class="field-group">
  <label>Current Age</label>
  <div class="inputs">
    <input type="number" id="age" min="18" max="80" placeholder="30" required>
    <span class="unit-label">yrs</span>
  </div>
</div>

<div class="field-group">
  <label>Net Investable Assets</label>
  <div class="inputs">
    <input type="number" id="networth" min="0" step="1" placeholder="100000" required>
    <span class="unit-label">$</span>
  </div>
</div>

<div class="field-group">
  <label>Annual Income (after tax)</label>
  <div class="inputs">
    <input type="number" id="income" min="0" step="1" placeholder="50000" required>
    <span class="unit-label">$</span>
  </div>
</div>

<div class="field-group">
  <label>Annual Expenses</label>
  <div class="inputs">
    <input type="number" id="expenses" min="0" step="1" placeholder="40000" required>
    <span class="unit-label">$</span>
  </div>
</div>

<div class="field-group">
  <label>Withdrawal Rate</label>
  <div class="inputs">
    <input type="number" id="withdrawal-rate" min="1" max="10" step="0.5" value="4" required>
    <span class="unit-label">%</span>
  </div>
</div>

<details class="optional-fields">
  <summary>Supplemental income (optional)</summary>
  <div class="supplemental-row">
    <div class="field-group">
      <label>Supplemental Per Month</label>
      <div class="inputs">
        <input type="number" id="supplemental-monthly" min="0" step="1" placeholder="0">
        <span class="unit-label">$</span>
      </div>
    </div>
    <div class="field-group">
      <label>Starting At Age</label>
      <div class="inputs">
        <input type="number" id="supplemental-age" min="18" max="120" placeholder="67">
        <span class="unit-label">yrs</span>
      </div>
    </div>
  </div>
</details>

<div class="section-label">Asset Allocation</div>

<div class="alloc-row">
  <div class="field-group">
    <label>Stocks</label>
    <div class="inputs">
      <input type="number" id="alloc-stocks" min="0" max="100" value="80" required>
      <span class="unit-label">%</span>
    </div>
  </div>
  <div class="field-group">
    <label>Bonds</label>
    <div class="inputs">
      <input type="number" id="alloc-bonds" min="0" max="100" value="15" required>
      <span class="unit-label">%</span>
    </div>
  </div>
  <div class="field-group">
    <label>Cash</label>
    <div class="inputs">
      <input type="number" id="alloc-cash" min="0" max="100" value="5" required>
      <span class="unit-label">%</span>
    </div>
  </div>
</div>
<div class="alloc-error" id="alloc-error">Allocation must sum to 100%.</div>

<div class="section-label">Expected Real Returns (after inflation)</div>

<div class="alloc-row">
  <div class="field-group">
    <label>Stocks</label>
    <div class="inputs">
      <input type="number" id="return-stocks" min="0" max="30" step="0.5" value="8" required>
      <span class="unit-label">%</span>
    </div>
  </div>
  <div class="field-group">
    <label>Bonds</label>
    <div class="inputs">
      <input type="number" id="return-bonds" min="0" max="30" step="0.5" value="3" required>
      <span class="unit-label">%</span>
    </div>
  </div>
  <div class="field-group">
    <label>Cash</label>
    <div class="inputs">
      <input type="number" id="return-cash" min="0" max="30" step="0.5" value="1" required>
      <span class="unit-label">%</span>
    </div>
  </div>
</div>

<div class="actions">
  <button class="btn-calc" onclick="calculate()">Calculate</button>
  <button class="btn-clear" onclick="clearResults()">Clear</button>
</div>

<div class="warning-msg" id="warning"></div>
<div class="error-msg" id="error"></div>
</div>

<div class="results-section" id="results-section">
  <div class="fire-headline" id="headline"></div>

  <div class="chart-container">
    <canvas id="chart"></canvas>
  </div>
  <div class="chart-legend">
    <span class="legend-working">Working</span>
    <span class="legend-retired">Retired</span>
    <span class="legend-fire">FIRE Target</span>
  </div>

  <div class="stats-header">Your Numbers</div>
  <div class="stats-row">
    <span class="stat-label">Annual Savings</span>
    <span class="stat-value" id="stat-savings"></span>
  </div>
  <div class="stats-row">
    <span class="stat-label">Savings Rate</span>
    <span class="stat-value" id="stat-rate"></span>
  </div>
  <div class="stats-row">
    <span class="stat-label">Blended Return</span>
    <span class="stat-value" id="stat-return"></span>
  </div>
  <div class="stats-header">Milestones</div>
  <div class="stats-row">
    <span class="stat-label">FIRE Year</span>
    <span class="stat-value milestone-value" id="stat-fire-year"></span>
  </div>
  <div class="stats-row">
    <span class="stat-label">FIRE Number</span>
    <span class="stat-value milestone-value" id="stat-fire-number"></span>
  </div>
  <div class="stats-row">
    <span class="stat-label" id="stat-coast-fi-label">Coast FI Number</span>
    <span class="stat-value" id="stat-coast-fi"></span>
  </div>
  <div class="stat-desc" id="coast-fi-desc">Portfolio needed today to coast with $0 savings</div>

  <div class="stats-header">Safe Spend Rates</div>
  <div class="stat-desc" id="stress-desc" style="text-align: left; margin-bottom: 0.4rem;">Annual spend at FIRE portfolio size</div>
  <table class="stress-table" id="stress-table">
    <thead>
      <tr><th>Rate</th><th>Annual Spend</th></tr>
    </thead>
    <tbody id="stress-tbody"></tbody>
  </table>

  <div class="stats-header">Am I FI Today?</div>
  <div class="fire-headline" id="fi-verdict" style="margin: 0.5rem 0 0.75rem;"></div>
  <table class="stress-table" id="fi-benchmarks">
    <thead>
      <tr><th>Benchmark</th><th>Required Portfolio</th><th>Gap</th></tr>
    </thead>
    <tbody id="fi-bench-tbody"></tbody>
  </table>
</div>
</div>

<script>
  const MAX_YEARS = 80;

  function val(id) {
    return parseFloat(document.getElementById(id).value) || 0;
  }

  function fmtMoney(n) {
    if (n >= 1e6) return '$' + (n / 1e6).toFixed(1) + 'M';
    if (n >= 1e3) return '$' + Math.round(n).toLocaleString();
    return '$' + Math.round(n);
  }

  function showError(msg) {
    const el = document.getElementById('error');
    el.textContent = msg;
    el.style.display = 'block';
    document.getElementById('results-section').style.display = 'none';
  }

  function isEmpty(id) {
    return document.getElementById(id).value.trim() === '';
  }

  function setFieldError(id, hasError) {
    const input = document.getElementById(id);
    input.classList.toggle('input-error', hasError);
    if (hasError) input.setAttribute('aria-invalid', 'true');
    else input.removeAttribute('aria-invalid');
  }

  function requiredPortfolio(expenses, withdrawalRate, supplementalAnnual, supplementalAge, age, returnRate) {
    const noSupplementTarget = expenses / withdrawalRate;
    if (supplementalAnnual <= 0 || supplementalAge <= age) {
      return Math.max(0, expenses - supplementalAnnual) / withdrawalRate;
    }

    const bridgeYears = supplementalAge - age;
    const annualGap = Math.min(expenses, supplementalAnnual);
    const ongoingExpenses = Math.max(0, expenses - supplementalAnnual);
    const bridge = returnRate === 0
      ? annualGap * bridgeYears
      : annualGap * (1 - Math.pow(1 + returnRate, -bridgeYears)) / returnRate;
    return Math.min(noSupplementTarget, ongoingExpenses / withdrawalRate + bridge);
  }

  function calculate() {
    document.getElementById('error').style.display = 'none';
    document.getElementById('warning').style.display = 'none';
    document.getElementById('alloc-error').style.display = 'none';

    const inputs = Array.from(document.querySelectorAll('.field-group input'));
    const invalidInputs = inputs.filter(function(input) { return !input.checkValidity(); });
    inputs.forEach(function(input) { setFieldError(input.id, invalidInputs.includes(input)); });
    if (invalidInputs.length > 0) {
      const hasMissingValue = invalidInputs.some(function(input) { return input.validity.valueMissing; });
      showError(hasMissingValue ? 'Please fill in all required fields.' : 'Please enter values within the allowed ranges.');
      invalidInputs[0].focus();
      return;
    }

    const age = val('age');
    const income = val('income');
    const expenses = val('expenses');
    const networth = val('networth');
    const allocStocks = val('alloc-stocks');
    const allocBonds = val('alloc-bonds');
    const allocCash = val('alloc-cash');
    const retStocks = val('return-stocks') / 100;
    const retBonds = val('return-bonds') / 100;
    const retCash = val('return-cash') / 100;
    const wr = val('withdrawal-rate') / 100;
    const supplementalMonthly = val('supplemental-monthly');
    const supplementalAnnual = supplementalMonthly * 12;
    const supplementalAge = val('supplemental-age');

    // Validation
    const allocSum = allocStocks + allocBonds + allocCash;
    if (Math.abs(allocSum - 100) > 0.01) {
      document.getElementById('alloc-error').style.display = 'block';
      return;
    }

    if (expenses > income) {
      const el = document.getElementById('warning');
      el.textContent = 'Expenses exceed income — the annual shortfall reduces your portfolio before FIRE.';
      el.style.display = 'block';
    }
    if (supplementalMonthly > 0 && isEmpty('supplemental-age')) {
      setFieldError('supplemental-age', true);
      showError('Enter the age when supplemental income begins.');
      return;
    }
    if (supplementalMonthly > 0 && supplementalAge < age) {
      setFieldError('supplemental-age', true);
      showError('Supplemental income starting age cannot be before your current age.');
      return;
    }

    const annualSavings = income - expenses;
    const savingsRate = income > 0 ? annualSavings / income : 0;
    const blendedReturn = (allocStocks * retStocks + allocBonds * retBonds + allocCash * retCash) / 100;
    let fireNumber = requiredPortfolio(expenses, wr, supplementalAnnual, supplementalAge, age, blendedReturn);

    // Projection
    let portfolio = networth;
    let cumContributions = networth;
    let cumReturns = 0;
    const data = [{ year: 0, contributions: cumContributions, returns: 0, total: portfolio }];
    let fireYear = portfolio >= fireNumber ? 0 : null;

    for (let y = 1; y <= MAX_YEARS; y++) {
      const yearReturn = portfolio * blendedReturn;
      const currentAge = age + y;
      const supplementalIncome = currentAge >= supplementalAge ? supplementalAnnual : 0;
      const yearSavings = (fireYear === null) ? annualSavings + supplementalIncome : supplementalIncome - expenses;
      portfolio += yearSavings + yearReturn;
      if (portfolio < 0) portfolio = 0;
      cumContributions += yearSavings;
      cumReturns += yearReturn;
      data.push({ year: y, contributions: cumContributions, returns: cumReturns, total: portfolio });

      const currentTarget = requiredPortfolio(expenses, wr, supplementalAnnual, supplementalAge, currentAge, blendedReturn);
      if (fireYear === null && portfolio >= currentTarget) {
        fireYear = y;
        fireNumber = currentTarget;
      }
    }

    // If never reached FIRE
    if (fireYear === null) {
      showError('FIRE target not reached within ' + MAX_YEARS + ' years. Try reducing expenses or increasing income.');
      return;
    }

    // Headline
    const fireAge = Math.round(age + fireYear);
    const currentYear = new Date().getFullYear();
    if (fireYear === 0) {
      document.getElementById('headline').innerHTML =
        '<strong>You are financially independent today at age ' + fireAge + '</strong>';
    } else {
      const yearLabel = fireYear === 1 ? 'year' : 'years';
      document.getElementById('headline').innerHTML =
        'You can reach Financial Independence in <strong>' + fireYear + ' ' + yearLabel + ' by age ' + fireAge + '</strong>';
    }

    // Stats
    document.getElementById('stat-savings').textContent = fmtMoney(annualSavings) + '/yr';
    document.getElementById('stat-rate').textContent = (Math.max(0, savingsRate) * 100).toFixed(1) + '%';
    document.getElementById('stat-return').textContent = (blendedReturn * 100).toFixed(1) + '%';
    document.getElementById('stat-fire-number').textContent = fmtMoney(fireNumber);
    document.getElementById('stat-fire-year').textContent = (currentYear + fireYear).toString();

    // Coast FI: present value of FIRE number discounted back fireYear years
    const coastFI = fireNumber / Math.pow(1 + blendedReturn, fireYear);
    const coastEl = document.getElementById('stat-coast-fi');
    const coastLabel = document.getElementById('stat-coast-fi-label');
    const coastDesc = document.getElementById('coast-fi-desc');
    coastEl.textContent = fmtMoney(coastFI);
    coastDesc.style.display = 'block';
    if (networth >= coastFI) {
      coastLabel.innerHTML = 'Coast FI Number <span class="coast-reached">(reached)</span>';
    } else {
      const delta = coastFI - networth;
      coastLabel.innerHTML = 'Coast FI Number <span class="coast-delta">(' + fmtMoney(delta) + ' to go)</span>';
    }

    // Withdrawal stress test
    const firePortfolio = data[fireYear].total;
    const stressRates = [3, 4, 5];
    const userRate = val('withdrawal-rate');
    const tbody = document.getElementById('stress-tbody');
    tbody.innerHTML = '';
    for (const rate of stressRates) {
      const rateDecimal = rate / 100;
      const annualSpend = firePortfolio * rateDecimal;
      const tr = document.createElement('tr');
      if (rate === userRate) tr.className = 'stress-active';
      tr.innerHTML = '<td>' + rate.toFixed(1) + '%' + (rate === userRate ? ' ←' : '') + '</td>' +
        '<td>' + fmtMoney(annualSpend) + '/yr</td>';
      tbody.appendChild(tr);
    }

    // Am I FI Today?
    const benchTbody = document.getElementById('fi-bench-tbody');
    benchTbody.innerHTML = '';
    const requiredToday = requiredPortfolio(expenses, wr, supplementalAnnual, supplementalAge, age, blendedReturn);
    const gap = requiredToday - networth;
    const tr = document.createElement('tr');
    const gapValue = gap > 0
      ? '<span class="gap-negative">−' + fmtMoney(gap) + '</span>'
      : '<span class="gap-positive">+' + fmtMoney(Math.abs(gap)) + '</span>';
    tr.innerHTML = '<td>' + userRate.toFixed(1) + '% (SWR)</td>' +
      '<td>' + fmtMoney(requiredToday) + '</td>' +
      '<td>' + gapValue + '</td>';
    benchTbody.appendChild(tr);
    const verdictEl = document.getElementById('fi-verdict');
    if (gap <= 0) {
      verdictEl.innerHTML = '<strong style="color:#a3d9a5">Yes</strong> — your portfolio covers the target at your selected withdrawal rate';
    } else {
      verdictEl.innerHTML = '<strong style="color:var(--accent)">Not yet</strong> — your portfolio doesn\'t cover the target at your selected withdrawal rate';
    }

    document.getElementById('results-section').style.display = 'block';

    // Chart extends to 20 years or fireYear + 10, whichever is longer
    const chartYears = Math.min(Math.max(20, fireYear + 10), MAX_YEARS);
    const chartData = data.slice(0, chartYears + 1);
    drawChart(chartData, fireNumber, fireYear);
  }

  function drawChart(data, fireNumber, fireYear) {
    const canvas = document.getElementById('chart');
    const dpr = window.devicePixelRatio || 1;
    const rect = canvas.getBoundingClientRect();
    canvas.width = rect.width * dpr;
    canvas.height = rect.height * dpr;
    const ctx = canvas.getContext('2d');
    ctx.scale(dpr, dpr);

    const w = rect.width;
    const h = rect.height;
    const pad = { top: 20, right: 20, bottom: 35, left: 60 };
    const plotW = w - pad.left - pad.right;
    const plotH = h - pad.top - pad.bottom;

    // Clear
    ctx.clearRect(0, 0, w, h);

    // Scales
    const maxYear = data[data.length - 1].year;
    const maxVal = Math.max(fireNumber, data[data.length - 1].total) * 1.1;

    function xPos(year) { return pad.left + (year / maxYear) * plotW; }
    function yPos(val) { return pad.top + plotH - (val / maxVal) * plotH; }

    // Style constants
    const accent = '#bf616a';
    const muted = '#909498';
    const gridColor = 'rgba(144,148,152,0.15)';

    // Grid lines (Y)
    ctx.strokeStyle = gridColor;
    ctx.lineWidth = 1;
    const yTicks = 5;
    for (let i = 0; i <= yTicks; i++) {
      const v = (maxVal / yTicks) * i;
      const y = yPos(v);
      ctx.beginPath();
      ctx.moveTo(pad.left, y);
      ctx.lineTo(w - pad.right, y);
      ctx.stroke();
    }

    // Portfolio area — accumulation phase (up to FIRE year)
    ctx.beginPath();
    ctx.moveTo(xPos(data[0].year), yPos(0));
    for (let i = 0; i <= fireYear && i < data.length; i++) {
      ctx.lineTo(xPos(data[i].year), yPos(data[i].total));
    }
    ctx.lineTo(xPos(data[fireYear].year), yPos(0));
    ctx.closePath();
    ctx.fillStyle = accent + '99';
    ctx.fill();

    // Portfolio area — retirement phase (after FIRE year)
    if (fireYear < data.length - 1) {
      ctx.beginPath();
      ctx.moveTo(xPos(data[fireYear].year), yPos(0));
      for (let i = fireYear; i < data.length; i++) {
        ctx.lineTo(xPos(data[i].year), yPos(data[i].total));
      }
      ctx.lineTo(xPos(data[data.length - 1].year), yPos(0));
      ctx.closePath();
      ctx.fillStyle = accent + '44';
      ctx.fill();
    }

    // FIRE target line (dashed)
    ctx.strokeStyle = muted;
    ctx.lineWidth = 1.5;
    ctx.setLineDash([6, 4]);
    ctx.beginPath();
    ctx.moveTo(pad.left, yPos(fireNumber));
    ctx.lineTo(w - pad.right, yPos(fireNumber));
    ctx.stroke();
    ctx.setLineDash([]);

    // FIRE label
    ctx.fillStyle = muted;
    ctx.font = '11px Inter, sans-serif';
    ctx.textAlign = 'right';
    ctx.fillText(fmtMoney(fireNumber), w - pad.right, yPos(fireNumber) - 5);

    // Dot at FIRE crossing
    if (fireYear <= data[data.length - 1].year) {
      const dp = data[fireYear];
      const cx = xPos(fireYear);
      const cy = yPos(dp.total);
      ctx.beginPath();
      ctx.arc(cx, cy, 5, 0, Math.PI * 2);
      ctx.fillStyle = accent;
      ctx.fill();
      ctx.strokeStyle = '#222426';
      ctx.lineWidth = 2;
      ctx.stroke();
    }

    // Axes labels
    ctx.fillStyle = muted;
    ctx.font = '11px Inter, sans-serif';
    ctx.textAlign = 'center';

    // X-axis: year labels
    const xTickCount = Math.min(maxYear, 8);
    const xStep = Math.ceil(maxYear / xTickCount);
    for (let y = 0; y <= maxYear; y += xStep) {
      ctx.fillText('Yr ' + y, xPos(y), h - pad.bottom + 18);
    }

    // Y-axis: value labels
    ctx.textAlign = 'right';
    for (let i = 0; i <= yTicks; i++) {
      const v = (maxVal / yTicks) * i;
      ctx.fillText(fmtMoney(v), pad.left - 8, yPos(v) + 4);
    }
  }

  function clearResults() {
    document.getElementById('results-section').style.display = 'none';
    document.getElementById('error').style.display = 'none';
    document.getElementById('warning').style.display = 'none';
    document.getElementById('alloc-error').style.display = 'none';
    document.querySelectorAll('.field-group input').forEach(function(input) {
      setFieldError(input.id, false);
    });
  }

  // Enter key triggers calculation
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') calculate();
  });

  document.querySelectorAll('.field-group input').forEach(function(input) {
    input.addEventListener('input', function() {
      setFieldError(input.id, false);
    });
  });

</script>
