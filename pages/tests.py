from django.test import TestCase
from django.utils import timezone

from .models import Page


class PageTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.page = Page.objects.create(
            title="Page One",
            slug="page-one",
            content="Lorem ipsum...",
            updated=timezone.now(),
        )

    def test_model_content(self):
        self.assertEqual(self.page.title, "Page One")
        self.assertEqual(self.page.content, "Lorem ipsum...")

    def test_page_footer_view(self):
        response = self.client.get("/page-one/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "page.html")
        self.assertContains(response, "Page One")

    def test_page_footer_nanbar(self):
        response = self.client.get("/")
        self.assertContains(response, "Page One")
