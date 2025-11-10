from django.urls import path
from .views_api import (
    UserListAPIView, UserDetailAPIView,
    ProfileListAPIView, ProfileDetailAPIView,
    GroupListAPIView, GroupDetailAPIView
)

urlpatterns = [
    # Utilisateurs
    path('users/', UserListAPIView.as_view(), name='api-user-list'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='api-user-detail'),

    # Profiles
    path('profiles/', ProfileListAPIView.as_view(), name='api-profile-list'),
    path('profiles/<int:pk>/', ProfileDetailAPIView.as_view(), name='api-profile-detail'),

    # Groupes
    path('groups/', GroupListAPIView.as_view(), name='api-group-list'),
    path('groups/<int:pk>/', GroupDetailAPIView.as_view(), name='api-group-detail'),
]
