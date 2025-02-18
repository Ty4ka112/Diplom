from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Администратор имеет все права
        if request.user and request.user.is_staff:
            return True
        # Обычные пользователи имеют только права на чтение
        return request.method in permissions.SAFE_METHODS

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Администратор имеет все права
        if request.user and request.user.is_staff:
            return True
        # Обычные пользователи могут управлять только своими объектами
        return obj.created_by == request.user
