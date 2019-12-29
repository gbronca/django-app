from django.urls import path, reverse_lazy
# from .views import signup, user_profile
from django.contrib.auth import views as auth_views

app_name = 'cart'

urlpatterns = [
    path('',auth_views.TemplateView.as_view(template_name='cart/cart.html'))
    # path('signup/',signup, name='signup'),
]