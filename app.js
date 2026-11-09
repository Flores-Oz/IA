(function () {
  'use strict';
  const STORAGE = 'redes-neuronales-preguntas-v1';
  const TOPIC_STORAGE = 'redes-neuronales-tema-v1';
  const escape = (value) => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const inline = value => escape(value).replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>').replace(/`([^`]+)`/g, '<code>$1</code>');
  function evaluate(question, response) {
    if (question.kind === 'open') return {correct: null, expected: question.answer, explanation: question.explanation};
    return {correct: String(response) === String(question.answer), expected: question.options[question.answer], explanation: question.explanation};
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = {evaluate, escape, inline};
  if (typeof document === 'undefined') return;

  const course = window.COURSE;
  const root = document.getElementById('lesson-content');
  if (!course || !Array.isArray(course.lessons) || !course.lessons.length) {
    root.innerHTML = '<p class="error-message">No se pudo cargar el contenido. Abre Iniciar.cmd y vuelve a entrar a la página.</p>';
    return;
  }
  let saved = {};
  try { const data = JSON.parse(localStorage.getItem(STORAGE) || '{}'); if (data && typeof data === 'object' && !Array.isArray(data)) saved = data; } catch (_) { /* Practice still works without browser storage. */ }
  const save = () => { try { localStorage.setItem(STORAGE, JSON.stringify(saved)); } catch (_) {} };
  const byId = new Map(course.lessons.map(lesson => [lesson.id, lesson]));
  const fromHash = () => {
    try {
      const hash = decodeURIComponent(location.hash.slice(1));
      if (byId.has(hash)) return hash;
      const previous = localStorage.getItem(TOPIC_STORAGE);
      if (byId.has(previous)) return previous;
    } catch (_) {}
    return course.lessons[0].id;
  };
  let active = fromHash();
  const sourceLink = source => `material/${encodeURIComponent(source.document)}#page=${source.pages[0]}`;
  function sourceHTML(source) {
    const label = `${escape(source.document)} · p. ${source.pages.join(', ')}`;
    if (window.PDF_LINKS_ENABLED === false) return `<li>${label}</li>`;
    return `<li><a href="${sourceLink(source)}" target="_blank" rel="noopener">${label}</a></li>`;
  }

  function sectionHTML(section) {
    const paragraphs = (section.paragraphs || []).map(p => `<p>${inline(p)}</p>`).join('');
    const formula = section.formula ? `<div class="formula">${escape(section.formula)}</div>` : '';
    const code = section.code ? `<pre><code>${escape(section.code)}</code></pre>` : '';
    const table = section.table ? `<div class="table-wrap"><table><thead><tr>${section.table[0].map(c=>`<th scope="col">${inline(c)}</th>`).join('')}</tr></thead><tbody>${section.table.slice(1).map(row=>`<tr>${row.map(c=>`<td>${inline(c)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>` : '';
    return `<section class="${section.type || 'explanation'}"><h2>${escape(section.title)}</h2>${paragraphs}${formula}${code}${table}</section>`;
  }

  function questionHTML(q, index, lesson) {
    const state = saved[q.id] && typeof saved[q.id] === 'object' ? saved[q.id] : {};
    const checked = Boolean(state.checked) && state.response !== undefined && String(state.response).trim() !== '';
    const response = state.response ?? '';
    const result = checked ? evaluate(q, response) : null;
    const input = q.kind === 'open'
      ? `<label for="answer-${q.id}" class="question-label">TU EXPLICACIÓN</label><textarea id="answer-${q.id}" name="answer" placeholder="Escribe lo que entendiste…" ${checked?'disabled':''}>${escape(response)}</textarea>`
      : `<div class="options">${q.options.map((option, i)=>`<label class="option ${checked && i===q.answer?'correct':''} ${checked && String(i)===String(response) && !result.correct?'incorrect':''}"><input type="radio" name="answer" value="${i}" ${String(i)===String(response)?'checked':''} ${checked?'disabled':''}><span>${inline(option)}</span></label>`).join('')}</div>`;
    const feedback = checked ? `<div class="feedback ${result.correct===false?'wrong':''}" role="status"><div class="feedback-title">${result.correct===null?'Compara tu explicación':result.correct?'Correcto.':'Revisa esta idea.'}</div><div class="expected"><strong>${result.correct===null?'Respuesta de referencia':'Respuesta correcta'}</strong><p>${inline(result.expected)}</p></div><p>${inline(result.explanation)}</p>${q.criteria?`<p class="rubric"><strong>Comprueba que mencionaste:</strong> ${q.criteria.map(inline).join(' · ')}.</p>`:''}</div>` : '';
    return `<form class="question-card" data-question="${q.id}"><p class="question-label">PREGUNTA ${index+1} · ${q.kind==='open'?'EXPLICA CON TUS PALABRAS':q.tag||'COMPRENSIÓN'}</p><fieldset><legend>${inline(q.prompt)}</legend>${input}</fieldset><div class="question-actions">${checked?'<button class="button secondary" type="button" data-retry="'+q.id+'">Intentar de nuevo</button>':'<button class="button" type="submit" '+(String(response).trim()===''?'disabled':'')+'>'+(q.kind==='open'?'Comparar mi respuesta':'Comprobar respuesta')+'</button>'}</div>${feedback}</form>`;
  }

  function render(shouldFocus=false) {
    const lesson = byId.get(active);
    const index = course.lessons.indexOf(lesson);
    document.title = `${lesson.title} · Redes neuronales`;
    document.getElementById('topics').innerHTML = course.lessons.map((item,i)=>`<button class="topic-button" type="button" data-topic="${item.id}" ${item.id===active?'aria-current="page"':''}><span class="topic-number">${String(i+1).padStart(2,'0')}</span><span>${escape(item.shortTitle||item.title)}</span></button>`).join('');
    root.innerHTML = `<article><div class="lesson-meta"><p class="eyebrow">TEMA ${String(index+1).padStart(2,'0')} DE ${course.lessons.length}</p><a class="jump-link" href="#questions">Ir a las preguntas ↓</a></div><h1>${escape(lesson.title)}</h1><p class="intro">${inline(lesson.intro)}</p>${lesson.sections.map(sectionHTML).join('')}<details class="source-details"><summary>${window.PDF_LINKS_ENABLED === false?'Fuentes del tema':'Ver las páginas del material'}</summary><ul>${lesson.sources.map(sourceHTML).join('')}</ul></details><section class="questions" id="questions"><div class="questions-header"><h2>Ahora, compruébalo.</h2><a class="jump-link" href="#lesson">Volver a la explicación ↑</a></div><p class="questions-subtitle">Responde antes de ver la solución. Si te equivocas, lee el porqué y vuelve a intentarlo.</p><div id="question-list">${lesson.questions.map((q,i)=>questionHTML(q,i,lesson)).join('')}</div></section><nav class="lesson-nav" aria-label="Cambiar de tema">${index?`<button class="button secondary" data-topic="${course.lessons[index-1].id}">← ${escape(course.lessons[index-1].shortTitle||course.lessons[index-1].title)}</button>`:'<span></span>'}${index<course.lessons.length-1?`<button class="button secondary" data-topic="${course.lessons[index+1].id}">${escape(course.lessons[index+1].shortTitle||course.lessons[index+1].title)} →</button>`:'<span></span>'}</nav></article>`;
    if (shouldFocus) {
      document.getElementById('lesson').focus({preventScroll:true});
      window.scrollTo({top:0,behavior:'instant'});
    }
  }

  document.addEventListener('click', event => {
    const topic = event.target.closest('[data-topic]');
    if (topic && byId.has(topic.dataset.topic)) {
      active = topic.dataset.topic;
      try { localStorage.setItem(TOPIC_STORAGE, active); } catch (_) {}
      history.replaceState(null,'',`#${active}`);
      render(true);
      return;
    }
    const retry = event.target.closest('[data-retry]');
    if (retry) {
      const form = retry.closest('form');
      const id = retry.dataset.retry;
      delete saved[id]; save();
      const lesson = byId.get(active);
      const index = lesson.questions.findIndex(q=>q.id===id);
      if (index>=0) { form.outerHTML = questionHTML(lesson.questions[index],index,lesson); document.querySelector(`[data-question="${id}"] input, [data-question="${id}"] textarea`)?.focus({preventScroll:true}); }
    }
  });
  document.addEventListener('input', event => {
    const form = event.target.closest('form[data-question]');
    if (!form || event.target.name!=='answer') return;
    const response = event.target.value;
    saved[form.dataset.question] = {response,checked:false}; save();
    const submit = form.querySelector('[type="submit"]');
    if (submit) submit.disabled = !response.trim();
  });
  document.addEventListener('submit', event => {
    const form = event.target.closest('form[data-question]');
    if (!form) return;
    event.preventDefault();
    const response = new FormData(form).get('answer');
    if (response===null || !String(response).trim()) return;
    const lesson = byId.get(active);
    const index = lesson.questions.findIndex(q=>q.id===form.dataset.question);
    if (index<0) return;
    saved[form.dataset.question] = {response:String(response),checked:true}; save();
    form.outerHTML = questionHTML(lesson.questions[index],index,lesson);
    const feedback = document.querySelector(`[data-question="${lesson.questions[index].id}"] .feedback`);
    if (feedback) { feedback.setAttribute('tabindex','-1'); feedback.focus({preventScroll:true}); }
  });
  window.addEventListener('hashchange',()=>{ if (byId.has(location.hash.slice(1))) {active=fromHash();render(true);} });
  render();
})();
