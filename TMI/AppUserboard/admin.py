from django.contrib import admin
from .models import Board
from .models import Comment

class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created']
    list_filter = ['created']
    search_fields = ['text', 'created']
    ordering = ['-created' ]

class CommentAdmin(admin.ModelAdmin):
    list_display = ['board', 'author','text', 'board']
    list_filter = ['board']

admin.site.register(Board, BoardAdmin)
admin.site.register(Comment, CommentAdmin)