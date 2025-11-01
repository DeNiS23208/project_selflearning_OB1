from django.db import models
from django.conf import settings
from learning.models import Material

User = settings.AUTH_USER_MODEL


class Question(models.Model):
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name="questions",
        verbose_name="Материал"
    )
    text = models.CharField(max_length=255, verbose_name="Текст вопроса")

    def __str__(self):
        return f"{self.material.title}: {self.text}"

class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers",
        verbose_name="Вопрос"
    )
    text = models.CharField(max_length=255, verbose_name="Текст ответа")
    is_correct = models.BooleanField(default=False,verbose_name="Правильный ответ")

    def __str__(self):
        return f"{self.text} ({'верно' if self.is_correct else 'ошибка'})"

class TestAttempt(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="test_attempts",
        verbose_name="Пользователь"
    )
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name="attempts",
        verbose_name="Материал"
    )
    score = models.PositiveIntegerField(default=0, verbose_name="Очки")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} → {self.material.title} ({self.score} баллов)"