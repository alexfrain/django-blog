from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blogging.models import Post

# Create your views here.


class PostListView(ListView):
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')
    template_name = 'blogging/list.html'


class PostDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = 'blogging/detail.html'
