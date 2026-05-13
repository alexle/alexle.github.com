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

  .field-group .unit-label {
    color: var(--muted);
    font-size: 0.85rem;
    white-space: nowrap;
    min-width: 1.5rem;
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
</style>

<div class="fire-calc">
<p style="color: var(--muted); font-size: 0.9rem; margin: 0 0 1.5rem;">Project when you can achieve financial independence.</p>

<div class="fire-inputs">
<div class="field-group">
  <label>Current Age</label>
  <div class="inputs">
    <input type="number" id="age" min="18" max="80" placeholder="30">
    <span class="unit-label">yrs</span>
  </div>
</div>

<div class="field-group">
  <label>Current Net Worth</label>
  <div class="inputs">
    <input type="number" id="networth" min="0" step="1000" placeholder="100000">
    <span class="unit-label">$</span>
  </div>
</div>

<div class="field-group">
  <label>Annual Income (after tax)</label>
  <div class="inputs">
    <input type="number" id="income" min="0" step="1000" placeholder="50000">
    <span class="unit-label">$</span>
  </div>
</div>

<div class="field-group">
  <label>Annual Expenses</label>
  <div class="inputs">
    <input type="number" id="expenses" min="0" step="1000" placeholder="40000">
    <span class="unit-label">$</span>
  </div>
</div>

<div class="field-group">
  <label>Safe Withdrawal Rate</label>
  <div class="inputs">
    <input type="number" id="withdrawal-rate" min="1" max="10" step="0.5" value="4">
    <span class="unit-label">%</span>
  </div>
</div>

<div class="section-label">Asset Allocation</div>

<div class="alloc-row">
  <div class="field-group">
    <label>Stocks</label>
    <div class="inputs">
      <input type="number" id="alloc-stocks" min="0" max="100" value="80">
      <span class="unit-label">%</span>
    </div>
  </div>
  <div class="field-group">
    <label>Bonds</label>
    <div class="inputs">
      <input type="number" id="alloc-bonds" min="0" max="100" value="15">
      <span class="unit-label">%</span>
    </div>
  </div>
  <div class="field-group">
    <label>Cash</label>
    <div class="inputs">
      <input type="number" id="alloc-cash" min="0" max="100" value="5">
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
      <input type="number" id="return-stocks" min="0" max="30" step="0.5" value="7">
      <span class="unit-label">%</span>
    </div>
  </div>
  <div class="field-group">
    <label>Bonds</label>
    <div class="inputs">
      <input type="number" id="return-bonds" min="0" max="30" step="0.5" value="3">
      <span class="unit-label">%</span>
    </div>
  </div>
  <div class="field-group">
    <label>Cash</label>
    <div class="inputs">
      <input type="number" id="return-cash" min="0" max="30" step="0.5" value="1">
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
    <span class="stat-label">FIRE Number</span>
    <span class="stat-value" id="stat-fire-number"></span>
  </div>
  <div class="stats-row">
    <span class="stat-label">FIRE Year</span>
    <span class="stat-value" id="stat-fire-year"></span>
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
      <tr><th>Rate</th><th>Annual Spend</th><th>vs. Expenses</th></tr>
    </thead>
    <tbody id="stress-tbody"></tbody>
  </table>

  <div class="stats-header">Am I FI Today?</div>
  <div class="stats-row">
    <span class="stat-label">Your Current Withdrawal Rate</span>
    <span class="stat-value" id="stat-current-wr"></span>
  </div>
  <div class="stat-desc" id="current-wr-desc">expenses / current net worth</div>
  <table class="stress-table" id="fi-benchmarks">
    <thead>
      <tr><th>Benchmark</th><th>Required Portfolio</th><th>Gap</th></tr>
    </thead>
    <tbody id="fi-bench-tbody"></tbody>
  </table>
  <div class="fire-headline" id="fi-verdict" style="margin-top: 0.75rem;"></div>
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

  function calculate() {
    document.getElementById('error').style.display = 'none';
    document.getElementById('warning').style.display = 'none';
    document.getElementById('alloc-error').style.display = 'none';

    // Check required fields
    const required = ['age', 'income', 'expenses', 'networth', 'alloc-stocks', 'alloc-bonds', 'alloc-cash', 'return-stocks', 'return-bonds', 'return-cash', 'withdrawal-rate'];
    if (required.some(isEmpty)) {
      showError('Please fill in all fields.');
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

    // Validation
    const allocSum = allocStocks + allocBonds + allocCash;
    if (Math.abs(allocSum - 100) > 0.01) {
      document.getElementById('alloc-error').style.display = 'block';
      return;
    }

    if (income < 0) { showError('Income cannot be negative.'); return; }
    if (expenses >= income) {
      const el = document.getElementById('warning');
      el.textContent = 'Expenses exceed income — savings rate is negative. Results assume no new contributions.';
      el.style.display = 'block';
    }
    if (wr <= 0) { showError('Withdrawal rate must be greater than 0.'); return; }

    const annualSavings = income - expenses;
    const savingsRate = income > 0 ? annualSavings / income : 0;
    const blendedReturn = (allocStocks * retStocks + allocBonds * retBonds + allocCash * retCash) / 100;
    const fireNumber = expenses / wr;

    // Projection
    let portfolio = networth;
    let cumContributions = networth;
    let cumReturns = 0;
    const data = [{ year: 0, contributions: cumContributions, returns: 0, total: portfolio }];
    let fireYear = null;

    for (let y = 1; y <= MAX_YEARS; y++) {
      const yearReturn = portfolio * blendedReturn;
      const yearSavings = (fireYear === null) ? annualSavings : -expenses;
      portfolio += yearSavings + yearReturn;
      if (portfolio < 0) portfolio = 0;
      cumContributions += yearSavings;
      cumReturns += yearReturn;
      data.push({ year: y, contributions: cumContributions, returns: cumReturns, total: portfolio });

      if (fireYear === null && portfolio >= fireNumber) {
        fireYear = y;
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
    document.getElementById('headline').innerHTML =
      'You can reach Financial Independence in <strong>' + fireYear + ' years by age ' + fireAge + '</strong>';

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
    const stressRates = [3, 3.5, 4, 4.5, 5];
    const userRate = val('withdrawal-rate');
    // Ensure user's rate is in the list
    const rates = stressRates.includes(userRate) ? stressRates : [...stressRates, userRate].sort((a, b) => a - b);
    const tbody = document.getElementById('stress-tbody');
    tbody.innerHTML = '';
    for (const rate of rates) {
      const rateDecimal = rate / 100;
      const annualSpend = firePortfolio * rateDecimal;
      const diff = (annualSpend - expenses) / 12;
      const diffStr = (diff >= 0 ? '+' : '') + fmtMoney(diff) + '/mo';
      const tr = document.createElement('tr');
      if (rate === userRate) tr.className = 'stress-active';
      tr.innerHTML = '<td>' + rate.toFixed(1) + '%' + (rate === userRate ? ' ←' : '') + '</td>' +
        '<td>' + fmtMoney(annualSpend) + '/yr</td>' +
        '<td>' + diffStr + '</td>';
      tbody.appendChild(tr);
    }

    // Am I FI Today?
    const currentWR = networth > 0 ? (expenses / networth) * 100 : 0;
    document.getElementById('stat-current-wr').textContent = currentWR.toFixed(2) + '%';
    const benchmarks = [3, 3.5, 4];
    const benchTbody = document.getElementById('fi-bench-tbody');
    benchTbody.innerHTML = '';
    let verdict = 'Not yet';
    for (const bench of benchmarks) {
      const required = expenses / (bench / 100);
      const gap = required - networth;
      const tr = document.createElement('tr');
      tr.innerHTML = '<td>' + bench.toFixed(1) + '% (SWR)</td>' +
        '<td>' + fmtMoney(required) + '</td>' +
        '<td>' + (gap <= 0 ? '<span style="color:#a3d9a5">✓ covered</span>' : fmtMoney(gap) + ' short') + '</td>';
      benchTbody.appendChild(tr);
    }
    if (currentWR <= 3) verdict = 'Safe';
    else if (currentWR <= 4) verdict = 'Lean';
    const verdictEl = document.getElementById('fi-verdict');
    if (verdict === 'Safe') {
      verdictEl.innerHTML = '<strong style="color:#a3d9a5">Safe</strong> — your portfolio covers expenses at a conservative withdrawal rate';
    } else if (verdict === 'Lean') {
      verdictEl.innerHTML = '<strong style="color:#e0a458">Lean</strong> — you could retire today, but with less safety margin';
    } else {
      verdictEl.innerHTML = '<strong style="color:var(--accent)">Not yet</strong> — your portfolio doesn\'t cover expenses at a 4% withdrawal rate';
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
  }

  // Enter key triggers calculation
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') calculate();
  });

</script>
