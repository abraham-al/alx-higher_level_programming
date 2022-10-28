$(function () {
    $.ajax({
        type:'GET',
        url: 'https://www.fourtonfish.com/hellosalut/hello/',
        success: (function() {
            $('INPUT#btn_translate').on('click', function () {
                $.getJSON(url + $('INPUT#language_code').val(), function (data) {
                  $('DIV#hello').text(data.hello);
                });
              });
        })
    });
});
