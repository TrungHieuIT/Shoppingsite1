from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from core.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from accounts.models import CustomerUser
from django.contrib.auth.decorators import login_required

@require_POST
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id = id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.remove(product)
    return redirect('cart:cart_detail')

@login_required(login_url="/accounts/login/")
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'homepage/gioHang.html', {'cart': cart})
