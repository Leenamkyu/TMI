from django import forms
from .models import Companion

#새로추가 8/9        
class DateForm(forms.Form):
    date = forms.DateField(input_formats=['%d/%m/%Y %H:%M'])       

class CompanionPost(forms.ModelForm):
    class Meta:
        model = Companion
        start_date = forms.DateField(input_formats=['%m/%d/%Y'])
        end_date = forms.DateField(input_formats=['%m/%d/%Y'])
        fields = ['status','category','title', 'country', 'city', 'bucket_list', 'start_date','end_date','body'] #새로 추가 
       
