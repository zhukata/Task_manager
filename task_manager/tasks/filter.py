import django_filters
from django import forms
from django.utils.translation import gettext as _

from task_manager.labels.models import Label
from task_manager.tasks.models import Task


class TaskFilter(django_filters.FilterSet):
    labels = django_filters.ModelChoiceFilter(queryset=Label.objects.all())
    only_author = django_filters.BooleanFilter(field_name='author', label=_('Only your tasks'), method='author_filter', widget=forms.CheckboxInput)

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'only_author']

    def author_filter(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
