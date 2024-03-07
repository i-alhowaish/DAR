// let currentFiles = []; // Array to track current standard images
// let currentFiles360 = []; // Array to track current 360-degree images

// // Event listener for standard image file input changes
// document.getElementById('inp_images').addEventListener('change', function(event) {
//     handleNewFiles(event.target.files, currentFiles, 'img_box');
// });

// // Event listener for 360-degree image file input changes
// document.getElementById('inp_images360').addEventListener('change', function(event) {
//     handleNewFiles(event.target.files, currentFiles360, 'img_box360');
// });

// // Function to handle new file selections and add them to the appropriate array
// function handleNewFiles(files, currentArray, previewBoxId) {
//     Array.from(files).forEach(file => {
//         const reader = new FileReader();

//         reader.onload = function(e) {
//             const imageObject = {
//                 id: 'temp' + Math.random().toString().substr(2, 8), // Generate a temporary ID
//                 url: e.target.result, // Data URL for preview
//                 file: file, // The original file object
//                 type: 'new' // Mark as a new file
//             };

//             currentArray.push(imageObject);
//             const dataTransfer = new DataTransfer();
//             currentArray.forEach(file => dataTransfer.items.add(file));

//             document.getElementById('inp_images').files = dataTransfer.files;
//             renderPreviews(currentArray, previewBoxId); // Update previews
//         };

//         //reader.readAsDataURL(file);
//     });
// }

// // Function to render image previews
// function renderPreviews(files, previewBoxId) {
//     const previewContainer = document.getElementById(previewBoxId);
//     previewContainer.innerHTML = ''; // Clear existing previews

//     files.forEach((image, index) => {
//         const previewWrapper = document.createElement('div');
//         previewWrapper.innerHTML = `
//             <img src="${image.url}" alt="Image Preview" style="width: 100px; height: 100px;">
//             <span> <i class="fa-solid fa-xmark" onclick="removeImage('${image.id}', '${previewBoxId}')"> </i> </span>
//         `;
//         previewContainer.appendChild(previewWrapper);
//     });
// }

// // Function to remove an image from the array and update previews
// function removeImage(imageId, previewBoxId) {
//     if (previewBoxId === 'img_box') {
//         currentFiles = currentFiles.filter(image => image.id !== imageId);
//         renderPreviews(currentFiles, 'img_box');
//     } else if (previewBoxId === 'img_box360') {
//         currentFiles360 = currentFiles360.filter(image => image.id !== imageId);
//         renderPreviews(currentFiles360, 'img_box360');
//     }
// }

// // Example usage to load existing images into the arrays (replace with your actual existing images data)
// document.addEventListener('DOMContentLoaded', function() {
//     // Load existing images for illustration; replace these with actual server-sent data
//     document.querySelectorAll('#existingImages .existing-image-wrapper').forEach(imgWrapper => {
//         const imageId = imgWrapper.getAttribute('data-image-id');
//         const imgUrl = imgWrapper.querySelector('img').src;
//         currentFiles.push({ id: imageId, url: imgUrl, type: 'existing' });
//     });

//     // Load existing 360 images into the currentFiles360 array
//     document.querySelectorAll('#existingImages360 .existing-image360-wrapper').forEach(imgWrapper => {
//         const imageId = imgWrapper.getAttribute('data-image-id');
//         const imgUrl = imgWrapper.querySelector('img').src;
//         currentFiles360.push({ id: imageId, url: imgUrl, type: 'existing' });
//     });
//     //handleNewFiles(currentFiles, currentFiles, 'img_box')
//     renderPreviews(currentFiles, 'img_box');
//     renderPreviews(currentFiles360, 'img_box360');
// });




// new adjusments





let currentFiles = []; // Mutable array to track current file selection
// document.addEventListener('DOMContentLoaded', function() {
// var deletionField = document.createElement('input');
// deletionField.type = 'hidden';
// deletionField.id='delete';
// document.getElementById('form').appendChild(deletionField);
// }


let existing_images = [];
let existing_images360 = [];

document.getElementById('inp_images').addEventListener('change', function(event) {
    updateFileArray(event.target.files);
    renderPreviews();
});
function renderexcist(files, previewBoxId) {
    const previewContainer = document.getElementById(previewBoxId);
    previewContainer.innerHTML = ''; // Clear existing previews
    if (files.length == 0){
        previewContainer.remove();
        return
    }

    files.forEach((image, index) => {
        const previewWrapper = document.createElement('div');
        previewWrapper.classList.add('col');
        previewWrapper.classList.add('img-card');
        previewWrapper.innerHTML = `
            <img src="${image.url}" alt="Preview Image">
            <span> <i class="fa-solid fa-xmark" onclick="removeImage('${image.id}', '${previewBoxId}')"> </i> </span>
        `;
        previewContainer.appendChild(previewWrapper);
    });
}


