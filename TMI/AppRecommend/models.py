from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class RecommendPost(models.Model):
    user = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    body = models.TextField()
    update = models.DateTimeField('published date')
    likes = models.ManyToManyField(User, blank=True, related_name='like')

    def like_count(self):
        return self.likes.count()


class Comment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.ForeignKey('RecommendPost', related_name='comments', on_delete = models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text