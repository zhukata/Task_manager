from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from task_manager.tasks.forms import TaskCraeteForm
from task_manager.tasks.models import Task

class TaskIndexView(View):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, 'tasks/tasks.html', context={
            'tasks': tasks,
        })


class TaskShowView(View):
    pass


class TaskCreateView(SuccessMessageMixin, CreateView):
    form_class = TaskCraeteForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks')
    success_message = "Task was created successfully"


class TaskUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    form_class = TaskCraeteForm
    model = Task
    template_name = 'task/update.html'
    success_url = reverse_lazy('tasks')
    success_message = "Task was updated successfully"


class TaskDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task/delete.html'
    success_url = reverse_lazy('task')
    success_message = "Task was deleted"