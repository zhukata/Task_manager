from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django_filters.views import FilterView

from task_manager.mixins import AuthorRequiredMixin
from task_manager.tasks.forms import TaskCraeteForm, TaskFilter
from task_manager.tasks.models import Task


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


class TaskCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = TaskCraeteForm
    template_name = 'layouts/create.html'
    success_url = reverse_lazy('tasks')
    success_message = _("Task was created successfully")
    extra_context = {'title': _('Create task'),
                     'form_url': 'task_create', #reverse
                     'button_name': _('Create'), }

    def form_valid(self, form):
        task = form.save(commit=False)
        task.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    form_class = TaskCraeteForm
    model = Task
    template_name = 'layouts/update.html'
    success_url = reverse_lazy('tasks')
    success_message = _("Task was updated successfully")
    extra_context = {'title': _('Update task'),
                     'form_url': 'task_update',
                     'button_name': _('Update'), }


class TaskDeleteView(SuccessMessageMixin, AuthorRequiredMixin, DeleteView):
    model = Task
    template_name = 'layouts/delete.html'
    success_url = reverse_lazy('tasks')
    success_message = _("Task was deleted")
    extra_context = {'title': _('Delete task'),
                     'form_url': 'task_delete',
                     'button_name': _('Delete'), }
