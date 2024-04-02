// var markerCoordinates = [24.686708, 46.572200];
// var lat = markerCoordinates[0];
// var lng = markerCoordinates[1];

// var map = L.map('map').setView(markerCoordinates, 13);
// L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
//     maxZoom: 19,
//     attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">DAR</a>'
// }).addTo(map);



// var marker = L.marker(markerCoordinates).addTo(map).bindPopup(`اذهب الى <a href="https://www.google.com/maps?q=${lat}, ${lng}" target="_blank">قوقل ماب</a>`)
// .openPopup();




function openGoogleMaps() {
  var lat = markerCoordinates[0];
  var lng = markerCoordinates[1];
  window.open('https://www.google.com/maps?q=' + lat + ',' + lng, '_blank');
}




var markerCoordinates = [24.686708, 46.572200];
var lat = markerCoordinates[0];
var lng = markerCoordinates[1];
var marker;
var map ;
document.addEventListener('DOMContentLoaded',function(){

  let lt= document.getElementById('latInput');
  let lg = document.getElementById('lngInput');
  markerCoordinates[0]=lt.innerHTML;
  markerCoordinates[1]=lg.innerHTML;
  lat = markerCoordinates[0];
  lng = markerCoordinates[1];
  console.log(markerCoordinates)
  map = L.map('map').setView(markerCoordinates, 13);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">DAR</a>'
}).addTo(map);
marker =  L.marker(markerCoordinates).addTo(map).bindPopup(`اذهب الى <a href="https://www.google.com/maps?q=${lat}, ${lng}" target="_blank">قوقل ماب</a>`)
.openPopup();




  
});
