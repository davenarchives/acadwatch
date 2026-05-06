const form = document.getElementById('risk-form');
const initialResultScript = document.getElementById('initial-result');
const initialResult = JSON.parse(initialResultScript.textContent || 'null');
const riskCard = document.getElementById('risk-card');
const riskLevel = document.getElementById('risk-level');
const confidenceScore = document.getElementById('confidence-score');
const scoreRing = document.getElementById('score-ring');
const scoreBar = document.getElementById('score-bar');
const factorList = document.getElementById('factor-list');
const actionList = document.getElementById('action-list');
const insight = document.getElementById('ai-insight');
const statusPill = document.getElementById('status-pill');
const predictionCard = document.getElementById('prediction-card');
const predictionLabel = document.getElementById('prediction-label');
const predictionCaption = document.getElementById('prediction-caption');
const predictionIcon = document.getElementById('prediction-icon');
const circumference = 264;
const initialValues = Object.fromEntries(new FormData(form).entries());
let updateTimer;

function markFieldState(control) {
    const card = control.closest('[data-field-card]');
    const warning = card?.querySelector('.field-warning');
    const min = control.min === '' ? null : Number(control.min);
    const max = control.max === '' ? null : Number(control.max);
    const value = Number(control.value);
    const currentValue = control.type === 'radio'
        ? new FormData(form).get(control.name)
        : control.value;
    let message = '';

    if (!card) {
        return true;
    }

    card.classList.toggle('is-changed', currentValue !== initialValues[control.name]);

    if (control.required && control.value === '') {
        message = 'Required';
    } else if (control.type === 'number' && Number.isNaN(value)) {
        message = 'Enter a number';
    } else if (control.type === 'number' && min !== null && value < min) {
        message = `Minimum ${min}`;
    } else if (control.type === 'number' && max !== null && value > max) {
        message = `Maximum ${max}`;
    }

    card.classList.toggle('is-invalid', message !== '');
    if (warning) {
        warning.textContent = message;
    }

    return message === '';
}

function validateControls() {
    return [...form.querySelectorAll('input, select')]
        .map(markFieldState)
        .every(Boolean);
}

function palette(level) {
    if (level === 'High') {
        return {
            card: 'rounded-2xl border border-rose-300/20 bg-rose-400/10 p-5 transition duration-300',
            bar: '#fb7185',
            barClass: 'h-full rounded-full bg-rose-400 transition-all duration-500',
            insight: 'This student may benefit from timely support and a coordinated intervention plan.'
        };
    }

    if (level === 'Medium') {
        return {
            card: 'rounded-2xl border border-amber-300/20 bg-amber-400/10 p-5 transition duration-300',
            bar: '#fbbf24',
            barClass: 'h-full rounded-full bg-amber-400 transition-all duration-500',
            insight: 'Some signals suggest closer monitoring would be helpful over the next review cycle.'
        };
    }

    return {
        card: 'rounded-2xl border border-emerald-300/20 bg-emerald-400/10 p-5 transition duration-300',
        bar: '#34d399',
        barClass: 'h-full rounded-full bg-emerald-400 transition-all duration-500',
        insight: 'Current signals look steady. Continue supportive monitoring and regular check-ins.'
    };
}

function renderList(target, items) {
    target.innerHTML = '';
    items.forEach((item) => {
        const li = document.createElement('li');
        li.className = 'rounded-xl border border-white/10 bg-white/[0.04] px-3 py-2';
        li.textContent = item;
        target.appendChild(li);
    });
}

function renderPrediction(result) {
    const isDropout = result.label === 'Likely to Dropout';

    predictionCard.className = isDropout
        ? 'mt-5 rounded-2xl border border-rose-300/25 bg-rose-400/10 p-5 transition duration-300'
        : 'mt-5 rounded-2xl border border-emerald-300/25 bg-emerald-400/10 p-5 transition duration-300';
    predictionLabel.textContent = isDropout ? 'Dropout' : 'Non-Dropout';
    predictionCaption.textContent = isDropout
        ? 'The model currently predicts a dropout outcome.'
        : 'The model currently predicts the student will continue.';
    predictionIcon.className = isDropout
        ? 'flex h-11 w-11 shrink-0 items-center justify-center rounded-2xl bg-rose-400/15 text-rose-200'
        : 'flex h-11 w-11 shrink-0 items-center justify-center rounded-2xl bg-emerald-400/15 text-emerald-200';
    predictionIcon.innerHTML = isDropout
        ? '<i data-lucide="alert-triangle" class="h-5 w-5"></i>'
        : '<i data-lucide="check-circle-2" class="h-5 w-5"></i>';

    if (window.lucide) {
        window.lucide.createIcons();
    }
}

function renderResult(result) {
    if (!result) {
        return;
    }

    const style = palette(result.risk_level);
    const score = Math.max(0, Math.min(100, Number(result.confidence || 0)));

    renderPrediction(result);
    riskCard.className = style.card;
    riskLevel.textContent = result.risk_level;
    confidenceScore.textContent = `${score.toFixed(1).replace('.0', '')}%`;
    scoreRing.style.stroke = style.bar;
    scoreRing.style.strokeDashoffset = String(circumference - (circumference * score / 100));
    scoreBar.className = style.barClass;
    scoreBar.style.width = `${score}%`;
    insight.textContent = style.insight;
    renderList(factorList, result.factors || []);
    renderList(actionList, result.actions || []);
}

async function updatePrediction() {
    statusPill.textContent = 'Updating';
    statusPill.className = 'rounded-full bg-sky-400/10 px-3 py-1 text-xs font-semibold text-sky-200 ring-1 ring-sky-300/20';

    const payload = Object.fromEntries(new FormData(form).entries());

    try {
        const response = await fetch(form.dataset.apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();
        if (!response.ok) {
            throw new Error(data.error || 'Prediction failed');
        }

        renderResult(data);
        statusPill.textContent = 'Live';
        statusPill.className = 'rounded-full bg-emerald-400/10 px-3 py-1 text-xs font-semibold text-emerald-200 ring-1 ring-emerald-300/20';
    } catch (error) {
        statusPill.textContent = 'Needs input';
        statusPill.className = 'rounded-full bg-amber-400/10 px-3 py-1 text-xs font-semibold text-amber-200 ring-1 ring-amber-300/20';
    }
}

function scheduleUpdate() {
    const isValid = validateControls();
    window.clearTimeout(updateTimer);
    if (isValid) {
        updateTimer = window.setTimeout(updatePrediction, 300);
    } else {
        statusPill.textContent = 'Check values';
        statusPill.className = 'rounded-full bg-rose-400/10 px-3 py-1 text-xs font-semibold text-rose-200 ring-1 ring-rose-300/20';
    }
}

form.addEventListener('input', scheduleUpdate);
form.addEventListener('change', scheduleUpdate);
validateControls();
renderResult(initialResult);

if (window.lucide) {
    window.lucide.createIcons();
}
