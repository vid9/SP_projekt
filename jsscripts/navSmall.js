/**
 * Created by vidce on 20. 11. 2016.
 */
function smallBar() {
    var x = document.getElementById("navSmall");
    if (x.className.indexOf("show") == -1) {
        x.className += " show";
    } else {
        x.className = x.className.replace(" show", "");
    }
}