from django.shortcuts import render, get_object_or_404
from .models import Course, Material
from django.contrib.auth.decorators import login_required


@login_required
def course_list(request):
    """Отображает список всех курсов"""
    courses = Course.objects.all()
    return render(request, "courses.html", {"courses": courses})


def course_detail(request, pk):
    """Отображает детальную страницу курса"""
    course = get_object_or_404(Course, pk=pk)
    return render(request, "course_detail.html", {"course": course})


def materials_list(request):
    materials = Material.objects.all()
    return render(request, "materials_list.html", {"materials": materials})
