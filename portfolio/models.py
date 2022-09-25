from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class TechStack(models.Model):
    name = models.CharField(
        max_length=63,
        verbose_name="Name",
        unique=True,
    )

    class Meta:
        verbose_name = "Techstack"
        verbose_name_plural = "Techstacks"

    def __str__(self):
        return self.name


class Tool(models.Model):
    name = models.CharField(
        max_length=63,
        verbose_name="Name",
        unique=True,
    )

    class Meta:
        verbose_name = "Tool"
        verbose_name_plural = "Tools"

    def __str__(self):
        return self.name


class Project(models.Model):
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
    subtitle = models.CharField(
        max_length=63,
        verbose_name="Subtitle",
        unique=True,
        blank=False,
    )
    image = models.ImageField(
        upload_to="projects/",
        verbose_name="Image",
        help_text="Recommended resolution: 1040px * 585px",
        blank=False,
        null=True,
    )
    thumbnail = models.ImageField(
        upload_to="projects/",
        verbose_name="Thumbnail",
        help_text="Recommended resolution: 150px * 150px",
        blank=False,
        null=True,
    )
    content = models.TextField()
    techstack = models.ManyToManyField(TechStack)
    tools = models.ManyToManyField(Tool)
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
    seo = models.TextField(
        verbose_name="SEO Description",
        max_length=255,
        blank=True,
        null=True,
        default=None,
    )

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})

    def display_techstack(self):
        return ", ".join([stack.name for stack in self.techstack.all()])

    def display_tools(self):
        return ", ".join([tool.name for tool in self.tools.all()])
