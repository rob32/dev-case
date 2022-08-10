from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView

from blog.forms import CommentCreationForm
from config.models import MainConfig
from pages.models import Page

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


class BlogDetailView(DetailView):
    template_name = "blog/blog_detail.html"
    model = BlogPost
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_config"] = MainConfig.get_solo()
        context["pages"] = Page.objects.all()
        context["form"] = CommentCreationForm()
        context["comments"] = Comment.objects.filter(
            post=self.get_object(), public=True
        )
        return context

    def post(self, *args, **kwargs):
        self.object = self.get_object(self.get_queryset())
        form = CommentCreationForm(self.request.POST)
        if form.is_valid():
            form.instance.post = self.object
            form.save()
            return HttpResponseRedirect(self.object.get_absolute_url())
        else:
            context = self.get_context_data(**kwargs)
            context.update({"form": form})
            return self.render_to_response(context)


blog_detail = BlogDetailView.as_view()
