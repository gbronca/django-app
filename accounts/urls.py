from django.urls import path
from .views import signup
from django.contrib.auth import views as auth_views
# from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/',signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html',
                   extra_context={'title':'Login'}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html',
                    extra_context={'title':'Logout'}), name='logout'),
]