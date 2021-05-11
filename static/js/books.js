$(document).ready(function(){
    $('#search-btn1').on('click', function(e){
        e.preventDefault();
        console.log('Eg náði að ýta á takkann')
        var searchText = $('#search-box1').val();
        $.ajax( {
            url: '/bakur?search_filter=' + searchText,
            type: 'GET',
            success: function(res){
                console.log('Eg er komin hingað')
                var newHtml = res.data.map(d => {
                    return `<div class="well candy">
                            <a href="/bakur/${d.id}">
                                <img class="books-img" src="${d.firstImage}" />
                                <h4>${d.name}</h4>
                                <p>${d.description}</p>
                            </a>
                    </div>`
                });
                $('.books').html(newHtml.join(''));
                $('search-box').val('');
            },
            error: function(xhr, status, error){
                //TODO: show toastr
                console.error(error);
            }
        })
    });
});