from django.urls import path
from . import views

app_name = 'ai_model'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('my-activity/', views.my_activity, name='my_activity'),
    path('like/<slug:slug>/', views.toggle_like, name='like'),
    path('<slug:slug>/', views.detail, name='detail'),
]
