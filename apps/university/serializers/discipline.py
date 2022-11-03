from rest_framework import serializers

from apps.university.models import Discipline, Course, DisciplineCourse


class DisciplineSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Course.objects.all(), required=False
    )

    class Meta:
        model = Discipline
        fields = ('id', 'name', 'courses')
