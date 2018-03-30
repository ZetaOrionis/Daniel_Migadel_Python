$(document).ready(function(){

  $('#ville1').autocomplete({ //$(this) = autocomplete
    source :
      function(request, response) {
        $.ajax({
          url : 'http://infoweb-ens/~jacquin-c/codePostal/codePostalComplete.php',
          dataType : 'json',
          type : "GET",
          data: {
            commune : $('#ville1').val()
          }
        }).done(function(data) {
          var transData = data.map(function(item){
            return {
              label : item.Ville+"-"+item.CodePostal,
              value : item.Ville
            };
          })
          return response(transData);
        });
      },
      minLength:2,
      select: function(event,ui) {
        $("#ville1").val(ui.item.Ville);
      }
  });

  $(function() {
    $("#tabs").tabs();
  });

  $('#ville2').autocomplete({ //$(this) = autocomplete
    source :
      function(request, response) {
        $.ajax({
          url : 'http://infoweb-ens/~jacquin-c/codePostal/codePostalComplete.php',
          dataType : 'json',
          type : "GET",
          data: {
            commune : $('#ville2').val()
          }
        }).done(function(data) {
          var transData = data.map(function(item){
            return {
              label : item.Ville+"-"+item.CodePostal,
              value : item.Ville
            };
          })
          return response(transData);
        });
      },
      minLength:2,
      select: function(event,ui) {
        $("#ville2").val(ui.item.Ville);
      }
  });

});
