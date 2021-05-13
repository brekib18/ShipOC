$(document).ready(function(){
    $('#search-btn').on('click', function(e){
        e.preventDefault();
        console.log('takkinn virkar')
        console.log('ytti a takkann')
        var searchText = $('#search-box').val();
        $.ajax( {
            url: '/cereals?search_filter=' + searchText,
            type: 'GET',
            success: function(res){
                var newHtml = res.data.map(d => {
                    console.log('Hér er ég')
                    console.log(res.data)
                    console.log(res.data)
                    console.log('hallo')
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

console.log('blabla')

