from django.urls import path
from .views import signup
# from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/',signup, name='signup')
    # path('', views.ProductListView.as_view(), name='products_list'),
    # path('<pk>', views.ProductDetailView.as_view(), name='product_detail'),
]