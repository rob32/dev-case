from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="Name",
        unique=True,
    )
    slug = models.SlugField(
        max_length=30,
        help_text="Unique identifying part of the URL",
        blank=False,
        unique=True,
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_list", kwargs={"slug": self.slug})


class BlogPost(models.Model):
    STATUS = (
        (0, "Draft"),
        (1, "Published"),
    )
    title = models.CharField(
        max_length=63,
        verbose_name="Title",
        unique=True,
        blank=False,
    )
    slug = models.SlugField(
        max_length=63,
        verbose_name="Slug",
        help_text="Unique identifying part of the URL",
        blank=False,
        unique=True,
    )
    image = models.ImageField(
        upload_to="blog-posts/",
        verbose_name="Image",
        help_text="Recommended resolution: 1040px * 585px",
        blank=True,
        null=True,
    )
    content = models.TextField()
    status = models.IntegerField(
        choices=STATUS,
        default=1,
        verbose_name="Status",
    )
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name="Created at",
        editable=True,
        blank=False,
    )
    updated = models.DateTimeField(
        auto_now=True,
        editable=True,
        verbose_name="updated at",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
    )
    category = models.ManyToManyField(Category)
    seo = models.TextField(
        verbose_name="SEO Description",
        max_length=255,
        blank=True,
        null=True,
        default=None,
    )

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    def display_categories(self):
        return ", ".join([cat.name for cat in self.category.all()])


class Comment(models.Model):
    post = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    author = models.CharField(
        verbose_name="Author",
        blank=False,
        null=False,
        max_length=63,
    )
    message = models.TextField(max_length=1023, verbose_name="Message")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date")
    public = models.BooleanField(default=False, verbose_name="Public")

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
