from django import forms

from task_manager.labels.models import Label


class LabelCreateForm(forms.ModelForm):
    name = forms.CharField(label='Name')

    class Meta:
        model = Label
        fields = ['name']
