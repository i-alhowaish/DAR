// Creating the map
var map = L.map('map').setView([24.710087, 46.716614], 10);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 1,
    maxZoom: 16,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">DAR</a>'
}).addTo(map);

document.addEventListener('DOMContentLoaded',function(){
  const container = document.getElementById('propertiesdiv');
  container.innerHTML
  

// Loop through each child div
container.childNodes.forEach(child => {
  if (child.nodeType === Node.ELEMENT_NODE) { 
  let id = child.querySelector(".idInput").innerHTML;
  let lt = child.querySelector(".latInput");
  let lg= child.querySelector(".lngInput");
  let price = child.querySelector(".priceInput").innerHTML;
  var markerCoordinates = [lt.innerHTML,lg.innerHTML];
  var lat = markerCoordinates[0];
  var lng = markerCoordinates[1];
  price = cleanprice(parseFloat(price));
  var stepIcon = L.divIcon({
    className: 'custom-icon', // custom class for CSS styling
    html: `
    <div class="listing-div">
      <span>${price}</span></div>'`,
    iconSize: [65, 65], // size of the icon
});




var marker = L.marker(markerCoordinates, {icon: stepIcon});

marker.bindPopup(`اذهب الى <a href="/property_information/${id}" target="_blank">صفحة العقار</a>`);
marker.addTo(map);
}
    // Check if the child is a div
   

});
})

// Icon for 1
// ibrahim start for loop
// var stepIcon = L.divIcon({
//     className: 'custom-icon', // custom class for CSS styling
//     html: `
//     <div class="listing-div">
//       <span>500 الف</span></div>'`,
//     iconSize: [65, 65], // size of the icon
// });

// var markerCoordinates = [24.686708, 46.572200];
// var lat = markerCoordinates[0];
// var lng = markerCoordinates[1];


// var marker = L.marker(markerCoordinates, {icon: stepIcon});

// marker.bindPopup(`اذهب الى <a href="#" target="_blank">صفحة العقار</a>`);
// marker.addTo(map);

// // ibrahim end for loop




// // Icon for 2
// var stepIcon = L.divIcon({
//     className: 'custom-icon', // custom class for CSS styling
//     html: `
//     <div class="listing-div">
//       <span>800 الف</span></div>'`,
//     iconSize: [65, 65], // size of the icon
// });

// var markerCoordinates = [24.728401, 46.649151];
// var lat = markerCoordinates[0];
// var lng = markerCoordinates[1];


// var marker = L.marker(markerCoordinates, {icon: stepIcon});

// marker.bindPopup(`اذهب الى <a href="#" target="_blank">صفحة العقار</a>`); 
// marker.addTo(map);
// marker.on('click', function(ev) { marker.openPopup([markerCoordinates[0]+0.0005, markerCoordinates[1]]) });



// // Icon for 3
// var stepIcon = L.divIcon({
//     className: 'custom-icon', // custom class for CSS styling
//     html: `
//     <div class="listing-div">
//       <span>1 مليون</span></div>'`,
//     iconSize: [65, 65], // size of the icon
// });

// var markerCoordinates = [24.728401, 46.759151];
// var lat = markerCoordinates[0];
// var lng = markerCoordinates[1];


// var marker = L.marker(markerCoordinates, {icon: stepIcon});

// marker.bindPopup(`اذهب الى <a href="#">صفحة العقار</a>`); 
// marker.addTo(map);
// marker.on('click', function(ev) { marker.openPopup([markerCoordinates[0]+0.0005, markerCoordinates[1]]) });




// to know where is location of a click

// var popup = L.popup();

// function onMapClick(e) {
//     popup
//         .setLatLng(e.latlng)
//         .setContent("You clicked the map at " + e.latlng.toString())
//         .openOn(map);
// }

// map.on('click', onMapClick);






L.control.locate().addTo(map);



function cleanprice(price){
  if(price >= 1000000000){
    price = price/1000000000;
    price=price.toFixed(1);
    console.log(price)
    return price=`${price} بليون`;
  }
  if(price >= 1000000){
    price = price/1000000;
    price=price.toFixed(1);
    console.log(price)
    return price=`${price} مليون`;
  }
  if(price >= 1000){
    price = price/1000;
    price=price.toFixed(1);
    console.log(price);
    return price=`${price} الف`;
  }

}

function changeCity() {
  var citySelector = document.getElementById('citySelector');
  var city = citySelector.value;
  var coordinates;

  switch (city) {
    case 'منطقة الرياض':
      coordinates = [24.7136, 46.6753]; // Riyadh coordinates
      break;
    case 'المنطقة الشرقية':
      coordinates = [26.354423, 49.996033]; // Eastern Province (Al Sharqiyah) coordinates
      break;
      case 'منطقة الباحة':
        coordinates = [20.0129, 41.4677]; // Al Bahah
        break;
      case 'منطقة الجوف':
        coordinates = [29.9677, 39.9832]; // Al Jouf
        break;
      case 'منطقة الحدود الشمالية':
        coordinates = [30.1975, 41.6966]; // Northern Borders
        break;
      case 'منطقة القصيم':
        coordinates = [26.2794, 43.766]; // Al Qassim
        break;
      case 'منطقة المدينة المنورة':
        coordinates = [24.4686, 39.6142]; // Medina
        break;
      case 'منطقة تبوك':
        coordinates = [28.3835, 36.5662]; // Tabuk
        break;
      case 'منطقة جازان':
        coordinates = [16.8896, 42.5611]; // Jazan
        break;
      case 'منطقة حائل':
        coordinates = [27.5158, 41.6907]; // Hail
        break;
      case 'منطقة عسير':
        coordinates = [19.9069, 42.5487]; // Asir
        break;
      case 'منطقة مكة المكرمة':
        coordinates = [21.3891, 39.8579]; // Makkah
        break;
      case 'منطقة نجران':
        coordinates = [17.4924, 44.1277]; // Najran
        break;
    default:
      coordinates = [24.7136, 46.6753]; // Default to Riyadh if no match
  }

  map.flyTo(coordinates, 10); // Fly to the selected city location with zoom level 12
}

// Set the map view to Riyadh coordinates by default on page load
window.onload = changeCity;