""" View definitions for blog app """
from django.views.generic import ListView
from .models import Post


class BlogListView(ListView):
    """ Define view to list blog """
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
