from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='username', widget=forms.TextInput())
    password1 = forms.CharField(label='password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='repeat password', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = { 'first_name': 'first_name', 'last_name': 'last_name', 'email': 'email'}