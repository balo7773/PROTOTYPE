# accounts/models.py
# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Any custom fields for your CustomUser model
    age = models.IntegerField(null=True, blank=True)
    fullname = models.CharField(max_length=255, blank=True, null=True)

    # Add related_name to groups and user_permissions to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Different related_name from the default User
        blank=True,
        help_text='The groups this user belongs to.'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # Different related_name from the default User
        blank=True,
        help_text='Specific permissions for this user.'
    )