from rest_framework import viewsets

from apps.university.models import Course, Curator, Discipline, Group, Student
from apps.university.serializers.course import CourseSerializer
from apps.university.serializers.curator import CuratorSerializer
from apps.university.serializers.discipline import DisciplineSerializer
from apps.university.serializers.group import GroupSerializer
from apps.university.serializers.student import StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CuratorViewSet(viewsets.ModelViewSet):
    queryset = Curator.objects.all()
    serializer_class = CuratorSerializer


class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
