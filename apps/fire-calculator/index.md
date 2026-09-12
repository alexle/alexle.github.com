---
layout: app
title: "FIRE Calculator"
permalink: /fire-calculator/
---

<!-- markdownlint-disable MD033 -->
<style>
  .fire-calc {
    --highlight: #a3d9a5;
    --text-small: 0.8rem;
    --text-label: 0.85rem;
    --text-body: 0.9rem;
    --text-heading: 1.1rem;
    --text-emphasis: 1.4rem;
  }

  .fire-inputs { max-width: 480px; }

  .fire-intro {
    color: var(--muted);
    font-size: var(--text-body);
    margin-bottom: 1.5rem;
  }

  .fire-intro p { margin: 0 0 0.6rem; }
  .fire-intro p:last-child { margin-bottom: 0; }

  .field-group input.input-error {
    border-color: var(--accent);
    box-shadow: 0 0 0 1px var(--accent);
  }

  .field-group .unit-label {
    min-width: 1.5rem;
  }

  .optional-fields {
    margin: -0.35rem 0 1rem;
  }

  .optional-fields summary {
    color: var(--muted);
    cursor: pointer;
    font-size: var(--text-small);
    width: fit-content;
  }

  .optional-fields[open] summary { margin-bottom: 0.75rem; }

  .supplemental-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.75rem;
  }

  .supplemental-row .field-group { margin-bottom: 0; }

  @media (max-width: 520px) {
    .supplemental-row { grid-template-columns: 1fr; }
  }

  .section-label {
    font-size: var(--text-label);
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

  .alloc-row .field-group {
    flex: 1;
    margin-bottom: 0;
    min-width: 0;
  }

  .alloc-row input { min-width: 0; }

  .alloc-error {
    color: var(--accent);
    font-size: var(--text-small);
    margin-top: 0.25rem;
    display: none;
  }

  .error-msg {
    color: var(--accent);
    font-size: var(--text-label);
    margin-top: 0.5rem;
    display: none;
  }

  .warning-msg {
    color: #e0a458;
    font-size: var(--text-label);
    margin-top: 0.5rem;
    display: none;
  }

  .fire-headline {
    font-size: var(--text-heading);
    font-weight: 400;
    color: var(--muted);
    margin-bottom: 1rem;
    line-height: 1.4;
  }

  .fire-headline strong {
    font-size: var(--text-emphasis);
    color: var(--accent);
  }

  .fi-status-row {
    font-size: var(--text-heading);
    margin-top: 1rem;
  }

  .fi-status-row .stats-header {
    font-size: inherit;
    margin: 0;
  }

  .fi-verdict {
    color: var(--muted);
    font-size: var(--text-body);
    line-height: 1.4;
    margin: 0.5rem 0 0.75rem;
  }

  .fi-verdict #fi-status {
    font-size: var(--text-emphasis);
  }

  .fi-status-yes { color: #a3d9a5; }
  .fi-status-not-yet { color: var(--accent); }

  .fi-explanation {
    display: block;
    font-size: inherit;
    margin-top: 0.2rem;
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
    font-size: var(--text-small);
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
    font-size: var(--text-body);
  }

  .stats-row .stat-label { color: var(--muted); }
  .stats-row .stat-value { font-weight: 500; }
  .stats-row .stat-value.milestone-value { color: var(--highlight); }

  .stats-header {
    font-size: var(--text-heading);
    color: inherit;
    margin-top: 1rem;
    margin-bottom: 0.25rem;
  }

  .stats-header:first-child { margin-top: 0; }

  .stat-desc {
    font-size: var(--text-body);
    color: var(--muted);
    text-align: right;
  }

  .coast-reached {
    color: #a3d9a5;
    font-size: inherit;
    font-weight: 500;
  }

  .coast-delta {
    color: var(--muted);
    font-size: inherit;
  }

  .coast-desc { font-size: var(--text-small); }

  .stress-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 0.5rem;
    font-size: var(--text-body);
    table-layout: fixed;
  }

  .stress-table th {
    color: var(--muted);
    font-weight: 400;
    text-align: left;
    padding: 0.35rem 0;
    border-bottom: 1px solid var(--border);
  }

  #action-insights .stress-table th { vertical-align: bottom; }

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

  .visually-hidden {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
  }
