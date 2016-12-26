/**
 * Created by vidce on 13. 11. 2016.
 */
function go() {
    window.location.href = "index.html";
}


function check(form) { /*function to check userid & password*/
    /*the following code checkes whether the entered userid and password are matching*/
    if(form.userid.value != ""/* && form.pswrd.value == "test"*/) {
        if(form.userid.value != "") {/*tip uporabnika osnovni*/
            window.location.href = "suporabnik.html";/*opens the target page while Id & password matches*/
        } else {
            window.open('puporabnik.html','_self')/*opens the target page while Id & password matches*/
        }
    }
    else {
        alert("Error Password or Username")/*displays error message*/
    }
    return true;
}
