/*
JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json

    The name must be displayed in the HTML tag DIV#character
    You can’t use document.querySelector to select the HTML tag
    You must use the JQuery API
    html file: 7-main.html
*/
$(() => {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    success: (data) => {
      $('#character').text(data.name);
    }
  });
});
