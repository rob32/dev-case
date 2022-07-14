from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from contact.views import contact

from .feeds import BlogFeed
from .views import about, home, search

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("search/", search, name="search"),
    path("blog/", include("blog.urls")),
    path("projects/", include("portfolio.urls")),
    path("feed/", BlogFeed(), name="feed"),
    path("", include("pages.urls")),
]

admin.site.site_header = "Dev-Case Admin"  # "Django Administration"
admin.site.index_title = "Dev-Case Site administration "  # "Site administration".
admin.site.site_title = "DevCase-Admin"  # "Django site admin"

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
