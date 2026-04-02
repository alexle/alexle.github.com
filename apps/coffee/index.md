---
layout: app
title: "Café au Le"
permalink: /coffee/
---

<!-- markdownlint-disable MD033 -->
<style>
  .coffee-order {
    --muted: #909498;
    --accent: #bf616a;
    --input-bg: #2d3033;
    --border: #444;
    --gold: #d4a843;
  }

  /* Option toggles (size, roast) */
  .option-toggle {
    display: flex;
    gap: 0.5rem;
    margin: 0.5rem 0;
  }

  .option-toggle button {
    flex: 1;
    padding: 0.5rem 0.8rem;
    border: 1px solid var(--border);
    border-radius: 4px;
    background: transparent;
    color: var(--muted);
    font: inherit;
    font-size: 0.85rem;
    cursor: pointer;
    transition: all 0.2s ease-out;
    text-align: center;
  }

  .option-toggle button.active,
  .option-toggle button:hover {
    border-color: var(--accent);
    color: var(--accent);
  }

  .opt-label {
    display: block;
    font-weight: 500;
    margin-bottom: 0.15rem;
  }

  .opt-detail {
    font-size: 0.75rem;
    color: var(--muted);
  }

  /* Menu card */
  .menu-card {
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1.2rem;
    margin: 1.5rem 0;
  }

  .menu-card .drink-name {
    font-size: 1.1rem;
    font-weight: 500;
    margin-bottom: 0.3rem;
  }

  .menu-card .drink-desc {
    color: var(--muted);
    font-size: 0.85rem;
    margin-bottom: 0.5rem;
  }

  .menu-card .drink-time {
    color: var(--gold);
    font-size: 0.8rem;
  }

  /* Field groups */
  .field-group { margin-bottom: 1rem; }

  .field-group label {
    display: block;
    font-size: 0.85rem;
    color: var(--muted);
    margin-bottom: 0.3rem;
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
    box-sizing: border-box;
  }

  .field-group input:focus {
    outline: none;
    border-color: var(--accent);
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

  .btn-order { background: var(--accent); color: inherit; }
  .btn-order:hover { opacity: 0.85; }
  .btn-order:disabled {
    opacity: 0.4;
    cursor: not-allowed;
  }

  .btn-back {
    background: transparent;
    border: 1px solid var(--muted) !important;
    color: var(--muted);
  }

  .btn-back:hover {
    border-color: inherit !important;
    color: inherit;
  }

  /* Cooldown */
  .cooldown-msg {
    color: var(--muted);
    font-size: 0.8rem;
    margin-top: 0.3rem;
  }

  /* State sections */
  .state { display: none; }
  .state.active { display: block; }

  /* Brewing / done states */
  .status-text {
    text-align: center;
    margin: 1rem 0;
  }

  .status-text .headline {
    font-size: 1.2rem;
    color: var(--gold);
    margin-bottom: 0.5rem;
  }

  .status-text .subtext {
    color: var(--muted);
    font-size: 0.9rem;
  }

  .confirm-summary {
    color: var(--muted);
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
  }

  .intro-text {
    color: var(--muted);
    font-size: 0.9rem;
    margin: 0 0 0.5rem;
  }

  .status-text.top { margin-top: 2rem; }
  .actions.centered { justify-content: center; }
</style>

<div class="coffee-order">

<!-- STATE: Menu -->
<div class="state active" id="state-menu">
  <p class="intro-text">Fresh pourover, brewed to order. Pick your size and I'll get started.</p>

  <div class="menu-card" id="menu-card-pourover">
    <div class="drink-name">Pourover Coffee</div>
    <div class="drink-desc">Hand-poured, freshly ground, brewed to order</div>
    <div class="drink-time">~5 min brew time</div>
  </div>

  <div class="field-group">
    <label>Size</label>
    <div class="option-toggle">
      <button onclick="setOption('size','small')" id="size-small" class="active"><span class="opt-label">Small</span><span class="opt-detail">8 oz</span></button>
      <button onclick="setOption('size','large')" id="size-large"><span class="opt-label">Large</span><span class="opt-detail">12 oz</span></button>
    </div>
  </div>

  <div class="field-group">
    <label>Roast</label>
    <div class="option-toggle">
      <button onclick="setOption('roast','light')" id="roast-light" class="active"><span class="opt-label">Light Roast</span><span class="opt-detail">Bright &amp; clean</span></button>
      <button onclick="setOption('roast','rotating')" id="roast-rotating"><span class="opt-label">Rotating Pick</span><span class="opt-detail">Monthly selection</span></button>
    </div>
  </div>

  <div class="actions">
    <button class="btn-order" id="btn-order" onclick="startOrder()">Order</button>
  </div>
  <div class="cooldown-msg" id="cooldown-msg"></div>
</div>

<!-- STATE: Confirm -->
<div class="state" id="state-confirm">
  <p class="confirm-summary" id="confirm-summary"></p>

  <div class="field-group">
    <label for="customer-name">Your name (optional)</label>
    <input type="text" id="customer-name" maxlength="30" placeholder="Who's this for?">
  </div>

  <div class="actions">
    <button class="btn-order" id="btn-place" onclick="placeOrder()">Place Order</button>
    <button class="btn-back" onclick="showState('menu')">Back</button>
  </div>
</div>

<!-- STATE: Brewing -->
<div class="state" id="state-brewing">
  <div class="status-text top">
    <div class="headline">Brewing...</div>
    <div class="subtext">Alex has been notified and will start brewing shortly.</div>
  </div>
</div>

<!-- STATE: Done -->
<div class="state" id="state-done">
  <div class="status-text top">
    <div class="headline">Order placed!</div>
    <div class="subtext" id="done-msg">Your pourover is on the way. Sit tight.</div>
  </div>
  <div class="actions centered">
    <button class="btn-order" onclick="orderAnother()">Order Another</button>
  </div>
</div>

</div>

<script>
  // --- Config ---
  var COFFEE_SUB = '{{ site.coffee_sub }}';
  var COOLDOWN_MS = 10000;
  var COOLDOWN_KEY = 'coffee_last_order';

  var SIZES = { small: '8 oz', large: '12 oz' };
  var ROASTS = { light: 'Light Roast', rotating: 'Rotating Pick' };
  var selected = { size: 'small', roast: 'light' };

  // --- State management ---
  var STATES = ['menu', 'confirm', 'brewing', 'done'];

  function showState(name) {
    STATES.forEach(function(s) {
      var el = document.getElementById('state-' + s);
      if (s === name) {
        el.classList.add('active');
      } else {
        el.classList.remove('active');
      }
    });
  }

  // --- Cooldown ---
  function canOrder() {
    var last = localStorage.getItem(COOLDOWN_KEY);
    if (!last) return true;
    return Date.now() - parseInt(last, 10) > COOLDOWN_MS;
  }

  function recordOrder() {
    localStorage.setItem(COOLDOWN_KEY, Date.now().toString());
  }

  function getRemainingCooldown() {
    var last = localStorage.getItem(COOLDOWN_KEY);
    if (!last) return 0;
    var remaining = COOLDOWN_MS - (Date.now() - parseInt(last, 10));
    return remaining > 0 ? remaining : 0;
  }

  var cooldownTimer = null;

  function updateCooldownUI() {
    var btn = document.getElementById('btn-order');
    var msg = document.getElementById('cooldown-msg');
    var remaining = getRemainingCooldown();

    if (remaining > 0) {
      btn.disabled = true;
      msg.textContent = 'You can order again in ' + Math.ceil(remaining / 1000) + 's';
      if (!cooldownTimer) {
        cooldownTimer = setInterval(function() {
          var r = getRemainingCooldown();
          if (r <= 0) {
            clearInterval(cooldownTimer);
            cooldownTimer = null;
            btn.disabled = false;
            msg.textContent = '';
          } else {
            msg.textContent = 'You can order again in ' + Math.ceil(r / 1000) + 's';
          }
        }, 1000);
      }
    } else {
      btn.disabled = false;
      msg.textContent = '';
    }
  }

  // --- Option selection ---
  function setOption(group, value) {
    selected[group] = value;
    var opts = group === 'size' ? SIZES : ROASTS;
    Object.keys(opts).forEach(function(k) {
      document.getElementById(group + '-' + k).classList.toggle('active', k === value);
    });
  }

  function capitalize(s) { return s.charAt(0).toUpperCase() + s.slice(1); }

  function orderSummary() {
    var size = capitalize(selected.size) + ' (' + SIZES[selected.size] + ')';
    return size + ' ' + ROASTS[selected.roast] + ' Pourover';
  }

  // --- Order flow ---
  function startOrder() {
    if (!canOrder()) return;
    document.getElementById('confirm-summary').innerHTML = "You're ordering: <strong>" + orderSummary() + '</strong>';
    document.getElementById('customer-name').value = '';
    showState('confirm');
  }

  function placeOrder() {
    var btn = document.getElementById('btn-place');
    btn.disabled = true;

    var name = document.getElementById('customer-name').value.trim();
    var time = new Date().toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' });
    var who = name || 'Someone';
    var body = who + ' ordered a ' + orderSummary() + ' - ' + time;

    // Send notification (fire and forget)
    fetch('https://ntfy.sh/' + COFFEE_SUB, {
      method: 'POST',
      headers: { 'Title': 'Coffee Order!' },
      body: body
    }).catch(function() {});

    recordOrder();
    showState('brewing');

    // Transition to done after 3 seconds
    setTimeout(function() {
      var doneMsg = name
        ? 'Sit tight, ' + name + '. Your drink is on the way.'
        : 'Sit tight. Your drink is on the way.';
      document.getElementById('done-msg').textContent = doneMsg;
      showState('done');
      btn.disabled = false;
    }, 3000);
  }

  function orderAnother() {
    showState('menu');
    updateCooldownUI();
  }

  // --- Init ---
  updateCooldownUI();

  // Enter key on confirm screen places order
  document.getElementById('customer-name').addEventListener('keydown', function(e) {
    if (e.key === 'Enter') placeOrder();
  });
</script>
