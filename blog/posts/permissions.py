from rest_framework import permissions
from django.contrib.auth import get_user_model


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class IsUserOrIsAdmin(permissions.BasePermission):
    """Allow access to the respective User object and to admin users."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (request.user and request.user.is_staff) or (
            isinstance(obj, get_user_model()) and request.user == obj
        )

