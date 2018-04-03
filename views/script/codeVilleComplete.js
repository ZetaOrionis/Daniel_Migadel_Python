$(document).ready(function(){

  $('#ville1').autocomplete({ //$(this) = autocomplete
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

  $('#activite').autocomplete({ //$(this) = autocomplete
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

  $(function() {
    $("#tabs").tabs();
  });

  $('#ville2').autocomplete({ //$(this) = autocomplete
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

});
