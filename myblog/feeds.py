from django.contrib.syndication.views import Feed
from django.urls import reverse
from myblog.models import Post

class LatestEntriesFeed(Feed):
    title = "Latest Posts"
    link = "/feed/"
    description = "Updates on changes and additions to myblog."

    def items(self):
        return Post.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    # item_link is only needed if Post has no get_absolute_url method.
    def item_link(self, item):
        #return reverse('blog_detail', args=[item.pk])
        return item.get_absolute_url()