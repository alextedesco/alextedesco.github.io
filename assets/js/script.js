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

  document.addEventListener('DOMContentLoaded', function() {
    const headerHeight = document.querySelector('header').offsetHeight;
  
    // Scroll to section and adjust for fixed header
    function scrollToSection(event) {
      event.preventDefault();
      const targetId = this.getAttribute('href');
      const targetPosition = targetId === '#' ? 0 : document.querySelector(targetId).offsetTop - headerHeight;
  
      window.scrollTo({
        top: targetPosition,
        behavior: 'smooth'
      });
    }
  
    // Attach click event to each navigation link
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(function(link) {
      link.addEventListener('click', scrollToSection);
    });
  });