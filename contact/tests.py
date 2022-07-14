from django.test import TestCase
from django.utils import timezone

from .models import Contact


class ContactTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.contact = Contact.objects.create(
            name="Max",
            message="Lorem ipsum...",
            email="test@testuser.com",
            date=timezone.now(),
        )

    def test_contact_model_content(self):
        self.assertEqual(self.contact.name, "Max")
        self.assertEqual(self.contact.message, "Lorem ipsum...")

    def test_contact_view(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact.html")
        self.assertContains(response, "Contact")
