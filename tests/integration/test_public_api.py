import os

import pytest
import requests

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000")


@pytest.mark.order(1)
def test_get_courses_public():
    r = requests.get(f"{BASE_URL}/api/courses/")
    assert r.status_code == 200
    assert isinstance(r.json(), list)


@pytest.mark.order(2)
def test_teacher_login_and_create_course():
    # 1) Пробуем зарегистрировать учётку преподавателя (если уже есть — вернёт 400/409, и это норм)
    reg = requests.post(
        f"{BASE_URL}/api/auth/register/",
        json={
            "username": "teacher",
            "email": "t@ex.com",
            "password": "123456",
            "role": "TEACHER",
        },
        timeout=10,
    )
    assert reg.status_code in (201, 200, 400), reg.text  # 400 = уже существует

    # 2) Логинимся
    tok = requests.post(
        f"{BASE_URL}/api/auth/token/",
        data={"username": "teacher", "password": "123456"},
        timeout=10,
    )
    assert tok.status_code == 200, tok.text
    access = tok.json()["access"]

    # 3) Создаём курс
    headers = {"Authorization": f"Bearer {access}"}
    new_course = {"title": "Python Advanced", "description": "Продвинутый курс"}
    r = requests.post(
        f"{BASE_URL}/api/courses/", json=new_course, headers=headers, timeout=10
    )
    assert r.status_code in (200, 201), r.text
    assert "title" in r.json()
