<!DOCTYPE html>
<html>
  <head>
    <title>Home</title>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
    <link rel="stylesheet" href="../views/css/jquery-ui.css" >
    <link rel="stylesheet" href="../views/css/reset.css" >
    <link rel="stylesheet" href="../views/css/home.css" >
    <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/jquery-ui.min.js"></script>
    <script type="text/javascript" src="{{ url('views', path='script/home.js') }}" charset="utf-8"></script>
  </head>
  <body>
    
    <img src="{{ url('views', path='img/wallpaper.png') }}" width="600" height="auto" />
    <div id="tabs">
      <ul>
        <li><a href="#tabs-1">Recherche par Ville et Activité </a></li>
        <li><a href="#tabs-2">Recherche par Ville </a></li>
        <li><a href="#tabs-3">Recherche par Activité </a></li>
      </ul>
      <div id="tabs-1">
        <form method="get" action="/villeActivite">
          <p>Ville :
            <input id="ville1" type="text" name="ville1">
          </p>
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
