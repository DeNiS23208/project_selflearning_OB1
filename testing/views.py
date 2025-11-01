from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Question, Answer, TestAttempt
from .serializers import QuestionSerializer, TestAttemptSerializer
from learning.models import Material


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().select_related("material")
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class TestAttemptViewSet(viewsets.ModelViewSet):
    queryset = TestAttempt.objects.all().select_related("user", "material")
    serializer_class = TestAttemptSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["post"])
    def check(self, request):
        """
        Проверяет ответы студента и возвращает результат.
        """
        user = request.user
        material_id = request.data.get("material")
        answers = request.data.get("answers", [])

        # Загружаем все правильные ответы
        correct_answers = Answer.objects.filter(
            question__material_id=material_id, is_correct=True
        ).values_list("id", flat=True)

        # Считаем количество правильных
        correct_count = sum(1 for ans in answers if ans in correct_answers)

        # Сохраняем результат
        attempt = TestAttempt.objects.create(
            user=user,
            material=Material.objects.get(id=material_id),
            score=correct_count
        )

        return Response({
            "user": user.username,
            "material": material_id,
            "correct": correct_count,
            "total": len(correct_answers),
            "score": attempt.score
        })
