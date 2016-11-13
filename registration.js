/**
 * Created by vidce on 13. 11. 2016.
 */
function add(form) { /*function to add user into system
    /*the following adds user info into page system*/
    if(form.userid.value != "current_values") {
        window.open('index.html',_self)/*opens the target page while Id & password matches*/
    }
    else {
        alert("Error Username")/*displays error message*/
    }
}