from django import forms
from .models import *

class questionForm(forms.ModelForm):
    class Meta:
        model = civilQuestions
        fields = '__all__'