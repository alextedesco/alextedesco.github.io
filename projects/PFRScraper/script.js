const label = document.querySelector('.label');
const options = document.getElementById('options');

options.addEventListener('change', function() {
  const selectedOption = this.options[this.selectedIndex];
  const teamName = selectedOption.textContent;

  if (teamName) {
    label.textContent = 'Select a team: ' + teamName;
  } else {
    label.textContent = 'Select a team:';
  }
});

// Set default label text
label.textContent = 'Select a team: ' + options.options[0].textContent;
