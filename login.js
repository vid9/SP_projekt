/**
 * Created by vidce on 13. 11. 2016.
 */

function check(form) { /*function to check userid & password*/
    /*the following code checkes whether the entered userid and password are matching*/
    if(form.userid.value == "myuserid" && form.pswrd.value == "mypswrd") {
        window.open('target.html')/*opens the target page while Id & password matches*/
    }
    else {
        alert("Error Password or Username")/*displays error message*/
    }
}
