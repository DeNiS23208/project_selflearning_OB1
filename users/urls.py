from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import ProfileView, RegisterView
from . import views_html

urlpatterns = [
    # Регистрация
    path("register/", RegisterView.as_view(), name="register"),
    # Вход (логин) — выдача токена (access + refresh)
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # Обновление access-токена по refresh-токену
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    #  Проверка токена
    path("me/", ProfileView.as_view(), name="user_profile"),
    #  Авторизация пользователя если уже зарегистрирован
    path("login/", views_html.user_login, name="login"),
    #  Регистрация пользователя
    path("register/", views_html.user_register, name="register"),
    #  Страница выхода в случае если пользователь выходит
    path("logout/", views_html.user_logout, name="logout"),
]
