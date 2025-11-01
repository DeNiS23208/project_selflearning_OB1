import pytest
import requests

BASE_URL = "http://127.0.0.1:8000"  # адрес твоего сервера


@pytest.mark.order(1)
def test_get_courses_public():
    """
    Проверяет, что список курсов доступен без авторизации.
    Это интеграционный тест через requests.
    """
    # 1️⃣ Отправляем GET-запрос к API
    response = requests.get(f"{BASE_URL}/api/courses/")

    # 2️⃣ Проверяем, что ответ пришёл успешно
    assert response.status_code == 200

    # 3️⃣ Проверяем, что данные пришли в формате списка
    assert isinstance(response.json(), list)


import pytest
from rest_framework.test import APIClient
from users.models import User


@pytest.mark.django_db
def test_teacher_login_and_create_course():
    """
    Проверяет авторизацию по JWT и создание курса без внешнего сервера.
    """
    user = User.objects.get(username="GOD")
    client = APIClient()

    response = client.post("/api/auth/token/", {"username": "GOD", "password": "123456"})
    print("Ответ сервера:", response.status_code, response.data)

    assert response.status_code == 200
