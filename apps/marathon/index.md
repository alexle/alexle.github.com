---
layout: app
title: "Marathon Buddy"
permalink: /marathon/
---

<!-- markdownlint-disable MD033 -->
<style>
  .marathon-app {
    --muted: #909498;
    --accent: #bf616a;
    --input-bg: #2d3033;
    --border: #444;
    --easy: #8fbcbb;
    --tempo: #d08770;
    --interval: #bf616a;
    --long: #5e81ac;
    --rest-color: #4c566a;
    --cross: #b48ead;
    --race-pace: #ebcb8b;
    --race: #a3be8c;
    --phase-base: #5e81ac;
    --phase-build: #d08770;
    --phase-peak: #bf616a;
    --phase-taper: #a3be8c;
  }

  .state { display: none; }
  .state.active { display: block; }

  .field-group { margin-bottom: 1.2rem; }
  .field-group label {
    display: block;
    font-size: 0.85rem;
    color: var(--muted);
    margin-bottom: 0.7rem;
  }
  .field-group select,
  .field-group input[type="number"],
  .field-group input[type="date"] {
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
  .field-group select {
    padding-right: 2rem;
    appearance: none;
    -webkit-appearance: none;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%23909498' stroke-width='1.5' fill='none'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 0.7rem center;
  }
  .field-group select:focus,
  .field-group input:focus {
    outline: none;
    border-color: var(--accent);
  }

  .unit-toggle {
    display: flex;
    margin-bottom: 1rem;
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

  .days-toggle {
    display: flex;
    gap: 0.5rem;
  }
  .days-toggle button {
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
  }
  .days-toggle button.active,
  .days-toggle button:hover {
    border-color: var(--accent);
    color: var(--accent);
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
  .btn-primary { background: var(--accent); color: inherit; }
  .btn-primary:hover { opacity: 0.85; }
  .btn-secondary {
    background: transparent;
    border: 1px solid var(--muted) !important;
    color: var(--muted);
  }
  .btn-secondary:hover {
    border-color: inherit !important;
    color: inherit;
  }

  .plan-summary { margin: 1.5rem 0; }
  .plan-summary h3 {
    font-size: 1.1rem;
    margin: 0 0 0.5rem;
    font-weight: 500;
  }
  .plan-summary p {
    color: var(--muted);
    font-size: 0.9rem;
    line-height: 1.6;
    margin: 0 0 1rem;
  }

  .characteristics {
    list-style: none;
    padding: 0;
    margin: 0 0 1rem;
    counter-reset: char-counter;
  }
  .characteristics li {
    counter-increment: char-counter;
    padding: 0.35rem 0;
    font-size: 0.9rem;
    line-height: 1.5;
    color: var(--muted);
  }
  .characteristics li::before {
    content: counter(char-counter) ".";
    color: var(--accent);
    font-weight: 600;
    margin-right: 0.4rem;
  }
  .characteristics .char-title {
    font-weight: 600;
    color: #d0d3d8;
  }
  .characteristics .char-title::after {
    content: ": ";
  }

  .best-for {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin: 0.5rem 0 1rem;
  }
  .best-for .tag {
    padding: 0.25rem 0.7rem;
    border-radius: 12px;
    font-size: 0.78rem;
    background: var(--input-bg);
    color: var(--muted);
    border: 1px solid var(--border);
  }

  .slider-group { margin-bottom: 1.2rem; }
  .slider-group label {
    display: flex;
    justify-content: space-between;
    font-size: 0.85rem;
    color: var(--muted);
    margin-bottom: 0.3rem;
  }
  .slider-group .slider-val {
    color: var(--accent);
    font-weight: 500;
  }
  .slider-group input[type="range"] {
    width: 100%;
    accent-color: var(--accent);
  }

  .race-date-info {
    font-size: 0.85rem;
    color: var(--muted);
    margin-top: 0.3rem;
  }
  .race-date-info strong { color: var(--accent); }

  .schedule-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
  }
  .schedule-header h3 {
    font-size: 1.05rem;
    font-weight: 500;
    margin: 0;
  }
  .expand-toggle {
    font-size: 0.8rem;
    color: var(--muted);
    cursor: pointer;
    background: none;
    border: none;
    font: inherit;
    font-size: 0.8rem;
    color: var(--accent);
  }

  .legend {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin-bottom: 1rem;
    font-size: 0.78rem;
  }
  .legend-item {
    display: flex;
    align-items: center;
    gap: 0.3rem;
    color: var(--muted);
  }
  .legend-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    display: inline-block;
  }

  .week-card {
    border: 1px solid var(--border);
    border-radius: 8px;
    margin-bottom: 0.5rem;
    overflow: hidden;
    border-left: 3px solid var(--border);
  }
  .week-card.phase-base { border-left-color: var(--phase-base); }
  .week-card.phase-build { border-left-color: var(--phase-build); }
  .week-card.phase-peak { border-left-color: var(--phase-peak); }
  .week-card.phase-taper { border-left-color: var(--phase-taper); }
  .week-card.current-week {
    border-left-color: var(--race);
    box-shadow: 0 0 0 1px var(--race);
  }

  .week-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.7rem 1rem;
    cursor: pointer;
    user-select: none;
  }
  .week-header:hover { background: rgba(255,255,255,0.03); }
  .week-left {
    display: flex;
    align-items: center;
    gap: 0.6rem;
  }
  .week-num {
    font-weight: 500;
    font-size: 0.9rem;
  }
  .week-phase {
    font-size: 0.75rem;
    padding: 0.15rem 0.5rem;
    border-radius: 3px;
    color: #fff;
    opacity: 0.85;
  }
  .week-phase.base { background: var(--phase-base); }
  .week-phase.build { background: var(--phase-build); }
  .week-phase.peak { background: var(--phase-peak); }
  .week-phase.taper { background: var(--phase-taper); }
  .week-miles {
    font-size: 0.85rem;
    color: var(--muted);
  }
  .week-chevron {
    font-size: 0.7rem;
    color: var(--muted);
    transition: transform 0.2s;
  }
  .week-card.expanded .week-chevron { transform: rotate(90deg); }

  .week-body {
    display: none;
    padding: 0 1rem 0.7rem;
  }
  .week-card.expanded .week-body { display: block; }

  .day-row {
    display: flex;
    align-items: baseline;
    padding: 0.3rem 0;
    font-size: 0.85rem;
    gap: 0.5rem;
  }
  .day-row .type-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
    margin-top: 0.3rem;
  }
  .day-name {
    width: 2.5rem;
    flex-shrink: 0;
    color: var(--muted);
    font-size: 0.8rem;
  }
  .day-dist {
    width: 3.5rem;
    flex-shrink: 0;
    font-weight: 500;
    text-align: right;
  }
  .day-desc {
    color: var(--muted);
    font-size: 0.82rem;
  }

  .intro-text {
    color: var(--muted);
    font-size: 0.9rem;
    margin: 0 0 1.5rem;
    line-height: 1.5;
  }

  .customize-header {
    font-size: 1.05rem;
    font-weight: 500;
    margin: 0 0 0.3rem;
  }
  .customize-sub {
    font-size: 0.85rem;
    color: var(--muted);
    margin: 0 0 1.5rem;
  }

  @media (max-width: 380px) {
    .day-row { flex-wrap: wrap; }
    .day-desc {
      width: 100%;
      padding-left: 3.1rem;
      margin-top: 0.1rem;
    }
  }
</style>

<div class="marathon-app">

<!-- STATE: Select -->
<div class="state active" id="state-select">
  <p class="intro-text">Browse popular marathon training plans. Pick a plan and tier to see what it's about, then generate a full week-by-week schedule with optional customization.</p>

  <div class="field-group">
    <label>Training Plan</label>
    <select id="plan-select" onchange="onPlanChange()">
      <option value="">Choose a plan...</option>
    </select>
  </div>

  <div class="field-group" id="tier-group" style="display:none;">
    <label>Tier</label>
    <select id="tier-select" onchange="onTierChange()">
      <option value="">Choose a tier...</option>
    </select>
  </div>

  <div id="plan-info" style="display:none;">
    <h3 style="font-size:1.1rem; font-weight:500; margin:0 0 1rem;" id="info-title"></h3>
    <h4 style="font-size:0.95rem; font-weight:600; color:#d0d3d8; margin:0 0 0.5rem;">Key Characteristics</h4>
    <ol class="characteristics" id="info-chars"></ol>
    <label style="font-size:0.85rem; color:var(--muted); margin-bottom:0.3rem; display:block;">Best For</label>
    <div class="best-for" id="info-bestfor"></div>
    <div class="actions">
      <button class="btn-primary" onclick="goCustomize()">View Full Plan</button>
    </div>
  </div>
</div>

<!-- STATE: Customize -->
<div class="state" id="state-customize">
  <p class="customize-header" id="cust-title"></p>
  <p class="customize-sub" id="cust-sub"></p>

  <div class="unit-toggle">
    <button id="btn-mi" class="active" onclick="setUnit('mi')">Miles</button>
    <button id="btn-km" onclick="setUnit('km')">Kilometers</button>
  </div>

  <div class="slider-group">
    <label>Peak Weekly Mileage <span class="slider-val" id="mpw-val"></span></label>
    <input type="range" id="mpw-slider" min="30" max="85" step="1" oninput="onMpwChange()">
  </div>

  <div class="field-group">
    <label>Race Date (optional)</label>
    <input type="date" id="race-date" onchange="onRaceDateChange()">
    <div class="race-date-info" id="race-date-info"></div>
  </div>

  <div class="field-group">
    <label>Days Per Week</label>
    <div class="days-toggle">
      <button onclick="setDays(5)">5</button>
      <button onclick="setDays(6)">6</button>
      <button class="active" onclick="setDays(7)">7</button>
    </div>
  </div>

  <div class="field-group">
    <label>Long Run Cap (optional)</label>
    <input type="number" id="long-cap" min="10" max="26" step="1" placeholder="e.g. 20">
  </div>

  <div class="actions">
    <button class="btn-primary" onclick="generateSchedule()">Generate Schedule</button>
    <button class="btn-secondary" onclick="showState('select')">Back</button>
  </div>
</div>

<!-- STATE: Schedule -->
<div class="state" id="state-schedule">
  <div class="schedule-header">
    <h3 id="sched-title"></h3>
    <button class="expand-toggle" onclick="toggleExpandAll()">Expand All</button>
  </div>

  <div class="legend" id="sched-legend">
    <span class="legend-item"><span class="legend-dot" style="background:var(--easy)"></span>Easy</span>
    <span class="legend-item"><span class="legend-dot" style="background:var(--tempo)"></span>Tempo</span>
    <span class="legend-item"><span class="legend-dot" style="background:var(--interval)"></span>Interval</span>
    <span class="legend-item"><span class="legend-dot" style="background:var(--long)"></span>Long</span>
    <span class="legend-item"><span class="legend-dot" style="background:var(--race-pace)"></span>Race Pace</span>
    <span class="legend-item"><span class="legend-dot" style="background:var(--cross)"></span>Cross</span>
    <span class="legend-item"><span class="legend-dot" style="background:var(--rest-color)"></span>Rest</span>
  </div>

  <div id="schedule-container"></div>

  <div class="actions">
    <button class="btn-secondary" onclick="showState('customize')">Customize</button>
    <button class="btn-secondary" onclick="showState('select')">Change Plan</button>
  </div>
</div>

</div>

