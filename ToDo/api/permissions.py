# Импортируем модуль permissions из rest_framework для работы с разрешениями
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    # Метод has_permission проверяет, есть ли у пользователя разрешение на выполнение действия
    def has_permission(self, request, view):
        # Если пользователь аутентифицирован и является сотрудником (администратором)
        if request.user and request.user.is_staff:
            return True
        # Разрешаем только безопасные методы (например, GET, HEAD, OPTIONS)
        return request.method in permissions.SAFE_METHODS

# Определяем класс IsOwnerOrReadOnly, который наследует от permissions.BasePermission
class IsOwnerOrReadOnly(permissions.BasePermission):
    # Метод has_object_permission проверяет, есть ли у пользователя разрешение на выполнение действия с определенным объектом
    def has_object_permission(self, request, view, obj):
        # Если пользователь аутентифицирован и является сотрудником (администратором)
        if request.user and request.user.is_staff:
            return True
        # Разрешаем действие только если пользователь является создателем объекта
        return obj.created_by == request.user
