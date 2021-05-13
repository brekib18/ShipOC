$(document).ready(function(){
    $('#search-btn3').on('click', function(e){
        e.preventDefault();
        console.log('Eg náði að ýta á takkann')
        var searchText = $('#search-box3').val();
        $.ajax( {
            url: '/accessories?search_filter=' + searchText,
            type: 'GET',
            success: function(res){
                var newHtml = res.data.map(d => {
                    return `<div class="well candy">
                            <a href="/accessories/${d.id}">
                                <img class="product-img" src="${d.firstImage}" />
                                <h4>${d.name}</h4>
                                <p>${d.description}</p>
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
        })
    });
});