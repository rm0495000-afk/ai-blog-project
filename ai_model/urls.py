from django.urls import path
from . import views

app_name = 'ai_model'

urlpatterns = [

    # HOME
    path('', views.index, name='index'),

    # COMPANY PAGES
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),

    # DASHBOARD
    path('dashboard/', views.dashboard, name='dashboard'),

    # LIKE
    path('like/<slug:slug>/', views.toggle_like, name='like'),

    # API
    path('api/posts/', views.api_posts, name='api_posts'),
    path('api/analytics/', views.api_analytics, name='analytics'),

    # TEMP ADMIN
    path('setup-admin/', views.setup_admin, name='setup_admin'),

    # DETAIL (ALWAYS LAST)
    path('<slug:slug>/', views.detail, name='detail'),
]
