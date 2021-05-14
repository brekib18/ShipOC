$(document).ready(function(){
    $('.filter_button').on('click', function (e) {
        console.log(this.value)
        e.preventDefault();
        $.ajax( {
            url: '/cereals?filter='+this.value,
            type: 'GET',
            success: function(res){

                var newHtml = res.data.map(d => {
                    return `<div class="well_cereal">
                            <a href="/cereals/${d.id}">
                                <img class="product-img" src="${d.firstImage}" />
                                <h4>${d.name}</h4>
                                <p>${d.price} kr.</p>
                            </a>
                    </div>`
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

