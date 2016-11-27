/**
 * Created by vidce on 22. 11. 2016.
 */

var map;
var directionsDisplay;

function initMap() {

    document.getElementById("Serija").addEventListener("change", enableModel, false);
    document.getElementById("Znamka").addEventListener("change", enableSerija, false);
    document.getElementById("Model").disabled = true;
    document.getElementById("Serija").disabled = true;

    directionsDisplay = new google.maps.DirectionsRenderer;

    var ljubljana = {lat: 46.056946, lng: 14.505751};
    map = new google.maps.Map(document.getElementById('map'), {
        mapTypeControl: false,
        center: ljubljana,
        zoom: 8
    });
    directionsDisplay.setMap(map);

    var origin_input = document.getElementById('origin-input');
    var destination_input = document.getElementById('destination-input');

    var origin_autocomplete = new google.maps.places.Autocomplete(origin_input);
    origin_autocomplete.bindTo('bounds', map);
    var destination_autocomplete =
        new google.maps.places.Autocomplete(destination_input);
    destination_autocomplete.bindTo('bounds', map);
}


function calculateAndDisplayRoute() {
    var directionsService = new google.maps.DirectionsService;
    directionsService.route({
        origin: document.getElementById('origin-input').value,
        destination: document.getElementById('destination-input').value,
        travelMode: 'DRIVING'
    }, function(response, status) {
        if (status === 'OK') {
            directionsDisplay.setDirections(response);
            var route = response.routes[0];
            document.getElementById("dist").innerHTML = "Razdalja: "+Math.round(route.legs[0].distance.value/100)/10+" km";
            document.getElementById("poraba").innerHTML = "Poraba: "+Math.round(((route.legs[0].distance.value/100)/10)*6.6)/100+" l";
        } else {
            window.alert('Directions request failed due to ' + status);
        }
    });
}
