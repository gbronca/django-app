from django.urls import path, reverse_lazy
from .views import view_cart, add_to_cart, adjust_cart, remove_from_cart

app_name = 'cart'

urlpatterns = [
    path('', view_cart, name='cart'),
    path('add/<id>/', add_to_cart, name='add'),
    path('adjust/<id>/', adjust_cart, name='adjust_cart'),
    path('remove/<id>/', remove_from_cart, name='remove'),
]