from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def home(request):
    return render(request, 'Blog/home.html',{})

def post(request):
    posts = Post.objects.all().order_by('title')  # Show all posts, even if unpublished
    return render(request, 'Blog/post.html', {'posts': posts})  


