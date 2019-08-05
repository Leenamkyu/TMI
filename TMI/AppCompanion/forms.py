from django import forms
from .models import Companion

class CompanionPost(forms.ModelForm):
    class Meta:
        model = Companion
        fields = ['title', 'country', 'city', 'bucket_list', 'body']