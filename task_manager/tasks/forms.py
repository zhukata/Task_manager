import django_filters
from django import forms

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task


class TaskCraeteForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput())
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label="Status")

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels', ]
        labels = {'description': 'Description', 'executor': 'Executor', 'labels': 'Labels', }

BOOLEAN_CHOICES = (('false', 'False'), ('true', 'True'),)

class TaskFilter(django_filters.FilterSet):
    flag = django_filters.BooleanFilter(widget=forms.CheckboxInput)
    labels = django_filters.ModelChoiceFilter(queryset=Label.objects.all())
    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'flag']
