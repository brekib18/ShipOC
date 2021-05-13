  $(document).ready(function(){
    $('.cart_btn').on('click', function(e) {
        console.log('ha')
        e.preventDefault()
        var currentID = this.id
        var itemsInStorage = localStorage.getItem('Cart')
        var itemsToAdd = 1
        var varQuant = $(".section > div > input").val();
        if (varQuant) {
            itemsToAdd = parseInt(varQuant);
        }
        itemsInStorage = itemsInStorage ? JSON.parse(itemsInStorage) : {};
        if (itemsInStorage[currentID]) {

            itemsInStorage[currentID] += itemsToAdd
        } else {

            itemsInStorage[currentID] = itemsToAdd;
        }
        var current_num = localStorage.getItem('quant_cart');
        var next_num = (parseInt(current_num) + itemsToAdd).toString();
        localStorage.setItem('quant_cart', next_num);
        // $('#cart')[0].innerText = 'View Cart(' + next_num + ')'
        localStorage.setItem('Cart', JSON.stringify(itemsInStorage));
        if (varQuant) {
            $(".section > div > input").val('1');
        }
    });})



