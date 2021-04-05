let nodes = []
let map;

function addMarker(props){
    var marker = new google.maps.Marker({
        position: props.coor,
        map: map
    })
}

function clearMarkers() {
    setMapOnAll(null);
}

// Sets the map on all markers in the array.
function setMapOnAll(map) {
for (let i = 0; i < markers.length; i++) {
    markers[i].setMap(map);
}
}

// Deletes all markers in the array by removing references to them.
function deleteMarkers() {
    clearMarkers();
    nodes = [];
}

function initMap() {

    var options = {
        zoom: 15,
        center: {lat:  -6.175392, lng: 106.827153}
    }

    map = new google.maps.Map(document.getElementById('map'), options)

    // This event listener will call addMarker() when the map is clicked.
    google.maps.event.addListener(map, "click", function(event){
        addMarker({coor: event.latLng});
        nodes.push(JSON.stringify(event.latLng.toJSON(), null, 2))
    });

    // google.maps.event.addListener(map, 'click',
    // function(event){
    //     addMarker({coor:event.latLng})
    //     nodes.push([event.latLng["lat"], event.latLng["lng"]])
    // })
    
}



// document.getElementById("clear").onclick = deleteMarkers()

$(document).ready(function() {
    $('#submit').click(function(event) {
        // $.post('result', nodes, function() {console.log("ok")})
        // event.preventDefault();
        console.log(JSON.stringify(nodes))
        $.ajax({
            url: "/result",
            type: "POST",
            data: JSON.stringify(nodes),
            contentType: "application/json; charset=utf-8",
            success: function(dat) { console.log(dat); }
        });
    })

})
