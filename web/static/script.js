let nodes = []
let fileContent

$(document).ready(function() {
    $('#submit').click(function(event) {
        // $.post('result', nodes, function() {console.log("ok")})
        // event.preventDefault();
        $.ajax({
            url: "/search",
            type: "POST",
            // data: JSON.stringify(nodes),
            data: fileContent,
            contentType: "application/json; charset=utf-8"
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

