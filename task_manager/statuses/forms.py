from django import forms

from task_manager.statuses.models import Status


class StatusCraeteForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput())

    class Meta:
        model = Status
        fields = ['name']
