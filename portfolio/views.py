from django.shortcuts import get_object_or_404, render

from config.models import MainConfig
from pages.models import Page

from .models import Project


def project_list(request):
    main_config = MainConfig.get_solo()
    # projects = get_list_or_404(Project, status=1)
    projects = Project.objects.filter(status=1)
    pages = Page.objects.all()
    context = {
        "projects": projects,
        "main_config": main_config,
        "pages": pages,
    }
    return render(request, "portfolio/project_list.html", context=context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, status=1)
    main_config = MainConfig.get_solo()
    pages = Page.objects.all()
    context = {
        "project": project,
        "main_config": main_config,
        "pages": pages,
    }
    return render(request, "portfolio/project_detail.html", context=context)
