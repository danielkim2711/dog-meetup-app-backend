from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('users/', views.create_users, name='users'),
    path('users/<int:pk>/', views.get_user, name='user'),
    path('profiles/', views.get_profiles, name="profiles"),
    path('profiles/<int:pk>/', views.get_profile, name="profile"),
    path('dogs/', views.get_dogs, name="dogs"),
    path('dogs/<int:pk>/', views.get_dog, name="dog"),
    path('activities/', views.get_activities, name="activities"),
    path('activities/<int:pk>/', views.get_activity, name="activity"),
]
