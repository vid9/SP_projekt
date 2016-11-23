/**
 * Created by vidce on 22. 11. 2016.
 */

var map;

function CenterControl(controlDiv, map) {

    // Set CSS for the control border.
    var controlUI = document.createElement('div');
    controlUI.style.backgroundColor = '#4CAF50';
    controlUI.style.border = '10px';
    controlUI.style.cursor = 'pointer';
    controlUI.style.textAlign = 'center';
    controlUI.title = 'Izračunaj razdaljo med podanima krajema';
    controlDiv.appendChild(controlUI);

    // Set CSS for the control interior.
    var controlText = document.createElement('div');
    controlText.style.color = 'rgb(25,25,25)';
    controlText.style.fontFamily = 'Arial';
    controlText.style.fontSize = '16px';
    controlText.style.lineHeight = '38px';
    controlText.style.paddingLeft = '5px';
    controlText.style.paddingRight = '5px';
    controlText.innerHTML = 'Izračunaj';
    controlUI.appendChild(controlText);

    // Setup the click event listeners: calculate the distance between places.
    controlUI.addEventListener('click', function () {
        calculateDistance();
    });
}


function initMap() {
    var origin_place_id = null;
    var destination_place_id = null;
    var ljubljana = {lat: 46.056946, lng: 14.505751};
    map = new google.maps.Map(document.getElementById('map'), {
        mapTypeControl: false,
        center: ljubljana,
        zoom: 8
    });

    var centerControlDiv = document.createElement('div');
    var centerControl = new CenterControl(centerControlDiv, map);

    centerControlDiv.index = 1;
    map.controls[google.maps.ControlPosition.TOP_RIGHT].push(centerControlDiv);

    google.maps.event.addDomListener(window,"load", calculateDistance);

    var travel_mode = 'DRIVING'
    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    directionsDisplay.setMap(map);


    var origin_input = document.getElementById('origin-input');
    var destination_input = document.getElementById('destination-input');

    map.controls[google.maps.ControlPosition.TOP_LEFT].push(origin_input);
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(destination_input);

    var origin_autocomplete = new google.maps.places.Autocomplete(origin_input);
    origin_autocomplete.bindTo('bounds', map);
    var destination_autocomplete =
        new google.maps.places.Autocomplete(destination_input);
    destination_autocomplete.bindTo('bounds', map);


    function expandViewportToFitPlace(map, place) {
        if (place.geometry.viewport) {
            map.fitBounds(place.geometry.viewport);
        } else {
            map.setCenter(place.geometry.location);
            map.setZoom(17);
        }
    }

    origin_autocomplete.addListener('place_changed', function() {
        var place = origin_autocomplete.getPlace();
        if (!place.geometry) {
            window.alert("Autocomplete's returned place contains no geometry");
            return;
        }
        expandViewportToFitPlace(map, place);

        // If the place has a geometry, store its place ID and route if we have
        // the other place ID
        origin_place_id = place.place_id;
        route(origin_place_id, destination_place_id, travel_mode,
            directionsService, directionsDisplay);
    });

    destination_autocomplete.addListener('place_changed', function() {
        var place = destination_autocomplete.getPlace();
        if (!place.geometry) {
            window.alert("Autocomplete's returned place contains no geometry");
            return;
        }
        expandViewportToFitPlace(map, place);

        // If the place has a geometry, store its place ID and route if we have
        // the other place ID
        destination_place_id = place.place_id;
        route(origin_place_id, destination_place_id, travel_mode,
            directionsService, directionsDisplay);
    });

    function route(origin_place_id, destination_place_id, travel_mode,
                   directionsService, directionsDisplay) {
        if (!origin_place_id || !destination_place_id) {
            return;
        }
        directionsService.route({
            origin: {'placeId': origin_place_id},
            destination: {'placeId': destination_place_id},
            travelMode: 'DRIVING'
        }, function(response, status) {
            if (status === 'OK') {
                directionsDisplay.setDirections(response);
            } else {
                window.alert('Directions request failed due to ' + status);
            }
        });
    }
}

function calculateDistance(){
    var origin = document.getElementById("origin-input").value;
    var destination = document.getElementById("destination-input").value;
    var service = new google.maps.DistanceMatrixService();
    service.getDistanceMatrix(
        {
            origins: [origin],
            destinations: [destination],
            travelMode: google.maps.TravelMode.DRIVING,
            avoidHighways: false,
            avoidTolls: false,
            unitSystem: google.maps.UnitSystem.IMPERIAL
        },
        callback
    );
}

function callback(response, status) {
    var orig = document.getElementById("origin-input"),
        dest = document.getElementById("destination-input"),
        dist = document.getElementById("dist");

    try{
        if(status=="OK") {
            orig.value = response.originAddresses[0];
            dest.value = response.destinationAddresses[0];
            dist.value = toFixed((response.rows[0].elements[0].distance.value)/1000,1);
        } else {
            alert("Error: " + status);
        }
    }catch(e){
        if(e){
            // If fails, Do something else
        }
    }
}

function toFixed(value, precision) {
    var precision = precision || 0,
        power = Math.pow(10, precision),
        absValue = Math.abs(Math.round(value * power)),
        result = (value < 0 ? '-' : '') + String(Math.floor(absValue / power));

    if (precision > 0) {
        var fraction = String(absValue % power),
            padding = new Array(Math.max(precision - fraction.length, 0) + 1).join('0');
        result += '.' + padding + fraction;
    }
    return result;
}
