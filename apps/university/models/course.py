from django.db import models


class Course(models.Model):
    """Направление"""

    name = models.CharField(max_length=64, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
