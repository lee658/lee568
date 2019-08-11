from django import forms
from .models import Information

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = '__all__'
