from django import forms
from .models import Examination

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Examination
        fields = '__all__'