from django.db import models

class RecommendPost(models.Model):
    user = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    body = models.TextField()
    update = models.DateTimeField('published date')
