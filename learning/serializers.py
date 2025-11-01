from rest_framework import serializers

from .models import Course, Material, Section


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ("id", "section", "title", "content", "order")


class SectionSerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ("id", "course", "title", "order", "materials")


class CourseSerializer(serializers.ModelSerializer):
    """
    Сериализатор курсов.
    Включает связанные разделы (read-only).
    """

    sections = SectionSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(
        source="owner.username"
    )  # показываем имя владельца

    class Meta:
        model = Course
        fields = (
            "id",
            "owner",
            "title",
            "description",
            "created_at",
            "updated_at",
            "sections",
        )

    def create(self, validated_data):
        """
        При создании курса автоматически назначаем владельца — текущего пользователя.
        """
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)
