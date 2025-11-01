from rest_framework import viewsets, permissions
from .models import Course, Section, Material
from .serializers import CourseSerializer, SectionSerializer, MaterialSerializer
from .permissions import IsOwnerOrReadOnly


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Кастомное разрешение: только владелец курса может его менять.
    Остальные могут только читать.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешаем безопасные методы (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешаем изменение, только если текущий пользователь — владелец
        return getattr(obj, "owner", None) == request.user


class CourseViewSet(viewsets.ModelViewSet):
    """
    ViewSet для курсов.
    Правила:
    - ADMIN → может всё
    - TEACHER → может создавать и редактировать свои курсы
    - STUDENT → только смотреть
    """
    queryset = Course.objects.all().select_related("owner")
    serializer_class = CourseSerializer

    def get_permissions(self):
        # Правила зависят от роли пользователя
        user = self.request.user

        # 1. Неавторизованные пользователи могут только читать
        if not user.is_authenticated:
            return [permissions.AllowAny()]

        # 2. Админ — полный доступ
        if user.role == "ADMIN":
            return [permissions.IsAuthenticated()]

        # 3. Преподаватель — может создавать и редактировать свои курсы
        if user.role == "TEACHER":
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]

        # 4. Студент — только чтение
        return [permissions.AllowAny()]


class SectionViewSet(viewsets.ModelViewSet):
    """
    ViewSet для разделов.
    """
    queryset = Section.objects.all().select_related("course")
    serializer_class = SectionSerializer

    def get_permissions(self):
        user = self.request.user
        if not user.is_authenticated:
            return [permissions.AllowAny()]
        if user.role == "ADMIN":
            return [permissions.IsAuthenticated()]
        if user.role == "TEACHER":
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]
        return [permissions.AllowAny()]


class MaterialViewSet(viewsets.ModelViewSet):
    """
    ViewSet для материалов.
    """
    queryset = Material.objects.all().select_related("section")
    serializer_class = MaterialSerializer

    def get_permissions(self):
        user = self.request.user
        if not user.is_authenticated:
            return [permissions.AllowAny()]
        if user.role == "ADMIN":
            return [permissions.IsAuthenticated()]
        if user.role == "TEACHER":
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]
        return [permissions.AllowAny()]
