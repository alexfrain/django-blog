from django.urls import path
from blogging.views import stub_view

urlpatterns = [
    path('', stub_view, name='blog_index'),
]
