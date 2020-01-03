from django.shortcuts import render, redirect, reverse

def view_cart(request):
    """A view that returns the cart contents page"""
    return render(request, 'cart/cart.html')
    

def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""

    # Default quantity to 1 if request.get fails
    quantity = 1
    # quantity=int(request.POST.get('quantity'))
 
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    print(cart)
    request.session['cart'] = cart
    return redirect('tickets:detail', id)
    

def adjust_cart(request, id):
    """Adjust the quantity of the specified product to the specifies amount"""

    # Default quantity to 1 if request.get fails
    quantity = 1
    quantity=int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
