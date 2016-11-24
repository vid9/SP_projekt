/**
 * Created by vidce on 23. 11. 2016.
 */


function start(){
    document.getElementById("Serija").addEventListener("change", enableModel, false);
    document.getElementById("Znamka").addEventListener("change", enableSerija, false);
    document.getElementById("Model").disabled = true;
    document.getElementById("Serija").disabled = true;
    window.alert("loaded")
    //document.getElementById("Serija").addEventListener("change", enableModel, false);
}

function enableModel(){
    document.getElementById("Model").disabled = false;
    removeOptions(document.getElementById("Model"));
    var audi =  [
        {value: "audi", text: "2017"},
        {value: "audi", text: "Sport"},
        {value: "audi", text: "Premium++"}
    ];
    var bmw=  [
        {value: "bmw", text: "2016"},
        {value: "bmw", text: "2005"},
        {value: "bmw", text: "GTI"}
    ];;
    var volvo=  [
        {value: "volvo", text: "280"},
        {value: "volvo", text: "2017"},
        {value: "volvo", text: "Sport"}
    ];;

    var e = document.getElementById("Serija");
    var text = e.options[e.selectedIndex].value;
    switch (text) {
        case ("audi"):
            var select = document.getElementById('Model'),
                option,
                i = 0,
                il = audi.length;

            for (; i < il; i += 1) {
                option = document.createElement('option');
                option.setAttribute('value', audi[i].value);
                option.appendChild(document.createTextNode(audi[i].text));
                select.appendChild(option);
            }
            break;

        case ("bmw"):
            var select = document.getElementById('Model'),
                option,
                i = 0,
                il = bmw.length;

            for (; i < il; i += 1) {
                option = document.createElement('option');
                option.setAttribute('value', bmw[i].value);
                option.appendChild(document.createTextNode(bmw[i].text));
                select.appendChild(option);
            }
            break;

        case ("volvo"):
            var select = document.getElementById('Model'),
                option,
                i = 0,
                il = volvo.length;

            for (; i < il; i += 1) {
                option = document.createElement('option');
                option.setAttribute('value', volvo[i].value);
                option.appendChild(document.createTextNode(volvo[i].text));
                select.appendChild(option);
            }
            break;
    }
}


function enableSerija() {
    var index = document.getElementById("Serija");
    removeOptions(index);
    removeOptions(document.getElementById("Model"));
    document.getElementById("Serija").disabled = false;
    document.getElementById("Model").disabled = true;
    index.selectedIndex = 0;


    var audi =  [
        {value: "audi", text: "A4"},
        {value: "audi", text: "Q3"},
        {value: "audi", text: "Q5"}
    ];
    var bmw=  [
        {value: "bmw", text: "Car 1"},
        {value: "bmw", text: "Car 2"},
        {value: "bmw", text: "Car 3"}
    ];;
    var volvo=  [
        {value: "volvo", text: "Auto 1"},
        {value: "volvo", text: "Auto 2"},
        {value: "volvo", text: "Auto 3"}
    ];;

    var e = document.getElementById("Znamka");
    var text = e.options[e.selectedIndex].value;

    switch (text) {
        case ("audi"):
            var select = document.getElementById('Serija'),
                option,
                i = 0,
                il = audi.length;

            for (; i < il; i += 1) {
                option = document.createElement('option');
                option.setAttribute('value', audi[i].value);
                option.appendChild(document.createTextNode(audi[i].text));
                select.appendChild(option);
            }
            break;

        case ("bmw"):
            var select = document.getElementById('Serija'),
                option,
                i = 0,
                il = bmw.length;

            for (; i < il; i += 1) {
                option = document.createElement('option');
                option.setAttribute('value', bmw[i].value);
                option.appendChild(document.createTextNode(bmw[i].text));
                select.appendChild(option);
            }
            break;

        case ("volvo"):
            var select = document.getElementById('Serija'),
                option,
                i = 0,
                il = volvo.length;

            for (; i < il; i += 1) {
                option = document.createElement('option');
                option.setAttribute('value', volvo[i].value);
                option.appendChild(document.createTextNode(volvo[i].text));
                select.appendChild(option);
            }
            break;
    }

}


function removeOptions(selectbox)
{
    var i;
    for(i = selectbox.options.length - 1 ; i > 0 ; i--)
    {
        selectbox.remove(i);
    }
}

