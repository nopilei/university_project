from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Type(models.TextChoices):
        CURATOR = 'curator'
        ADMIN = 'admin'
        STUDENT = 'student'

    type = models.CharField(max_length=64, choices=Type.choices)
