from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PaymentForm
from django.conf import settings
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
    return render(request, 'checkout/checkout.html')