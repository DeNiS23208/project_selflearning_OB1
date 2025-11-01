from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "Администратор"
        TEACHER = "TEACHER", "Преподаватель"
        STUDENT = "STUDENT", "Студент"
        STUPID = "STUPID", "Тупица"

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.STUDENT
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