</style>

<div class="fire-calc">
<div class="fire-intro">
  <p>Project when you can achieve financial independence.</p>
  <p>FI means your investments can cover your living expenses. All amounts are in today's dollars and assume constant real returns (<a href="https://www.financialplanningassociation.org/sites/default/files/2020-05/7%20Determining%20Withdrawal%20Rates%20Using%20Historical%20Data.pdf">link</a>).</p>
</div>

<form class="fire-inputs" id="fire-form" novalidate>
<div class="field-group">
  <label for="age">Current Age</label>
  <div class="inputs">
    <input type="number" id="age" min="18" max="80" placeholder="30" required>
    <span class="unit-label">yrs</span>
  </div>
</div>

<div class="field-group">
  <label for="networth">Net Investable Assets</label>
  <div class="inputs">
    <input type="number" id="networth" min="0" step="1" placeholder="100000" required>
    <span class="unit-label">$</span>
  </div>
</div>

<div class="field-group">
  <label for="income">Annual Income (after tax)</label>
  <div class="inputs">
    <input type="number" id="income" min="0" step="1" placeholder="50000" required>
    <span class="unit-label">$</span>
  </div>
</div>

<div class="field-group">
  <label for="expenses">Annual Expenses</label>
  <div class="inputs">
    <input type="number" id="expenses" min="0" step="1" placeholder="40000" required>
    <span class="unit-label">$</span>
  </div>
</div>

<div class="field-group">
  <label for="withdrawal-rate">Withdrawal Rate</label>
  <div class="inputs">
    <input type="number" id="withdrawal-rate" min="1" max="10" step="0.5" value="4" required>
    <span class="unit-label">%</span>
  </div>
</div>

<details class="optional-fields">
  <summary>Supplemental income (optional)</summary>
  <div class="supplemental-row">
    <div class="field-group">
      <label for="supplemental-monthly">Supplemental Per Month</label>
      <div class="inputs">
        <input type="number" id="supplemental-monthly" min="0" step="1" placeholder="0">
        <span class="unit-label">$</span>
      </div>
    </div>
    <div class="field-group">
      <label for="supplemental-age">Starting At Age</label>
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
    <label for="alloc-stocks">Stocks</label>
    <div class="inputs">
      <input type="number" id="alloc-stocks" min="0" max="100" value="80" required>
      <span class="unit-label">%</span>
    </div>
  </div>
  <div class="field-group">
    <label for="alloc-bonds">Bonds</label>
    <div class="inputs">
      <input type="number" id="alloc-bonds" min="0" max="100" value="15" required>
      <span class="unit-label">%</span>
    </div>
  </div>
  <div class="field-group">
    <label for="alloc-cash">Cash</label>
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
    <label for="return-stocks">Stocks</label>
    <div class="inputs">
      <input type="number" id="return-stocks" min="0" max="30" step="0.5" value="8" required>
      <span class="unit-label">%</span>
    </div>
  </div>
  <div class="field-group">
    <label for="return-bonds">Bonds</label>
    <div class="inputs">
      <input type="number" id="return-bonds" min="0" max="30" step="0.5" value="3" required>
      <span class="unit-label">%</span>
    </div>
  </div>
  <div class="field-group">
    <label for="return-cash">Cash</label>
    <div class="inputs">
      <input type="number" id="return-cash" min="0" max="30" step="0.5" value="1" required>
      <span class="unit-label">%</span>
    </div>
  </div>
</div>

<div class="actions">
  <button class="btn-calc" type="submit">Calculate</button>
  <button class="btn-clear" id="clear-button" type="button">Clear</button>
</div>

<div class="warning-msg" id="warning" role="status" aria-live="polite"></div>
<div class="error-msg" id="error" role="alert" aria-live="assertive"></div>
</form>

