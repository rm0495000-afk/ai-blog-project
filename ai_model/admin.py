from django.contrib import admin
from unfold.admin import ModelAdmin   # 🔥 IMPORTANT
from .models import Post

@admin.register(Post)
class PostAdmin(ModelAdmin):           # 🔥 IMPORTANT
    list_display = ("title",)
