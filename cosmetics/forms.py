from django import forms
from .models import LoginCosmetic

class LoginForm(forms.ModelForm):
    class Meta:
        model=LoginCosmetic
        fields= '__all__'