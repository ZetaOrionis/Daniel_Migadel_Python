$(document).ready(function(){

  initialisationMap();
  champsAbsent();
  sortTable();
  fenetreModal();

});

//Cette fonction permet d'afficher une fenêtre modale qui contient une google map
//indiquant la position de l'équipement séléctionné dans le tableau
function fenetreModal() {
  $('.donnee').click(function() {
    $('.modal').css("display", "block");
    $('.modalbg').css("display", "block");
    $('.modal').empty();
    $('.modal').append("<span class=\"modal_close\">&#215;</span>");
    $('.modal').append("<div id=\"mapSpecifique\"></div>");

    var lati = $('#lat').data('latitude');
    var lngi = $('#lng').data('longitude');
    var mycenter = new google.maps.LatLng(lati,lngi);
    var mapCanvas = document.getElementById("mapSpecifique");
    mapOptions = {center:mycenter, zoom: 12};
    var map = new google.maps.Map(mapCanvas,mapOptions);
    var marker = new google.maps.Marker({position:mycenter});
    marker.setMap(map);

    $('.modal_close').click(function() {
      $('.modal').css("display", "none");
      $('.modalbg').css("display", "none");
    });

  });
}

//Cette fonction permet de remplacer les champs vide par la valeur 'abs'
function champsAbsent() {
  var absent = $('td:empty');
  absent.text("abs");
  $(absent).css({
    color : "red",
    fontStyle : "italic"
  });
}

//Cette fonction permet de tri par ordre alphabétique le tableau en fonction de la première colonne
function sortTable() {
    tbody = $('#table').find('tbody');
    tbody.find('tr').sort(function(a, b) {
      return $('td:first', a).text().localeCompare($('td:first', b).text());
    }).appendTo(tbody);
}

//Cette fonction permet d'afficher la map situé en bas de la page HTML, elle permet d'affiché tous les
//coordonnées présentent dans le tableau sous forme de groupe de marqueurs.
function initialisationMap() {

  var lati = document.getElementById('lat');
  var lngi = document.getElementById('lng');



  var coordonnees = document.querySelectorAll('[data-latitude],[data-longitude]');
  console.log(coordonnees);
  console.log(coordonnees.item(0));
  console.log(coordonnees.item(1));
  for (i = 0; i < 10; ++i) {
    console.log(coordonnees[i]);
    if(i == 0) {
      var lat = coordonnees[i].innerHTML;
      console.log("lat0"+lat);
    } else {
      if(i%2 != 0) {
        var lat = coordonnees[i].innerHTML;
        console.log("lat"+lat);

      } else {
        var lng = coordonnees[i].innerHTML;
        console.log("lng"+lng);
        console.log(lat+" - "+lng);
      }
    }

    console.log(coordonnees[i].innerHTML);
  }



  var arraylist = document.getElementById('table').rows;

  console.log(coordonnees);

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 8,
    center: {lat: 47.216501, lng: -1.554609}
  });

  var locations = [];
  for (var i = 0; i < arraylist.length-1; i++) {
      locations.push({lat: parseFloat(lati.innerText), lng: parseFloat(lngi.innerText)});
  }

  // Create an array of alphabetical characters used to label the markers.
  var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

  // Add some markers to the map.
  // Note: The code uses the JavaScript Array.prototype.map() method to
  // create an array of markers based on a given "locations" array.
  // The map() method here has nothing to do with the Google Maps API.
  var markers = locations.map(function(location, i) {
    return new google.maps.Marker({
      position: location,
      label: labels[i % labels.length]
    });
  });

  // Add a marker clusterer to manage the markers.
  var markerCluster = new MarkerClusterer(map, markers,
      {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});


}
