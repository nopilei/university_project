from rest_framework import serializers

from apps.university.models import Student, Curator, Course


class _StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id',)
        ref_name = 'D'


class _CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id',)
        ref_name = 'E'


class CuratorSerializer(serializers.ModelSerializer):
    students = _StudentSerializer(many=True, read_only=True)
    courses = _CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Curator
        fields = ('id', 'user', 'courses', 'students')
