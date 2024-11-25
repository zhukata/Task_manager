from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.utils.translation import gettext as _
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics, viewsets
from rest_framework .permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from task_manager.base_views import BaseCreateView, BaseDeleteView, BaseUpdateView
from task_manager.tasks.filters import TaskFilter
from task_manager.tasks.forms import TaskCreateForm
from task_manager.tasks.mixins import CheckAuthorMixin
from task_manager.tasks.models import Task
from task_manager.tasks.serializers import TaskSerializer


class TaskIndexView(LoginRequiredMixin, FilterView):
    model = Task
    filterset_class = TaskFilter
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'
    extra_context = {'title': _('Tasks'),
                     'button_name1': _('Create task'),
                     'button_name2': _('Show'), }


class TaskShowView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/show.html'


class TaskCreateView(BaseCreateView):
    form_class = TaskCreateForm
    success_url = reverse_lazy('tasks')
    success_message = _("Task was created successfully")
    extra_context = {'title': _('Create task'),
                     'button_name': _('Create'), }

    def form_valid(self, form):
        task = form.save(commit=False)
        task.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(BaseUpdateView):
    form_class = TaskCreateForm
    model = Task
    success_url = reverse_lazy('tasks')
    success_message = _("Task was updated successfully")
    extra_context = {'title': _('Update task'),
                     'button_name': _('Update'), }


class TaskDeleteView(CheckAuthorMixin, BaseDeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    success_message = _("Task was deleted")
    extra_context = {'title': _('Delete task'),
                     'button_name': _('Yes, delete'), }


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (Token)
