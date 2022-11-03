from rest_framework import serializers

from apps.university.models import Curator, Course


class CuratorSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Course.objects.all(), required=False
    )

    class Meta:
        model = Curator
        fields = ('id', 'user', 'courses')
