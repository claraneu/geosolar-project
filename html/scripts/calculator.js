function getData(){
    let muni = ["København","Aarhus","Køge"];

    return muni;
}

//If we make API, we can just exchange code up there


//Jquery: Helps me simplify js to enable dropdown. Google search

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