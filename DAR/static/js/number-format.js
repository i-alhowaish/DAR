addEventListener("DOMContentLoaded", () => {

  $(function(){
    $("#size-from").keyup(function(e){
      $(this).val(format($(this).val()));
    });
    $("#size-to").keyup(function(e){
      $(this).val(format($(this).val()));
    });
    $("#price-from").keyup(function(e){
      $(this).val(format($(this).val()));
    });
    $("#price-to").keyup(function(e){
      $(this).val(format($(this).val()));
    });


  });
  var format = function(num){
    var str = num.toString().replace("", ""), parts = false, output = [], i = 1, formatted = null;
    if(str.indexOf(".") > 0) {
      parts = str.split(".");
      str = parts[0];
    }
    str = str.split("").reverse();
    for(var j = 0, len = str.length; j < len; j++) {
      if(str[j] != ",") {
        output.push(str[j]);
        if(i%3 == 0 && j < (len - 1)) {
          output.push(",");
        }
        i++;
      }
    }
    formatted = output.reverse().join("");
    return("" + formatted + ((parts) ? "." + parts[1].substr(0, 2) : ""));
  };

});



function maxLengthCheck(object) {
  if (object.value.length > object.max.length)
    object.value = object.value.slice(0, object.max.length)
}
  
function isNumeric (evt) {
  var theEvent = evt || window.event;
  var key = theEvent.keyCode || theEvent.which;
  key = String.fromCharCode (key);
  var regex = /[0-9]|\./;
  if ( !regex.test(key) ) {
    theEvent.returnValue = false;
    if(theEvent.preventDefault) theEvent.preventDefault();
  }
}



