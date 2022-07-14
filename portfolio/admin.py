from django.contrib import admin

from .models import Project, TechStack, Tool


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "created")
    list_filter = ("status", "created")
    search_fields = ("title", "author")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("status",)


@admin.register(TechStack)
class TechStackAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ("name",)
