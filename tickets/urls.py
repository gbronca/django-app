from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

app_name = 'tickets'

urlpatterns = [
    path('bugs/', views.BugListView.as_view(template_name='tickets/bugs.html'), name='bugs'),
    path('features/', views.FeaturesListView.as_view(template_name='tickets/features.html'), name='features'),
    path('detail/<int:pk>/', views.TicketDetailView.as_view(), name='detail'),
    path('new/', views.TicketCreateView.as_view(), name='new-ticket'),
    path('detail/<int:pk>/update', views.TicketUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/delete', views.TicketDeleteView.as_view(), name='delete'),
    path('user/<username>/', views.UserBugListView.as_view(template_name='tickets/user_bugs.html'), name='user'),
]