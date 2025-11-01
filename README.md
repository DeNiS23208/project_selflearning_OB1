# 📘 Платформа самообучения студентов

Учебный бэкенд-сервис, реализованный на **Django REST Framework**,  
для создания и прохождения курсов с системой тестирования.

---

## 🚀 Возможности

- Регистрация, JWT-авторизация, роли пользователей  
- Управление курсами, разделами и материалами  
- Прохождение тестов и сохранение результатов  
- Права доступа (владелец / студент / админ)  
- Публичный просмотр курсов  
- Документация Swagger  
- PostgreSQL + ORM  
- Поддержка CORS

---

## 🧩 Установка и запуск

```bash
# 1. Клонируем репозиторий
git clone https://github.com/DeNiS23208/project_selflearning_OB1.git
cd project_selflearning_OB1

# 2. Создаём виртуальное окружение
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows

# 3. Устанавливаем зависимости
pip install -r requirements.txt

# 4. Применяем миграции
python manage.py migrate

# 5. Создаём суперпользователя
python manage.py createsuperuser

# 6. Запускаем сервер
python manage.py runserver
```

---

## 🔑 Тестовые пользователи

| Роль | Логин | Пример действий |
|------|--------|-----------------|
| **Admin** | admin / пароль | CRUD всех объектов |
| **Teacher** | teacher / пароль | создание курсов |
| **Student** | student / пароль | просмотр и тесты |

---

## 📚 Документация API

Swagger: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)  
OpenAPI schema: [http://127.0.0.1:8000/api/schema/](http://127.0.0.1:8000/api/schema/)

---

## ⚙️ Переменные окружения (.env.template)

```
DEBUG=True
SECRET_KEY=замени_на_свой
DATABASE_URL=postgres://user:password@db:5432/selflearning_db
ALLOWED_HOSTS=127.0.0.1,localhost
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

---

## ✅ Технологии

- Django 5.x  
- Django REST Framework  
- drf-spectacular  
- PostgreSQL  
- JWT (SimpleJWT)  
- CORS Headers  
- PEP8, Git
