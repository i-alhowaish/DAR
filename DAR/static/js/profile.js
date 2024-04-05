let timeoutReference; // Declare this outside your function to make it accessible globally
  
const copyContent = async () => {
  clearTimeout(timeoutReference); // Clear any existing timeout
  try {
    await navigator.clipboard.writeText('Your text to copy');
    document.getElementById('copySuccessMessage').style.display = 'flex'; // Use 'flex' to show the message
    // Hide the message after 5 seconds
    timeoutReference = setTimeout(() => {
      document.getElementById('copySuccessMessage').style.display = 'none';
    }, 5000);
  } catch (err) {
    console.error('Failed to copy: ', err);
  }
}

// Function to close the message
function closeMessage() {
  clearTimeout(timeoutReference); // Clear the timeout
  document.getElementById('copySuccessMessage').style.display = 'none';
}

// Event listener for the close button
document.getElementById('closeMessage').onclick = closeMessage; // Assign the onclick handler