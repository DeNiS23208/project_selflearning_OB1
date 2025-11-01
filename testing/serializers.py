from rest_framework import serializers
from .models import Question, Answer, TestAttempt

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("id", "text", "is_correct")

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ("id", "material", "text", "answers")

class TestAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestAttempt
        fields = ("id", "user", "material", "score", "created_at")