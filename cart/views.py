from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect

def view_cart(request):
    """A view that returns the cart contents page"""
    return render(request, 'cart/cart.html', {'title': 'Cart'})
    

def add_to_cart(request, id):
    """Add a product to the cart.
    If the product already exists in the cart,
    it increments its quantity by 1"""

    quantity = 1
    cart = request.session.get('cart', {})

    if not cart:
        cart[id] = cart.get(id, quantity)
    else:
        if id in cart:
            cart[id] += 1
        else:
            cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    

def adjust_cart(request, id):
    """Decrease the quantity of a specified product.
    If there is only one product item in the cart,
    it removes the product."""

    cart = request.session.get('cart', {})
    if id in cart:
        if cart[id] > 1:
            cart[id] -= 1
        else: 
            cart.pop(id)

    request.session['cart'] = cart

    return redirect(reverse('cart:cart'))

def remove_from_cart(request, id):
    """Remove a product from the cart, regardless of its quantity."""
    cart = request.session.get('cart', {})
    quantity = request.POST.get('data-value')
    print(quantity)
    if id in cart:
        cart.pop(id)

    request.session['cart'] = cart

    return redirect(reverse('cart:cart'))
