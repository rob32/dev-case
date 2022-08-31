from django.core.mail import send_mail
from django.shortcuts import render

from dev_case.settings import EMAIL_NOTIFICATION, EMAIL_RECIPIENT, USE_EMAIL_SMTP

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

            if USE_EMAIL_SMTP and EMAIL_NOTIFICATION:
                try:
                    send_mail(
                        subject=" DevCase: new message via contact-form",
                        message=f"You have a new message from {user_name} - {user_email}",
                        recipient_list=[EMAIL_RECIPIENT],
                    )
                except Exception:
                    pass

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
