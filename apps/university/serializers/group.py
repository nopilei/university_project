from rest_framework import serializers

from apps.university.models import Student, Group


class _StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id',)
        ref_name = 'GGG'


class GroupSerializer(serializers.ModelSerializer):
    students = _StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('id', 'name', 'course', 'students')
