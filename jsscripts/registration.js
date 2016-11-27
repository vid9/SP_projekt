/**
 * Created by vidce on 13. 11. 2016.
 */
function profil() {
    window.location.href = "profil.html";
}

function start(){
    document.getElementById('capture').addEventListener('change', handleFileSelect, false);
}

function handleFileSelect(evt) {
    var files = evt.target.files; // FileList object
    var reader = new FileReader();
    f = files[0];
    reader.onload = (function(theFile) {
        return function(e) {
            // add thumbnail.
            var img = document.getElementById('output');
            img.src = e.target.result;
        };
    })(f);

    // Read in the image file as a data URL.
    reader.readAsDataURL(f);
}
