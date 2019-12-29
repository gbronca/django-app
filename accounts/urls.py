from django.urls import path, reverse_lazy
from .views import signup, user_profile
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('signup/',signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html',
                   extra_context={'title':'Login'}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', user_profile, name='profile'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
                                template_name='accounts/password_reset.html',
                                success_url = reverse_lazy('accounts:password_reset_done')),
         name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]