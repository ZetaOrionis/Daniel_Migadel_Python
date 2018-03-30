<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Accueil</title>
    <link rel="stylesheet" href="../views/css/reponseInstallation.css"/>
  </head>
  <body>
    <table id="table">
      <tr>
        <th>Nom</th>
        <th>Ville</th>
        <th>Code Postal</th>
        <th>Installation ID</th>
        <th>Coordonnée ID</th>
      </tr>
      % (lat) = lat
      % (lng) = lng
      % for rep in reponseInstallation:
        % (installationId, coordId, name, noVoie, libelleVoie, cp, commune) = rep
        <tr>
          <td> {{name}} </td>
          <td> {{commune}} </td>
          <td> {{cp}} </td>
          <td> {{installationId}} </td>
          <td> {{coordId}} </td>
          <td id="lat"> {{lat}} </td>
          <td id="lng"> {{lng}} </td>
        </tr>
      % end
    </table>

    <div id="map"></div>
    <script>

      var lati = document.getElementById('lat');
      var lngi = document.getElementById('lng');
      var arrayLignes = document.getElementById("table").rows;

      var lati2 = -31.563910;
      var lngi2 = 147.154312;

      function initMap() {

        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 3,
          center: {lat: -28.024, lng: 140.887}
        });

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

      var locations = [];
      for (var i = 0; i < arrayLignes.length; i++) {
        if (i%2 == 0) {
          locations.push({lat: parseFloat(lati.innerText), lng: parseFloat(lngi.innerText)});
        } else {
          locations.push({lat: lati2, lng: lngi2});
        }
      }

    </script>
    <script src="https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/markerclusterer.js">
    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAFlDCeM6-nRxCV0CeuvFMRFZ84fPvMi8U&callback=initMap">
    </script>

  </body>
</html>
