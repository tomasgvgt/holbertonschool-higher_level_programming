/*
JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

    All movie titles must be list in the HTML tag UL#list_movies
    You can’t use document.querySelector to select the HTML tag
    You must use the JQuery API
    html file: 8-main.html
*/


$(() => {
    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.hbtn.io/api/films/?format=json',
        success: (data) => {
        for (let item in data.results) {
            $('#list_movies').append(('<li>' + data.results[item].title + '</li>'));
        }
    }
    });
  });
