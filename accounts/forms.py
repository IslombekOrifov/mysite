from typing import Any, Dict
from django import forms 

from .models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username',]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']