from rest_framework import viewsets

from apps.university.models import Course, Curator, Discipline, Group, Student
from apps.university.serializers.course import CourseSerializer
from apps.university.serializers.curator import CuratorSerializer
from apps.university.serializers.discipline import DisciplineSerializer
from apps.university.serializers.group import GroupSerializer
from apps.university.serializers.student import StudentSerializer
from apps.user.permissions import IsAdminOrReadOnly, IsCuratorOrReadOnly


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]


class CuratorViewSet(viewsets.ModelViewSet):
    queryset = Curator.objects.all()
    serializer_class = CuratorSerializer
    permission_classes = [IsAdminOrReadOnly]


class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [IsAdminOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsCuratorOrReadOnly|IsAdminOrReadOnly]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsCuratorOrReadOnly | IsAdminOrReadOnly]
