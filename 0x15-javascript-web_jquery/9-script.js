/*
JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.

    The translation of “hello” must be displayed in the HTML tag DIV#hello
    You can’t use document.querySelector to select the HTML tag
    You must use the JQuery API
    Your script must work when it is imported from the <head> tag
    html file: 9-main.html
*/
$(() => {
    $.ajax({
      type: 'GET',
      url: 'https://fourtonfish.com/hellosalut/?lang=fr',
      success: (data) => {
        $('#hello').text(data.hello);
        }
    });
  });
