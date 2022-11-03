from django.db import models


class Discipline(models.Model):
    name = models.CharField(max_length=64, unique=True)
    courses = models.ManyToManyField('Course', through='DisciplineCourse', related_name='disciplines')


class DisciplineCourse(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['course', 'discipline'], name='course_discipline_unique'),
        ]
