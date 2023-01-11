function checkprice()
{
    console.log('checkprice button clicked')
    var sqft=document.getElementById('uisqft');
    console.log("sqft="+sqft.value);
    var location=document.getElementById('uiLocations');
    console.log("location="+location.value);
    //var url = "http://127.0.0.1:5000/predict_home_price";
    var result=document.getElementById('uiresult');
    var url = "http://127.0.0.1:5000/get_predicted_price";
    $.post(url,
    {
        total_sqft:sqft.value,
        location:location.value
    },function(data,status)
    {
        console.log(data.estimated_price)
        result.innerHTML="<h2>"+data.estimated_price.toString()+" lakh</h2>";
        console.log(status)
    });


}

function onPageLoad() {
    console.log( "document loaded" );
     var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.locations; // get location from the json file
            var uiLocations = document.getElementById("uiLocations"); // access the location
           // $('#uiLocations').empty(); // make the location field empty if needed
           // show all the elements available in locations and show inside the ui
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
  }
window.onload=onPageLoad;