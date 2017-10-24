function showPosition(position) {
     var xhttp = new XMLHttpRequest();
     xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
         response = JSON.parse(this.responseText);
         document.getElementById('location').value = response.results[0].formatted_address;
        }
      };
      xhttp.open("GET", 'http://maps.googleapis.com/maps/api/geocode/json?latlng='+position.coords.latitude+', '+position.coords.longitude+'+&sensor=true', true);
      xhttp.send();

}
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}