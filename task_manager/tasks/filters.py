import django_filters
from django import forms
from django.utils.translation import gettext as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from django.contrib.auth import get_user_model


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label=_('Status')
    )
    executor = django_filters.ModelChoiceFilter(
        queryset=get_user_model().objects.all(),
        label=_('Executor')
    )
    label = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_('Label')
    )
    only_author = django_filters.BooleanFilter(
        field_name='author',
        label=_('Only your tasks'),
        method='author_filter',
        widget=forms.CheckboxInput
    )

    # class Meta:
    #     model = Task
    #     fields = ['status', 'executor', 'labels', 'only_author']
    #     labels = {'status': _('Status'), 'executor': _('Executor'), }

    def author_filter(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
