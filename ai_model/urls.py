from django.urls import path
from . import views

app_name = 'ai_model'

urlpatterns = [

    # =========================
    # HOME
    # =========================
    path('', views.index, name='index'),

    # =========================
    # DASHBOARD
    # =========================
    path('dashboard/', views.dashboard, name='dashboard'),

    # =========================
    # LIKE / UNLIKE
    # =========================
    path('like/<slug:slug>/', views.toggle_like, name='like'),

    # =========================
    # API ENDPOINTS
    # =========================
    path('api/posts/', views.api_posts, name='api_posts'),
    path('api/analytics/', views.api_analytics, name='analytics'),

    # =========================
    # TEMP ADMIN SETUP (OPEN ONCE)
    # =========================
    path('setup-admin/', views.setup_admin, name='setup_admin'),

    # =========================
    # DETAIL PAGE (SLUG MUST BE LAST)
    # =========================
    path('<slug:slug>/', views.detail, name='detail'),
]
