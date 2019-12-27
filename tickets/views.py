from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Ticket

class BugListView(ListView):

    template_name = 'tickets/bugs.html'

    def get_queryset(self, *args, **kwargs):
        return Ticket.objects.all()
