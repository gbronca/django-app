from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created, please login')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form, 'title': 'Sign up'})


@login_required
def user_profile(request):
    return render(request, 'accounts/profile.html', {'title': 'My Profile'})
