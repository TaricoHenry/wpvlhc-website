// Navigation stays visible if JavaScript is unavailable.
const header = document.querySelector('.site-header');
const toggle = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#site-navigation');

if (header && toggle && navigation) {
  const desktop = window.matchMedia('(min-width: 64rem)');
  const setOpen = (open) => {
    toggle.setAttribute('aria-expanded', String(open));
    header.classList.toggle('menu-open', open);
  };

  toggle.hidden = false;
  header.dataset.menuReady = 'true';
  toggle.addEventListener('click', () => {
    setOpen(toggle.getAttribute('aria-expanded') !== 'true');
  });
  navigation.addEventListener('click', (event) => {
    if (event.target.closest('a')) setOpen(false);
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      setOpen(false);
      toggle.focus();
    }
  });
  document.addEventListener('click', (event) => {
    if (!header.contains(event.target)) setOpen(false);
  });
  desktop.addEventListener('change', () => setOpen(false));
}
