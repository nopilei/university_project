from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

from apps.user.models import User


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.type == User.Type.ADMIN or request.method in SAFE_METHODS


class IsCuratorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.type == User.Type.CURATOR or request.method in SAFE_METHODS
