from django.urls import path

from .views import blog_detail, blog_list

urlpatterns = [
    path("", blog_list, name="blog"),
    path("<slug:slug>/", blog_detail, name="blog_detail"),
]
