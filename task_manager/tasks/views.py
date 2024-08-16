from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _

from task_manager.mixins import AuthorRequiredMixin
from task_manager.tasks.forms import TaskCraeteForm
from task_manager.tasks.models import Task

class TaskIndexView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'


class TaskShowView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/show.html'


class TaskCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = TaskCraeteForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks')
    success_message = _("Task was created successfully")

    def form_valid(self, form):
        task = form.save(commit=False)
        task.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    form_class = TaskCraeteForm
    model = Task
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks')
    success_message = _("Task was updated successfully")


class TaskDeleteView(SuccessMessageMixin, AuthorRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks')
    success_message = _("Task was deleted")