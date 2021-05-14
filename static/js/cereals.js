$(document).ready(function(){
    $('#search-btn').on('click', function(e){
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax( {
            url: '/cereals?search_filter=' + searchText,
            type: 'GET',
            success: function(res){
                var newHtml = res.data.map(d => {
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
        })
    });
});