<script>
var APP = { planKey: '', tierKey: '', unit: 'mi', daysPerWeek: 7, targetMPW: 0, raceDate: '', longCap: 0 };
var KM_PER_MI = 1.609344;
var STATES = ['select', 'customize', 'schedule'];
var allExpanded = false;

function showState(name) {
  STATES.forEach(function(s) {
    var el = document.getElementById('state-' + s);
    if (s === name) el.classList.add('active');
    else el.classList.remove('active');
  });
}

function setUnit(u) {
  APP.unit = u;
  document.getElementById('btn-mi').classList.toggle('active', u === 'mi');
  document.getElementById('btn-km').classList.toggle('active', u === 'km');
  updateMpwLabel();
}

function setDays(n) {
  APP.daysPerWeek = n;
  document.querySelectorAll('.days-toggle button').forEach(function(b) {
    b.classList.toggle('active', parseInt(b.textContent) === n);
  });
}

function updateMpwLabel() {
  var val = parseInt(document.getElementById('mpw-slider').value);
  var label = APP.unit === 'km' ? Math.round(val * KM_PER_MI) + ' kpw' : val + ' mpw';
  document.getElementById('mpw-val').textContent = label;
}

function onMpwChange() { updateMpwLabel(); }

function onRaceDateChange() {
  var dateStr = document.getElementById('race-date').value;
  APP.raceDate = dateStr;
  var info = document.getElementById('race-date-info');
  if (!dateStr || !APP.tierKey) { info.textContent = ''; return; }
  var tier = PLANS[APP.planKey].tiers[APP.tierKey];
  var race = new Date(dateStr + 'T00:00:00');
  var start = new Date(race);
  start.setDate(start.getDate() - tier.weeks * 7);
  var today = new Date(); today.setHours(0,0,0,0);
  var diffDays = Math.round((start - today) / 86400000);
  var startStr = start.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
  if (diffDays > 0) info.innerHTML = 'Training starts <strong>' + startStr + '</strong> (' + diffDays + ' days from now)';
  else if (diffDays === 0) info.innerHTML = 'Training starts <strong>today</strong>';
  else info.innerHTML = 'Training started <strong>' + startStr + '</strong> (week ' + Math.min(Math.ceil(-diffDays / 7) + 1, tier.weeks) + ')';
}

function D(day, type, miles, desc) { return { day: day, type: type, miles: miles, desc: desc || '' }; }
function W(num, phase, days) { return { week: num, phase: phase, days: days }; }

var TYPE_COLORS = { easy: 'var(--easy)', tempo: 'var(--tempo)', interval: 'var(--interval)', long: 'var(--long)', rest: 'var(--rest-color)', cross: 'var(--cross)', 'race-pace': 'var(--race-pace)', race: 'var(--race)' };
var DAY_NAMES = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];

