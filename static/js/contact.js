$(document).ready(function(){
    $('#send').on('click', function(e) {
        e.preventDefault();

        var contact_conf = document.getElementById('contact_container')
        var mess = document.createElement('div');
        mess.className ='contact_response'
        mess.textContent = 'thank you'

    })})

function sendMessage(){
    setTimeout(
        function (){
            var cont = document.createElement('div');
            var im = document.createElement('img')
            im.src = "../../static/images/ce.png"
            im.id = 'cer_im'
            cont.className = "contact"
            cont.textContent = "Thank you we will answer soon!!"
            cont.appendChild(im)
            var chat = document.getElementById('contact_container')
            chat.appendChild(cont)

        },1000
    );
}