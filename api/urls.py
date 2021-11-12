from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('users/', views.get_users, name="users"),
    path('users/<str:pk>/', views.get_user, name="user"),
]
