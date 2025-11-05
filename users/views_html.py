from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect



User = get_user_model()


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            next_url = request.GET.get("next") or "/"
            return redirect(next_url)
        return render(request, "login.html", {"error": "Неверные данные"})
    return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect("/users/login/")


def user_register(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if not username or not password:
            return render(request, "register.html", {"error": "Заполните поля"})
        if User.objects.filter(username=username.exists()):
            return render(request, "register.html", {"error", "Имя занято"})
        user = User.objects.create_user(username=username, password=password)
        login(request,user)
        return redirect("/")
    return render(request, "register.html")
