from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from .models import Ticket

class BugListView(ListView):
    paginate_by = 5
    model = Ticket

    def get_queryset(self, *args, **kwargs):
        return Ticket.objects.filter(issue='Bug').order_by('-date_posted')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['type'] = 'Bugs'
        is_paginated = True
        return context


class UserBugListView(ListView):
    paginate_by = 5
    model = Ticket

    def get_queryset(self, *args, **kwargs):
        username = get_object_or_404(User, username=self.kwargs.get('username'))
        return Ticket.objects.filter(issue='Bug', username=username).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['type'] = 'Bugs'
        is_paginated = True
        return context


class FeaturesListView(ListView):
    paginate_by = 5
    model = Ticket

    def get_queryset(self, *args, **kwargs):
        return Ticket.objects.filter(issue='Feature').order_by('-date_posted')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['type'] = 'Features'
        is_paginated = True
        return context


class UserFeatureListView(ListView):
    paginate_by = 5
    model = Ticket

    def get_queryset(self, *args, **kwargs):
        username = get_object_or_404(User, username=self.kwargs.get('username'))
        return Ticket.objects.filter(issue='Feature', username=username).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['type'] = 'Features'
        is_paginated = True
        return context


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

