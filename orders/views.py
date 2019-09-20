from django.shortcuts import render
from django.db.models import F
from .models import Order
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from core.models import Product
from accounts.models import CustomerUser

def order_create(request):
    cart = Cart(request)
    if request.CustomerUser.is_authenticated():
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save()
                for item in cart:
                    OrderItem.objects.create(
                        order=order,
                        product=item['product'],
                        price=item['price'],
                        quantity=item['quantity']
                )
            
                cart.clear()
            return render(request, "homepage/created.html", {'order': order})
        else:
            form = OrderCreateForm()
        return render(request, "homepage/create.html", {'form': form})
    else:
        return render(request,'homepage/dangky.html')