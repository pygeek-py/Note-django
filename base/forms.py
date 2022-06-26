from django import forms
from .models import note

class noteform(forms.ModelForm):
    class Meta:
        model = note
        fields = '__all__'
        exclude = ['create']