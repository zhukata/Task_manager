from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

from task_manager.statuses.forms import StatusCraeteForm
from task_manager.statuses.models import Status


class StatusIndexView(ListView):
    model = Status
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'
    extra_context = {'title': _('Statuses'),
                     'button_name': _('Create status'), }


class StatusCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = StatusCraeteForm
    template_name = 'layouts/create.html'
    success_url = reverse_lazy('statuses')
    success_message = _("Status was created successfully")
    extra_context = {'title': _('Create status'),
                     'form_url': 'status_create',
                     'button_name': _('Create'), }


class StatusUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    form_class = StatusCraeteForm
    model = Status
    template_name = 'layouts/update.html'
    success_url = reverse_lazy('statuses')
    success_message = _("Status was updated successfully")
    extra_context = {'title': _('Update status'),
                     'form_url': 'status_update',
                     'button_name': _('Update'), }


class StatusDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'layouts/delete.html'
    success_url = reverse_lazy('statuses')
    success_message = _("Status was deleted")
    extra_context = {'title': _('Delete status'),
                     'form_url': 'status_delete',
                     'button_name': _('Delete'), }
