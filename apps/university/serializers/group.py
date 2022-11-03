from rest_framework import serializers

from apps.university.const import MAX_STUDENTS_PER_GROUP, MAX_STUDENTS_ERROR_MESSAGE
from apps.university.models import Student, Group, Course


class GroupSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Student.objects.all(), required=False
    )

    class Meta:
        model = Group
        fields = ('id', 'name', 'course', 'students')

    def validate_students(self, value):
        if len(value) >= MAX_STUDENTS_PER_GROUP:
            raise serializers.ValidationError(MAX_STUDENTS_ERROR_MESSAGE)
        return value
