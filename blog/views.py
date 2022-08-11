from django.shortcuts import get_object_or_404, render

from config.models import MainConfig
from pages.models import Page

from .forms import CommentForm
from .models import BlogPost, Comment


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
    comments = post.comments.filter(public=True)
    main_config = MainConfig.get_solo()
    pages = Page.objects.all()
    form = CommentForm()
    is_submitted = False

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            author = form.cleaned_data["author"]
            message = form.cleaned_data["message"]
            new_message = Comment(
                post=post,
                author=author,
                message=message,
            )
            new_message.save()
            is_submitted = True
            form = CommentForm()

    context = {
        "post": post,
        "main_config": main_config,
        "pages": pages,
        "comments": comments,
        "form": form,
        "is_submitted": is_submitted,
    }
    return render(request, "blog/blog_detail.html", context=context)
