/**
 * Created by vidce on 13. 11. 2016.
 */
function add(form) { /*function to add user into system
    /*the following adds user info into page system*/
    if(form.userid.value != "") {
        window.location.href = "index.html";/*reopens main page where new user can login now*/
    }
    else {
        alert("Error! User could not be created.")/*displays error message*/
    }
}