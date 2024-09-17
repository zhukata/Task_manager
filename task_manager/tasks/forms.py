from django import forms
from django.utils.translation import gettext as _

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task


class TaskCreateForm(forms.ModelForm):
    name = forms.CharField(label=_('Name'))
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label=_("Status"))

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels', ]
        labels = {
            'description': _('Description'),
            'executor': _('Executor'),
            'labels': _('Labels'),
        }
