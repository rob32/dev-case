from django.contrib import admin

from blog.models import BlogPost, Category, Comment


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "created", "updated")
    list_filter = ("status", "created")
    search_fields = ("title", "author")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("status",)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post", "message", "date", "public")
    list_filter = ("author", "public")
    search_fields = ("author", "post")
    ordering = ("-date",)
    actions = ["activate_comments"]

    def activate_comments(self, request, queryset):
        queryset.update(public=True)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
