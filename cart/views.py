from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
# from .models import Cart
from tickets.models import Ticket

@login_required
def add_to_cart(request, id):
    ticket = get_object_or_404(Ticket, id=id)

