from django import forms
from django.utils.translation import gettext as _

from task_manager.statuses.models import Status


class StatusCraeteForm(forms.ModelForm):
    name = forms.CharField(label=_('Name'), widget=forms.TextInput())

    class Meta:
        model = Status
        fields = ['name']
