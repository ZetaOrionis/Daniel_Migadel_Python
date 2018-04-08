
  // This example requires the Places library. Include the libraries=places
  // parameter when you first load the API. For example:
  // <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">

var LAT = 0;
var LONG = 0;
  function initMap() {
    var input = /** @type {!HTMLInputElement} */(
        document.getElementById('ville1'));
    var autocomplete = new google.maps.places.Autocomplete(input);

    google.maps.event.addDomListener(input, 'keydown', function(e) {
        if (e.keyCode == 13 && $('.pac-container:visible').length) {
            e.preventDefault();
        }
    });
    autocomplete.addListener('place_changed', function() {

      var place = autocomplete.getPlace();
      if (!place.geometry) {

        window.alert("No details available for input: '" + place.name + "'");
        return;
      }

      // console.log("Latitude --> "+place.geometry.location.lat());
      // console.log("Longitude --> "+place.geometry.location.lng());
      // console.log(place.address_components[0]["long_name"]);
      // console.log(place.address_components[1]);
      latitude = place.geometry.location.lat();
      longitude = place.geometry.location.lng();
      $("#latitude").val(latitude);
      $("#longitude").val(longitude);
      ville = $("#pac-input").val();
      $("#ville").val(ville);

      console.log($("#latitude").val());
      console.log($("#longitude").val());
      console.log($("#ville").val());
      LAT = latitude;
      LONG = longitude;
      // if(place.address_components[2]["long_name"] == "Pays de la Loire"){
      //   console.log("La ville est dans les Pays de la Loire");
      // }else{
      //   console.log("Error not Pays de la Loire");
      // }

    });
    console.log("LAT = "+LAT)
    console.log("LONG = "+LONG)
  }
  console.log("LAT = "+LAT);
  console.log("LONG = "+LONG);

google.maps.event.addDomListener(window, 'load', initMap);


$( document ).ready(function() {
  $(document).on('input', '#slider', function() {
      $('#slider_value').html( $(this).val() );
  });
});

// $(document).ready(function(){
//
//   $('#ville').autocomplete({ //$(this) = autocomplete
//     source :
//       function(request, response) {
//         $.ajax({
//           url : 'http://infoweb-ens/~jacquin-c/codePostal/codePostalComplete.php',
//           dataType : 'json',
//           type : "GET",
//           data: {
//             commune : $('#ville').val()
//           }
//         }).done(function(data) {
//           var transData = data.map(function(item){
//             return {
//               label : item.Ville+"-"+item.CodePostal,
//               value : item.CodePostal
//             };
//           })
//           return response(transData);
//         });
//       },
//       minLength:2
//   });
//
// });
