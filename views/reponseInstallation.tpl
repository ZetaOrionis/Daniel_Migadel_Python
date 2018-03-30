<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Accueil</title>
    <link rel="stylesheet" href="../views/css/reponseInstallation.css":<
  </head>
  <body>
    <table>
      <tr>
        <th>Activité</th>
        <th>Ville</th>
        <th>Complexe</th>
        <th>Code Postal</th>
      </tr>

      % for rep in reponseInstallation:
        % (installationId, coordId, name, noVoie, libelleVoie, cp, commune) = rep
        <tr>
          <td> {{name}} </td>
          <td> {{commune}} </td>
          <td> {{cp}} </td>
          <td> {{installationId}} </td>
        </tr>
      % end

    </table>
  </body>
</html>
