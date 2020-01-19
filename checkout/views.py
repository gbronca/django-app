from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PaymentForm
from django.conf import settings
from tickets.models import Ticket
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe_publishable = settings.STRIPE_PUBLISHABLE_KEY

@login_required
def checkout(request):

    price = 10
    payment_form = PaymentForm()

    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)

        if payment_form.is_valid():
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                total += quantity * price

            try:
                payment = stripe.Charge.create(
                amount = int(total * 100),
                currency = 'gbp',
                card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                message.error(request, 'Your card was declined')

            if payment.paid:
                messages.success(request, 'Paid successfuly completed')
                for id, quantity in cart.items():
                    ticket = get_object_or_404(Ticket, pk=id)
                    ticket.upvotes += quantity
                    ticket.save()
                request.session['cart'] = {}
                return redirect(reverse('index'))

            else:
                messages.error(request, 'Error')
        else:
            messages.error(request, 'Something went wrong, please try again')

        context = {
            'publishable': stripe_publishable,
        }

    else:
        # payment_form = PaymentForm()
        context = {
        'publishable': stripe_publishable,
        'payment_form': payment_form,
        }

    return render(request, 'checkout/checkout.html', context)