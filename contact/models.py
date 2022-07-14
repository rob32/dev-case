from django.db import models
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(
        max_length=63,
        blank=False,
        null=False,
    )
    message = models.TextField(
        max_length=767,
        blank=False,
        null=False,
    )
    email = models.EmailField(
        max_length=63,
        blank=False,
        null=False,
    )
    date = models.DateTimeField(
        default=timezone.now,
        blank=False,
    )

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.date}--{self.email}"
