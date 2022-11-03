from rest_framework import viewsets

from apps.user.models import User
from apps.user.permissions import IsAdminOrReadOnly
from apps.user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = [IsAdminOrReadOnly]