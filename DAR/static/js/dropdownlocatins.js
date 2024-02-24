var jsonData = JSON.parse(document.getElementById('json-data').textContent);
console.log('Data from server:', jsonData);

const citydropwon = document.querySelector('#citySelect');

const dist = document.querySelector('#neighborhoodSelect');

citydropwon.innerHTML =  document.createElement("select");
dist.innerHTML =document.createElement("select");
//var j= document.querySelector('#json-data');
var j = JSON.parse(document.getElementById('json-data').textContent);

document.addEventListener('DOMContentLoaded',function(){
    document.querySelector('#regionSelect').onchange=populatecity();
});

document.addEventListener('DOMContentLoaded',function(){
    document.querySelector('#citySelect').onchange=populatedist();
});




function populatedist() {
    // Get the selected state and city
    var selectedr= document.querySelector('#regionSelect').value;
    var selectedc= document.querySelector('#citySelect').value;
    
    // Get neighborhoods for the selected state and city from the JSON data
    var neighborhoods = j[selectedr][selectedc];
    
    // Populate the neighborhood dropdown list with neighborhoods associated with the selected state and city
    var neighborhoodDropdown = document.getElementById("neighborhoodSelect");
    neighborhoodDropdown.innerHTML = "";
    neighborhoods.forEach(function(neighborhood) {
        var option = document.createElement("option");
        option.text = neighborhood;
        neighborhoodDropdown.add(option);
    });
}

function populatecity() {
    
    var selected = document.querySelector('#regionSelect').value;
    var cities = Object.keys(j[selected]);
    citydropwon.innerHTML = '';
    cities.forEach(function(city) {
        var option = document.createElement("option");
        option.text = city;
        citydropwon.add(option);
    });
}

