from django.db.models import Q
from django.shortcuts import render

from blog.models import BlogPost
from config.models import MainConfig, SocialAccountsConfig
from pages.models import AboutSiteConfig, IndexSiteConfig, Page
from portfolio.models import Project

# TODO: refactor and tweak queries


def home(request):
    main_config = MainConfig.get_solo()
    index_config = IndexSiteConfig.get_solo()
    social_accounts = SocialAccountsConfig.get_solo()
    posts = BlogPost.objects.filter(status=1)
    projects = Project.objects.filter(status=1)
    pages = Page.objects.all()
    context = {
        "main_config": main_config,
        "index_config": index_config,
        "social_accounts": social_accounts,
        "posts": posts,
        "projects": projects,
        "pages": pages,
    }
    return render(request, "index.html", context=context)


def about(request):
    main_config = MainConfig.get_solo()
    about_config = AboutSiteConfig.get_solo()
    social_accounts = SocialAccountsConfig.get_solo()
    pages = Page.objects.all()
    context = {
        "main_config": main_config,
        "about_config": about_config,
        "social_accounts": social_accounts,
        "pages": pages,
    }
    return render(request, "about.html", context=context)


def search(request):
    main_config = MainConfig.get_solo()
    posts = BlogPost.objects.filter(status=1)
    pages = Page.objects.all()

    if request.method == "GET":
        query = request.GET.get("q")
        if query:
            posts = BlogPost.objects.filter(
                Q(title__icontains=query) | Q(category__name__icontains=query)
            )

    context = {
        "main_config": main_config,
        "posts": posts,
        "pages": pages,
    }

    return render(request, "search.html", context=context)
