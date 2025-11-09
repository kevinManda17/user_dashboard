from django.urls import path
from .views_api import (
    UserListAPIView, UserDetailAPIView,
    ProfileListAPIView, ProfileDetailAPIView,
    GroupListAPIView, GroupDetailAPIView
)

urlpatterns = [
    # Utilisateurs
    path('api/users/', UserListAPIView.as_view(), name='api-user-list'),
    path('api/users/<int:pk>/', UserDetailAPIView.as_view(), name='api-user-detail'),

    # Profiles
    path('api/profiles/', ProfileListAPIView.as_view(), name='api-profile-list'),
    path('api/profiles/<int:pk>/', ProfileDetailAPIView.as_view(), name='api-profile-detail'),

    # Groupes
    path('api/groups/', GroupListAPIView.as_view(), name='api-group-list'),
    path('api/groups/<int:pk>/', GroupDetailAPIView.as_view(), name='api-group-detail'),
]
