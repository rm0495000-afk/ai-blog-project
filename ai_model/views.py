from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Post, Comment

def index(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'ai_model/index.html', {'posts': posts})


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.views += 1
    post.save()

    if request.method == "POST" and request.user.is_authenticated:
        Comment.objects.create(
            post=post,
            user=request.user,
            text=request.POST.get('comment')
        )

    comments = Comment.objects.filter(post=post)
    return render(request, 'ai_model/detail.html', {
        'post': post,
        'comments': comments
    })


@login_required
def toggle_like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('ai_model:detail', slug=slug)


def user_login(request):
    error = None
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('/')
        error = "Invalid credentials"
    return render(request, 'ai_model/login.html', {'error': error})


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')


@login_required
def dashboard(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'ai_model/dashboard.html', {'posts': posts})


@login_required
def my_activity(request):
    comments = Comment.objects.filter(user=request.user)
    liked_posts = Post.objects.filter(likes=request.user)
    return render(request, 'ai_model/my_activity.html', {
        'comments': comments,
        'liked_posts': liked_posts
    })
