from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import requests
from django.core.files.base import ContentFile

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()

    image = models.ImageField(upload_to='posts/', blank=True)
    ai_summary = models.TextField(blank=True)

    views = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, blank=True, related_name='liked_posts')

    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        if not self.ai_summary:
            self.ai_summary = self.content[:150] + "..."

        # AI IMAGE AUTO DOWNLOAD
        if not self.image:
            url = f"https://picsum.photos/seed/{self.slug}/800/500"
            res = requests.get(url)
            if res.status_code == 200:
                self.image.save(
                    f"{self.slug}.jpg",
                    ContentFile(res.content),
                    save=False
                )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
