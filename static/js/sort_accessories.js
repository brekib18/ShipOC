$(document).ready(function(){
    $('.sort_button').on('click', function (e) {
        e.preventDefault();
        $.ajax( {
            url: '/accessories?sort_button='+this.value,
            type: 'GET',
            success: function(res){

                var newHtml = res.data.map(d => {
                    return `<div class="well_cereal">
                            <a href="/accessories/${d.id}">
                                <img class="product-img" src="${d.firstImage}" />
                                <h4>${d.name}</h4>
                                <p>${d.price} kr.</p>
                            </a>
                    </div>`
                });
                $('.accessories').html(newHtml.join(''));
                $('search-box').val('');
            },
            error: function(xhr, status, error){
                //TODO: show toastr
                console.error(error);
            }
            });
        });})


