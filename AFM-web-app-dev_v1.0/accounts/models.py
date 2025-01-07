# accounts/models.py
# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Any custom fields for your CustomUser model
    AGE_CHOICES = [
        ('0-18', '0-18'),
        ('18-35', '18-35'),
        ('36-50', '36-50'),
        ('51-65', '51-65'),
        ('65+', '65+'),
    ]

    age = models.CharField(
        max_length=5,  # The length here should match the length of the longest choice
        choices=AGE_CHOICES,
        default='18-35'
    )
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