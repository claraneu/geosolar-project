//Jquery: Helps me simplify js to enable dropdown. (Everytime I see a dollar-sign)

$(document).ready(function() {
    $('.js-example-basic-single').select2({
        placeholder: "Enter Kommune",
        allowClear: true
    });

   getData(); 
});

//This makes API call to my http trigger using the fetch (used for making http request)

function getData(){

    let url = "https://geosolarapi.azurewebsites.net/api/HttpTrigger3"
    fetch(url)
    .then(response => response.json()) //these two are promises, giving asynchronous behavior, so that the promise first gets resolved when
    .then(data => {
        
        let muni = data.kommuner //data has an array called kommuner that we stored in variable called muni. Then we used an array to iterate that array 
        for (i = 0; i < muni.length; i++) { //According to the documentation (found on select2) the following two lines shows how you add options to the dropdown
            let newOption = new Option(muni[i], muni[i], false, false); //create option object (I think)
            $('#dkmuni').append(newOption).trigger('change');//then we append (=add) that option to the select box (dropdown)
    
          }
          
    });   
    
} 


//This is Jquery saying "give me the item that used the id # and make it so, that when it is clicked, the following funcion will be executed:
$("#user-input").click(function() //use jquery to store three variables in the user-input
{
    let municipalities = $("#dkmuni").val()
    let energy = $("#engcon").val() 
    let household = $("#hh-size").val()

//Validate input
    //This means that nothing was entered by user in these two fields, so warning is displayed
    if (energy == "" && household == "") {
        displayWarning("Please fill out one of the two fields")
        return
    }

    // Needs to be 1 and 5, otherwise warning is triggered and the function is exited
    if  (parseInt(household)>= 5 || parseInt(household) <= 1 ){
        displayWarning("Max. household of 4")
        return
    }
 // Using a function to reuse code: This method we used, is a refactoring method (a extract function) by identifiying code that was almost the same

    if (energy == ""){
        energy = "na" //If there is no input in the energy field, na needs to be send to API to ensure proper calculation
    }

    if (household == ""){
        household = "0" //send 0 to API
    }


    let url = "https://geosolarapi.azurewebsites.net/api/HttpTrigger4?municipalities="+
    municipalities+"&energy="+energy+"&household="+household
    let dataFromApi
    fetch(url)
    .then(response => response.json()) //these two are promises, giving asynchronous behavior, so that the promise first gets resolved when
    .then(data => {
        dataFromApi =data

    }); //The fetch returns a promise (line 13), and we already know its a json file ()
  
    let solarpanels = dataFromApi.solarpanels
    alert(solarpanels)
    let investmentcost = dataFromApi.investmentcost
    alert (investmentcost)
    let breakeven = dataFromApi.breakeven
    alert (breakeven)

  
    //dataFromApi = {"solarpanels": 5, "investmentcost": 3000, "breakeven": 4.5}

    //dataFromApi.solarpanels -> 5 

});



function displayWarning (warningtext) {
    document.getElementById("warningtext").innerHTML = warningtext;
    document.getElementById("warningtext").style.visibility = "visible";
}
//Warning for wrong input - so far,only for household. not working and only for when pushing the button

// document.getElementById("user-input").addEventListener("click", function()
// {
  
// let hhsize = document.getElementById("user-input").value

//     if (hhsize > 4){
//         document.getElementById("warningtext").innerHTML="Max. input allowed: 4"
//         document.getElementById("warningtext").style.visibility="visible";
//         return
//     }
//     alert("Thanks for giving me a valid number")

// })



//INPUT VALIDATION

//document.getElementById("user-input").addEventListener("click", function() //user input button 
