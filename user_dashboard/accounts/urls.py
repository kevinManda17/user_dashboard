from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    DashboardView, RegisterView,
    ProfileListView, ProfileDetailView,
    ProfileCreateView, ProfileUpdateView, ProfileDeleteView,
    GroupListView, GroupCreateView, GroupDetailView
)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('profiles/', ProfileListView.as_view(), name='profile_list'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profiles/create/', ProfileCreateView.as_view(), name='profile_create'),
    path('profiles/<int:pk>/edit/', ProfileUpdateView.as_view(), name='profile_update'),
    path('profiles/<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile_delete'),
    path('groups/', GroupListView.as_view(), name='group_list'),
    path('groups/create/', GroupCreateView.as_view(), name='group_create'),
    path('groups/<int:pk>/', GroupDetailView.as_view(), name='group_detail'),
]
