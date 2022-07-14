from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from blog.models import BlogPost, Category


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="TestUser",
            email="testuser@email.com",
            password="testPasswort!123456",
        )
        cls.category_1 = Category.objects.create(
            name="Django",
            slug="django",
        )
        cls.category_2 = Category.objects.create(
            name="Python",
            slug="python",
        )
        cls.post = BlogPost.objects.create(
            title="Article One",
            slug="article-one",
            content="Lorem ipsum...",
            status=1,
            created=timezone.now(),
            author=cls.user,
        )
        cls.post.category.add(cls.category_1, cls.category_2)

    def test_model_content(self):
        self.assertEqual(self.post.title, "Article One")
        self.assertEqual(self.post.author.username, "TestUser")
        self.assertEqual(self.post.category.first().name, "Django")

    def test_blog_detail_url(self):
        response = self.client.get("/blog/article-one/")
        self.assertEqual(response.status_code, 200)

    def test_blog_list_url(self):
        url = reverse("blog")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_blog_list_template(self):
        response = self.client.get("/blog/")
        self.assertTemplateUsed(response, "blog/blog_list.html")
        self.assertContains(response, "Blog")
        self.assertContains(response, "Article One")
        self.assertContains(response, "Django")
        self.assertContains(response, "Python")

    def test_blog_detail_template(self):
        response = self.client.get(
            reverse("blog_detail", kwargs={"slug": self.post.slug})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blog_detail.html")
        self.assertContains(response, "Lorem ipsum...")
