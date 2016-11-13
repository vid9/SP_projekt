/**
 * Created by vidce on 13. 11. 2016.
 */

function check(form) { /*function to check userid & password*/
    /*the following code checkes whether the entered userid and password are matching*/
    if(form.userid.value == "myuserid" && form.pswrd.value == "mypswrd") {
        if(form.userid.value == "osnovni uporabnik") {
            window.open('suporabnik.html')/*opens the target page while Id & password matches*/
        } else {
            window.open('puporabnik.html')/*opens the target page while Id & password matches*/
        }

    }
    else {
        alert("Error Password or Username")/*displays error message*/
    }
}
