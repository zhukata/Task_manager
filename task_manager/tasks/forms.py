from django import forms

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task


class TaskCreateForm(forms.ModelForm):
    name = forms.CharField(label='Name')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label="Status")

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels', ]
        labels = {'description': 'Description', 'executor': 'Executor', 'labels': 'Labels', }
