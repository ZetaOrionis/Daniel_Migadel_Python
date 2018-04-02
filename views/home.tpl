<!DOCTYPE html>
<html>
  <head>
    <title>Home</title>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
    <link rel="stylesheet" href="../views/css/jquery-ui.css" >
    <link rel="stylesheet" href="../views/css/home.css" >
    <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/jquery-ui.min.js"></script>
    <script type="text/javascript" src="{{ url('views', path='script/codeVilleComplete.js') }}" charset="utf-8"></script>
  </head>
  <body>
    
    <img src="{{ url('views', path='img/wallpaper.png') }}" width="500" height="auto" />
    <div id="tabs">
      <ul>
        <li><a href="#tabs-1">Recheche Activité - 1</a></li>
        <li><a href="#tabs-2">Recheche Activité - 2</a></li>
      </ul>
      <div id="tabs-1">
        <form method="get" action="/traitement">
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
        <form method="get" action="/test">
          <p>Ville :
            <input id="ville2" type="text" name="ville2">
          </p>
          <input type="submit" value="Rechercher">
        </form>
      </div>
    </div>
  </body>
</html>
