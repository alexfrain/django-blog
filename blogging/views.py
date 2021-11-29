from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post

# Create your views here.


class PostListView(ListView):
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"


class PublishedPostsFeed(Feed):
    title = "Coolest Posts"
    link = "/siteposts/"
    description = "Cool posts from the mind of an author."

    def items(self):
        return Post.objects.exclude(published_date__exact=None).order_by(
            "-published_date"
        )

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return reverse("blog_detail", args=[item.pk])
