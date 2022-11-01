from rest_framework import serializers

from apps.university.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'user', 'gender', 'group')
