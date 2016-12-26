/**
 * Created by vidce on 20. 11. 2016.
 */
function smallBar() {
    var x = document.getElementById("navigation");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}