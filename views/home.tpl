<!DOCTYPE html>
<html>
  <head>
    <title>Home</title>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>

    <link rel="stylesheet" href="../views/css/reset.css" >
    <link rel="stylesheet" href="../views/css/home.css" >
    <link rel="stylesheet" href="../views/css/jquery-ui.css" >
    <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/jquery-ui.min.js"></script>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAFlDCeM6-nRxCV0CeuvFMRFZ84fPvMi8U&libraries=places"></script>
    <script type="text/javascript" src="{{ url('views', path='script/home.js') }}" charset="utf-8"></script>
    <script type="text/javascript" src="{{ url('views', path='script/codeVilleComplete.js') }}" charset="utf-8"></script>

  </head>
  <body>

    <img src="{{ url('views', path='img/wallpaper.png') }}" width="500" height="auto" />

      <!-- <p>Activité :
        <input id="activite" type="text" name="activite">
      </p> -->
    <div id="tabs">
      <ul>
        <li><a href="#tabs-1">Recherche par Ville et Activité </a></li>
        <li><a href="#tabs-2">Recherche par Ville </a></li>
        <li><a href="#tabs-3">Recherche par Activité </a></li>
      </ul>


      <div id="tabs-1">
        <form method="get" action="/villeActivite">
          <!-- <input id="pac-input" class="controls" type="text"
          placeholder="Enter a location" size="50"> -->
          <div id="villePrecise">
          <input type="radio" id="radio1" name="radio" value="ville">Je précise une ville
          <p>Ville :
            <input id="ville2" type="text" class="controls" name="ville2">
          </p>
        </div>

          <div id="adresse">
          <input type="radio" id="radio2" name="radio" value="adresse">Je choisis un rayon autour de moi
          <p>Ville :
            <input id="ville1" type="text" class="controls" name="ville1">
          </p>
          <span>Dans un rayon de <span id="slider_value">1</span> km
          <input id="slider" type="range" min="1" max="100" value="1" name="slider">
          </span>
          <input id="latitude" type="hidden" name="latitude">
          <input id="longitude" type="hidden" name="longitude">
        </div>

          <p>Activité :
            <input id="activite" type="text" name="activite">
          </p>
          <input id="Rechercher" type="submit" value="Rechercher">
        </form>
      </div>





      <div id="tabs-2">
        <form method="get" action="/ville">
          <p>Ville :
            <input id="ville2" type="text" name="ville2">
          </p>
          <input id="latitude" type="hidden" name="latitude">
          <input id="longitude" type="hidden" name="longitude">
          <input id="slider" type="range" min="1" max="100" value="1">
          <input type="submit" value="Rechercher">
        </form>
      </div>



      <div id="tabs-3">
        <form method="get" action="/activite">
          <p>Activité :
            <input id="activite2" type="text" name="activite2">
          </p>
          <input type="submit" value="Rechercher">
        </form>
      </div>


    </div>
  </body>
</html>
