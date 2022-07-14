from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from blog.models import BlogPost

from .settings import FEED_DESCRIPTION, FEED_TITLE


class BlogFeed(Feed):
    title = FEED_TITLE
    description = FEED_DESCRIPTION
    link = "/feed/"

    def items(self):
        return BlogPost.objects.order_by("-created")[:15]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 23)

    def item_pubdate(self, item):
        return item.created
