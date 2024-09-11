from django import forms
from django.utils.translation import gettext as _

from task_manager.labels.models import Label


class LabelCreateForm(forms.ModelForm):
    name = forms.CharField(label=_('Name'))

    class Meta:
        model = Label
        fields = ['name']
