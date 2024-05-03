$(document).ready(function () {
  $('#btn_translate, #language_code').on('click keypress', function (event) {
    const keycode = (event.keyCode ? event.keyCode : event.which);
    if (keycode === 13 || event.type === 'click') {
      const languageCode = $('#language_code').val();
      $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode }, function (data) {
        $('#hello').text(data.hello);
      });
    }
  });
});
