$(document).ready(function(){

  //Cette fonction permet l'autocompletion de l'input 'ville1'
  $('#ville1').autocomplete({
    source :
      function(request, response) {
        $.ajax({
          url : '/autocompletionville',
          dataType : 'json',
          type : "GET",
          data: {
            commune : $('#ville1').val()
          }
        }).done(function(data) {
          var transData = data.map(function(value){
            return {
              label : value,
              value : value
            };
          })
          return response(transData);
        });
      },
      minLength:2,
      select: function(event,ui) {
        $("#ville1").val(ui.value);
      }
  });

  //Cette fonction permet l'autocompletion de l'input 'activite'
  $('#activite').autocomplete({
    source :
      function(request, response) {
        $.ajax({
          url : '/autocompletionactivite',
          dataType : 'json',
          type : "GET",
          data: {
            activite : $('#activite').val()
          }
        }).done(function(data) {
          var transData = data.map(function(value){
            return {
              label : value,
              value : value
            };
          })
          return response(transData);
        });
      },
      minLength:2,
      select: function(event,ui) {
        $("#activite").val(ui.value);
      }
  });

  //Cette fonction fait appel à la fonction tabs de jquery.ui qui permet de créer des onglets
  $(function() {
    $("#tabs").tabs();
  });

  //Cette fonction permet l'autocompletion de l'input 'ville2'
  
  $('#ville2').autocomplete({
    source :
      function(request, response) {
        $.ajax({
          url : '/autocompletionville',
          dataType : 'json',
          type : "GET",
          data: {
            commune : $('#ville2').val()
          }
        }).done(function(data) {
          var transData = data.map(function(value){
            return {
              label : value,
              value : value
            };
          })
          return response(transData);
        });
      },
      minLength:2,
      select: function(event,ui) {
        $("#ville2").val(ui.value);
      }
  });


   //Cette fonction permet l'autocompletion de l'input 'ville2'
  $('#activite2').autocomplete({
    source :
      function(request, response) {
        $.ajax({
          url : '/autocompletionactivite',
          dataType : 'json',
          type : "GET",
          data: {
            activite : $('#activite2').val()
          }
        }).done(function(data) {
          var transData = data.map(function(value){
            return {
              label : value,
              value : value
            };
          })
          return response(transData);
        });
      },
      minLength:2,
      select: function(event,ui) {
        $("#activite").val(ui.value);
      }
  });

});
