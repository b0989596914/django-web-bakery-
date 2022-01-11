from django import forms
from .models import Person
from django.core.exceptions import ValidationError

class PersonModelForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'  # __all__ 表示要全部呈現中所有欄位

        labels = {
            'name': '姓名',
            'tel': '電話號碼',
            'data': '日期',
            'time': '時間',
            'email': '電子郵件',
            'way_id' : '取貨方式'
        }
