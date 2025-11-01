from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """
    Разрешение для роли ADMIN.
    Пользователь с этой ролью имеет полный доступ.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "ADMIN"


class IsTeacher(permissions.BasePermission):
    """
    Разрешение для роли TEACHER.
    Преподаватели могут создавать и редактировать курсы.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "TEACHER"


class IsStudent(permissions.BasePermission):
    """
    Разрешение для роли STUDENT.
    Студенты могут только просматривать данные.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "STUDENT"


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
        Разрешение, позволяющее редактировать только владельцу.
        Все остальные пользователи могут только читать.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
