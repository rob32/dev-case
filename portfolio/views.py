from django.shortcuts import get_object_or_404, render

from pages.models import Page

from .models import Project


def project_list(request):
    # projects = get_list_or_404(Project, status=1)
    projects = Project.objects.filter(status=1)
    pages = Page.objects.all()
    context = {
        "projects": projects,
        "pages": pages,
    }
    return render(request, "portfolio/project_list.html", context=context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, status=1)
    pages = Page.objects.all()
    context = {
        "project": project,
        "pages": pages,
    }
    return render(request, "portfolio/project_detail.html", context=context)
