from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from portfolio.models import Project, TechStack, Tool


class ProjectTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="TestUser",
            email="testuser@email.com",
            password="testPasswort!123456",
        )
        cls.techstack = TechStack.objects.create(
            name="Django",
        )
        cls.tool = Tool.objects.create(
            name="Docker",
        )
        cls.project = Project.objects.create(
            title="Project One",
            slug="project-one",
            subtitle="This is a Subtitle",
            image="not-a-real-image.jpg",
            thumbnail="not-a-real-image.jpg",
            content="Lorem ipsum...",
            status=1,
            created=timezone.now(),
            author=cls.user,
        )
        cls.project.techstack.add(cls.techstack)
        cls.project.tools.add(cls.tool)

    def test_model_content(self):
        self.assertEqual(self.project.title, "Project One")
        self.assertEqual(self.project.author.username, "TestUser")
        self.assertEqual(self.project.techstack.first().name, "Django")

    def test_project_detail_view(self):
        response = self.client.get("/projects/project-one/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "portfolio/project_detail.html")
        self.assertContains(response, "Project One")
        self.assertContains(response, "Django")
        self.assertContains(response, "Docker")

    def test_project_list_view(self):
        response = self.client.get("/projects/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "portfolio/project_list.html")
        self.assertContains(response, "Project One")
