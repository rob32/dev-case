from django.contrib.sitemaps import Sitemap
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from blog.models import BlogPost
from pages.models import Page
from portfolio.models import Project

from .settings import SESSION_COOKIE_SECURE


class BlogPostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return BlogPost.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.updated


class ProjectSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Project.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.updated


class PageSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.6

    def items(self):
        return Page.objects.all()

    def lastmod(self, obj):
        return obj.updated


class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return ["home", "about"]

    def location(self, item):
        return reverse(item)


def get_sitemap_absolute_url(request):
    domain = get_current_site(request)
    scheme = "https" if SESSION_COOKIE_SECURE else "http"
    return f"{scheme}://{domain}/sitemap.xml"
