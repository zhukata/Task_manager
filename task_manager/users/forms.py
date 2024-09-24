from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label=_('First name'), widget=forms.TextInput())
    last_name = forms.CharField(label=_('Last name'), widget=forms.TextInput())

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


class UserUpdateForm(UserRegisterForm):

    def clean_username(self):
        """Reject usernames that differ only in case."""
        username = self.cleaned_data.get("username")
        return username
