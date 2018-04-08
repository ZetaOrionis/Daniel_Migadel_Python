<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <link rel="stylesheet" href="../views/css/reponse.css"/>
    <title>Accueil</title>
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/jquery-ui.min.js"></script>
    <script src="https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/markerclusterer.js"></script>
    <script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAFlDCeM6-nRxCV0CeuvFMRFZ84fPvMi8U"></script>
    <script type="text/javascript" src="{{ url('views', path='script/reponse.js') }}" charset="utf-8"></script>
  </head>
  <body>
    % (lenreponse) = lenreponse
    <h2>Nous avons trouvé <span id="lenreponse"> {{lenreponse}} </span> résultats !</h2>
    <table id="table">
      <thead>
        <tr>
          <th>Activité</th>
          <th>Equipement</th>
          <th>Type d'équipement</th>
          <th>Nom du Lieu</th>
          <th>Adresse</th>
          <th>Commune</th>
        </tr>
      </thead>
      % for rep in reponse :
        % (activiteLib, equNom, equipTypeLib, name, noVoie, libelleVoie, commune, equGpsY, equGpsX) = rep
        % print(rep)
        <tr class="donnee">
          <td>{{activiteLib}}</td>
          <td>{{equNom}}</td>
          <td>{{equipTypeLib}}</td>
          <td>{{name}}</td>
          <td>{{noVoie}}{{libelleVoie}}</td>
          <td>{{commune}}</td>
          <div class="coordonnee">
            <td id="lat" data-latitude="{{equGpsY}}"> {{equGpsY}} </td>
            <td id="lng" data-longitude="{{equGpsX}}" > {{equGpsX}} </td>
          </div>
        </tr>
      % end
    </table>

    <div class="modal"></div>
    <div class="modalbg"></div>

    <div id="map"></div>



  </body>
</html>
