$(function() {

    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.hbtn.io/api/films/?format=json',
        success: function(data) {
            for (let i = 0; i <= data.results.length; i++) {
                $('UL#list_movies').append('<li>' + data.results[i].title + '</li>');
              }
        }
            });
});
