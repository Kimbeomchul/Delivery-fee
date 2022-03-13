from rest_framework import permissions

from users.models import User


class IsOwnerOrReadOnly(permissions.IsAuthenticated):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `user` attribute.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.__class__ == User:
            return bool(obj == request.user)

        # Instance must have an attribute named `user`.
        return bool(
            request.method in permissions.SAFE_METHODS
            or obj.user == request.user
        )
