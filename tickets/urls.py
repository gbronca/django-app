from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

app_name = 'tickets'

urlpatterns = [
    path('bugs/', views.BugListView.as_view(template_name='tickets/tickets.html'), name='bugs'),
    path('features/', views.FeaturesListView.as_view(template_name='tickets/tickets.html'), name='features'),
    # path('bugs/<status>', views.BugStatusListView.as_view(template_name='tickets/tickets.html'), name='bugs'), # check
    # path('features/<status>', views.FeaturesStatusListView.as_view(template_name='tickets/tickets.html'), name='features'), # check
    path('detail/<int:pk>/', views.TicketDetailView.as_view(), name='detail'),
    path('new/', views.TicketCreateView.as_view(), name='new_ticket'),
    path('detail/<int:pk>/update', views.TicketUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/delete', views.TicketDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/comment', views.add_comment_to_ticket, name='add_comment_to_ticket'),
    path('user-bugs/<username>/', views.UserBugListView.as_view(template_name='tickets/user_tickets.html'), name='user_bugs'),
    path('user-features/<username>/', views.UserFeatureListView.as_view(template_name='tickets/user_tickets.html'), name='user_features'),
    path('vote/<int:pk>/', views.ticket_upvote, name='vote'),
]