from django import forms
from .models import Board, Comment

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'text', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class SearchForm(forms.Form):
    word = forms.CharField(label='Search Word')