<div class="results-section" id="results-section" aria-live="polite">
  <div class="fire-headline" id="headline"></div>

  <div class="chart-container" id="chart-container">
    <canvas id="chart" role="img" aria-describedby="chart-summary">Portfolio projection chart</canvas>
    <p class="visually-hidden" id="chart-summary"></p>
  </div>
  <div class="chart-legend" id="chart-legend">
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
  <div id="coast-fi-group">
  <div class="stats-row">
    <span class="stat-label" id="stat-coast-fi-label">Coast FI Number</span>
    <span class="stat-value" id="stat-coast-fi"></span>
  </div>
  <div class="stat-desc coast-desc">Amount needed today to reach FI by <span id="coast-fi-year"></span> with $0 additional savings</div>
  </div>

  <div class="stats-header" id="stress-heading"></div>
  <table class="stress-table">
    <thead>
      <tr><th>Withdrawal Rate</th><th>Target Portfolio</th></tr>
    </thead>
    <tbody id="stress-tbody"></tbody>
  </table>

  <div class="fi-status-row">
    <div class="stats-header">Am I FI Today?</div>
  </div>
  <div class="fi-verdict">
    <strong id="fi-status"></strong>
    <span class="fi-explanation" id="fi-explanation"></span>
  </div>

  <div id="action-insights">
    <div class="stats-header">Ways to Reach FI Sooner</div>
    <table class="stress-table">
      <thead>
        <tr><th>Invest More Each Month</th><th>FI Age</th><th>Sooner By</th></tr>
      </thead>
      <tbody id="scenario-tbody"></tbody>
    </table>
  </div>
</div>
</div>

