$(document).ready(function(){
    $('#chat-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('.chat_input').val();
        console.log(searchText);
    })})


