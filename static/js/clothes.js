$(document).ready(function(){
    $('#search-btn2').on('click', function(e){
        e.preventDefault();
        console.log('Eg náði að ýta á takkann')
        var searchText = $('#search-box2').val();
        $.ajax( {
            url: '/fot?search_filter=' + searchText,
            type: 'GET',
            success: function(res){
                console.log('Eg er komin hingað')
                var newHtml = res.data.map(d => {
                    return `<div class="well candy">
                            <a href="/fot/${d.id}">
                                <img class="product-img" src="${d.firstImage}" />
                                <h4>${d.name}</h4>
                                <p>${d.description}</p>
                            </a>
                    </div>`
                });
                $('.clothes').html(newHtml.join(''));
                $('search-box').val('');
            },
            error: function(xhr, status, error){
                //TODO: show toastr
                console.error(error);
            }
        })
    });
});