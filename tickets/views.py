from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from .models import Ticket

class BugListView(ListView):
    model = Ticket
    # template_name = 'tickets/bugs.html'
    context_object_name = 'bugs'

    def get_queryset(self, *args, **kwargs):
        return Ticket.objects.filter(issue='Bug').order_by('-date_posted')


class FeaturesListView(ListView):
    model = Ticket
    # template_name = 'tickets/features.html'
    context_object_name = 'features'

    def get_queryset(self, *args, **kwargs):
        return Ticket.objects.filter(issue='Feature').order_by('-date_posted')


class TicketDetailView(DetailView):
    model = Ticket


class TicketCreateView(LoginRequiredMixin ,CreateView):
    model = Ticket
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.username = self.request.user

        return super().form_valid(form)


class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ticket
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.username = self.request.user

        return super().form_valid(form)

    def test_func(self):
        ticket = self.get_object()
        if self.request.user == ticket.username:
            return True
        return False


class TicketDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ticket
    success_url = '/'

    def test_func(self):
        ticket = self.get_object()
        if self.request.user == ticket.username:
            return True
        return False

