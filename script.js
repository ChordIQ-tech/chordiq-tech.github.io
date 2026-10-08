(function () {
  var EN = document.documentElement.lang === 'en';
  // diffusion-field hero background
  var cv = document.getElementById('field');
  if (cv) {
    var ctx = cv.getContext('2d', { alpha: true });
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var N = 84;
    var u = new Float32Array(N * N);
    var v = new Float32Array(N * N);
    var sources = [];
    function seed() {
      u.fill(0);
      var k = 3 + (Math.random() * 3 | 0);
      sources = [];
      for (var i = 0; i < k; i++) {
        sources.push({ x: 4 + (Math.random() * (N - 8) | 0), y: 4 + (Math.random() * (N - 8) | 0),
          val: Math.random() < 0.5 ? 1 : -0.7 });
      }
    }
    seed();
    function step(iters) {
      for (var it = 0; it < iters; it++) {
        for (var s = 0; s < sources.length; s++) u[sources[s].y * N + sources[s].x] = sources[s].val;
        for (var y = 1; y < N - 1; y++) {
          for (var x = 1; x < N - 1; x++) {
            var i = y * N + x;
            v[i] = 0.25 * (u[i - 1] + u[i + 1] + u[i - N] + u[i + N]);
          }
        }
        var t = u; u = v; v = t;
      }
    }
    function color(t) {
      if (t >= 0) { var a = Math.min(t, 1); return [51 + a * 40, 200 + a * 25, 184, a * 0.9]; }
      var b = Math.min(-t, 1); return [233, 162, 61, b * 0.78];
    }
    var raf = null, tick = 0;
    function resize() {
      var r = cv.getBoundingClientRect();
      cv.width = Math.max(1, r.width | 0);
      cv.height = Math.max(1, r.height | 0);
    }
    window.addEventListener('resize', resize);
    resize();
    function draw() {
      var W = cv.width, H = cv.height;
      ctx.clearRect(0, 0, W, H);
      var cw = W / (N - 2), ch = H / (N - 2);
      for (var y = 1; y < N - 1; y++) {
        for (var x = 1; x < N - 1; x++) {
          var val = u[y * N + x];
          if (Math.abs(val) < 0.02) continue;
          var c = color(val);
          ctx.fillStyle = 'rgba(' + (c[0] | 0) + ',' + (c[1] | 0) + ',' + (c[2] | 0) + ',' + c[3].toFixed(3) + ')';
          ctx.fillRect((x - 1) * cw, (y - 1) * ch, cw + 1, ch + 1);
        }
      }
    }
    if (reduce) { step(400); draw(); }
    else {
      (function frame() {
        step(2); draw(); tick++;
        if (tick % 520 === 0) seed();
        raf = requestAnimationFrame(frame);
      })();
      document.addEventListener('visibilitychange', function () {
        if (document.hidden) { cancelAnimationFrame(raf); raf = null; }
        else if (!raf) { (function frame() { step(2); draw(); tick++; if (tick % 520 === 0) seed(); raf = requestAnimationFrame(frame); })(); }
      });
    }
  }

  // copy-to-clipboard
  function copyText(text, btn) {
    var done = function (ok) {
      var old = btn.textContent;
      btn.textContent = ok ? (EN ? 'Copied' : 'Copiado') : (EN ? 'Select and copy' : 'Selecione e copie');
      setTimeout(function () { btn.textContent = old; }, 1600);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () { done(true); }, function () { done(false); });
    } else { done(false); }
  }
  document.querySelectorAll('.copy-btn[data-copy]').forEach(function (btn) {
    btn.addEventListener('click', function () { copyText(btn.getAttribute('data-copy'), btn); });
  });

  // lead form -> WhatsApp deep link
  var form = document.getElementById('lead-form');
  var okNote = document.getElementById('ok-note');
  function buildMessage() {
    var nome = (document.getElementById('f-nome').value || '').trim();
    var email = (document.getElementById('f-email').value || '').trim();
    var empresa = (document.getElementById('f-empresa').value || '').trim();
    var problema = (document.getElementById('f-problema').value || '').trim();
    var lines = EN ? ['Hello! I came from the ChordIQ website.', '', 'Name: ' + nome, 'E-mail: ' + email] : ['Olá! Vim pelo site da ChordIQ.', '', 'Nome: ' + nome, 'E-mail: ' + email];
    if (empresa) lines.push((EN ? 'Company: ' : 'Empresa: ') + empresa);
    lines.push('', (EN ? 'Problem: ' : 'Problema: ') + problema);
    return lines.join('\n');
  }
  if (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      if (!form.reportValidity()) return;
      var msg = buildMessage();
      var url = 'https://wa.me/5584991287602?text=' + encodeURIComponent(msg);
      window.open(url, '_blank', 'noopener');
      okNote.classList.add('show');
    });
  }
  var copyMsgBtn = document.getElementById('copy-msg');
  if (copyMsgBtn) {
    copyMsgBtn.addEventListener('click', function () {
      copyText(buildMessage(), copyMsgBtn);
      okNote.classList.add('show');
    });
  }
})();
