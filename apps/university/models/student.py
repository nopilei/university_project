from django.db import models

from apps.user.models import User


class Student(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M'
        FEMALE = 'F'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, related_name='students', null=True)
