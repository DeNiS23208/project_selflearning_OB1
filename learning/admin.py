from django.contrib import admin

from .models import Course, Material, Section


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "updated_at", "created_at")
    search_fields = ("title", "owner__username")
    list_filter = ("owner",)
    ordering = ("created_at",)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "order")
    list_filter = ("course",)
    ordering = ("course", "order")


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("title", "section", "order")
    list_filter = ("section",)
    ordering = ("section", "order")
