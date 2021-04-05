let nodes = []
let fileContent
let map

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
        $.ajax({
            url: "/result",
            type: "POST",
            // data: JSON.stringify(nodes),
            data: fileContent,
            contentType: "application/json; charset=utf-8",
            success: function(dat) { console.log(dat); }
        });
    })

})

document.getElementById('input-file').addEventListener('change', getFile)

function getFile(event) {
	const input = event.target
    if ('files' in input && input.files.length > 0) {
        fileContent = placeFileContent(input.files[0])
    }
}

function placeFileContent(file) {
	readFileContent(file).then(content => {
        fileContent = content
        console.log(fileContent)
    }).catch(error => console.log(error))
}

function readFileContent(file) {
	const reader = new FileReader()
    return new Promise((resolve, reject) => {
        reader.onload = event => resolve(event.target.result)
        reader.onerror = error => reject(error)
        reader.readAsText(file)
    })
}

