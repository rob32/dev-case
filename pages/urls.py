from django.urls import path

from .views import page_footer

urlpatterns = [
    path("<slug:slug>/", page_footer, name="page"),
]
