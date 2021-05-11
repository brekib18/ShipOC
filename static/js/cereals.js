$(document).ready(function(){
    $('#search-btn').on('click', function(e){
        e.preventDefault();
        console.log('Eg náði að ýta á takkann')
        var searchText = $('#search-box').val();
        $.ajax( {
            url: '/morgunkorn?search_filter=' + searchText,
            type: 'GET',
            success: function(res){
                var newHtml = res.data.map(d => {
                    return `<div class="well candy">
                            <a href="/morgunkorn/${d.id}">
                                <img class="cereal-img" src="${d.firstImage}" />
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