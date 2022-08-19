from pages.models import Page


def pages_footer(request):
    pages = Page.objects.all()
    return {
        "pages": pages,
    }
