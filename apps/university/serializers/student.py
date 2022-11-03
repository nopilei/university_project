from rest_framework import serializers

from apps.university.const import MAX_STUDENTS_PER_GROUP
from apps.university.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'user', 'gender', 'group')

    def validate_group(self, value):
        if Student.objects.filter(group_id=value).count() == MAX_STUDENTS_PER_GROUP:
            raise serializers.ValidationError(f'Maximum number of students is {MAX_STUDENTS_PER_GROUP}')
        return value
