from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=15)
    address = models.TextField()

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Укажите уникальное имя
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_set",  # Укажите уникальное имя
        blank=True
    )


