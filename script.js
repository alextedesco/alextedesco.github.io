document.addEventListener('DOMContentLoaded', function() {
    const progressBar = document.getElementById('progress-bar');
  
    window.addEventListener('scroll', function() {
      const windowHeight = window.innerHeight;
      const fullHeight = document.body.clientHeight;
      const scrolled = window.scrollY;
      const width = (scrolled / (fullHeight - windowHeight)) * 100;
  
      progressBar.style.width = width + '%';
    });
  });