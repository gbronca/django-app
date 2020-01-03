from django.shortcuts import get_object_or_404
from tickets.models import Ticket


def cart_contents(request):
    """Ensures that the cart contents are
    avaliable when rendering every page"""

    price = 10
    total = 0
    tickets_count = 0

    cart = request.session.get('cart', {})

    cart_items = []
    upvote_list = []

    for id, quantity in cart.items():
        ticket = get_object_or_404(Ticket, pk=id)

        upvote_list.append(id)
        tickets_count += quantity
        total += quantity * price

        cart_items.append({'id': id, 'quantity': quantity,
                           'ticket': ticket, 'price': price})

    return {'ticket_count': tickets_count,
            'cart_items': cart_items,
            'total': total,
            'upvote_list': upvote_list}
