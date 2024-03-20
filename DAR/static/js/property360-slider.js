document.addEventListener('DOMContentLoaded', function() {
  const panoramas = [];
  const imageContainers = document.querySelectorAll('.image360-container');

  // Initialize all panoramas but don't display them initially
  imageContainers.forEach((container, index) => {
    const panoramaImagePath = container.getAttribute('data-panorama-image');
    const panoramaImage = new PANOLENS.ImagePanorama(panoramaImagePath);
    const viewer = new PANOLENS.Viewer({
      container: container,
      autoRotate: false,
      autoRotateSpeed: 0.3,
      controlBar: false,
    });

    viewer.add(panoramaImage);
    panoramas.push({viewer, container});
    container.style.display = 'none'; // Hide all initially
  });

  // Make the first panorama visible
  if (panoramas.length > 0) {
    panoramas[0].container.style.display = 'block';
  }

  const propertyImage360 = document.querySelector('.property-image360');
  const navigationContainer = document.createElement('div');
  navigationContainer.className = 'panorama-navigation';
  
  // Create left arrow control
  const leftArrow = document.createElement('button');
  leftArrow.innerHTML = '&lt;'; // '<' character
  leftArrow.className = 'panorama-arrow left-arrow';
  
  // Create right arrow control
  const rightArrow = document.createElement('button');
  rightArrow.innerHTML = '&gt;'; // '>' character
  rightArrow.className = 'panorama-arrow right-arrow';
  
  navigationContainer.appendChild(leftArrow);
  navigationContainer.appendChild(rightArrow);
  propertyImage360.appendChild(navigationContainer);

  let currentIndex = 0;

  // Function to switch panorama
  const switchPanorama = (newIndex) => {
    panoramas[currentIndex].container.style.display = 'none'; // Hide current panorama

    currentIndex = newIndex;
    if (currentIndex < 0) {
      currentIndex = panoramas.length - 1; // Loop to last if index is below 0
    } else if (currentIndex >= panoramas.length) {
      currentIndex = 0; // Loop to first if index exceeds length
    }
    panoramas[currentIndex].container.style.display = 'block'; // Show new panorama
  };

  // Event listeners for arrows
  document.querySelector('.left-arrow').addEventListener('click', () => switchPanorama(currentIndex - 1));
  document.querySelector('.right-arrow').addEventListener('click', () => switchPanorama(currentIndex + 1));
});