""" View definitions for blog app """
from django.views.generic import ListView, DetailView
from .models import Post


class BlogListView(ListView):
    """ Define view to list blog """
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'


class BlogDetailView(DetailView):
    """ Define detail view for each blog post """
    model = Post
    template_name = 'post_detail.html'
