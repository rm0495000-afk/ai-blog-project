from django.urls import path
from . import views

app_name = 'ai_model'

urlpatterns = [

    # HOME
    path('', views.index, name='index'),

    # STATIC PAGES (MUST BE ABOVE SLUG)
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),

    # USER
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('my-activity/', views.my_activity, name='my_activity'),

    # DASHBOARD
    path('dashboard/', views.dashboard, name='dashboard'),

    # LIKE
    path('like/<slug:slug>/', views.toggle_like, name='like'),

    # 🔴 SLUG — ALWAYS LAST
    path('<slug:slug>/', views.detail, name='detail'),
]
