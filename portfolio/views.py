from django.shortcuts import get_object_or_404, render

from .models import Project


def project_list(request):
    # projects = get_list_or_404(Project, status=1)
    projects = Project.objects.filter(status=1)
    context = {
        "projects": projects,
    }
    return render(request, "portfolio/project_list.html", context=context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, status=1)
    context = {
        "project": project,
    }
    return render(request, "portfolio/project_detail.html", context=context)
