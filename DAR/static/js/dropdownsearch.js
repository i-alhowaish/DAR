document.addEventListener('DOMContentLoaded',function(){
    var regdiv = document.getElementById('regdiv');
    var citydiv = document.getElementById('citydiv');
    var distdiv = document.getElementById('distdiv');
    // s =document.createElement("select");
    // s.add()
    regdiv.innerHTML="";
    citydiv.innerHTML="";
    distdiv.innerHTML="";
    var s = document.createElement("select");
    s.className = "form-control" ;
    s.name = "region";
    s.id ="citySelector";
    regdiv.append(s);

    s = document.createElement("select");
    s.className = "form-control" ;
    s.name = "city";
    s.id ="citySelect";
    s.disabled=true;
    citydiv.append(s);


    s = document.createElement("select");
    s.className = "form-control" ;
    s.name = "neighborhood";
    s.id ="neighborhoodSelect";
    s.disabled=true;
    
    distdiv.append(s);
    // var x = document.getElementById('regionSelect').value;
    // console.log(x)
    populateregion();
    document.getElementById('citySelector').onchange = populatecity;
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

function populateregion(){
    readjson().then(data =>{
        var regions = Object.keys(data);
        var regoininput = document.getElementById('citySelector') ;
        var option = document.createElement("option");
        option.text = 'الرجاءاختيار المنطقة';
        option.value = "";
        regoininput.add(option);
        regions.forEach(function(reg) {
            var option = document.createElement("option");
            option.text = reg;
            option.value = reg;
        
            regoininput.add(option);
        });

    })
}

function populatecity() {
// console.log('populate');
console.log('populate city');
readjson().then( data => {
var selected = document.getElementById('citySelector').value;
var cities;
if (selected == ''){
   cities=[];
}
else{
    cities = Object.keys(data[selected]);
}

// console.error(cities);
var citydropwon =document.getElementById('citySelect');
citydropwon.innerHTML="";
var option = document.createElement("option");
option.text = 'الرجاءاختيار المدينة';
option.value = "";
citydropwon.add(option);
cities.forEach(function(city) {
    var option = document.createElement("option");
    option.text = city;
    option.value = city;

    citydropwon.add(option);
});
if (citydropwon.length == 1){
    citydropwon.innerHTML="";
    citydropwon.disabled=true;
}
else{
    citydropwon.disabled=false;
}
// var cit = document.getElementById('citySelect');
// cit.disabled=false;
var distdropwon =document.getElementById('neighborhoodSelect');
distdropwon.innerHTML="";
distdropwon.disabled=true;


}).catch(error => console.error('Error loading cities:', error));

} 


function populatedist() {
    readjson().then( data => {
        var selectedr = document.getElementById('citySelector').value;
        var selectedc = document.getElementById('citySelect').value;
        let dist;
        if (selectedc ==''){
            console.log(`dist is ${selectedc}`);
           dist=[]; 
        }
        else {
            dist =data[selectedr][selectedc];
        }

         
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
        // var option = document.createElement("option");
        //     option.text = 'لا يوجد احياء';
        //     distdropwon.add(option);
            distdropwon.disabled=true;}
            console.log(distdropwon[0].innerHTML);
            
    }
    

        ).catch(error => console.error('Error loading cities:', error));
}

