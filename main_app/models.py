from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, through='Like', related_name='post_likes')

    class Meta:
        ordering = ['-created_date']

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies')
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created_date']
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_photos')

    def __str__(self):
        return f"Photo for post_id: {self.post_id} @{self.url}"