<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Accueil</title>
  </head>
  <body>
    <table>
      <tr>
        <th>Activité</th>
        <th>Ville</th>
        <th>Complexe</th>
        <th>Code Postal</th>
      </tr>

      % for rep in reponse:
        % (activite, ville, complexe, cp) = rep
        <tr>
          <td> {{activite}} </td>
          <td> {{ville}} </td>
          <td> {{complexe}} </td>
          <td> {{cp}} </td>
        </tr>
      % end

    </table>
  </body>
</html>
