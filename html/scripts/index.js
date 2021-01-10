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
        alert("This is not a number")
        return
    }

    if (zipcode.length !== 4){
        alert("Please enter a 4-digit Zipcode")
        return
    }
    alert("Thanks for giving me a valid zipcode")

})

