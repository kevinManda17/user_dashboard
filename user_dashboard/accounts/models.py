from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_groups')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('elder', 'Aine'),
    ('member', 'Membre'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Nouveau : rôle dans un groupe
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')

    def __str__(self):
        return self.full_name or self.user.username
