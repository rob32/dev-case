from django.db import models

from solo.models import SingletonModel

ABOUT_EXAMPLE_CONTENT = """

## Work Experience

Lorem ipsum dolor sit amet, **consectetur**.
Lorem ipsum dolor sit amet, __consectetur__.
Lorem ipsum dolor sit amet, `consectetur`...

## Education

Lorem ipsum dolor sit amet, **consectetur**.
Lorem ipsum dolor sit amet, __consectetur__.
Lorem ipsum dolor sit amet, `consectetur`...

"""


class MainConfig(SingletonModel):
    site_name = models.CharField(
        max_length=255,
        default="dev-case.com",
    )
    favicon = models.ImageField()
    copyright_footer = models.CharField(
        max_length=255,
        default="Your Name © 2022",
    )
    email_adresse = models.CharField(
        max_length=255,
        default="email [@] adress [dot] com",
    )

    class Meta:
        verbose_name = "Main Settings"

    def __str__(self):
        return "MainConfig"


class SocialAccountsConfig(SingletonModel):
    github = models.CharField(
        max_length=255,
        default="",
        blank=True,
        null=True,
    )
    gitlab = models.CharField(
        max_length=255,
        default="",
        blank=True,
        null=True,
    )
    instagram = models.CharField(
        max_length=255,
        default="",
        blank=True,
        null=True,
    )
    linkedin = models.CharField(
        max_length=255,
        default="",
        blank=True,
        null=True,
    )
    mastodon = models.CharField(
        max_length=255,
        default="",
        blank=True,
        null=True,
    )
    twitter = models.CharField(
        max_length=255,
        default="",
        blank=True,
        null=True,
    )
    xing = models.CharField(
        max_length=255,
        default="",
        blank=True,
        null=True,
    )
    youtube = models.CharField(
        max_length=255,
        default="",
        blank=True,
        null=True,
    )
    rss = models.CharField(
        max_length=255,
        default="",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Social Accounts"

    def __str__(self):
        return "SocialAccountsConfig"
