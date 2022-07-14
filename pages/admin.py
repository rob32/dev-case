from django.contrib import admin

from solo.admin import SingletonModelAdmin

from .models import AboutSiteConfig, IndexSiteConfig, Page


@admin.register(Page)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "updated")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(IndexSiteConfig, SingletonModelAdmin)
admin.site.register(AboutSiteConfig, SingletonModelAdmin)