var PLANS = {
  hansons: {
    name: 'Hansons Marathon Method',
    tiers: {
      beginner: {
        name: 'Beginner', weeks: 18, peakMPW: 57, maxLong: 16,
        summary: 'Built on cumulative fatigue — training on tired legs so the marathon feels manageable. The controversial cap of 16 miles for the longest run is deliberate: Hansons argues the last 10 miles of a marathon matter more than the first 16, and weekly volume builds that endurance.',
        characteristics: [
          { title: 'Cumulative Fatigue', detail: 'The defining principle. You train on tired legs so 26.2 feels manageable. No single run exceeds 16 miles — the training effect comes from accumulated fatigue across the week.' },
          { title: 'SOS Days (Something of Substance)', detail: 'Three quality sessions per week: tempo, speed/strength, and long run. Every other day is easy recovery.' },
          { title: 'No Runs Over 16 Miles', detail: 'Controversial but deliberate. The last 16 miles of a marathon matter more than the first 16. Cumulative weekly volume builds that endurance without the injury risk of 20+ mile runs.' },
          { title: 'Marathon-Pace Heavy', detail: 'Tempo runs at marathon pace are a cornerstone. You practice race effort frequently rather than relying on one weekly long run.' },
          { title: 'Progressive Structure', detail: 'Base phase (weeks 1-5), speed (weeks 6-9), strength/tempo (weeks 10-15), then taper (weeks 16-18).' }
        ],
        bestFor: ['Consistent weekly volume', 'Marathon-pace practice', 'Injury-prone runners', '40-60 mpw comfortable'],
        schedule: [
          W(1,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','easy',3,'Easy'),D('Thu','easy',4,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',3,'Easy'),D('Sun','easy',6,'Easy long')]),
          W(2,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','easy',4,'Easy'),D('Thu','easy',4,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',3,'Easy'),D('Sun','easy',7,'Easy long')]),
          W(3,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',4,'Easy'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',4,'Easy'),D('Sun','easy',8,'Easy long')]),
          W(4,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',4,'Easy'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',4,'Easy'),D('Sun','easy',8,'Easy long')]),
          W(5,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',5,'Easy'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',4,'Easy'),D('Sun','easy',10,'Easy long')]),
          W(6,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',6,'Speed: 12x400m'),D('Wed','easy',5,'Easy'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','long',10,'Long run')]),
          W(7,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',6,'Speed: 8x600m'),D('Wed','easy',5,'Easy'),D('Thu','easy',6,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','long',12,'Long run')]),
          W(8,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',7,'Speed: 6x800m'),D('Wed','easy',5,'Easy'),D('Thu','easy',6,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','long',12,'Long run')]),
          W(9,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',7,'Speed: 5x1000m'),D('Wed','easy',5,'Easy'),D('Thu','easy',6,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',6,'Easy'),D('Sun','long',14,'Long run')]),
          W(10,'Build',[D('Mon','rest',0,'Rest'),D('Tue','tempo',7,'Strength: 3x2mi @ MP'),D('Wed','easy',5,'Easy'),D('Thu','easy',6,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',6,'Easy'),D('Sun','long',14,'Long run')]),
          W(11,'Build',[D('Mon','rest',0,'Rest'),D('Tue','tempo',8,'Strength: 2x3mi @ MP'),D('Wed','easy',6,'Easy'),D('Thu','easy',6,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',6,'Easy'),D('Sun','long',15,'Long run')]),
          W(12,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',8,'Strength: 3x2mi @ MP'),D('Wed','easy',6,'Easy'),D('Thu','easy',7,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',6,'Easy'),D('Sun','long',15,'Long run')]),
          W(13,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',9,'Tempo: 4x1.5mi @ MP-10s'),D('Wed','easy',6,'Easy'),D('Thu','easy',7,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',6,'Easy'),D('Sun','long',16,'Long run')]),
          W(14,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',9,'Tempo: 2x3mi @ MP-10s'),D('Wed','easy',6,'Easy'),D('Thu','easy',7,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',6,'Easy'),D('Sun','long',16,'Long run')]),
          W(15,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',10,'Tempo: 2x4mi @ MP'),D('Wed','easy',6,'Easy'),D('Thu','easy',7,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',6,'Easy'),D('Sun','long',16,'Long run')]),
          W(16,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','tempo',8,'Tempo: 2x3mi @ MP'),D('Wed','easy',5,'Easy'),D('Thu','easy',6,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','long',14,'Long run')]),
          W(17,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','tempo',6,'Tempo: 2x2mi @ MP'),D('Wed','easy',4,'Easy'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',4,'Easy'),D('Sun','long',10,'Long run')]),
          W(18,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','easy',3,'Easy'),D('Thu','easy',3,'Shakeout'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','race',26.2,'Marathon')])
        ]
      },
      advanced: {
        name: 'Advanced', weeks: 18, peakMPW: 63, maxLong: 16,
        summary: 'Same cumulative fatigue philosophy as Beginner but with higher volume and faster paces. Adds more aggressive speed work and tempo intensities while keeping the 16-mile long run cap.',
        characteristics: [
          { title: 'Cumulative Fatigue', detail: 'Same core principle as Beginner — training on tired legs. Higher overall volume amplifies the fatigue effect.' },
          { title: 'Faster SOS Days', detail: 'Speed work includes shorter, faster intervals. Tempo runs push closer to lactate threshold rather than just marathon pace.' },
          { title: 'Higher Volume Easy Days', detail: 'Easy days bump from 5-6 miles to 7-8 miles, adding significant weekly volume without additional quality stress.' },
          { title: '16-Mile Cap Maintained', detail: 'Even the Advanced plan caps long runs at 16 miles. The difference is you arrive at the long run with more accumulated fatigue from the week.' },
          { title: 'Race-Specific Simulation', detail: 'Late-plan tempo runs simulate racing on tired legs — the closest thing to the marathon experience without running 26.2.' }
        ],
        bestFor: ['Sub-3:30 goal', 'High weekly volume', 'Experienced runners', 'BQ attempts'],
        schedule: [
          W(1,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',4,'Easy'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',4,'Easy'),D('Sun','easy',7,'Easy long')]),
          W(2,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',5,'Easy'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',4,'Easy'),D('Sun','easy',8,'Easy long')]),
          W(3,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','easy',5,'Easy'),D('Thu','easy',6,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','easy',10,'Easy long')]),
          W(4,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','easy',5,'Easy'),D('Thu','easy',6,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','easy',10,'Easy long')]),
          W(5,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','easy',6,'Easy'),D('Thu','easy',6,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','easy',12,'Easy long')]),
          W(6,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',7,'Speed: 12x400m @ 5K pace'),D('Wed','easy',6,'Easy'),D('Thu','easy',7,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',6,'Easy'),D('Sun','long',12,'Long run')]),
          W(7,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',7,'Speed: 8x600m @ 5K pace'),D('Wed','easy',6,'Easy'),D('Thu','easy',7,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',6,'Easy'),D('Sun','long',13,'Long run')]),
          W(8,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',8,'Speed: 6x800m @ 5K pace'),D('Wed','easy',6,'Easy'),D('Thu','easy',7,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',6,'Easy'),D('Sun','long',14,'Long run')]),
          W(9,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',8,'Speed: 5x1000m @ 5K pace'),D('Wed','easy',6,'Easy'),D('Thu','easy',7,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',7,'Easy'),D('Sun','long',15,'Long run')]),
          W(10,'Build',[D('Mon','rest',0,'Rest'),D('Tue','tempo',8,'Strength: 3x2mi @ MP'),D('Wed','easy',6,'Easy'),D('Thu','easy',7,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',7,'Easy'),D('Sun','long',15,'Long run')]),
          W(11,'Build',[D('Mon','rest',0,'Rest'),D('Tue','tempo',9,'Strength: 2x3mi @ MP'),D('Wed','easy',7,'Easy'),D('Thu','easy',7,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',7,'Easy'),D('Sun','long',16,'Long run')]),
          W(12,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',9,'Strength: 3x2mi @ MP-5s'),D('Wed','easy',7,'Easy'),D('Thu','easy',8,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',7,'Easy'),D('Sun','long',16,'Long run')]),
          W(13,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',10,'Tempo: 4x1.5mi @ MP-10s'),D('Wed','easy',7,'Easy'),D('Thu','easy',8,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',7,'Easy'),D('Sun','long',16,'Long run')]),
          W(14,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',10,'Tempo: 2x4mi @ MP-10s'),D('Wed','easy',7,'Easy'),D('Thu','easy',8,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',7,'Easy'),D('Sun','long',16,'Long run')]),
          W(15,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',10,'Tempo: 3x3mi @ MP'),D('Wed','easy',7,'Easy'),D('Thu','easy',8,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',7,'Easy'),D('Sun','long',16,'Long run')]),
          W(16,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','tempo',8,'Tempo: 2x3mi @ MP'),D('Wed','easy',6,'Easy'),D('Thu','easy',7,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',6,'Easy'),D('Sun','long',14,'Long run')]),
          W(17,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','tempo',7,'Tempo: 2x2mi @ MP'),D('Wed','easy',5,'Easy'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',4,'Easy'),D('Sun','long',10,'Long run')]),
          W(18,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',4,'Easy'),D('Thu','easy',3,'Shakeout'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','race',26.2,'Marathon')])
        ]
      }
    }
  },
  daniels: {
    name: 'Jack Daniels Running Formula',
    tiers: {
      '2q': {
        name: '2Q (Two Quality Days)', weeks: 18, peakMPW: 60, maxLong: 22,
        summary: 'Two hard days per week, everything else easy. All paces derived from your VDOT score. Quality sessions are carefully structured with specific pace targets — the long run is often a workout, not just easy mileage.',
        characteristics: [
          { title: 'VDOT-Based Paces', detail: 'All training paces derived from your VDOT score. Easy, Marathon, Threshold, Interval, and Repetition paces are precisely calculated — no guessing.' },
          { title: 'Two Quality Days', detail: 'Only two hard sessions per week. Every other run is easy. Quality over quantity — the hard days are carefully structured with specific pace targets.' },
          { title: 'Phase Periodization', detail: 'Four distinct phases: Foundation (easy volume), Early Quality (reps + intervals), Transition Quality (threshold + cruise intervals), Final Quality (marathon-specific).' },
          { title: 'Long Run Workouts', detail: 'Long runs often include quality segments — e.g., 15 miles with middle 8 at marathon pace. The long run is a quality session, not just a slog.' },
          { title: 'Flexible Weekly Structure', detail: 'Daniels prescribes effort percentages, not rigid daily schedules. You distribute volume across available days.' }
        ],
        bestFor: ['Pace-driven runners', 'Science-based approach', 'Flexible scheduling', 'Experience with structured training'],
        schedule: [
          W(1,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',6,'Easy'),D('Thu','easy',5,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',12,'Easy long')]),
          W(2,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',7,'Easy'),D('Thu','easy',5,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',13,'Easy long')]),
          W(3,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','easy',7,'Easy'),D('Thu','easy',6,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',14,'Easy long')]),
          W(4,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',6,'Easy'),D('Thu','easy',5,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',12,'Recovery long')]),
          W(5,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',8,'Q1: 6x800m @ I pace w/ jog'),D('Wed','easy',6,'Easy'),D('Thu','easy',6,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',15,'Q2: Long w/ 4mi @ MP')]),
          W(6,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',8,'Q1: 5x1000m @ I pace'),D('Wed','easy',6,'Easy'),D('Thu','easy',6,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',16,'Q2: Long w/ 6mi @ MP')]),
          W(7,'Build',[D('Mon','rest',0,'Rest'),D('Tue','tempo',9,'Q1: 3x2mi @ T pace'),D('Wed','easy',6,'Easy'),D('Thu','easy',6,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',16,'Q2: Long w/ 6mi @ MP')]),
          W(8,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','easy',6,'Easy'),D('Thu','easy',5,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',13,'Recovery long')]),
          W(9,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',9,'Q1: 4x1200m @ I pace'),D('Wed','easy',6,'Easy'),D('Thu','easy',7,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',17,'Q2: Long w/ 8mi @ MP')]),
          W(10,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',10,'Q1: 4x2mi @ T pace'),D('Wed','easy',6,'Easy'),D('Thu','easy',7,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',18,'Q2: Long w/ 10mi @ MP')]),
          W(11,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',9,'Q1: 5x1000m @ I pace'),D('Wed','easy',6,'Easy'),D('Thu','easy',7,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',20,'Q2: Long w/ 10mi @ MP')]),
          W(12,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','easy',6,'Easy'),D('Thu','easy',5,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',14,'Recovery long')]),
          W(13,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',10,'Q1: 3x3mi @ T pace'),D('Wed','easy',6,'Easy'),D('Thu','easy',7,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',20,'Q2: Long w/ 12mi @ MP')]),
          W(14,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',9,'Q1: 6x1000m @ I pace'),D('Wed','easy',6,'Easy'),D('Thu','easy',7,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',18,'Q2: Long w/ 8mi @ MP')]),
          W(15,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','race-pace',10,'Q1: 5x2mi @ MP'),D('Wed','easy',5,'Easy'),D('Thu','easy',6,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',17,'Q2: Endurance')]),
          W(16,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','tempo',8,'Q1: 2x2mi @ T pace'),D('Wed','easy',5,'Easy'),D('Thu','easy',5,'Easy'),D('Fri','easy',4,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',14,'Q2: Long w/ 4mi @ MP')]),
          W(17,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','tempo',6,'Q1: 2x1.5mi @ T pace'),D('Wed','easy',4,'Easy'),D('Thu','easy',5,'Easy'),D('Fri','easy',4,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',10,'Easy long')]),
          W(18,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','easy',4,'Easy'),D('Thu','easy',3,'Shakeout'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','race',26.2,'Marathon')])
        ]
      },
      '4wk': {
        name: '4-Week Cycle', weeks: 16, peakMPW: 65, maxLong: 22,
        summary: 'Structured in repeating 4-week mesocycles with progressive overload. Each cycle builds on the previous one with increasing intensity. More structured than the 2Q plan with specific daily assignments.',
        characteristics: [
          { title: 'VDOT-Based Paces', detail: 'Same precision pacing as 2Q — all workouts calibrated to your current fitness level through VDOT.' },
          { title: '4-Week Mesocycles', detail: 'Each 4-week block has a specific focus: build, build, peak, recovery. Systematic progression with built-in deloads.' },
          { title: 'More Structured Days', detail: 'Unlike the flexible 2Q plan, this prescribes specific workouts for specific days. Less flexibility but more guidance.' },
          { title: 'Higher Peak Mileage', detail: 'Peaks at 65 mpw versus 60 for 2Q. More volume overall, suited for runners who thrive on mileage.' },
          { title: 'Phase Periodization', detail: 'Same four phases as 2Q but compressed into 16 weeks with tighter mesocycle structure.' }
        ],
        bestFor: ['Higher mileage tolerance', 'Prefer rigid structure', 'Experienced marathoners', 'Time-goal focused'],
        schedule: [
          W(1,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','easy',7,'Easy'),D('Thu','easy',6,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',13,'Easy long')]),
          W(2,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','easy',8,'Easy'),D('Thu','easy',6,'Easy'),D('Fri','easy',6,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',14,'Easy long')]),
          W(3,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',7,'Easy'),D('Wed','easy',8,'Easy'),D('Thu','easy',7,'Easy'),D('Fri','easy',6,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',15,'Easy long')]),
          W(4,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',6,'Easy'),D('Thu','easy',5,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',12,'Recovery long')]),
          W(5,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',8,'6x800m @ I pace'),D('Wed','easy',7,'Easy'),D('Thu','tempo',8,'3x2mi @ T pace'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',16,'Long w/ 4mi @ MP')]),
          W(6,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',9,'5x1000m @ I pace'),D('Wed','easy',7,'Easy'),D('Thu','tempo',9,'2x3mi @ T pace'),D('Fri','easy',6,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',17,'Long w/ 6mi @ MP')]),
          W(7,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',9,'4x1200m @ I pace'),D('Wed','easy',8,'Easy'),D('Thu','tempo',9,'4x2mi @ T pace'),D('Fri','easy',6,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',18,'Long w/ 8mi @ MP')]),
          W(8,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','easy',7,'Easy'),D('Thu','easy',6,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',14,'Recovery long')]),
          W(9,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',9,'5x1000m @ I pace'),D('Wed','easy',8,'Easy'),D('Thu','tempo',10,'3x3mi @ T pace'),D('Fri','easy',6,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',20,'Long w/ 10mi @ MP')]),
          W(10,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',10,'4x1600m @ I pace'),D('Wed','easy',8,'Easy'),D('Thu','tempo',10,'2x4mi @ T pace'),D('Fri','easy',6,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',22,'Long w/ 12mi @ MP')]),
          W(11,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','race-pace',10,'5x2mi @ MP'),D('Wed','easy',8,'Easy'),D('Thu','tempo',9,'3x2mi @ T pace'),D('Fri','easy',6,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',20,'Long w/ 10mi @ MP')]),
          W(12,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','easy',7,'Easy'),D('Thu','easy',6,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',14,'Recovery long')]),
          W(13,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','tempo',8,'2x3mi @ T pace'),D('Wed','easy',6,'Easy'),D('Thu','race-pace',8,'4x1.5mi @ MP'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',16,'Long w/ 6mi @ MP')]),
          W(14,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','tempo',7,'2x2mi @ T pace'),D('Wed','easy',5,'Easy'),D('Thu','easy',5,'Easy'),D('Fri','easy',4,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',12,'Easy long')]),
          W(15,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','tempo',6,'2x1.5mi @ T pace'),D('Wed','easy',4,'Easy'),D('Thu','easy',4,'Easy'),D('Fri','easy',3,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',8,'Easy long')]),
          W(16,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','easy',4,'Easy'),D('Thu','easy',3,'Shakeout'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','race',26.2,'Marathon')])
        ]
      }
    }
  },
  higdon: {
    name: "Hal Higdon",
    tiers: {
      novice1: {
        name: 'Novice 1', weeks: 18, peakMPW: 40, maxLong: 20,
        summary: 'The most popular first-marathon plan in the world. The goal is completion, not a time target. Simple structure with gradual long run progression, cross-training days, and generous rest.',
        characteristics: [
          { title: 'Finish-Line Focus', detail: 'The goal is completion, not a time target. Run by feel and effort — the schedule tells you how far, not how fast.' },
          { title: 'Gradual Long Run Progression', detail: 'Long runs increase by 1-2 miles per week, reaching 20 miles, with step-back weeks every 3rd week for recovery.' },
          { title: 'Cross-Training Days', detail: 'Dedicated cross-training days (bike, swim, yoga) to build fitness without the impact stress of more running.' },
          { title: 'Simple Structure', detail: 'No pace prescriptions. Three run days, one cross-train day, one long run, two rest days. Straightforward and approachable.' },
          { title: 'Rest-Heavy', detail: 'Multiple rest days per week. Recovery is built into the DNA of the program rather than being an afterthought.' }
        ],
        bestFor: ['First marathoners', 'Low injury risk', 'Minimal time commitment', '3-4 days/week runners'],
        schedule: [
          W(1,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',3,'Easy'),D('Wed','cross',0,'Cross-train'),D('Thu','easy',3,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','long',6,'Long run')]),
          W(2,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',3,'Easy'),D('Wed','cross',0,'Cross-train'),D('Thu','easy',3,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','long',7,'Long run')]),
          W(3,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',3.5,'Easy'),D('Wed','cross',0,'Cross-train'),D('Thu','easy',3.5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','long',8,'Long run')]),
          W(4,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',3.5,'Easy'),D('Wed','cross',0,'Cross-train'),D('Thu','easy',3.5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','long',6,'Step-back')]),
          W(5,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','cross',0,'Cross-train'),D('Thu','easy',4,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','long',9,'Long run')]),
          W(6,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','cross',0,'Cross-train'),D('Thu','easy',4,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','long',10,'Long run')]),
          W(7,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',4.5,'Easy'),D('Wed','cross',0,'Cross-train'),D('Thu','easy',4.5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','long',11,'Long run')]),
          W(8,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',4.5,'Easy'),D('Wed','cross',0,'Cross-train'),D('Thu','easy',4.5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','long',8,'Step-back')]),
          W(9,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','cross',0,'Cross-train'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','long',13,'Long run')]),
          W(10,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','cross',0,'Cross-train'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','long',14,'Long run')]),
          W(11,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','cross',0,'Cross-train'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','long',15,'Long run')]),
          W(12,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','cross',0,'Cross-train'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','long',10,'Step-back')]),
          W(13,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','cross',0,'Cross-train'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','long',17,'Long run')]),
          W(14,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','cross',0,'Cross-train'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','long',18,'Long run')]),
          W(15,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','cross',0,'Cross-train'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','long',20,'Long run')]),
          W(16,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','cross',0,'Cross-train'),D('Thu','easy',4,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','long',12,'Taper long')]),
          W(17,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','cross',0,'Cross-train'),D('Thu','easy',3,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','long',8,'Taper long')]),
          W(18,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',3,'Easy'),D('Wed','rest',0,'Rest'),D('Thu','easy',2,'Shakeout'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','race',26.2,'Marathon')])
        ]
      },
      novice2: {
        name: 'Novice 2', weeks: 18, peakMPW: 43, maxLong: 20,
        summary: 'A step up from Novice 1 with an extra running day and slightly more mileage. Still completion-focused but begins to introduce the idea of pace variety.',
        characteristics: [
          { title: 'Extra Running Day', detail: 'Four run days instead of three. The added easy day builds more aerobic base without adding intensity.' },
          { title: 'Pace Awareness', detail: 'Introduces the concept of running some days faster than others, though still effort-based rather than pace-prescribed.' },
          { title: 'Same Long Run Progression', detail: 'Identical long run schedule to Novice 1 — peaks at 20 miles with step-back weeks.' },
          { title: 'Reduced Cross-Training', detail: 'Cross-training drops to make room for the extra run day. Still one cross-train day per week.' }
        ],
        bestFor: ['Second marathon', 'Comfortable running 4 days/week', 'Completion + modest time goal', 'Building from Novice 1'],
        schedule: [
          W(1,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',3,'Easy'),D('Wed','easy',3,'Easy'),D('Thu','cross',0,'Cross-train'),D('Fri','easy',3,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',6,'Long run')]),
          W(2,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',3.5,'Easy'),D('Wed','easy',3,'Easy'),D('Thu','cross',0,'Cross-train'),D('Fri','easy',3.5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',7,'Long run')]),
          W(3,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','easy',3.5,'Easy'),D('Thu','cross',0,'Cross-train'),D('Fri','easy',4,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',8,'Long run')]),
          W(4,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','easy',3,'Easy'),D('Thu','cross',0,'Cross-train'),D('Fri','easy',3,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',6,'Step-back')]),
          W(5,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','easy',4,'Easy'),D('Thu','cross',0,'Cross-train'),D('Fri','easy',4,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',10,'Long run')]),
          W(6,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',4.5,'Easy'),D('Wed','easy',4,'Easy'),D('Thu','cross',0,'Cross-train'),D('Fri','easy',4.5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',11,'Long run')]),
          W(7,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',4,'Easy'),D('Thu','cross',0,'Cross-train'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',12,'Long run')]),
          W(8,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',4.5,'Easy'),D('Wed','easy',4,'Easy'),D('Thu','cross',0,'Cross-train'),D('Fri','easy',4,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',9,'Step-back')]),
          W(9,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',5,'Easy'),D('Thu','cross',0,'Cross-train'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',14,'Long run')]),
          W(10,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',5,'Easy'),D('Thu','cross',0,'Cross-train'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',15,'Long run')]),
          W(11,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',5,'Easy'),D('Thu','cross',0,'Cross-train'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',16,'Long run')]),
          W(12,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',4,'Easy'),D('Thu','cross',0,'Cross-train'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',12,'Step-back')]),
          W(13,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',5,'Easy'),D('Thu','cross',0,'Cross-train'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',18,'Long run')]),
          W(14,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',5,'Easy'),D('Thu','cross',0,'Cross-train'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',19,'Long run')]),
          W(15,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',5,'Easy'),D('Thu','cross',0,'Cross-train'),D('Fri','easy',5,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',20,'Long run')]),
          W(16,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',4,'Easy'),D('Thu','cross',0,'Cross-train'),D('Fri','easy',4,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',12,'Taper long')]),
          W(17,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','easy',3,'Easy'),D('Thu','cross',0,'Cross-train'),D('Fri','easy',3,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',8,'Taper long')]),
          W(18,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',3,'Easy'),D('Wed','easy',2,'Easy'),D('Thu','rest',0,'Rest'),D('Fri','easy',2,'Shakeout'),D('Sat','rest',0,'Rest'),D('Sun','race',26.2,'Marathon')])
        ]
      },
      int1: {
        name: 'Intermediate 1', weeks: 18, peakMPW: 50, maxLong: 20,
        summary: 'Adds tempo runs to the mix. Five running days per week with one quality session. The bridge between "just finish" and "finish with a time goal."',
        characteristics: [
          { title: 'Tempo Run Introduction', detail: 'One tempo run per week at a "comfortably hard" effort. The first real quality session in the Higdon progression.' },
          { title: 'Five Running Days', detail: 'Five days of running plus one cross-train and one rest day. Meaningful jump in weekly volume.' },
          { title: 'Long Run Progression', detail: 'Same 20-mile peak but with more mid-week volume supporting it. The long run is better supported by overall fitness.' },
          { title: 'Pace-Guided', detail: 'Introduces target paces for tempo runs while keeping easy days truly easy.' }
        ],
        bestFor: ['Time goal runners', 'Comfortable at 30+ mpw', 'Ready for quality sessions', 'Building toward BQ'],
        schedule: [
          W(1,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','tempo',5,'Tempo 3mi'),D('Thu','easy',4,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','cross',0,'Cross-train'),D('Sun','long',8,'Long run')]),
          W(2,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','tempo',5,'Tempo 3mi'),D('Thu','easy',4,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','cross',0,'Cross-train'),D('Sun','long',9,'Long run')]),
          W(3,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','tempo',5,'Tempo 3mi'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','cross',0,'Cross-train'),D('Sun','long',10,'Long run')]),
          W(4,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','tempo',5,'Tempo 3mi'),D('Thu','easy',4,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','cross',0,'Cross-train'),D('Sun','long',7,'Step-back')]),
          W(5,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','tempo',6,'Tempo 4mi'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','cross',0,'Cross-train'),D('Sun','long',12,'Long run')]),
          W(6,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','tempo',6,'Tempo 4mi'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','cross',0,'Cross-train'),D('Sun','long',13,'Long run')]),
          W(7,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','cross',0,'Cross-train'),D('Sun','long',14,'Long run')]),
          W(8,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','tempo',6,'Tempo 4mi'),D('Thu','easy',4,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','cross',0,'Cross-train'),D('Sun','long',10,'Step-back')]),
          W(9,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','cross',0,'Cross-train'),D('Sun','long',16,'Long run')]),
          W(10,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','cross',0,'Cross-train'),D('Sun','long',17,'Long run')]),
          W(11,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',6,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','cross',0,'Cross-train'),D('Sun','long',18,'Long run')]),
          W(12,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','tempo',6,'Tempo 4mi'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','cross',0,'Cross-train'),D('Sun','long',13,'Step-back')]),
          W(13,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',6,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','cross',0,'Cross-train'),D('Sun','long',19,'Long run')]),
          W(14,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',6,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','cross',0,'Cross-train'),D('Sun','long',20,'Long run')]),
          W(15,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','cross',0,'Cross-train'),D('Sun','long',20,'Long run')]),
          W(16,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','tempo',6,'Tempo 3mi'),D('Thu','easy',4,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','cross',0,'Cross-train'),D('Sun','long',12,'Taper long')]),
          W(17,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','tempo',5,'Tempo 2mi'),D('Thu','easy',3,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','long',8,'Taper long')]),
          W(18,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',3,'Easy'),D('Wed','easy',2,'Easy'),D('Thu','easy',2,'Shakeout'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','race',26.2,'Marathon')])
        ]
      },
      int2: {
        name: 'Intermediate 2', weeks: 18, peakMPW: 52, maxLong: 20,
        summary: 'Builds on Intermediate 1 with added hill work and longer tempo runs. The most popular Higdon plan for experienced recreational runners targeting a specific time.',
        characteristics: [
          { title: 'Hill Training', detail: 'Dedicated hill repeat sessions to build power, running economy, and mental toughness.' },
          { title: 'Longer Tempo Runs', detail: 'Tempo runs extend to 5-7 miles, building sustained lactate threshold endurance.' },
          { title: 'Race-Pace Long Runs', detail: 'Some long runs include miles at marathon goal pace — bridging endurance and race-specific fitness.' },
          { title: 'Slightly Higher Volume', detail: 'Peaks at 52 mpw versus 50 for Int 1. The extra miles come from longer mid-week runs.' }
        ],
        bestFor: ['Experienced recreational runners', 'Specific time goal', 'Moderate mileage preference', 'BQ attempts'],
        schedule: [
          W(1,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','tempo',5,'Tempo 3mi'),D('Thu','easy',4,'Easy'),D('Fri','easy',4,'Easy'),D('Sat','cross',0,'Cross-train'),D('Sun','long',8,'Long run')]),
          W(2,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','tempo',6,'Tempo 4mi'),D('Thu','easy',5,'Easy'),D('Fri','easy',4,'Easy'),D('Sat','cross',0,'Cross-train'),D('Sun','long',9,'Long run')]),
          W(3,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','tempo',6,'Tempo 4mi'),D('Thu','easy',5,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','cross',0,'Cross-train'),D('Sun','long',10,'Long run')]),
          W(4,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','tempo',5,'Tempo 3mi'),D('Thu','easy',4,'Easy'),D('Fri','easy',4,'Easy'),D('Sat','cross',0,'Cross-train'),D('Sun','long',7,'Step-back')]),
          W(5,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',5,'Hill repeats 6x90s'),D('Wed','tempo',6,'Tempo 4mi'),D('Thu','easy',5,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','cross',0,'Cross-train'),D('Sun','long',12,'Long run')]),
          W(6,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',5,'Hill repeats 6x90s'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',5,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','cross',0,'Cross-train'),D('Sun','long',13,'Long run')]),
          W(7,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',6,'Hill repeats 8x90s'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',6,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','cross',0,'Cross-train'),D('Sun','long',14,'Long run')]),
          W(8,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','tempo',5,'Tempo 3mi'),D('Thu','easy',5,'Easy'),D('Fri','easy',4,'Easy'),D('Sat','cross',0,'Cross-train'),D('Sun','long',10,'Step-back')]),
          W(9,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',6,'800m repeats 5x800m'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',6,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','cross',0,'Cross-train'),D('Sun','long',16,'Long run')]),
          W(10,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',6,'800m repeats 6x800m'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',6,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','cross',0,'Cross-train'),D('Sun','long',17,'Long run w/ 4mi @ MP')]),
          W(11,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',6,'1mi repeats 4x1mi'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',6,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','cross',0,'Cross-train'),D('Sun','long',18,'Long run w/ 6mi @ MP')]),
          W(12,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','tempo',5,'Tempo 3mi'),D('Thu','easy',5,'Easy'),D('Fri','easy',4,'Easy'),D('Sat','cross',0,'Cross-train'),D('Sun','long',13,'Step-back')]),
          W(13,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',7,'1mi repeats 5x1mi'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',6,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','cross',0,'Cross-train'),D('Sun','long',19,'Long run w/ 6mi @ MP')]),
          W(14,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',7,'800m repeats 6x800m'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',6,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','cross',0,'Cross-train'),D('Sun','long',20,'Long run w/ 8mi @ MP')]),
          W(15,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',6,'1mi repeats 4x1mi'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',5,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','cross',0,'Cross-train'),D('Sun','long',20,'Long run w/ 8mi @ MP')]),
          W(16,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','tempo',6,'Tempo 4mi'),D('Thu','easy',5,'Easy'),D('Fri','easy',4,'Easy'),D('Sat','cross',0,'Cross-train'),D('Sun','long',12,'Taper long')]),
          W(17,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','tempo',5,'Tempo 3mi'),D('Thu','easy',4,'Easy'),D('Fri','easy',3,'Easy'),D('Sat','rest',0,'Rest'),D('Sun','long',8,'Taper long')]),
          W(18,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',3,'Easy'),D('Wed','easy',3,'Easy'),D('Thu','easy',2,'Shakeout'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','race',26.2,'Marathon')])
        ]
      },
      adv1: {
        name: 'Advanced 1', weeks: 18, peakMPW: 55, maxLong: 20,
        summary: 'For competitive runners who want structure without extreme mileage. Adds interval work and race-pace segments to long runs.',
        characteristics: [
          { title: 'Interval Sessions', detail: 'Track-style interval workouts (800m-1600m repeats) to develop VO2max and running economy.' },
          { title: 'Race-Pace Long Runs', detail: 'Long runs frequently include 4-8 miles at marathon goal pace. These are the key workouts of the plan.' },
          { title: 'Six Running Days', detail: 'Six days of running with one rest day. Cross-training is optional and supplementary.' },
          { title: 'Multiple Quality Sessions', detail: 'Two quality days per week: one speed/interval session and one tempo or race-pace session.' }
        ],
        bestFor: ['Competitive age-groupers', 'Sub-3:30 goal', '6 days/week runners', 'Speed + endurance balance'],
        schedule: [
          W(1,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','tempo',5,'Tempo 3mi'),D('Thu','easy',5,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','easy',5,'Easy'),D('Sun','long',10,'Long run')]),
          W(2,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','tempo',6,'Tempo 4mi'),D('Thu','easy',5,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','easy',5,'Easy'),D('Sun','long',11,'Long run')]),
          W(3,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','tempo',6,'Tempo 4mi'),D('Thu','easy',5,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','easy',5,'Easy'),D('Sun','long',12,'Long run')]),
          W(4,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','tempo',5,'Tempo 3mi'),D('Thu','easy',5,'Easy'),D('Fri','easy',4,'Easy'),D('Sat','easy',4,'Easy'),D('Sun','long',8,'Step-back')]),
          W(5,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',6,'6x800m'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',5,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','easy',5,'Easy'),D('Sun','long',13,'Long run')]),
          W(6,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',6,'6x800m'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',6,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','easy',5,'Easy'),D('Sun','long',14,'Long run')]),
          W(7,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',7,'8x800m'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',6,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','easy',6,'Easy'),D('Sun','long',15,'Long run')]),
          W(8,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','tempo',5,'Tempo 3mi'),D('Thu','easy',5,'Easy'),D('Fri','easy',4,'Easy'),D('Sat','easy',4,'Easy'),D('Sun','long',10,'Step-back')]),
          W(9,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',7,'5x1mi'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',6,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','easy',6,'Easy'),D('Sun','long',17,'Long run w/ 4mi @ MP')]),
          W(10,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',7,'5x1mi'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',6,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','easy',6,'Easy'),D('Sun','long',18,'Long run w/ 6mi @ MP')]),
          W(11,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',7,'6x1mi'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',6,'Easy'),D('Fri','easy',6,'Easy'),D('Sat','easy',6,'Easy'),D('Sun','long',19,'Long run w/ 8mi @ MP')]),
          W(12,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','tempo',5,'Tempo 3mi'),D('Thu','easy',5,'Easy'),D('Fri','easy',4,'Easy'),D('Sat','easy',5,'Easy'),D('Sun','long',13,'Step-back')]),
          W(13,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',7,'5x1mi'),D('Wed','tempo',8,'Tempo 6mi'),D('Thu','easy',6,'Easy'),D('Fri','easy',6,'Easy'),D('Sat','easy',6,'Easy'),D('Sun','long',20,'Long run w/ 8mi @ MP')]),
          W(14,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',7,'6x800m'),D('Wed','tempo',8,'Tempo 6mi'),D('Thu','easy',6,'Easy'),D('Fri','easy',6,'Easy'),D('Sat','easy',6,'Easy'),D('Sun','long',20,'Long run w/ 10mi @ MP')]),
          W(15,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',6,'5x1mi'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',6,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','easy',6,'Easy'),D('Sun','long',20,'Long run w/ 10mi @ MP')]),
          W(16,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','interval',5,'3x1mi'),D('Wed','tempo',6,'Tempo 4mi'),D('Thu','easy',5,'Easy'),D('Fri','easy',4,'Easy'),D('Sat','easy',5,'Easy'),D('Sun','long',14,'Taper long')]),
          W(17,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','tempo',5,'Tempo 3mi'),D('Thu','easy',4,'Easy'),D('Fri','easy',3,'Easy'),D('Sat','easy',4,'Easy'),D('Sun','long',8,'Taper long')]),
          W(18,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','easy',3,'Easy'),D('Thu','easy',3,'Shakeout'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','race',26.2,'Marathon')])
        ]
      },
      adv2: {
        name: 'Advanced 2', weeks: 18, peakMPW: 60, maxLong: 20,
        summary: 'Higdon\'s most demanding plan. Higher volume with three quality sessions per week. For experienced runners who can handle intensity on top of 50-60 mpw.',
        characteristics: [
          { title: 'Three Quality Sessions', detail: 'Interval, tempo, and race-pace long run in the same week. Significant training stress requires careful recovery management.' },
          { title: 'Highest Higdon Volume', detail: 'Peaks at 60 mpw — the ceiling of the Higdon system. Easy days are 7-9 miles.' },
          { title: 'Advanced Periodization', detail: 'Phases shift from aerobic base to VO2max development to marathon-specific work over the 18 weeks.' },
          { title: 'Aggressive Long Runs', detail: 'Long runs reach 20 miles with significant race-pace segments. These are the hardest workouts in the plan.' }
        ],
        bestFor: ['Experienced marathoners', 'Sub-3:15 goal', 'High volume tolerance', 'Three quality days/week'],
        schedule: [
          W(1,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','tempo',6,'Tempo 4mi'),D('Thu','easy',6,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','easy',6,'Easy'),D('Sun','long',11,'Long run')]),
          W(2,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',6,'Easy'),D('Fri','easy',6,'Easy'),D('Sat','easy',6,'Easy'),D('Sun','long',12,'Long run')]),
          W(3,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',7,'Easy'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',6,'Easy'),D('Fri','easy',6,'Easy'),D('Sat','easy',7,'Easy'),D('Sun','long',13,'Long run')]),
          W(4,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','tempo',5,'Tempo 3mi'),D('Thu','easy',5,'Easy'),D('Fri','easy',4,'Easy'),D('Sat','easy',5,'Easy'),D('Sun','long',9,'Step-back')]),
          W(5,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',7,'8x800m'),D('Wed','tempo',8,'Tempo 6mi'),D('Thu','easy',6,'Easy'),D('Fri','easy',6,'Easy'),D('Sat','easy',7,'Easy'),D('Sun','long',15,'Long run')]),
          W(6,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',7,'6x1mi'),D('Wed','tempo',8,'Tempo 6mi'),D('Thu','easy',7,'Easy'),D('Fri','easy',6,'Easy'),D('Sat','easy',7,'Easy'),D('Sun','long',16,'Long run w/ 4mi @ MP')]),
          W(7,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',8,'5x1200m'),D('Wed','tempo',8,'Tempo 6mi'),D('Thu','easy',7,'Easy'),D('Fri','easy',6,'Easy'),D('Sat','easy',7,'Easy'),D('Sun','long',17,'Long run w/ 6mi @ MP')]),
          W(8,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','tempo',6,'Tempo 4mi'),D('Thu','easy',5,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','easy',5,'Easy'),D('Sun','long',12,'Step-back')]),
          W(9,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',8,'6x1mi'),D('Wed','tempo',9,'Tempo 7mi'),D('Thu','easy',7,'Easy'),D('Fri','easy',6,'Easy'),D('Sat','easy',7,'Easy'),D('Sun','long',18,'Long run w/ 8mi @ MP')]),
          W(10,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',8,'5x1200m'),D('Wed','tempo',9,'Tempo 7mi'),D('Thu','easy',7,'Easy'),D('Fri','easy',6,'Easy'),D('Sat','easy',7,'Easy'),D('Sun','long',19,'Long run w/ 8mi @ MP')]),
          W(11,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',8,'6x1mi'),D('Wed','tempo',9,'Tempo 7mi'),D('Thu','easy',7,'Easy'),D('Fri','easy',7,'Easy'),D('Sat','easy',7,'Easy'),D('Sun','long',20,'Long run w/ 10mi @ MP')]),
          W(12,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','tempo',6,'Tempo 4mi'),D('Thu','easy',5,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','easy',5,'Easy'),D('Sun','long',13,'Step-back')]),
          W(13,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',8,'6x1mi'),D('Wed','tempo',9,'Tempo 7mi'),D('Thu','easy',7,'Easy'),D('Fri','easy',7,'Easy'),D('Sat','easy',8,'Easy'),D('Sun','long',20,'Long run w/ 10mi @ MP')]),
          W(14,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',7,'5x1200m'),D('Wed','tempo',8,'Tempo 6mi'),D('Thu','easy',7,'Easy'),D('Fri','easy',6,'Easy'),D('Sat','easy',7,'Easy'),D('Sun','long',20,'Long run w/ 12mi @ MP')]),
          W(15,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',7,'4x1mi'),D('Wed','tempo',7,'Tempo 5mi'),D('Thu','easy',6,'Easy'),D('Fri','easy',6,'Easy'),D('Sat','easy',7,'Easy'),D('Sun','long',18,'Dress rehearsal 10mi @ MP')]),
          W(16,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','interval',6,'3x1mi'),D('Wed','tempo',6,'Tempo 4mi'),D('Thu','easy',5,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','easy',5,'Easy'),D('Sun','long',14,'Taper long')]),
          W(17,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','tempo',5,'Tempo 3mi'),D('Thu','easy',4,'Easy'),D('Fri','easy',4,'Easy'),D('Sat','easy',4,'Easy'),D('Sun','long',10,'Taper long')]),
          W(18,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',4,'Easy'),D('Wed','easy',3,'Easy'),D('Thu','easy',3,'Shakeout'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','race',26.2,'Marathon')])
        ]
      }
    }
  },
  pfitzinger: {
    name: 'Pfitzinger',
    tiers: {
      '18_55': {
        name: '18/55 (18 weeks, 55 mpw)', weeks: 18, peakMPW: 55, maxLong: 20,
        summary: 'The entry point to Pfitzinger\'s system. Lactate threshold development is the foundation — all paces calculated from LT. Features the signature medium-long run mid-week and aggressive long runs with marathon-pace finishes.',
        characteristics: [
          { title: 'Lactate Threshold Focus', detail: 'LT development is the foundation. All paces calculated from lactate threshold. Heavy emphasis on tempo and threshold runs to raise the ceiling on sustainable pace.' },
          { title: 'Medium-Long Runs', detail: 'A unique mid-week run of 11-15 miles that bridges easy days and the weekend long run. This is Pfitzinger\'s signature — other plans lack this stimulus.' },
          { title: 'Aggressive Long Runs', detail: 'Long runs reach 20 miles and often finish with miles at marathon pace. The long run is a workout, not a slog.' },
          { title: 'VO2max Intervals', detail: 'Shorter, faster intervals (800m-1600m at 5K pace) to develop oxygen uptake. Placed strategically in Build and Peak phases.' },
          { title: 'Structured Recovery', detail: 'Every 3rd or 4th week drops volume 20-25% for adaptation. Recovery is periodized, not random.' }
        ],
        bestFor: ['Experienced runners', 'Sub-3:30 goal', 'Threshold-focused', 'Can handle 50+ mpw'],
        schedule: [
          W(1,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',7,'Aerobic'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',8,'Medium-long'),D('Sun','long',12,'Endurance')]),
          W(2,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',8,'Aerobic'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',9,'Medium-long'),D('Sun','long',13,'Endurance')]),
          W(3,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','easy',8,'Aerobic'),D('Thu','easy',6,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',9,'Medium-long'),D('Sun','long',14,'Endurance')]),
          W(4,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',7,'Aerobic'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',8,'Medium-long'),D('Sun','long',12,'Recovery week')]),
          W(5,'Build',[D('Mon','rest',0,'Rest'),D('Tue','tempo',8,'Lactate threshold 4mi @ LT'),D('Wed','easy',5,'Recovery'),D('Thu','easy',9,'Medium-long'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','long',15,'Endurance')]),
          W(6,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',8,'VO2max 5x1000m @ 5K pace'),D('Wed','easy',5,'Recovery'),D('Thu','easy',10,'Medium-long'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','long',16,'Endurance w/ 8mi @ MP')]),
          W(7,'Build',[D('Mon','rest',0,'Rest'),D('Tue','tempo',9,'Lactate threshold 5mi @ LT'),D('Wed','easy',5,'Recovery'),D('Thu','easy',11,'Medium-long'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','long',17,'Endurance')]),
          W(8,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','easy',8,'Aerobic'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',8,'Medium-long'),D('Sun','long',13,'Recovery week')]),
          W(9,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',9,'VO2max 6x1000m @ 5K pace'),D('Wed','easy',5,'Recovery'),D('Thu','easy',11,'Medium-long'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','long',18,'Endurance w/ 10mi @ MP')]),
          W(10,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',10,'Lactate threshold 6mi @ LT'),D('Wed','easy',5,'Recovery'),D('Thu','easy',12,'Medium-long'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','long',19,'Endurance')]),
          W(11,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',9,'VO2max 6x1000m @ 5K pace'),D('Wed','easy',5,'Recovery'),D('Thu','easy',12,'Medium-long'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','long',20,'Long w/ 12mi @ MP')]),
          W(12,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','easy',8,'Aerobic'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',8,'Medium-long'),D('Sun','long',14,'Recovery week')]),
          W(13,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',10,'Lactate threshold 7mi @ LT'),D('Wed','easy',5,'Recovery'),D('Thu','easy',12,'Medium-long'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','long',20,'Endurance w/ 12mi @ MP')]),
          W(14,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',9,'VO2max 5x1200m @ 5K pace'),D('Wed','easy',5,'Recovery'),D('Thu','easy',11,'Medium-long'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','long',18,'Endurance')]),
          W(15,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',9,'Lactate threshold 6mi @ LT'),D('Wed','easy',5,'Recovery'),D('Thu','easy',10,'Medium-long'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','long',17,'Dress rehearsal 10mi @ MP')]),
          W(16,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','interval',7,'VO2max 4x800m @ 5K pace'),D('Wed','easy',5,'Recovery'),D('Thu','easy',8,'Medium-long'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','long',13,'Endurance')]),
          W(17,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','tempo',7,'Lactate threshold 4mi @ LT'),D('Wed','easy',4,'Recovery'),D('Thu','easy',6,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',4,'Easy'),D('Sun','long',10,'Endurance')]),
          W(18,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',4,'Easy'),D('Thu','easy',3,'Shakeout'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','race',26.2,'Marathon')])
        ]
      },
      '18_70': {
        name: '18/70 (18 weeks, 70 mpw)', weeks: 18, peakMPW: 70, maxLong: 22,
        summary: 'The workhorse Pfitzinger plan. 70 mpw peak with longer medium-long runs, more aggressive long runs reaching 22 miles, and additional VO2max sessions.',
        characteristics: [
          { title: 'Lactate Threshold Focus', detail: 'Same LT-based philosophy as 18/55 with longer and more frequent threshold sessions.' },
          { title: 'Extended Medium-Long Runs', detail: 'Mid-week runs reach 13-15 miles — substantial training stimulus that sets this plan apart from lower-volume alternatives.' },
          { title: 'Longer Long Runs', detail: 'Long runs peak at 22 miles with marathon-pace finishes. Two 22-milers in the plan.' },
          { title: 'More VO2max Work', detail: 'Additional interval sessions compared to 18/55. Faster interval paces as fitness develops through the phases.' },
          { title: 'Higher Easy Day Volume', detail: 'Easy days are 8-10 miles, contributing significantly to aerobic development.' },
          { title: 'Structured Recovery', detail: 'Same periodized recovery weeks as 18/55 — essential at this volume level.' }
        ],
        bestFor: ['Competitive runners', 'Sub-3:10 goal', 'High mileage tolerance', '60+ mpw base'],
        schedule: [
          W(1,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',7,'Easy'),D('Wed','easy',10,'Aerobic'),D('Thu','easy',6,'Easy'),D('Fri','easy',7,'Easy'),D('Sat','easy',10,'Medium-long'),D('Sun','long',14,'Endurance')]),
          W(2,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',7,'Easy'),D('Wed','easy',10,'Aerobic'),D('Thu','easy',7,'Easy'),D('Fri','easy',7,'Easy'),D('Sat','easy',11,'Medium-long'),D('Sun','long',15,'Endurance')]),
          W(3,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',8,'Easy'),D('Wed','easy',11,'Aerobic'),D('Thu','easy',7,'Easy'),D('Fri','easy',8,'Easy'),D('Sat','easy',12,'Medium-long'),D('Sun','long',17,'Endurance')]),
          W(4,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','easy',9,'Aerobic'),D('Thu','easy',6,'Easy'),D('Fri','easy',6,'Easy'),D('Sat','easy',9,'Medium-long'),D('Sun','long',14,'Recovery week')]),
          W(5,'Build',[D('Mon','rest',0,'Rest'),D('Tue','tempo',10,'LT 5mi @ threshold'),D('Wed','easy',7,'Recovery'),D('Thu','easy',12,'Medium-long'),D('Fri','easy',7,'Easy'),D('Sat','easy',5,'Recovery'),D('Sun','long',18,'Endurance')]),
          W(6,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',10,'VO2max 5x1200m'),D('Wed','easy',7,'Recovery'),D('Thu','easy',13,'Medium-long'),D('Fri','easy',7,'Easy'),D('Sat','easy',5,'Recovery'),D('Sun','long',19,'Endurance w/ 10mi @ MP')]),
          W(7,'Build',[D('Mon','rest',0,'Rest'),D('Tue','tempo',11,'LT 6mi @ threshold'),D('Wed','easy',7,'Recovery'),D('Thu','easy',13,'Medium-long'),D('Fri','easy',8,'Easy'),D('Sat','easy',5,'Recovery'),D('Sun','long',20,'Endurance')]),
          W(8,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',7,'Easy'),D('Wed','easy',10,'Aerobic'),D('Thu','easy',7,'Easy'),D('Fri','easy',6,'Easy'),D('Sat','easy',10,'Medium-long'),D('Sun','long',15,'Recovery week')]),
          W(9,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',11,'VO2max 6x1000m'),D('Wed','easy',7,'Recovery'),D('Thu','easy',14,'Medium-long'),D('Fri','easy',8,'Easy'),D('Sat','easy',5,'Recovery'),D('Sun','long',20,'Endurance w/ 12mi @ MP')]),
          W(10,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',12,'LT 7mi @ threshold'),D('Wed','easy',7,'Recovery'),D('Thu','easy',14,'Medium-long'),D('Fri','easy',8,'Easy'),D('Sat','easy',5,'Recovery'),D('Sun','long',22,'Endurance')]),
          W(11,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',11,'VO2max 6x1200m'),D('Wed','easy',7,'Recovery'),D('Thu','easy',15,'Medium-long'),D('Fri','easy',8,'Easy'),D('Sat','easy',5,'Recovery'),D('Sun','long',22,'Long w/ 14mi @ MP')]),
          W(12,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',7,'Easy'),D('Wed','easy',10,'Aerobic'),D('Thu','easy',7,'Easy'),D('Fri','easy',6,'Easy'),D('Sat','easy',10,'Medium-long'),D('Sun','long',16,'Recovery week')]),
          W(13,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',12,'LT 8mi @ threshold'),D('Wed','easy',7,'Recovery'),D('Thu','easy',15,'Medium-long'),D('Fri','easy',8,'Easy'),D('Sat','easy',5,'Recovery'),D('Sun','long',22,'Endurance w/ 14mi @ MP')]),
          W(14,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',10,'VO2max 5x1200m'),D('Wed','easy',7,'Recovery'),D('Thu','easy',13,'Medium-long'),D('Fri','easy',8,'Easy'),D('Sat','easy',5,'Recovery'),D('Sun','long',20,'Endurance')]),
          W(15,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',10,'LT 6mi @ threshold'),D('Wed','easy',7,'Recovery'),D('Thu','easy',12,'Medium-long'),D('Fri','easy',7,'Easy'),D('Sat','easy',5,'Recovery'),D('Sun','long',18,'Dress rehearsal 12mi @ MP')]),
          W(16,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','interval',8,'VO2max 4x1000m'),D('Wed','easy',6,'Recovery'),D('Thu','easy',10,'Medium-long'),D('Fri','easy',6,'Easy'),D('Sat','easy',5,'Recovery'),D('Sun','long',15,'Endurance')]),
          W(17,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','tempo',8,'LT 4mi @ threshold'),D('Wed','easy',5,'Recovery'),D('Thu','easy',7,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','easy',4,'Recovery'),D('Sun','long',12,'Endurance')]),
          W(18,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','easy',5,'Easy'),D('Thu','easy',4,'Shakeout'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','race',26.2,'Marathon')])
        ]
      },
      '18_85': {
        name: '18/85 (18 weeks, 85 mpw)', weeks: 18, peakMPW: 85, maxLong: 22,
        summary: 'Elite-level volume. 85 mpw peak with doubles (two runs per day), extensive marathon-pace work, and the longest medium-long runs in any mainstream plan.',
        characteristics: [
          { title: 'Double Run Days', detail: 'Some days include morning and afternoon runs to accumulate volume without individual run length becoming excessive.' },
          { title: 'Lactate Threshold Focus', detail: 'Same foundation — tempo runs are longer (8-12 miles at LT) and threshold sessions more demanding.' },
          { title: 'Extended Medium-Long Runs', detail: 'Mid-week runs reach 15-17 miles. These alone exceed some plans\' long runs.' },
          { title: 'Elite Long Runs', detail: 'Long runs peak at 22 miles with extensive marathon-pace segments (up to 14 miles at MP within the long run).' },
          { title: 'High VO2max Volume', detail: 'More interval sessions at higher volume. 6-8 x 1000m at 5K pace is typical.' },
          { title: 'Mandatory Recovery Management', detail: 'At 85 mpw, recovery weeks and easy days are non-negotiable. Sleep, nutrition, and stress management become training variables.' }
        ],
        bestFor: ['Elite-adjacent runners', 'Sub-2:50 goal', 'Can handle 70+ mpw base', 'Full-time training commitment'],
        schedule: [
          W(1,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',9,'Easy'),D('Wed','easy',13,'Aerobic'),D('Thu','easy',8,'Easy'),D('Fri','easy',9,'Easy'),D('Sat','easy',13,'Medium-long'),D('Sun','long',16,'Endurance')]),
          W(2,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',9,'Easy'),D('Wed','easy',14,'Aerobic'),D('Thu','easy',9,'Easy'),D('Fri','easy',9,'Easy'),D('Sat','easy',14,'Medium-long'),D('Sun','long',18,'Endurance')]),
          W(3,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',10,'Easy'),D('Wed','easy',15,'Aerobic'),D('Thu','easy',9,'Easy'),D('Fri','easy',10,'Easy'),D('Sat','easy',15,'Medium-long'),D('Sun','long',20,'Endurance')]),
          W(4,'Base',[D('Mon','rest',0,'Rest'),D('Tue','easy',8,'Easy'),D('Wed','easy',12,'Aerobic'),D('Thu','easy',8,'Easy'),D('Fri','easy',8,'Easy'),D('Sat','easy',12,'Medium-long'),D('Sun','long',16,'Recovery week')]),
          W(5,'Build',[D('Mon','rest',0,'Rest'),D('Tue','tempo',13,'LT 7mi @ threshold'),D('Wed','easy',9,'Recovery'),D('Thu','easy',15,'Medium-long'),D('Fri','easy',9,'Easy'),D('Sat','easy',7,'Recovery'),D('Sun','long',20,'Endurance w/ 10mi @ MP')]),
          W(6,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',13,'VO2max 6x1200m'),D('Wed','easy',9,'Recovery'),D('Thu','easy',16,'Medium-long'),D('Fri','easy',10,'Easy'),D('Sat','easy',7,'Recovery'),D('Sun','long',22,'Endurance')]),
          W(7,'Build',[D('Mon','rest',0,'Rest'),D('Tue','tempo',14,'LT 8mi @ threshold'),D('Wed','easy',9,'Recovery'),D('Thu','easy',16,'Medium-long'),D('Fri','easy',10,'Easy'),D('Sat','easy',7,'Recovery'),D('Sun','long',22,'Endurance w/ 12mi @ MP')]),
          W(8,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',9,'Easy'),D('Wed','easy',13,'Aerobic'),D('Thu','easy',8,'Easy'),D('Fri','easy',8,'Easy'),D('Sat','easy',12,'Medium-long'),D('Sun','long',17,'Recovery week')]),
          W(9,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',14,'VO2max 7x1000m'),D('Wed','easy',9,'Recovery'),D('Thu','easy',17,'Medium-long'),D('Fri','easy',10,'Easy'),D('Sat','easy',7,'Recovery'),D('Sun','long',22,'Long w/ 14mi @ MP')]),
          W(10,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',14,'LT 8mi @ threshold'),D('Wed','easy',9,'Recovery'),D('Thu','easy',16,'Medium-long'),D('Fri','easy',10,'Easy'),D('Sat','easy',7,'Recovery'),D('Sun','long',22,'Endurance w/ 14mi @ MP')]),
          W(11,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',12,'VO2max 5x1200m'),D('Wed','easy',9,'Recovery'),D('Thu','easy',15,'Medium-long'),D('Fri','easy',9,'Easy'),D('Sat','easy',7,'Recovery'),D('Sun','long',20,'Dress rehearsal 12mi @ MP')]),
          W(12,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',9,'Easy'),D('Wed','easy',12,'Aerobic'),D('Thu','easy',8,'Easy'),D('Fri','easy',8,'Easy'),D('Sat','easy',12,'Medium-long'),D('Sun','long',17,'Recovery week')]),
          W(13,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',14,'LT 8mi @ threshold'),D('Wed','easy',9,'Recovery'),D('Thu','easy',16,'Medium-long'),D('Fri','easy',10,'Easy'),D('Sat','easy',7,'Recovery'),D('Sun','long',22,'Endurance w/ 14mi @ MP')]),
          W(14,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',12,'VO2max 6x1000m'),D('Wed','easy',9,'Recovery'),D('Thu','easy',15,'Medium-long'),D('Fri','easy',9,'Easy'),D('Sat','easy',7,'Recovery'),D('Sun','long',20,'Endurance')]),
          W(15,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',12,'LT 7mi @ threshold'),D('Wed','easy',8,'Recovery'),D('Thu','easy',14,'Medium-long'),D('Fri','easy',9,'Easy'),D('Sat','easy',7,'Recovery'),D('Sun','long',20,'Dress rehearsal 14mi @ MP')]),
          W(16,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','interval',10,'VO2max 4x1200m'),D('Wed','easy',7,'Recovery'),D('Thu','easy',12,'Medium-long'),D('Fri','easy',8,'Easy'),D('Sat','easy',6,'Recovery'),D('Sun','long',17,'Endurance')]),
          W(17,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','tempo',9,'LT 5mi @ threshold'),D('Wed','easy',6,'Recovery'),D('Thu','easy',8,'Easy'),D('Fri','easy',6,'Easy'),D('Sat','easy',5,'Recovery'),D('Sun','long',13,'Endurance')]),
          W(18,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',7,'Easy'),D('Wed','easy',5,'Easy'),D('Thu','easy',4,'Shakeout'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','race',26.2,'Marathon')])
        ]
      },
      '12_55': {
        name: '12/55 (12 weeks, 55 mpw)', weeks: 12, peakMPW: 55, maxLong: 20,
        summary: 'Compressed 12-week version for runners with an existing aerobic base. Same 55 mpw peak but faster ramp — requires arriving with a solid foundation of 40+ mpw.',
        characteristics: [
          { title: 'Compressed Timeline', detail: '12 weeks instead of 18. The base-building phase is eliminated — you must arrive with aerobic fitness already established.' },
          { title: 'Rapid Progression', detail: 'Jumps into quality work by week 2. Less gradual than the 18-week version — higher injury risk if undertrained.' },
          { title: 'Same Peak Stimulus', detail: 'Peak weeks match 18/55 in intensity and volume. You just get there faster.' },
          { title: 'Shorter Taper', detail: 'Two-week taper instead of three. Appropriate given the shorter overall plan duration.' }
        ],
        bestFor: ['Late race registration', 'Maintaining fitness between marathons', 'Solid 40+ mpw base', 'Experienced with Pfitzinger plans'],
        schedule: [
          W(1,'Build',[D('Mon','rest',0,'Rest'),D('Tue','tempo',8,'LT 4mi @ threshold'),D('Wed','easy',5,'Recovery'),D('Thu','easy',9,'Medium-long'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','long',15,'Endurance')]),
          W(2,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',8,'VO2max 5x1000m'),D('Wed','easy',5,'Recovery'),D('Thu','easy',10,'Medium-long'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','long',16,'Endurance w/ 8mi @ MP')]),
          W(3,'Build',[D('Mon','rest',0,'Rest'),D('Tue','tempo',9,'LT 5mi @ threshold'),D('Wed','easy',5,'Recovery'),D('Thu','easy',11,'Medium-long'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','long',17,'Endurance')]),
          W(4,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','easy',7,'Aerobic'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',7,'Medium-long'),D('Sun','long',13,'Recovery week')]),
          W(5,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',9,'VO2max 6x1000m'),D('Wed','easy',5,'Recovery'),D('Thu','easy',11,'Medium-long'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','long',18,'Endurance w/ 10mi @ MP')]),
          W(6,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',10,'LT 6mi @ threshold'),D('Wed','easy',5,'Recovery'),D('Thu','easy',12,'Medium-long'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','long',19,'Endurance')]),
          W(7,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',9,'VO2max 5x1200m'),D('Wed','easy',5,'Recovery'),D('Thu','easy',12,'Medium-long'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','long',20,'Long w/ 12mi @ MP')]),
          W(8,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','easy',8,'Aerobic'),D('Thu','easy',5,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',8,'Medium-long'),D('Sun','long',14,'Recovery week')]),
          W(9,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',10,'LT 7mi @ threshold'),D('Wed','easy',5,'Recovery'),D('Thu','easy',11,'Medium-long'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','long',18,'Dress rehearsal 10mi @ MP')]),
          W(10,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','interval',7,'VO2max 4x800m'),D('Wed','easy',5,'Recovery'),D('Thu','easy',8,'Medium-long'),D('Fri','rest',0,'Rest'),D('Sat','easy',5,'Easy'),D('Sun','long',13,'Endurance')]),
          W(11,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','tempo',7,'LT 4mi @ threshold'),D('Wed','easy',4,'Recovery'),D('Thu','easy',6,'Easy'),D('Fri','rest',0,'Rest'),D('Sat','easy',4,'Easy'),D('Sun','long',10,'Endurance')]),
          W(12,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',5,'Easy'),D('Wed','easy',4,'Easy'),D('Thu','easy',3,'Shakeout'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','race',26.2,'Marathon')])
        ]
      },
      '12_70': {
        name: '12/70 (12 weeks, 70 mpw)', weeks: 12, peakMPW: 70, maxLong: 22,
        summary: 'The most demanding compressed plan. 70 mpw peak in just 12 weeks. Requires arriving with 55+ mpw base and recent marathon experience.',
        characteristics: [
          { title: 'Compressed High Volume', detail: '12 weeks to 70 mpw peak. No gradual build — you must already be running 55+ mpw consistently.' },
          { title: 'Immediate Quality Work', detail: 'Threshold and interval sessions start in week 1. No introductory phase.' },
          { title: 'Aggressive Long Runs', detail: 'Long runs reach 22 miles by week 6. Marathon-pace finishes throughout.' },
          { title: 'High Risk / High Reward', detail: 'The fastest path to marathon-specific fitness. Also the highest injury risk of any Pfitzinger plan.' }
        ],
        bestFor: ['Fall/spring marathon doubles', 'Experienced 60+ mpw runners', 'Recent marathon base', 'Competitive time goals'],
        schedule: [
          W(1,'Build',[D('Mon','rest',0,'Rest'),D('Tue','tempo',10,'LT 5mi @ threshold'),D('Wed','easy',7,'Recovery'),D('Thu','easy',12,'Medium-long'),D('Fri','easy',7,'Easy'),D('Sat','easy',5,'Recovery'),D('Sun','long',18,'Endurance')]),
          W(2,'Build',[D('Mon','rest',0,'Rest'),D('Tue','interval',10,'VO2max 5x1200m'),D('Wed','easy',7,'Recovery'),D('Thu','easy',13,'Medium-long'),D('Fri','easy',7,'Easy'),D('Sat','easy',5,'Recovery'),D('Sun','long',19,'Endurance w/ 10mi @ MP')]),
          W(3,'Build',[D('Mon','rest',0,'Rest'),D('Tue','tempo',11,'LT 6mi @ threshold'),D('Wed','easy',7,'Recovery'),D('Thu','easy',13,'Medium-long'),D('Fri','easy',8,'Easy'),D('Sat','easy',5,'Recovery'),D('Sun','long',20,'Endurance')]),
          W(4,'Build',[D('Mon','rest',0,'Rest'),D('Tue','easy',7,'Easy'),D('Wed','easy',10,'Aerobic'),D('Thu','easy',7,'Easy'),D('Fri','easy',6,'Easy'),D('Sat','easy',9,'Medium-long'),D('Sun','long',15,'Recovery week')]),
          W(5,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',11,'VO2max 6x1000m'),D('Wed','easy',7,'Recovery'),D('Thu','easy',14,'Medium-long'),D('Fri','easy',8,'Easy'),D('Sat','easy',5,'Recovery'),D('Sun','long',22,'Endurance w/ 12mi @ MP')]),
          W(6,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',12,'LT 7mi @ threshold'),D('Wed','easy',7,'Recovery'),D('Thu','easy',14,'Medium-long'),D('Fri','easy',8,'Easy'),D('Sat','easy',5,'Recovery'),D('Sun','long',22,'Long w/ 14mi @ MP')]),
          W(7,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','interval',10,'VO2max 5x1200m'),D('Wed','easy',7,'Recovery'),D('Thu','easy',13,'Medium-long'),D('Fri','easy',8,'Easy'),D('Sat','easy',5,'Recovery'),D('Sun','long',20,'Endurance')]),
          W(8,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','easy',7,'Easy'),D('Wed','easy',10,'Aerobic'),D('Thu','easy',7,'Easy'),D('Fri','easy',6,'Easy'),D('Sat','easy',10,'Medium-long'),D('Sun','long',15,'Recovery week')]),
          W(9,'Peak',[D('Mon','rest',0,'Rest'),D('Tue','tempo',11,'LT 6mi @ threshold'),D('Wed','easy',7,'Recovery'),D('Thu','easy',12,'Medium-long'),D('Fri','easy',7,'Easy'),D('Sat','easy',5,'Recovery'),D('Sun','long',18,'Dress rehearsal 12mi @ MP')]),
          W(10,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','interval',8,'VO2max 4x1000m'),D('Wed','easy',6,'Recovery'),D('Thu','easy',10,'Medium-long'),D('Fri','easy',6,'Easy'),D('Sat','easy',5,'Recovery'),D('Sun','long',15,'Endurance')]),
          W(11,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','tempo',8,'LT 4mi @ threshold'),D('Wed','easy',5,'Recovery'),D('Thu','easy',7,'Easy'),D('Fri','easy',5,'Easy'),D('Sat','easy',4,'Recovery'),D('Sun','long',12,'Endurance')]),
          W(12,'Taper',[D('Mon','rest',0,'Rest'),D('Tue','easy',6,'Easy'),D('Wed','easy',5,'Easy'),D('Thu','easy',4,'Shakeout'),D('Fri','rest',0,'Rest'),D('Sat','rest',0,'Rest'),D('Sun','race',26.2,'Marathon')])
        ]
      }
    }
  }
};

// --- Populate plan dropdown ---
function initDropdowns() {
  var sel = document.getElementById('plan-select');
  Object.keys(PLANS).forEach(function(key) {
    var opt = document.createElement('option');
    opt.value = key;
    opt.textContent = PLANS[key].name;
    sel.appendChild(opt);
  });
}

function onPlanChange() {
  var key = document.getElementById('plan-select').value;
  APP.planKey = key;
  APP.tierKey = '';
  var tierGroup = document.getElementById('tier-group');
  var planInfo = document.getElementById('plan-info');
  planInfo.style.display = 'none';

  if (!key) { tierGroup.style.display = 'none'; return; }

  var tierSel = document.getElementById('tier-select');
  tierSel.innerHTML = '<option value="">Choose a tier...</option>';
  var tiers = PLANS[key].tiers;
  Object.keys(tiers).forEach(function(tk) {
    var opt = document.createElement('option');
    opt.value = tk;
    opt.textContent = tiers[tk].name;
    tierSel.appendChild(opt);
  });
  tierGroup.style.display = 'block';

  if (Object.keys(tiers).length === 1) {
    tierSel.value = Object.keys(tiers)[0];
    onTierChange();
  }
}

function onTierChange() {
  var tierKey = document.getElementById('tier-select').value;
  APP.tierKey = tierKey;
  var planInfo = document.getElementById('plan-info');
  if (!tierKey || !APP.planKey) { planInfo.style.display = 'none'; return; }

  var plan = PLANS[APP.planKey];
  var tier = plan.tiers[tierKey];

  document.getElementById('info-title').textContent = plan.name + ' — ' + tier.name;

  var charList = document.getElementById('info-chars');
  charList.innerHTML = '';
  tier.characteristics.forEach(function(c) {
    var li = document.createElement('li');
    li.innerHTML = '<span class="char-title">' + c.title + '</span>' + c.detail;
    charList.appendChild(li);
  });

  var bestFor = document.getElementById('info-bestfor');
  bestFor.innerHTML = '';
  tier.bestFor.forEach(function(tag) {
    var span = document.createElement('span');
    span.className = 'tag';
    span.textContent = tag;
    bestFor.appendChild(span);
  });

  planInfo.style.display = 'block';
}

function goCustomize() {
  var tier = PLANS[APP.planKey].tiers[APP.tierKey];
  document.getElementById('cust-title').textContent = PLANS[APP.planKey].name + ' — ' + tier.name;
  document.getElementById('cust-sub').textContent = tier.weeks + ' weeks · Peak ' + tier.peakMPW + ' mpw · Long run up to ' + tier.maxLong + ' mi';

  var slider = document.getElementById('mpw-slider');
  slider.value = tier.peakMPW;
  slider.min = Math.max(30, Math.round(tier.peakMPW * 0.6));
  slider.max = Math.min(85, Math.round(tier.peakMPW * 1.3));
  APP.targetMPW = tier.peakMPW;
  updateMpwLabel();

  document.getElementById('race-date').value = '';
  document.getElementById('race-date-info').textContent = '';
  document.getElementById('long-cap').value = '';
  APP.raceDate = '';
  APP.longCap = 0;

  showState('customize');
}

// --- Mileage scaling ---
function scaleMiles(baseMiles, ratio, dayType) {
  if (dayType === 'rest' || baseMiles === 0) return 0;
  var scaled = baseMiles * ratio;
  if (dayType !== 'cross' && scaled > 0 && scaled < 3) scaled = 3;
  if (dayType === 'long' && scaled > 22 && baseMiles <= 22) scaled = 22;
  return Math.round(scaled * 10) / 10;
}

function getScaledSchedule() {
  var tier = PLANS[APP.planKey].tiers[APP.tierKey];
  var ratio = parseInt(document.getElementById('mpw-slider').value) / tier.peakMPW;
  var longCap = parseFloat(document.getElementById('long-cap').value) || 0;
  var removePriority = ['rest', 'cross', 'easy'];

  return tier.schedule.map(function(week) {
    var days = week.days.map(function(d) {
      var miles = scaleMiles(d.miles, ratio, d.type);
      if (longCap && d.type === 'long' && miles > longCap) miles = longCap;
      if (APP.unit === 'km') miles = Math.round(miles * KM_PER_MI * 10) / 10;
      return { day: d.day, type: d.type, miles: miles, desc: d.desc };
    });

    if (APP.daysPerWeek < 7) {
      var runDays = days.filter(function(d) { return d.type !== 'rest'; });
      var restDays = days.filter(function(d) { return d.type === 'rest'; });
      var toRemove = 7 - APP.daysPerWeek - restDays.length;
      if (toRemove > 0) {
        var removable = runDays.filter(function(d) { return d.type === 'cross' || d.type === 'easy'; });
        removable.sort(function(a, b) {
          var pa = removePriority.indexOf(a.type);
          var pb = removePriority.indexOf(b.type);
          if (pa !== pb) return pb - pa;
          return a.miles - b.miles;
        });
        var removeSet = removable.slice(0, toRemove);
        days = days.map(function(d) {
          if (removeSet.indexOf(d) !== -1) return { day: d.day, type: 'rest', miles: 0, desc: 'Rest' };
          return d;
        });
      }
    }

    var total = days.reduce(function(sum, d) { return sum + d.miles; }, 0);
    return { week: week.week, phase: week.phase, days: days, total: Math.round(total * 10) / 10 };
  });
}

// --- Render schedule ---
function generateSchedule() {
  var tier = PLANS[APP.planKey].tiers[APP.tierKey];
  if (!tier.schedule.length) {
    alert('Schedule data not yet available for this plan. Try Pfitzinger 18/55.');
    return;
  }

  APP.targetMPW = parseInt(document.getElementById('mpw-slider').value);
  APP.longCap = parseFloat(document.getElementById('long-cap').value) || 0;
  APP.raceDate = document.getElementById('race-date').value;

  var schedule = getScaledSchedule();
  var unitLabel = APP.unit === 'km' ? 'km' : 'mi';

  document.getElementById('sched-title').textContent = PLANS[APP.planKey].name + ' — ' + tier.name;

  var currentWeek = 0;
  if (APP.raceDate) {
    var race = new Date(APP.raceDate + 'T00:00:00');
    var start = new Date(race);
    start.setDate(start.getDate() - tier.weeks * 7);
    var today = new Date(); today.setHours(0,0,0,0);
    var daysSinceStart = Math.floor((today - start) / 86400000);
    if (daysSinceStart >= 0) currentWeek = Math.floor(daysSinceStart / 7) + 1;
  }

  var container = document.getElementById('schedule-container');
  container.innerHTML = '';

  schedule.forEach(function(week) {
    var card = document.createElement('div');
    var phaseClass = 'phase-' + week.phase.toLowerCase();
    var isCurrent = currentWeek === week.week;
    card.className = 'week-card ' + phaseClass + (isCurrent ? ' current-week' : '');

    var header = document.createElement('div');
    header.className = 'week-header';
    header.onclick = function() { card.classList.toggle('expanded'); };
    header.innerHTML = '<div class="week-left"><span class="week-num">Week ' + week.week + '</span><span class="week-phase ' + week.phase.toLowerCase() + '">' + week.phase + '</span></div><div style="display:flex;align-items:center;gap:0.6rem;"><span class="week-miles">' + week.total + ' ' + unitLabel + '</span><span class="week-chevron">&#9654;</span></div>';

    var body = document.createElement('div');
    body.className = 'week-body';

    week.days.forEach(function(d) {
      var row = document.createElement('div');
      row.className = 'day-row';
      var color = TYPE_COLORS[d.type] || 'var(--muted)';
      var distStr = d.type === 'rest' ? '—' : d.miles + ' ' + unitLabel;
      row.innerHTML = '<span class="type-dot" style="background:' + color + '"></span><span class="day-name">' + d.day + '</span><span class="day-dist">' + distStr + '</span><span class="day-desc">' + d.desc + '</span>';
      body.appendChild(row);
    });

    card.appendChild(header);
    card.appendChild(body);
    container.appendChild(card);
  });

  allExpanded = false;
  document.querySelector('.expand-toggle').textContent = 'Expand All';
  showState('schedule');
}

function toggleExpandAll() {
  allExpanded = !allExpanded;
  document.querySelectorAll('.week-card').forEach(function(card) {
    if (allExpanded) card.classList.add('expanded');
    else card.classList.remove('expanded');
  });
  document.querySelector('.expand-toggle').textContent = allExpanded ? 'Collapse All' : 'Expand All';
}

// --- Init ---
initDropdowns();
</script>
