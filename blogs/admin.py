from django.contrib import admin
from django.utils.text import slugify
from . import models


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("title",)}

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("blog", "author", "created_at")


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
