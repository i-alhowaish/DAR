//---> Get Images
let images = [];
function img_select() {
  let image = document.getElementById("inp_images").files;

  for (i = 0; i < image.length; i++) {
    images.push({
      name: image[i].name,
      url: URL.createObjectURL(image[i]),
      file: image[i],
    });
  }
  document.getElementById("form").reset();
  document.getElementById("img_box").innerHTML = img_show();
}

//---> Show Images
function img_show() {
  let image = "";
  if (images.length > 0) {
    images.forEach((i) => {
      image += `<div class="col img-card">
      <img src="${i.url}">
      <span>
      <i class="fa-solid fa-xmark" onclick="delete_img(${images.indexOf(
        i
      )})"></i>
      </span>
    </div>`;
    });
    return image;
  } else {
    let emptyImgMsg = (document.querySelector(
      "#img_box"
    ).innerHTML = `<h6 class="empty-hd">لا توجد صور الان</h6>`);

    return emptyImgMsg;
  }
}

function delete_img(e) {
  images.splice(e, 1);
  document.getElementById("img_box").innerHTML = img_show();
}



//---> Get Images360
let images360 = [];
function img_select360() {
  let image = document.getElementById("inp_images360").files;

  for (i = 0; i < image.length; i++) {
    images360.push({
      name: image[i].name,
      url: URL.createObjectURL(image[i]),
      file: image[i],
    });
  }
  document.getElementById("form").reset();
  document.getElementById("img_box360").innerHTML = img_show360();
}

//---> Show Images360
function img_show360() {
  let image = "";
  if (images360.length > 0) {
    images360.forEach((i) => {
      image += `<div class="col img-card">
      <img src="${i.url}">
      <span>
      <i class="fa-solid fa-xmark" onclick="delete_img360(${images360.indexOf(
        i
      )})"></i>
      </span>
    </div>`;
    });
    return image;
  } else {
    let emptyImgMsg = (document.querySelector(
      "#img_box360"
    ).innerHTML = `<h6 class="empty-hd">لا توجد صور الان</h6>`);

    return emptyImgMsg;
  }
}

function delete_img360(e) {
  images360.splice(e, 1);
  document.getElementById("img_box360").innerHTML = img_show360();
}
