// Guard1 - Interactive Features

document.addEventListener('DOMContentLoaded', () => {
  // Mobile Menu Toggle
  const menuToggle = document.querySelector('.menu-toggle');
  const navList = document.querySelector('.nav-list');
  
  if (menuToggle && navList) {
    menuToggle.addEventListener('click', () => {
      const expanded = menuToggle.getAttribute('aria-expanded') === 'true';
      menuToggle.setAttribute('aria-expanded', String(!expanded));
      navList.classList.toggle('show');
    });
  }

  // Reading Progress Bar
  const progressBar = document.getElementById('progressBar');
  
  if (progressBar) {
    window.addEventListener('scroll', () => {
      const windowHeight = window.innerHeight;
      const documentHeight = document.documentElement.scrollHeight - windowHeight;
      const scrollTop = window.scrollY;
      const progress = (scrollTop / documentHeight) * 100;
      progressBar.style.width = progress + '%';
    });
  }

  // Theme Toggle
  const themeToggle = document.getElementById('themeToggle');
  
  if (themeToggle) {
    // Check for saved theme preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
      document.documentElement.setAttribute('data-theme', savedTheme);
      updateThemeButton(savedTheme);
    }
    
    themeToggle.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
      let newTheme;
      
      // Cycle through themes: light -> dark -> silver -> light
      if (currentTheme === 'light') {
        newTheme = 'dark';
      } else if (currentTheme === 'dark') {
        newTheme = 'silver';
      } else {
        newTheme = 'light';
      }
      
      if (newTheme === 'light') {
        document.documentElement.removeAttribute('data-theme');
        localStorage.setItem('theme', 'light');
      } else {
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
      }
      
      updateThemeButton(newTheme);
    });
    
    function updateThemeButton(theme) {
      switch(theme) {
        case 'dark':
          themeToggle.textContent = '⚪ Silver';
          break;
        case 'silver':
          themeToggle.textContent = '☀️ Light';
          break;
        default:
          themeToggle.textContent = '🌙 Dark';
      }
    }
  }

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });
});
