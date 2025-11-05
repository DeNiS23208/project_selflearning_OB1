from django.conf import settings
from django.db import models


class Course(models.Model):
    """
    Модель курса — верхний уровень структуры.
    Преподаватель (owner) создаёт курс и управляет им.
    """

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # связь с таблицей пользователей
        on_delete=models.CASCADE,  # при удалении преподавателя удаляются его курсы
        related_name="courses",  # позволяет обращаться user.courses
    )
    title = models.CharField(max_length=200, verbose_name="Название курса")
    description = models.TextField(blank=True, verbose_name="Описание")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title


class Section(models.Model):
    """
    Раздел курса (например, "Введение" или "Основы Python").
    """

    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="sections", verbose_name="Курс"
    )
    title = models.CharField(max_length=200, verbose_name="Название раздела")
    order = models.PositiveIntegerField(default=1, verbose_name="Порядок")

    class Meta:
        ordering = ["order"]
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"

    def __str__(self):
        return f"{self.course.title} / {self.title}"


class Material(models.Model):
    """
    Материал (урок, видео, статья), входящий в раздел.
    """

    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name="materials",
        verbose_name="Раздел",
    )
    title = models.CharField(max_length=200, verbose_name="Название материала")
    content = models.TextField(verbose_name="Содержание (текст или ссылка)")
    order = models.PositiveIntegerField(default=1, verbose_name="Порядок")

    class Meta:
        ordering = ["order"]
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"

    def __str__(self):
        return f"{self.section.title} / {self.title}"
