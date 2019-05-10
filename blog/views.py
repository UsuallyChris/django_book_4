""" View definitions for blog app """
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
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


class BlogCreateView(CreateView):
    """ Define create view for posts """
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    """ Define update view for posts """
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