<script>
  const MAX_YEARS = 80;

  function val(id) {
    return parseFloat(document.getElementById(id).value) || 0;
  }

  function fmtMoney(n) {
    const rounded = Math.round(n);
    return (rounded < 0 ? '-$' : '$') + Math.abs(rounded).toLocaleString();
  }

  function fmtMoneyCompact(n) {
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

  function focusField(input) {
    document.querySelectorAll('details').forEach(function(details) {
      if (details.contains(input)) details.open = true;
    });
    input.focus();
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

  function findFireMonth(age, networth, annualSavings, expenses, returnRate, withdrawalRate, supplementalAnnual, supplementalAge) {
    let portfolio = networth;
    const monthlyReturn = Math.pow(1 + returnRate, 1 / 12) - 1;
    for (let month = 0; month <= MAX_YEARS * 12; month++) {
      const currentAge = age + month / 12;
      const target = requiredPortfolio(expenses, withdrawalRate, supplementalAnnual, supplementalAge, currentAge, returnRate);
      if (portfolio >= target) return month;
      const supplementalIncome = age + (month + 1) / 12 >= supplementalAge ? supplementalAnnual / 12 : 0;
      portfolio = Math.max(0, portfolio * (1 + monthlyReturn) + annualSavings / 12 + supplementalIncome);
    }
    return null;
  }

  function fireAgeText(month, age) {
    if (month === null) return 'Beyond range';
    return Math.floor(age + month / 12).toString();
  }

  function monthDifferenceText(scenarioMonth, baseMonth) {
    if (scenarioMonth === null) return baseMonth === null ? 'No change' : 'Beyond range';
    if (baseMonth === null) return 'Now projected';
    const monthsSooner = baseMonth - scenarioMonth;
    if (monthsSooner === 0) return 'No change within monthly estimate';
    const duration = Math.abs(monthsSooner) + ' ' + (Math.abs(monthsSooner) === 1 ? 'month' : 'months');
    return monthsSooner > 0 ? duration : duration + ' later';
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
      focusField(invalidInputs[0]);
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
      ['alloc-stocks', 'alloc-bonds', 'alloc-cash'].forEach(function(id) { setFieldError(id, true); });
      focusField(document.getElementById('alloc-stocks'));
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
      focusField(document.getElementById('supplemental-age'));
      return;
    }
    if (supplementalMonthly > 0 && supplementalAge < age) {
      setFieldError('supplemental-age', true);
      showError('Supplemental income starting age cannot be before your current age.');
      focusField(document.getElementById('supplemental-age'));
      return;
    }

    const annualSavings = income - expenses;
    const savingsRate = income > 0 ? annualSavings / income : 0;
    const blendedReturn = (allocStocks * retStocks + allocBonds * retBonds + allocCash * retCash) / 100;
    let fireNumber = requiredPortfolio(expenses, wr, supplementalAnnual, supplementalAge, age, blendedReturn);

    // Projection
    let portfolio = networth;
    const data = [{ year: 0, total: portfolio }];
    let fireYear = portfolio >= fireNumber ? 0 : null;

    for (let y = 1; y <= MAX_YEARS; y++) {
      const yearReturn = portfolio * blendedReturn;
      const currentAge = age + y;
      const supplementalIncome = currentAge >= supplementalAge ? supplementalAnnual : 0;
      const yearSavings = (fireYear === null) ? annualSavings + supplementalIncome : supplementalIncome - expenses;
      portfolio += yearSavings + yearReturn;
      if (portfolio < 0) portfolio = 0;
      data.push({ year: y, total: portfolio });

      const currentTarget = requiredPortfolio(expenses, wr, supplementalAnnual, supplementalAge, currentAge, blendedReturn);
      if (fireYear === null && portfolio >= currentTarget) {
        fireYear = y;
        fireNumber = currentTarget;
      }
    }

    // Headline
    const currentYear = new Date().getFullYear();
    const fireAge = fireYear === null ? null : Math.round(age + fireYear);
    if (fireYear === null) {
      document.getElementById('headline').innerHTML =
        '<strong>FIRE is beyond the ' + MAX_YEARS + '-year projection</strong> at these assumptions';
    } else if (fireYear === 0) {
      document.getElementById('headline').innerHTML =
        '<strong style="color:#a3d9a5">You are financially independent today at age ' + fireAge + '</strong>';
    } else {
      const yearLabel = fireYear === 1 ? 'year' : 'years';
      document.getElementById('headline').innerHTML =
        'In this scenario, you reach FI in <strong>' + fireYear + ' ' + yearLabel + ' by age ' + fireAge + '</strong>';
    }

    // Actionable comparisons
    const baseFireMonth = findFireMonth(age, networth, annualSavings, expenses, blendedReturn, wr, supplementalAnnual, supplementalAge);
    const actionInsights = document.getElementById('action-insights');
    actionInsights.style.display = fireYear === 0 ? 'none' : 'block';
    const scenarioTbody = document.getElementById('scenario-tbody');
    scenarioTbody.innerHTML = '';
    const scenarios = [500, 1000, 2000].map(function(monthlyInvestment) {
      return {
        change: fmtMoney(monthlyInvestment),
        month: findFireMonth(age, networth, annualSavings + monthlyInvestment * 12, expenses, blendedReturn, wr, supplementalAnnual, supplementalAge)
      };
    });
    scenarios.forEach(function(scenario) {
      const row = document.createElement('tr');
      row.innerHTML = '<td>' + scenario.change + '</td>' +
        '<td>' + fireAgeText(scenario.month, age) + '</td>' +
        '<td>' + monthDifferenceText(scenario.month, baseFireMonth) + '</td>';
      scenarioTbody.appendChild(row);
    });

    // Stats
    document.getElementById('stat-savings').textContent = fmtMoney(annualSavings) + '/yr';
    document.getElementById('stat-rate').textContent = (savingsRate * 100).toFixed(1) + '%';
    document.getElementById('stat-return').textContent = (blendedReturn * 100).toFixed(1) + '%';
    document.getElementById('stat-fire-number').textContent = fmtMoney(fireNumber);
    document.getElementById('stat-fire-year').textContent = fireYear === null ? 'Not within ' + MAX_YEARS + ' years' : (currentYear + fireYear).toString();

    // Coast FI: present value of FIRE number discounted back to today
    const coastGroup = document.getElementById('coast-fi-group');
    const coastEl = document.getElementById('stat-coast-fi');
    const coastLabel = document.getElementById('stat-coast-fi-label');
    if (fireYear === null) {
      coastGroup.style.display = 'none';
    } else {
      const coastFI = fireNumber / Math.pow(1 + blendedReturn, fireYear);
      coastGroup.style.display = 'block';
      document.getElementById('coast-fi-year').textContent = currentYear + fireYear;
      coastEl.textContent = fmtMoney(coastFI);
      if (networth >= coastFI) {
        coastLabel.innerHTML = 'Coast FI Number <span class="coast-reached">(reached)</span>';
      } else {
        const delta = coastFI - networth;
        coastLabel.innerHTML = 'Coast FI Number <span class="coast-delta">(' + fmtMoney(delta) + ' to go)</span>';
      }
    }

    // Portfolio targets at alternate withdrawal rates
    const stressRates = [3, 4, 5];
    const userRate = val('withdrawal-rate');
    const targetAge = fireYear === null ? age : fireAge;
    document.getElementById('stress-heading').textContent = fireYear === null ?
      'Portfolio Targets Today' : 'Portfolio Targets at FIRE Age ' + fireAge;
    const tbody = document.getElementById('stress-tbody');
    tbody.innerHTML = '';
    for (const rate of stressRates) {
      const target = requiredPortfolio(expenses, rate / 100, supplementalAnnual, supplementalAge, targetAge, blendedReturn);
      const tr = document.createElement('tr');
      if (rate === userRate) tr.className = 'stress-active';
      tr.innerHTML = '<td>' + rate.toFixed(1) + '%' + (rate === userRate ? ' ←' : '') + '</td>' +
        '<td>' + fmtMoney(target) + '</td>';
      tbody.appendChild(tr);
    }

    // Am I FI Today?
    const requiredToday = requiredPortfolio(expenses, wr, supplementalAnnual, supplementalAge, age, blendedReturn);
    const gap = requiredToday - networth;
    const statusEl = document.getElementById('fi-status');
    const explanationEl = document.getElementById('fi-explanation');
    const targetExplanation = 'At your ' + userRate.toFixed(1) + '% withdrawal rate, the FI target is ' + fmtMoney(requiredToday) + '. ';
    if (gap <= 0) {
      statusEl.textContent = 'Yes';
      statusEl.className = 'fi-status-yes';
      explanationEl.innerHTML = targetExplanation + (gap === 0 ?
        'Your portfolio meets it exactly.' :
        'Your portfolio is <span class="gap-positive">' + fmtMoney(Math.abs(gap)) + '</span> above it.');
    } else {
      statusEl.textContent = 'Not yet';
      statusEl.className = 'fi-status-not-yet';
      explanationEl.innerHTML = targetExplanation +
        'Your portfolio is <span class="gap-negative">' + fmtMoney(gap) + '</span> short.';
    }

    document.getElementById('results-section').style.display = 'block';

    const chartContainer = document.getElementById('chart-container');
    const chartLegend = document.getElementById('chart-legend');
    if (fireYear === null) {
      chartContainer.style.display = 'none';
      chartLegend.style.display = 'none';
      document.getElementById('chart-summary').textContent = '';
    } else {
      chartContainer.style.display = 'block';
      chartLegend.style.display = 'flex';
      const chartYears = Math.min(Math.max(20, fireYear + 10), MAX_YEARS);
      const chartData = data.slice(0, chartYears + 1);
      document.getElementById('chart-summary').textContent =
        'Portfolio projection from ' + fmtMoney(networth) + ' today to a FIRE target of ' + fmtMoney(fireNumber) +
        ' in ' + (currentYear + fireYear) + ', assuming a constant ' + (blendedReturn * 100).toFixed(1) + '% real return.';
      drawChart(chartData, fireNumber, fireYear);
    }
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
    const maxVal = Math.max(1, fireNumber, data[data.length - 1].total) * 1.1;

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
    ctx.fillText(fmtMoneyCompact(fireNumber), w - pad.right, yPos(fireNumber) - 5);

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
      ctx.fillText(fmtMoneyCompact(v), pad.left - 8, yPos(v) + 4);
    }
  }

  function resetCalculator() {
    document.getElementById('fire-form').reset();
    document.getElementById('results-section').style.display = 'none';
    document.getElementById('error').style.display = 'none';
    document.getElementById('warning').style.display = 'none';
    document.getElementById('alloc-error').style.display = 'none';
    document.querySelectorAll('.field-group input').forEach(function(input) {
      setFieldError(input.id, false);
    });
    document.querySelectorAll('details').forEach(function(details) { details.open = false; });
  }

  document.getElementById('fire-form').addEventListener('submit', function(event) {
    event.preventDefault();
    calculate();
  });

  document.getElementById('clear-button').addEventListener('click', resetCalculator);

  document.querySelectorAll('.field-group input').forEach(function(input) {
    input.addEventListener('input', function() {
      setFieldError(input.id, false);
    });
  });

</script>
