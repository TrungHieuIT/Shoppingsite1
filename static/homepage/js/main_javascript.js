var x = document.getElementById("modal_quickView");

function showDialog(){
    x.show();
}

/*document.getElementById("quantity_input").value ="110";*/

function ready() {
    var removeCartItemButtons = document.getElementsByClassName('btn_remove_gioHang')
    for (var i = 0; i < removeCartItemButtons.length; i++) {
        var button = removeCartItemButtons[i]
        button.addEventListener('click', removeCartItem)
    }
}

function addItemToCart(image,title,price){
    var cart_row = document.createElement('div')
    cart_row.classList.add(cart_row)
    var cart_image = document.getElementsByClassName("image_SPCT")
    var cart_title = document.getElementsByClassName("product_name")
    var cart_price = document.getElementsByClassName("product_price")
    for (var i = 0; i < cart_title.length; i++) {
        if (cart_title[i].innerText == cart_title) {
            alert('This item is already added to the cart')
            return
        }
    }
    var cartRowContents = `
            <div class="inner">
            <img  class="image_SPCT" src="{% static 'media/'%}{{item.pro_image}}" alt="{{item.pro_name}}">
            </div>
            </div>
            <div class="product_content">		
                <div class="product_price discount">{{item.pro_price}}VND<span></span></div>
                <div class="product_name"><div>{{item.pro_name}}</div></div>
            </div>`
    cartRow.innerHTML = cartRowContents
    cartItems.append(cartRow)
    cartRow.getElementsByClassName('btn-danger')[0].addEventListener('click', removeCartItem)
    cartRow.getElementsByClassName('cart-quantity-input')[0].addEventListener('change', quantityChanged)
}