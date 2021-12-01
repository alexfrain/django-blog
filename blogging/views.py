from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.syndication.views import Feed
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from django.urls import reverse
from blogging.models import Post, Category
from blogging.serializers import UserSerializer, PostSerializer, CategorySerializer

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


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows published posts to be viewed or edited.
    """

    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows post categories to be viewed or edited.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
