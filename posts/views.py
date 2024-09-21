from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# Create your views here.

# def post_list(request):
#     post = Post.objects.all()
#     return render(request, "posts_list.html", {"post":post})

class PostList(ListView):
    model = Post
    template_name = "posts_list.html"

