from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'username',
            'type': 'text',
            'autofocus': '',
            'required': '',
            'placeholder': 'Username'
        }))
    password = forms.CharField(
        label="Password",
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'password',
            'type': 'password',
            'required': '',
            'placeholder': 'Password'
        }))
