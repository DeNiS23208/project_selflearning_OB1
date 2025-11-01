from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    """
    Вьюха для регистрации нового пользователя.
    CreateAPIView — готовое представление для создания объектов (CRUD - C из Create).
    """

    serializer_class = RegisterSerializer
    # Разрешаем всем (AllowAny), даже неавторизованным пользователям.
    permission_classes = [permissions.AllowAny]


class ProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = RegisterSerializer(request.user)
        return Response(serializer.data)
