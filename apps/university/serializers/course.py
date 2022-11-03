from rest_framework import serializers

from apps.university.models import Course


class CourseSerializer(serializers.ModelSerializer):
    disciplines = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True
    )
    groups = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True
    )
    curators = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True
    )

    class Meta:
        model = Course
        fields = ('id', 'name', 'date_created', 'disciplines', 'groups', 'curators')


