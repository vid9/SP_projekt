/**
 * Created by vidce on 23. 11. 2016.
 */

function previri() {
    var email = document.getElementById('email').value;
    var telefon = document.getElementById('telefon').value;
    var ime = document.getElementById('ime').value;
    var priimek = document.getElementById('priimek').value;
    var isnum = /^\d+$/.test(telefon);

    if( ime != "" && priimek != "" && email != "" && telefon != "") {
        if(validateEmail(email)== true && isnum == true) {
            window.location.href = "index.html";
        } else {
            alert("Neveljavna številka ali email!")/*displays error message*/
        }
    }
    else {
        console.log(ime);
        console.log(email);
        console.log(priimek);
        console.log(telefon);
        alert("Prosimo vnesite vse podatke!")/*displays error message*/
    }
    return true;
}

function validateEmail(elementValue){
    var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    return emailPattern.test(elementValue);
}

