$(document).ready(function(){
    $('.radio').on('change', function (e) {
        e.preventDefault();
        var radio_value = this.value
        console.log(radio_value)
        $.ajax( {
            url: '/cereals?filter=' + radio_value,
            type: 'GET',
            success: function(res){
                console.log('ahdghas;glak')
                console.log(res.data)
                var newHtml = res.data.map(d => {
                    console.log('her erum vid')
                    return `<div class="well candy">
                            <a href="/cereals/${d.id}">
                                <img class="product-img" src="${d.firstImage}" />
                                <h4>${d.name}</h4>
                                <p>${d.description}</p>
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
