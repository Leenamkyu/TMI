from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=20, default='no name')
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='board_images/')
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created']
     

class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=300)
    author = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text