from django.urls import path

from . import views

urlpatterns = [
    path("", views.project_list, name="projects"),
    path("<slug:slug>/", views.project_detail, name="project_detail"),
]
