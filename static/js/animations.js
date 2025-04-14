document.addEventListener('DOMContentLoaded', () => {
  const revealElements = document.querySelectorAll('.reveal');

  const revealOnScroll = () => {
    const windowHeight = window.innerHeight;

    revealElements.forEach((el) => {
      const elementTop = el.getBoundingClientRect().top;

      if (elementTop < windowHeight - 100) {
        el.classList.add('visible');
      }
    });
  };

  window.addEventListener('scroll', revealOnScroll);
  revealOnScroll(); // Run on load too
});
