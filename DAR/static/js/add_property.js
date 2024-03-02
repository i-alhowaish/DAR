let currentFiles = []; // Mutable array to track current file selection

document.getElementById('inp_images').addEventListener('change', function(event) {
    updateFileArray(event.target.files);
    renderPreviews();
});

function updateFileArray(newFiles) {
    // Append new files to the currentFiles array
    currentFiles = []
    currentFiles = currentFiles.concat(Array.from(newFiles));
}

function renderPreviews() {
    const previewContainer = document.getElementById('img_box');
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
    currentFiles360 = []
    currentFiles360 = currentFiles360.concat(Array.from(newFiles));
}

function renderPreviews360() {
  
    const previewContainer = document.getElementById('img_box360');
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



// //---> Get Images360
// let images360 = [];
// function img_select360() {
//   let image = document.getElementById("inp_images360").files;

//   for (i = 0; i < image.length; i++) {
//     images360.push({
//       name: image[i].name,
//       url: URL.createObjectURL(image[i]),
//       file: image[i],
//     });
//   }
//   document.getElementById("form").reset();
//   document.getElementById("img_box360").innerHTML = img_show360();
// }

// //---> Show Images360
// function img_show360() {
//   let image = "";
//   if (images360.length > 0) {
//     images360.forEach((i) => {
//       image += `<div class="col img-card">
//       <img src="${i.url}">
//       <span>
//       <i class="fa-solid fa-xmark" onclick="delete_img360(${images360.indexOf(
//         i
//       )})"></i>
//       </span>
//     </div>`;
//     });
//     return image;
//   } else {
//     let emptyImgMsg = (document.querySelector(
//       "#img_box360"
//     ).innerHTML = `<h6 class="empty-hd">لا توجد صور الان</h6>`);

//     return emptyImgMsg;
//   }
// }

// function delete_img360(e) {
//   images360.splice(e, 1);
//   document.getElementById("img_box360").innerHTML = img_show360();
// }
