from django.shortcuts import get_object_or_404, render

from config.models import MainConfig
from pages.models import Page

from .models import BlogPost


def blog_list(request):
    main_config = MainConfig.get_solo()
    # posts = get_list_or_404(BlogPost, status=1)
    posts = BlogPost.objects.filter(status=1)
    pages = Page.objects.all()
    context = {
        "posts": posts,
        "main_config": main_config,
        "pages": pages,
    }
    return render(request, "blog/blog_list.html", context=context)


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, status=1)
    main_config = MainConfig.get_solo()
    pages = Page.objects.all()
    context = {
        "post": post,
        "main_config": main_config,
        "pages": pages,
    }
    return render(request, "blog/blog_detail.html", context=context)
