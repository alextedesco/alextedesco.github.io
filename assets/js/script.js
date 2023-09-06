document.addEventListener('DOMContentLoaded', function() {
  const progressBar = document.getElementById('progress-bar');
  const headerHeight = document.querySelector('header').offsetHeight;

  window.addEventListener('scroll', function() {
    const windowHeight = window.innerHeight;
    const fullHeight = document.body.clientHeight;
    const scrolled = window.scrollY;
    const width = (scrolled / (fullHeight - windowHeight)) * 100;

    progressBar.style.width = width + '%';
  });

  // Scroll to section and adjust for fixed header
  function scrollToSection(event) {
    event.preventDefault();
    const targetId = this.getAttribute('href');

    if (targetId && targetId !== '#') {
      const targetElement = document.querySelector(targetId);

      if (targetElement) {
        const targetPosition = targetElement.offsetTop - headerHeight;

        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    } else {
      // Scroll to the top when any link with href="#" is clicked
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    }
  }

  // Attach click event to each navigation link
  const navLinks = document.querySelectorAll('nav a[href]');
  navLinks.forEach(function(link) {
    link.addEventListener('click', scrollToSection);
  });

  // Open the Resume link in a new tab when clicked
  const resumeLink = document.getElementById('resume-link');
  resumeLink.addEventListener('click', function(event) {
    event.preventDefault();
    window.open(this.getAttribute('href'), '_blank');
  });
});




var imgList = document.getElementById('imgList');
  var scrollRight = document.getElementById('scroll-right');
  var scrollLeft = document.getElementById('scroll-left');

// When a user clicks on the right arrow, the ul will scroll 750px to the right
  scrollRight.addEventListener('click', (event) => {
    imgList.scrollBy(750, 0);
});

// When a user clicks on the left arrow, the ul will scroll 750px to the left
  scrollLeft.addEventListener('click', (event) => {
    imgList.scrollBy(-750, 0);
});