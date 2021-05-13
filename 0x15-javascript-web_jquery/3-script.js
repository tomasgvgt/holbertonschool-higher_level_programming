/*
JavaScript script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header

    You can’t use document.querySelector to select the HTML tag
    You must use the JQuery API
    html file: 3-main.html
*/
$('#red_header').click(() => {
  $('header').addClass('red');
});
