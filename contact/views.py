from django.shortcuts import render

from config.models import MainConfig
from pages.models import Page

from .forms import ContactForm
from .models import Contact


def contact(request):
    main_config = MainConfig.get_solo()
    pages = Page.objects.all()
    is_submitted = False

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            user_name = form.cleaned_data["user_name"]
            user_message = form.cleaned_data["user_message"]
            user_email = form.cleaned_data["user_email"]

            new_contact = Contact(
                name=user_name,
                message=user_message,
                email=user_email,
            )

            new_contact.save()
            is_submitted = True
            form = ContactForm()
    else:
        form = ContactForm()

    context = {
        "main_config": main_config,
        "form": form,
        "is_submitted": is_submitted,
        "pages": pages,
    }

    return render(request, "contact.html", context=context)
