$(document).ready(function(){
    $('.filter_button').on('click', function (e) {
        console.log(this.value)
        e.preventDefault();
        $.ajax( {
            url: '/cereals?filter='+this.value,
            type: 'GET',
            success: function(res){
                console.log("this is res.data"+res.data.map)
                console.log("haha")
                var newHtml = res.data.map(d => {
                    return res.data
                });
                $('.cereals').html(newHtml.join(''));
                $('search-box').val('');
            },
            error: function(xhr, status, error){
                //TODO: show toastr
                console.error(error);
            }
            });
        });})

// function filter(){
//     console.log('jajajja')
//         e.preventDefault();
//         var radio_value = this.value
//         console.log(radio_value)
//         $.ajax( {
//             url: '/cereals?filter=' + radio_value,
//             type: 'GET',
//
//             success: function(res){
//                 console.log(url)
//                 console.log('her erum vid2')
//                 console.log(res)
//                 var newHtml = res.data.map(d => {
//
//                     return `<div class="well candy">
//                             <a href="/cereals/${d.id}">
//                                 <img class="product-img" src="${d.firstImage}" />
//                                 <h4>${d.name}</h4>
//                                 <p>${d.description}</p>
//                             </a>
//                     </div>`
//                 });
//                 $('.cereals').html(newHtml.join(''));
//                 $('search-box').val('');
//             },
//             error: function(xhr, status, error){
//                 //TODO: show toastr
//                 console.error(error);
//             }
//             });
//
// }
