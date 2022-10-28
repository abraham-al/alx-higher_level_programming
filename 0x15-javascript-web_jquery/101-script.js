$(function() {
    $('DIV#add_item').on('click', function() {
        $('UL.my_list').append('<li>Item</li>');
    });
    $('DIV#remove_item').on('click', function() {
        const data = $('UL.my_list li');
        if (data.length > 0) {
            data[data.length - 1].remove();
        }
    });
    $('DIV#clear_list').on('click', function() {
        $('UL.my_list').empty();
    });
});
