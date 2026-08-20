(() => {
  const script = document.currentScript;
  if (script?.src && !document.getElementById('ras-refinements')) {
    const polish = document.createElement('link');
    polish.id = 'ras-refinements';
    polish.rel = 'stylesheet';
    polish.href = new URL('../css/refinements.css', script.src).href;
    document.head.appendChild(polish);
  }

  const menuButton = document.querySelector('[data-menu-toggle]');
  const nav = document.querySelector('[data-nav]');

  if (menuButton && nav) {
    menuButton.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      menuButton.setAttribute('aria-expanded', String(open));
    });

    nav.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        nav.classList.remove('open');
        menuButton.setAttribute('aria-expanded', 'false');
      });
    });

    document.addEventListener('click', (event) => {
      if (!nav.classList.contains('open')) return;
      if (nav.contains(event.target) || menuButton.contains(event.target)) return;
      nav.classList.remove('open');
      menuButton.setAttribute('aria-expanded', 'false');
    });
  }

  const revealEls = document.querySelectorAll('[data-reveal]');
  if ('IntersectionObserver' in window && revealEls.length) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -24px 0px' });
    revealEls.forEach((el) => observer.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add('is-visible'));
  }

  document.querySelectorAll('[data-year]').forEach((el) => {
    el.textContent = new Date().getFullYear();
  });

  const chips = document.querySelectorAll('[data-filter]');
  const items = document.querySelectorAll('[data-topic]');
  const count = document.querySelector('[data-filter-count]');

  const updateCount = () => {
    if (!count) return;
    const visible = [...items].filter((item) => !item.hidden).length;
    count.textContent = `${visible} ${visible === 1 ? 'material' : 'materiais'}`;
  };

  if (chips.length && items.length) {
    chips.forEach((chip) => {
      chip.addEventListener('click', () => {
        chips.forEach((c) => c.classList.remove('active'));
        chip.classList.add('active');
        const filter = chip.dataset.filter;
        items.forEach((item) => {
          item.hidden = filter !== 'all' && item.dataset.topic !== filter;
        });
        updateCount();
      });
    });
    updateCount();
  }
})();
