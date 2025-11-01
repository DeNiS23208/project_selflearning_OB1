# Импортируем базовый "админ-класс" для пользователей,
# который уже умеет показывать поля, фильтры и формы Django-пользователя.
from django.contrib import admin
from django.contrib.auth.admin import \
    UserAdmin  # Admin-класс (админ-интерфейс) для модели пользователя

# Импортируем нашу модель пользователя
from .models import User


# Декоратор @admin.register говорит админке:
# "Пожалуйста, зарегистрируй модель User с классом админ-интерфейса CustomUserAdmin".
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Этот класс описывает, КАК наша модель User будет выглядеть и работать в админке.
    Мы наследуемся от готового UserAdmin, чтобы не изобретать велосипед,
    и просто добавляем/меняем нужные поля (например, role).
    """

    # Какие колонки показывать в таблице пользователей (список)
    # — они видны на странице /admin/users/user/
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "role",
        "is_staff",
        "is_active",
    )

    # По каким полям можно быстро фильтровать справа
    list_filter = ("role", "is_staff", "is_active")

    # По каким полям работает строка поиска сверху
    search_fields = ("username", "email")

    # Как группируются поля на странице просмотра/редактирования пользователя
    # "fieldsets" — это разделы формы:
    # 1) Блок без имени — логин и пароль
    # 2) "Персональные данные" — имя/фамилия, почта, НАША роль
    # 3) "Права доступа" — флаги и группы прав
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Персональные данные",
            {"fields": ("first_name", "last_name", "email", "role")},
        ),
        (
            "Права доступа",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
    )

    # Конфигурация формы "добавить пользователя" (в админке кнопка "ADD USER")
    # По умолчанию UserAdmin показывает простую форму — мы расширяем её, чтобы там была role.
    add_fieldsets = (
        (
            None,
            {
                "classes": (
                    "wide",
                ),  # класс wide делает форму растянутой (более удобное поле ввода)
                "fields": (
                    "username",
                    "email",
                    "role",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
