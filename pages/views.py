from django.shortcuts import render

from .models import Page


def page_footer(request, slug):
    page = Page.objects.get(slug=slug)
    context = {
        "page": page,
    }
    return render(request, "page.html", context=context)
