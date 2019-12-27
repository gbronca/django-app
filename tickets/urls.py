from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

app_name = 'tickets'

urlpatterns = [
    path('bugs/', views.BugListView.as_view(template_name='tickets/bugs.html'), name='bugs'),
]