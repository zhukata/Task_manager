from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label=_('first name'), widget=forms.TextInput())
    last_name = forms.CharField(label=_('last name'), widget=forms.TextInput())
    username = forms.CharField(label=_('username'), widget=forms.TextInput())
    password1 = forms.CharField(label=_('password'), widget=forms.PasswordInput(), min_length=3)
    password2 = forms.CharField(label=_('repeat password'), widget=forms.PasswordInput(), min_length=3)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


class UserUpdateForm(UserChangeForm):
    username = forms.CharField(label=_('username'), widget=forms.TextInput())
    password1 = forms.CharField(label=_('password'), widget=forms.PasswordInput(), min_length=3)
    password2 = forms.CharField(label=_('repeat password'), widget=forms.PasswordInput(), min_length=3)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
        labels = {'first_name': _('first name'), 'last_name': _('last name')}
        help_texts = {'password': None, }
