from django import forms

from task_manager.tasks.models import Task



class TaskCraeteForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput())

    class Meta:
        model = Task
        fields = ['name']