from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

# Create your views here.

def home(request):
    return render(request, 'Blog/home.html',{})

def post(request):
    posts = Post.objects.all().order_by('title') 
    return render(request, 'Blog/post.html', {'posts': posts})  

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():  # Add parentheses
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()  # Add parentheses
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm()
    
    return render(request, 'blog/post_new.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_new.html', {'form': form})
