document.addEventListener('DOMContentLoaded',function(){
    var citydiv = document.getElementById('citydiv');
    var distdiv = document.getElementById('distdiv');
    // s =document.createElement("select");
    // s.add()
    var s = document.createElement("select");
    s.className = "form-control" ;
    s.name = "city";
    s.id ="citySelect";
    s.disabled=true;
    s.required = true ;
    citydiv.append(s);


    s = document.createElement("select");
    s.className = "form-control" ;
    s.name = "neighborhood";
    s.id ="neighborhoodSelect";
    s.disabled=true;
    
    distdiv.append(s);
    // var x = document.getElementById('regionSelect').value;
    // console.log(x)
    document.getElementById('regionSelect').onchange = populatecity;
    document.getElementById('citySelect').onchange = populatedist;

    
});
// function readjson(){
//     console.log('res');
//     fetch("/jdata").then((res) => {
//         if (!res.ok) {
//                 throw new Error(`HTTP error! Status: ${res.status}`);
//             }
// console.log(res.status);
// return res.json();
// })}
function readjson() {
    console.log('Fetching JSON data');
    // Fetch returns a promise, handle it where it's called
    return fetch("/jdata").then(res => {
        if (!res.ok) {
            throw new Error(`HTTP error! Status: ${res.status}`);
        }
        return res.json();
    });
}


function populatecity() {
// console.log('populate');

readjson().then( data => {
var selected = document.getElementById('regionSelect').value;
var cities = Object.keys(data[selected]);
// console.error(cities);
var citydropwon =document.getElementById('citySelect');
citydropwon.innerHTML="";
var option = document.createElement("option");
option.text = 'الرجاءاختيار المدينة';
citydropwon.add(option);
cities.forEach(function(city) {
    var option = document.createElement("option");
    option.text = city;
    option.value = city;

    citydropwon.add(option);
});
var cit = document.getElementById('citySelect');
cit.disabled=false;
var distdropwon =document.getElementById('neighborhoodSelect');
distdropwon.innerHTML="";
distdropwon.disabled=true;

}).catch(error => console.error('Error loading cities:', error));

} 


function populatedist() {
    readjson().then( data => {
        var selectedr = document.getElementById('regionSelect').value;
        var selectedc = document.getElementById('citySelect').value;

        var dist =data[selectedr][selectedc];
        console.log(`${selectedr} and ${selectedc}`)
        var distdropwon =document.getElementById('neighborhoodSelect');
        
        distdropwon.innerHTML="";
        
        var option = document.createElement("option");
            option.text = 'الرجاءاختيار الحي';
            distdropwon.add(option);
        dist.forEach(function(distrect) {
            var option = document.createElement("option");
            option.text = distrect;
            option.value = distrect;
        
            distdropwon.add(option);
        });

        if (distdropwon.length != 1) {
        distdropwon.disabled=false;
        }

        else {
         distdropwon.innerHTML="";
        var option = document.createElement("option");
            option.text = 'لا يوجد احياء في هذه المدينة ';
            distdropwon.add(option);
            distdropwon.disabled=true;}
            
    }
    

        ).catch(error => console.error('Error loading cities:', error));
}

