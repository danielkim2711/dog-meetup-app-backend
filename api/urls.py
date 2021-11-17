from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('users/', views.get_users, name='users'),
    path('profiles/', views.get_profiles, name="profiles"),
    path('profiles/<int:pk>/', views.get_profile, name="profile"),
    path('dogs/', views.get_dogs, name="dogs"),
    path('dogs/<int:pk>/', views.get_dog, name="dog"),
]