document.addEventListener('DOMContentLoaded', function() {
    // Load existing images for illustration; replace these with actual server-sent data
    document.querySelectorAll('#existingImages .existing-image-wrapper').forEach(imgWrapper => {
        const imageId = imgWrapper.getAttribute('data-image-id');
        const imgUrl = imgWrapper.querySelector('img').src;
        existing_images.push({ id: imageId, url: imgUrl, type: 'existing' });
    });

    // Load existing 360 images into the currentFiles360 array
    document.querySelectorAll('#existingImages360 .existing-image360-wrapper').forEach(imgWrapper => {
        const imageId = imgWrapper.getAttribute('data-image-id');
        const imgUrl = imgWrapper.querySelector('img').src;
        existing_images360.push({ id: imageId, url: imgUrl, type: 'existing' });
    });
    //handleNewFiles(currentFiles, currentFiles, 'img_box')
    renderexcist(existing_images, 'existingImages');
    renderexcist(existing_images360, 'existingImages360');
});

function removeImage(imageId, previewBoxId) {
    if (previewBoxId === 'existingImages') {
        existing_images = existing_images.filter(image => image.id !== imageId);
        const deletionField = document.createElement('input');
        deletionField.type = 'hidden';
        deletionField.name = 'delete_images';
        deletionField.value = imageId;
        
        document.getElementById('form').appendChild(deletionField);
        renderexcist(existing_images, 'existingImages');
        
        
    } else if (previewBoxId === 'existingImages360') {
        existing_images360 = existing_images360.filter(image => image.id !== imageId);
        const deletionField360 = document.createElement('input');
        deletionField360.type = 'hidden';
        deletionField360.name = 'delete_images360';
        deletionField360.value = imageId;
        document.getElementById('form').appendChild(deletionField360);
        renderexcist(existing_images360, 'existingImages360');
    }

}



function updateFileArray(newFiles) {
    // Append new files to the currentFiles array
    //currentFiles = []
    currentFiles = currentFiles.concat(Array.from(newFiles));
    console.log(currentFiles);
    const dataTransfer = new DataTransfer();
    currentFiles.forEach(file => dataTransfer.items.add(file));
    document.getElementById('inp_images').files = dataTransfer.files;
}




function renderPreviews() {
    const previewContainer = document.getElementById('newimages');
    previewContainer.innerHTML = ''; // Clear existing previews
    
    currentFiles.forEach((file, index) => {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            const previewWrapper = document.createElement('div');
            previewWrapper.classList.add('col');
            previewWrapper.classList.add('img-card');
            
            previewWrapper.innerHTML = `
                <img src="${e.target.result}" alt="Preview Image">
                <span> <i class="fa-solid fa-xmark" onclick="deleteImage(${index})"> </i> </span>
            `;  
            previewContainer.appendChild(previewWrapper);
        };

        reader.readAsDataURL(file);
    });
}

function deleteImage(index) {
    // Remove the file at the specified index
    currentFiles.splice(index, 1);

    // Update the file input to reflect the changes
    const dataTransfer = new DataTransfer();
    currentFiles.forEach(file => dataTransfer.items.add(file));
    document.getElementById('inp_images').files = dataTransfer.files;

    // Re-render the previews
    renderPreviews();
}



let currentFiles360 = []; // Mutable array to track current file selection

document.getElementById('inp_images360').addEventListener('change', function(event) {
    updateFileArray360(event.target.files);
    renderPreviews360();
});

function updateFileArray360(newFiles) {
    // Append new files to the currentFiles360 array
    //currentFiles360 = []
    currentFiles360 = currentFiles360.concat(Array.from(newFiles));
    const dataTransfer = new DataTransfer();
    currentFiles360.forEach(file => dataTransfer.items.add(file));
    document.getElementById('inp_images360').files = dataTransfer.files;
}

function renderPreviews360() {
  
    const previewContainer = document.getElementById('newimages360');
    previewContainer.innerHTML = ''; // Clear existing previews
    
    currentFiles360.forEach((file, index) => {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            const previewWrapper = document.createElement('div');
            previewWrapper.classList.add('col');
            previewWrapper.classList.add('img-card');
            
            previewWrapper.innerHTML = `
                <img src="${e.target.result}" alt="Preview Image">
                <span> <i class="fa-solid fa-xmark" onclick="deleteImage360(${index})"> </i> </span>
            `;  
            previewContainer.appendChild(previewWrapper);
        };

        reader.readAsDataURL(file);
    });
}

function deleteImage360(index) {
    // Remove the file at the specified index
    currentFiles360.splice(index, 1);

    // Update the file input to reflect the changes
    const dataTransfer = new DataTransfer();
    currentFiles360.forEach(file => dataTransfer.items.add(file));
    document.getElementById('inp_images360').files = dataTransfer.files;

    // Re-render the previews
    renderPreviews360();
}
