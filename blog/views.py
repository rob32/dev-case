from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import render

from dev_case import settings

from .forms import CommentForm
from .models import BlogPost, Comment


def blog_list(request):
    posts = BlogPost.objects.prefetch_related("category").filter(status=1)
    context = {
        "posts": posts,
    }
    return render(request, "blog/blog_list.html", context=context)


def blog_detail(request, slug):
    try:
        post = BlogPost.objects.select_related("author").get(slug=slug)
    except BlogPost.DoesNotExist:
        raise Http404()
    comments = post.comments.filter(public=True)
    form = CommentForm()
    is_submitted = False

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            author = form.cleaned_data["author"]
            message = form.cleaned_data["message"]

            if settings.EMAIL_NOTIFICATION:
                send_mail(
                    "DevCase: blog comment received",
                    f"Message:{message} | Author: {author}",
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.EMAIL_RECIPIENT],
                    fail_silently=False,
                )

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
        "comments": comments,
        "form": form,
        "is_submitted": is_submitted,
    }
    return render(request, "blog/blog_detail.html", context=context)
