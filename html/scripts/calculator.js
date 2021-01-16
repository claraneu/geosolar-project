function getData(){
    let muni = ["København","Aarhus","Køge"];

    return muni;
}

//If we make API, we can just exchange code up there

$("#user-input").click(function(){
    alert("Text: " + $("#hh-size").val());
    let url = 

    fetch('https://geosolarapi.azurewebsites.net/api/HttpTrigger3?municipalities=test&energy=test&household=test')
    .then(response => response.json()) //these two are promises, giving asynchronous behavior, so that the promise first gets resolved when
    .then(data => alert(data)); //The fetch returns a promise (line 13), and we already know its a json file ()

  });


//Jquery: Helps me simplify js to enable dropdown.

$(document).ready(function() {
    $('.js-example-basic-single').select2({
        placeholder: "Enter Kommune",
        allowClear: true
    });

    let muni  = getData(); 

    for (i = 0; i < muni.length; i++) {
        let newOption = new Option(muni[i], muni[i], false, false); //has two values cause when we select the value it could be something different
        $('#dkmuni').append(newOption).trigger('change');//append data to my select box

      }


});




//dkmuni


