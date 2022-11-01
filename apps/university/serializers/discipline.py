from rest_framework import serializers

from apps.university.models import Discipline, Course


class _CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id',)
        ref_name = 'AA'


class DisciplineSerializer(serializers.ModelSerializer):
    courses = _CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Discipline
        fields = ('id', 'name', 'courses')
