from django.contrib import admin
from .models import Question, Answer, TestAttempt


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "material")
    list_filter = ("material",)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("text", "question", "is_correct")
    list_filter = ("is_correct", "question")


@admin.register(TestAttempt)
class TestAttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "material", "score", "created_at")
    list_filter = ("material", "user")
