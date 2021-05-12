$(document).ready(function(){
    $('.cart_btn').on('click', function(e){
        e.preventDefault();
        console.log("bla")
        $.ajax({
            url: '/karfa',
            type: 'POST',
            success: function (res){
                var newHtml = res.data.map(d => {

                    return `<div class="well candy">
                            <a href="/morgunkorn/${d.id}">
                                <img class="product-img" src="${d.firstImage}" />
                                <h4>${d.name}</h4>
                                <p>${d.description}</p>
                            </a>
                    </div>`
                });
            }

        })

    });
});