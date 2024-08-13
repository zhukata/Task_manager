from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm , UserChangeForm
from django.contrib.auth import get_user_model


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='username', widget=forms.TextInput())
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(), min_length=3)
    password2 = forms.CharField(label='repeat password', widget=forms.PasswordInput(), min_length=3)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        labels = { 'first_name': 'first_name', 'last_name': 'last_name', 'email': 'email'}


class UserUpdateForm(UserChangeForm):
    # def __init__(self, *args, **kwargs):
    #     super(UserChangeForm, self).__init__(*args, **kwargs)

    #     for fieldname in ['username', 'password1', 'password2']:
    #         self.fields[fieldname].help_text = None

    username = forms.CharField(label='username', widget=forms.TextInput())
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(), min_length=3)
    password2 = forms.CharField(label='repeat password', widget=forms.PasswordInput(), min_length=3)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        labels = { 'first_name': 'first_name', 'last_name': 'last_name', 'email': 'email'}
        help_texts = {'password': None,}


