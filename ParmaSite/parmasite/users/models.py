from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    password1 = models.CharField(max_length=30)

    USERNAME_FIELD = 'username'
    class Meta:
        verbose_name = "Добавить пользователя"
        verbose_name_plural = "Добавить пользователя"



