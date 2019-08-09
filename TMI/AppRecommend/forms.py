from django import forms
from .models import RecommendPost


class NewPost(forms.ModelForm):
    class Meta:
        model = RecommendPost
        fields = ['title', 'body']
