from django import template
from django.template.defaultfilters import stringfilter

from markdown import markdown as md

register = template.Library()


@register.filter
@stringfilter
def markdown(value):
    return md(value, extensions=["extra", "codehilite", "toc"])
