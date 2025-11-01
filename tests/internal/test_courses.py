import pytest
from rest_framework.test import APIClient
from users.models import User
from learning.models import Course


@pytest.mark.django_db  # даёт доступ к базе Django
def test_teacher_can_create_course():
    """
    Проверяет, что преподаватель может создать курс.
    Это внутренний (unit) тест через APIClient.
    """
    user = User.objects.create_user(
        username="teacher",
        password="123456",
        role="TEACHER"
    )

    # 2️⃣ Инициализируем тестовый клиент (встроенный в DRF)
    client = APIClient()

    # 3️⃣ "Авторизуем" нашего пользователя
    client.force_authenticate(user)

    # 4️⃣ Отправляем POST-запрос на создание курса
    response = client.post("/api/courses/", {
        "title": "Python 101",
        "description": "Основы языка"
    })

    # 5️⃣ Проверяем, что ответ успешен (201 Created)
    assert response.status_code == 201

    # 6️⃣ Проверяем, что курс действительно появился в базе
    assert Course.objects.count() == 1
    course = Course.objects.first()
    assert course.title == "Python 101"
    assert course.owner == user
