from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .cart import Cart
from store.models import Product


def cart_summary(request):
    cart = Cart(request)
    return render(request, 'cart/cart-summary.html', {'cart': cart})


def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id  = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, product_qty=product_qty)
        cart_quantity = cart.__len__()
        response = JsonResponse({'qty': cart_quantity})

        return response


def cart_delete(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id  = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        cart_quantity = cart.__len__()
        cart_total = cart.get_total_price()
        response = JsonResponse({'qty': cart_quantity, 'total': cart_total})

        return response

def cart_update(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id, product_qty=product_qty)

        cart_quantity = cart.__len__()
        cart_total = cart.get_total_price()
        response = JsonResponse({'qty': cart_quantity, 'total': cart_total})

        return response