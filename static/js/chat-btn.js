$(document).ready(function(){
    $('#chat-btn').on('click', function(e) {
        e.preventDefault();
        var input_val = document.getElementById('chat_input').value
        console.log(input_val)
        var chat = document.getElementById('chat')
        var newchat = document.createElement('div');
        newchat.className ='chat_response'
        newchat.textContent = input_val
        chat.appendChild(newchat)


    })})

function myClick(){
    setTimeout(
        function (){
            console.log('timeour')
            var service = document.createElement('div');
            service.className = "service"
            service.textContent = "We will answer you soon."
            var chat = document.getElementById('chat')
            chat.appendChild(service)

        },1000
    );
}


// console.log('bla')
// btn = document.getElementById('chat-btn')
// input = document.getElementsByClassName('chat_input')
// console.log(input)
// console.log('blabal')
//
// function chat(){
//     input.addEventListener("keydown",event=>{
//         if (event.keyCode == 13){
//             console.log('13')
//         }
// })}


