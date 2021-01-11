//Checks the input - 4 digits? - 
//zipcode id     zipcode-input
//button:   enterZipcodeButton


document.getElementById("enterZipcodeButton").addEventListener("click", function()
{
  
  let zipcode = document.getElementById("zipcode-input").value
    //returns value of the zipcode

    //Simulating that we are sending data to the backend

    //Validate zipcode 
    if (isNaN(zipcode)){
        document.getElementById("warningtext").innerHTML  ="Please enter 4-digit zipcode"
        document.getElementById("warningtext").style.visibility="visible"; //this changes the CSS
        return
    }

    if (zipcode.length !== 4){
        document.getElementById("warningtext").innerHTML="Danish zipcodes contain 4 digits"
        document.getElementById("warningtext").style.visibility="visible";
        return
    }
    alert("Thanks for giving me a valid zipcode")

})

