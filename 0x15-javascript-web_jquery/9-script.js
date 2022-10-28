$(function() {
    var $lists = $('DIV#hello');
    $.ajax({
        type: 'GET',
        url: 'https://fourtonfish.com/hellosalut/?lang=fr',
        success: function(data) {
             $lists.text(data.hello);
        }
    });
});
