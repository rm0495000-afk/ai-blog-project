from django.urls import path
from . import views

app_name = 'ai_model'

urlpatterns = [
    path('', views.index, name='index'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('like/<slug:slug>/', views.toggle_like, name='like'),

    path('api/posts/', views.api_posts, name='api_posts'),
    path('api/analytics/', views.api_analytics, name='analytics'),

    path('<slug:slug>/', views.detail, name='detail'),  # 🔴 ALWAYS LAST
]