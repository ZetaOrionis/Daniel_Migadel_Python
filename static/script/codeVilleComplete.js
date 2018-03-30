$(document).ready(function(){

  $('#ville').autocomplete({ //$(this) = autocomplete
    source :
      function(request, response) {
        $.ajax({
          url : 'http://infoweb-ens/~jacquin-c/codePostal/codePostalComplete.php',
          dataType : 'json',
          type : "GET",
          data: {
            commune : $('#ville').val()
          }
        }).done(function(data) {
          var transData = data.map(function(item){
            return {
              label : item.Ville+"-"+item.CodePostal,
              value : item.CodePostal
            };
          })
          return response(transData);
        });
      },
      minLength:2
  });


});
