function getData(){

    let url = "https://geosolarapi.azurewebsites.net/api/HttpTrigger3"
    let dataFromApi
    fetch(url)
    .then(response => response.json()) //these two are promises, giving asynchronous behavior, so that the promise first gets resolved when
    .then(data => {
        alert(data)
        console.log(data)
        
        let muni = data.kommuner //then plug only gets executed when the 
        for (i = 0; i < muni.length; i++) {
            let newOption = new Option(muni[i], muni[i], false, false); //has two values cause when we select the value it could be something different
            $('#dkmuni').append(newOption).trigger('change');//append data to my select box
    
          }
          
    }); //The fetch returns a promise (line 13), and we already know its a json file ()
  
    
}

//If we make API, we can just exchange code up there

$("#user-input").click(function(){
   
    let municipalities = $("#dk-muni").val()
    let energy = $("#engcon").val() //no input field created yet
    let household = $("#hh-size").val()

    let url = "https://geosolarapi.azurewebsites.net/api/HttpTrigger4?municipalities="+dkmuni+"&energy="+engcon+"&household="+household
    let dataFromApi
    fetch(url)
    .then(response => response.json()) //these two are promises, giving asynchronous behavior, so that the promise first gets resolved when
    .then(data => dataFromApi = data); //The fetch returns a promise (line 13), and we already know its a json file ()
  
    //dataFromApi = {"solarpanels": 5, "investmentcost": 3000, "breakeven": 4.5}

    //dataFromApi.solarpanels -> 5 

});


//Jquery: Helps me simplify js to enable dropdown.

$(document).ready(function() {
    $('.js-example-basic-single').select2({
        placeholder: "Enter Kommune",
        allowClear: true
    });

    let muni  = getData(); 




});




//Warning for wrong input - so far,only for household. not working and only for when pushing the button

document.getElementById("user-input").addEventListener("click", function()
{
  
let hhsize = document.getElementById("user-input").value

    if (hhsize > 4){
        document.getElementById("warningtext").innerHTML="Max. input allowed: 4"
        document.getElementById("warningtext").style.visibility="visible";
        return
    }
    alert("Thanks for giving me a valid number")

})