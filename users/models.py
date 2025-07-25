# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Class inheriting from Abstract User"""
    phone_number = models.CharField(max_length=15, blank=True, null=True)

