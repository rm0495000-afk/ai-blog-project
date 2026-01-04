from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User

from .models import Post, Comment


# =========================
# HOME / INDEX
# =========================
def index(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')

    q = request.GET.get('q')
    if q:
        posts = posts.filter(title__icontains=q)

    trending_posts = Post.objects.filter(
        is_published=True
    ).order_by('-views')[:3]

    return render(request, 'ai_model/index.html', {
        'posts': posts,
        'trending_posts': trending_posts,
        'query': q
    })


# =========================
# DETAIL PAGE ( /<slug>/ )
# =========================
def detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)

    # increase views
    post.views += 1
    post.save()

    # add comment
    if request.method == "POST" and request.user.is_authenticated:
        text = request.POST.get('comment')
        if text:
            Comment.objects.create(
                post=post,
                user=request.user,
                text=text
            )

    comments = Comment.objects.filter(post=post).order_by('-created_at')

    return render(request, 'ai_model/detail.html', {
        'post': post,
        'comments': comments
    })


# =========================
# DASHBOARD ( /dashboard/ )
# =========================
@login_required
def dashboard(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'ai_model/dashboard.html', {'posts': posts})


# =========================
# LIKE / UNLIKE ( /like/<slug>/ )
# =========================
@login_required
def toggle_like(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('ai_model:detail', slug=slug)


# =========================
# API – POSTS
# =========================
def api_posts(request):
    data = list(
        Post.objects.filter(is_published=True)
        .values('title', 'slug', 'views')
    )
    return JsonResponse(data, safe=False)


# =========================
# API – ANALYTICS
# =========================
def api_analytics(request):
    data = list(
        Post.objects.values('title', 'slug', 'views')
    )
    return JsonResponse(data, safe=False)


# =========================
# TEMP ADMIN SETUP (EASY FIX)
# =========================
def setup_admin(request):
    """
    Open this URL ONCE after deploy:
    /setup-admin/

    Username: admin
    Password: admin123
    """

    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@gmail.com",
            password="admin123"
        )
        return HttpResponse("Admin user created successfully")

    return HttpResponse("Admin already exists")
