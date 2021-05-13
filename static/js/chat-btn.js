$(document).ready(function(){
    $('#chat-btn').on('click', function(e) {
        e.preventDefault();
        var message = $('.chat_input').val();
        console.log('+Eg ýtti á takkann');
        $.ajax({
            url: '/chat/',

        })
        $('.chat_response').appendChild(message);
    })})


