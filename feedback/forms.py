from django import forms
from .models import Opinion
from django.core.exceptions import ValidationError

class OpinionModelForm(forms.ModelForm):

   class Meta:
       model = Opinion
       fields = '__all__'  

       labels = {
           'name': '姓名',
           'text': '建議',
       }
