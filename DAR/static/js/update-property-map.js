var markerCoordinates = [24.686708, 46.572200];
var lat = markerCoordinates[0];
var lng = markerCoordinates[1];
var marker;
var map ;
document.addEventListener('DOMContentLoaded',function(){

  let lt= document.getElementById('latInput');
  let lg = document.getElementById('lngInput');
  markerCoordinates[0]=lt.value;
  markerCoordinates[1]=lg.value;
  console.log(markerCoordinates)
  map = L.map('map').setView(markerCoordinates, 13);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">DAR</a>'
}).addTo(map);
marker = L.marker(markerCoordinates).addTo(map);
L.control.locate().addTo(map);
map.on('click', onMapClick);


  
});

// var map = L.map('map').setView(markerCoordinates, 13);
// L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
//     maxZoom: 19,
//     attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">DAR</a>'
// }).addTo(map);



// var marker = L.marker(markerCoordinates).addTo(map)


// L.control.locate().addTo(map);


// marker.on('click',function(event){
//    marker = event.target;
//    console.log(marker.lat)})
   function onMapClick(e) {
    // Remove previous marker if exists
    if (map.hasLayer(marker)) {
        map.removeLayer(marker);
    }
    // Add a new marker at the clicked location
    marker = new L.marker(e.latlng).addTo(map);
    let lt= document.getElementById('latInput');
    let lg = document.getElementById('lngInput');
    lt.value=e.latlng.lat;
    lg.value=e.latlng.lng;
    
    console.log(lt.value); // You can use this position to save it or perform any action
}
// map.on('click', onMapClick);


function openGoogleMaps() {
  var lat = markerCoordinates[0];
  var lng = markerCoordinates[1];
  window.open('https://www.google.com/maps?q=' + lat + ',' + lng, '_blank');
}


