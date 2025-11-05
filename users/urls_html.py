from django.urls import path
from . import views_html

urlpatterns = [
    path("login/", views_html.user_login, name="login"),
    path("logout/", views_html.user_logout, name="logout"),
    path("register/", views_html.user_register, name="register")
]
