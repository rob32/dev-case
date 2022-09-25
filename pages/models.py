from django.db import models
from django.urls import reverse

from solo.models import SingletonModel


class Page(models.Model):
    title = models.CharField(
        max_length=31,
        blank=False,
        null=False,
        unique=True,
    )
    slug = models.CharField(
        max_length=31,
        blank=False,
        null=False,
        unique=True,
    )
    content = models.TextField(
        max_length=4095,
        help_text="Markdown supported.",
    )
    updated = models.DateTimeField(
        auto_now=True,
        editable=True,
        verbose_name="updated at",
    )
    seo = models.TextField(
        verbose_name="SEO Description",
        max_length=255,
        blank=True,
        null=True,
        default=None,
    )

    class Meta:
        verbose_name = "Page-Footer"
        verbose_name_plural = "Pages-Footer"
        ordering = ["-updated"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("page", kwargs={"slug": self.slug})


class IndexSiteConfig(SingletonModel):
    headline = models.CharField(
        max_length=255,
        default="Welcome...",
    )
    intro_text = models.TextField(
        max_length=2047,
        default="Lorem ipsum dolor sit amet, consectetur",
    )
    seo = models.TextField(
        verbose_name="SEO Description",
        max_length=255,
        blank=True,
        null=True,
        default=None,
    )

    class Meta:
        verbose_name = "Home"

    def __str__(self):
        return "IndexSiteConfig"


class AboutSiteConfig(SingletonModel):
    intro_text = models.TextField(
        max_length=2047,
        default="Lorem ipsum dolor sit amet, consectetur",
        blank=False,
    )
    image = models.ImageField(
        help_text="Recommended resolution: 1:1 - Example: 500px * 500px",
        blank=False,
    )
    resume = models.FileField(
        upload_to="resume/",
        help_text="Optionally, recommended format: PDF",
        blank=True,
        null=True,
    )
    skills = models.CharField(
        max_length=511,
        default="Python Javascript CSS SQL",
        help_text="Listing separated by spaces",
        blank=False,
    )
    tools = models.CharField(
        max_length=511,
        default="Figma Docker Git Ngnix",
        help_text="Listing separated by spaces",
    )
    interessts = models.CharField(
        max_length=511,
        default="Music Linux Open-Source Pixel-Art",
        help_text="Listing separated by spaces",
    )
    markdown_content = models.TextField(
        max_length=4095,
        help_text="Main About-Content. Markdown supported",
        blank=True,
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
        verbose_name = "About"

    def __str__(self):
        return "AboutSiteConfig"

    def skills_as_list(self):
        return self.skills.split(" ")

    def tools_as_list(self):
        return self.tools.split(" ")

    def interessts_as_list(self):
        return self.interessts.split(" ")
