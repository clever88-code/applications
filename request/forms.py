from django import forms
from django.core.exceptions import ValidationError
from requests import request
from core.models import *

class Application_forms(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['number_cab'].widget.attrs.update({'placeholder': 'Введите гос.номер'})
        self.fields['description'].widget.attrs.update({'placeholder': 'Опишите проблему в кабинете'})


    class Meta:
        model = Application
        fields = ['number_cab', 'description']
