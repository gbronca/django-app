from django.urls import path, reverse_lazy
from .views import checkout

app_name = 'checkout'

urlpatterns = [
    path('', checkout, name='checkout'),
]