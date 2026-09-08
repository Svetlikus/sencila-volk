(() => {
  'use strict';
  document.documentElement.classList.add('js');
  const hr = document.documentElement.lang === 'hr';
  const words = hr ? {
    menu: 'Izbornik', close: 'Zatvori izbornik',
    type: 'Odaberite fotografiju u formatu JPG, PNG ili WebP.',
    size: 'Ukupna veličina fotografija može biti najviše 10 MB. Odaberite manje fotografije.',
    sending: 'Slanje…', remove: 'Ukloni fotografiju',
    local: 'Za slanje upita otvorite objavljenu stranicu. Možete nam pisati i na info@sencilavolk.si.',
    offline: 'Nema internetske veze. Provjerite vezu i pokušajte ponovno.',
    slow: 'Slanje traje dulje. Ako se stranica ne otvori, provjerite internetsku vezu. Za pomoć nam pišite na info@sencilavolk.si.'
  } : {
    menu: 'Meni', close: 'Zapri meni',
    type: 'Izberite fotografijo v obliki JPG, PNG ali WebP.',
    size: 'Skupna velikost fotografij je lahko največ 10 MB. Izberite manjše fotografije.',
    sending: 'Pošiljanje…', remove: 'Odstrani fotografijo',
    local: 'Za pošiljanje povpraševanja odprite objavljeno stran. Pišete nam lahko tudi na info@sencilavolk.si.',
    offline: 'Ni internetne povezave. Preverite povezavo in poskusite znova.',
    slow: 'Pošiljanje traja dlje. Če se stran ne odpre, preverite internetno povezavo. Za pomoč nam pišite na info@sencilavolk.si.'
  };

  const menu = document.querySelector('[data-menu]');
  const nav = document.getElementById('navigation');
  function closeMenu(returnFocus = false) {
    if (!menu || !nav) return;
    menu.setAttribute('aria-expanded', 'false');
    menu.setAttribute('aria-label', words.menu);
    nav.classList.remove('is-open');
    if (returnFocus) menu.focus();
  }
  menu?.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') !== 'true';
    menu.setAttribute('aria-expanded', String(open));
    menu.setAttribute('aria-label', open ? words.close : words.menu);
    nav.classList.toggle('is-open', open);
  });
  nav?.addEventListener('click', e => { if (e.target.closest('a')) closeMenu(); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeMenu(true); });
  document.addEventListener('click', e => {
    if (menu && nav && !menu.contains(e.target) && !nav.contains(e.target)) closeMenu();
  });
  window.matchMedia('(min-width: 1101px)').addEventListener('change', () => closeMenu());

  const product = document.getElementById('product');
  document.querySelectorAll('[data-product]').forEach(link => {
    link.addEventListener('click', () => {
      if (product) product.value = link.dataset.product;
    });
  });

  const form = document.getElementById('inquiry-form');
  if (!form) return;
  const status = document.getElementById('form-status');
  const files = [...form.querySelectorAll('input[type="file"]')];
  const allowed = new Set(['image/jpeg', 'image/png', 'image/webp']);
  const maxTotal = 10000000;
  let resetTimer;
  const submit = form.querySelector('button[type="submit"]');
  const submitLabel = submit.querySelector('span');
  const originalLabel = submitLabel.textContent;
  const isHosted = /^https?:$/.test(location.protocol);

  function announce(message) {
    status.textContent = message;
    status.hidden = !message;
  }
  function checkFiles() {
    files.forEach(input => input.setCustomValidity(''));
    let total = 0;
    for (const input of files) {
      const file = input.files[0];
      if (!file) continue;
      if (!allowed.has(file.type)) {
        input.setCustomValidity(words.type);
        return words.type;
      }
      total += file.size;
    }
    if (total > maxTotal) {
      files.find(input => input.files.length)?.setCustomValidity(words.size);
      return words.size;
    }
    return '';
  }
  files.forEach(input => {
    const row = input.closest('.file-row');
    const remove = row.querySelector('button');
    const name = row.querySelector('[data-filename]');
    const emptyLabel = name.textContent;
    input.addEventListener('change', () => {
      const file = input.files[0];
      name.textContent = file ? file.name : emptyLabel;
      remove.hidden = !file;
      row.classList.toggle('has-file', !!file);
      announce(checkFiles());
    });
    remove.addEventListener('click', () => {
      input.value = '';
      name.textContent = emptyLabel;
      remove.hidden = true;
      row.classList.remove('has-file');
      announce(checkFiles());
      input.focus();
    });
  });

  if (isHosted) {
    for (const [name, value] of Object.entries({
      _next: new URL('hvala.html', location.href).href,
      _url: location.href.split('#')[0]
    })) {
      const input = document.createElement('input');
      input.type = 'hidden';
      input.name = name;
      input.value = value;
      form.append(input);
    }
  }
  function restoreSubmit() {
    clearTimeout(resetTimer);
    submit.disabled = false;
    submit.removeAttribute('aria-busy');
    submitLabel.textContent = originalLabel;
  }
  window.addEventListener('pageshow', restoreSubmit);
  form.addEventListener('submit', e => {
    const error = checkFiles();
    if (!isHosted || !navigator.onLine || error) {
      e.preventDefault();
      announce(!isHosted ? words.local : !navigator.onLine ? words.offline : error);
      status.focus();
      return;
    }
    announce('');
    submit.disabled = true;
    submit.setAttribute('aria-busy', 'true');
    submitLabel.textContent = words.sending;
    // Native multipart POST keeps photographs intact and uses FormSubmit's
    // verification/error pages. No success state is simulated in the browser.
    resetTimer = setTimeout(() => {
      restoreSubmit();
      announce(words.slow);
    }, 45000);
  });
})();
