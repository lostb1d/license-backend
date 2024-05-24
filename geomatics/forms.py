from django import forms
from .models import *

class questionForm(forms.ModelForm):
    class Meta:
        model = questions
        fields = '__all__'