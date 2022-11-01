from django.db import models

from apps.university.models.course import Course


class Group(models.Model):
    name = models.CharField(max_length=64, unique=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name='groups', null=True)
