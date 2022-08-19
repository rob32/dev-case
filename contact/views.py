from django.shortcuts import render

from .forms import ContactForm
from .models import Contact


def contact(request):
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
        "form": form,
        "is_submitted": is_submitted,
    }

    return render(request, "contact.html", context=context)
