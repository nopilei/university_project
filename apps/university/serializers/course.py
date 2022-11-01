from rest_framework import serializers

from apps.university.models import Discipline, Group, Curator, Course


class CourseSerializer(serializers.ModelSerializer):
    disciplines = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Discipline.objects.all(), required=False
    )

    # disciplines = _CourseDisciplineSerializer(many=True, required=False)
    groups = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Group.objects.all(), required=False
    )
    # groups = _CourseGroupSerializer(many=True, required=False)
    curators = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Curator.objects.all(), required=False
    )
    # curators = _CourseCuratorSerializer(many=True, required=False)

    class Meta:
        model = Course
        fields = ('id', 'name', 'date_created', 'disciplines', 'groups', 'curators')

    # def create(self, validated_data):
    #     disciplines = validated_data.pop('disciplines', [])
    #     groups = validated_data.pop('groups', [])
    #     curators = validated_data.pop('curators', [])
    #
    #     course = Course.objects.create(**validated_data)
    #     course.disciplines.add()


