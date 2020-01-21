from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm
from tickets.models import Ticket


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created, please login')
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form, 'title': 'Sign up'})


@login_required
def user_profile(request):

    if request.method == 'POST':
        profile_form = UserUpdateForm(request.POST, instance=request.user)

        if profile_form.is_valid():
            # prevent a user from changing the joined date by disabling 
            # the read only tag from html
            # the form only saves username, email, first name and last name.
            form = profile_form.save(commit=False)
            form.save(update_fields=['username', 'email', 'first_name', 'last_name'])

            messages.success(request, 'Your account has been updated')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Something went wrong, please try again')
            return redirect('accounts:profile')
    else:
        profile_form = UserUpdateForm(instance=request.user)

    context = {
        'profile_form': profile_form,
        'title': f'{request.user.username} Profile',
    }
    return render(request, 'accounts/profile.html', context)


def index(request):
    # Bugs
    total_bugs = Ticket.objects.filter(issue='Bug').count()
    total_bugs_in_progress = Ticket.objects.filter(issue='Bug', status='In Progress').count()
    total_bugs_pending = Ticket.objects.filter(issue='Bug', status='Pending').count()
    total_bugs_completed = Ticket.objects.filter(issue='Bug', status='Completed').count()
    top_voted_bugs = Ticket.objects.filter(issue='Bug').order_by('-upvotes')[:3]
    
    # Features
    total_features = Ticket.objects.filter(issue='Feature').count()
    total_features_in_progress = Ticket.objects.filter(issue='Feature', status='In Progress').count()
    total_features_pending = Ticket.objects.filter(issue='Feature', status='Pending').count()
    total_features_completed = Ticket.objects.filter(issue='Feature', status='Completed').count()
    top_voted_features = Ticket.objects.filter(issue='Feature').order_by('-upvotes')[:3]


    context = {
        'total_bugs': total_bugs,
        'total_bugs_in_progress': total_bugs_in_progress,
        'total_bugs_pending': total_bugs_pending,
        'total_bugs_completed': total_bugs_completed,
        'top_voted_bugs': top_voted_bugs,
        'total_features': total_features,
        'total_features_in_progress': total_features_in_progress,
        'total_features_pending': total_features_pending,
        'total_features_completed': total_features_completed,
        'top_voted_features': top_voted_features,
    }
    return render(request, 'accounts/index.html', context)
