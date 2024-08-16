from django import forms

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from django.contrib.auth import get_user_model



class TaskCraeteForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput())
    status = forms.ModelChoiceField(queryset=Status.objects.all(), empty_label="----------", label="Status")


    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor',]
        labels = {'description': 'Description', 'executor': 'Executor', }


    # executor = forms.ModelChoiceField(queryset=get_user_model().objects.all(), empty_label="----------", label="Executor")
    # labels = forms.ModelChoiceField(queryset=Label.objects.all(), empty_label="----------", label="Labels")
        # description = forms.CharField(label='Description', widget=forms.Textarea())