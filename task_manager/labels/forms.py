from django import forms

from task_manager.labels.models import Label


class LabelCraeteForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput())

    class Meta:
        model = Label
        fields = ['name']