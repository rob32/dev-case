from django.shortcuts import render

from config.models import MainConfig

from .models import Page


def page_footer(request, slug):
    main_config = MainConfig.get_solo()
    page = Page.objects.get(slug=slug)
    context = {
        "main_config": main_config,
        "page": page,
    }
    return render(request, "page.html", context=context)
