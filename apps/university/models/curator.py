from django.db import models

from apps.user.models import User


class Curator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField('Course', through='CuratorCourse', related_name='curators')


class CuratorCourse(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    curator = models.ForeignKey(Curator, on_delete=models.CASCADE)