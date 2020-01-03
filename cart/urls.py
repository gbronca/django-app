from django.urls import path, reverse_lazy
from .views import view_cart, add_to_cart, adjust_cart

app_name = 'cart'

urlpatterns = [
    path('', view_cart, name='cart'),
    path('add/<id>/', add_to_cart, name='add'),
    path('remove/<pk>/', adjust_cart, name='adjust_cart'),
]