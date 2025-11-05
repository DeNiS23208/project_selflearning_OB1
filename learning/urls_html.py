from django.urls import path
from . import views_html

urlpatterns = [
    path("", views_html.course_list, name="course_list"),
    path("courses/<int:pk>/", views_html.course_detail, name="course_detail"),
    path("materials/", views_html.materials_list, name="materials_list"),
]
