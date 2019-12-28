from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Ticket

class BugListView(ListView):

    template_name = 'tickets/bugs.html'
    context_object_name = 'bugs'

    def get_queryset(self, *args, **kwargs):
        return Ticket.objects.filter(issue='Bug').order_by('-date_posted')
