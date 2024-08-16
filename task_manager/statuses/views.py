from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.utils.translation import gettext as _

from task_manager.statuses.forms import StatusCraeteForm
from task_manager.statuses.models import Status

class StatusIndexView(ListView):
    model = Status
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'
    

class StatusCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = StatusCraeteForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses')
    success_message = _("Status was created successfully")


class StatusUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    form_class = StatusCraeteForm
    model = Status
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses')
    success_message = _("Status was updated successfully")


class StatusDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses')
    success_message = _("Status was deleted")
