from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib import messages

from task_manager.mixins import CreateMixin, DeleteMixin, IndexMixin, UpdateMixin
from task_manager.statuses.forms import StatusCraeteForm
from task_manager.statuses.models import Status


class StatusIndexView(IndexMixin):
    model = Status
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'
    extra_context = {'title': _('Statuses'),
                     'button_name': _('Create status'), }


class StatusCreateView(CreateMixin):
    form_class = StatusCraeteForm
    success_url = reverse_lazy('statuses')
    success_message = _("Status was created successfully")
    extra_context = {'title': _('Create status'),
                     'form_url': 'status_create',
                     'button_name': _('Create'), }


class StatusUpdateView(UpdateMixin):
    form_class = StatusCraeteForm
    model = Status
    success_url = reverse_lazy('statuses')
    success_message = _("Status was updated successfully")
    extra_context = {'title': _('Update status'),
                     'form_url': 'status_update',
                     'button_name': _('Update'), }


class StatusDeleteView(DeleteMixin):
    model = Status
    success_url = reverse_lazy('statuses')
    success_message = _("Status was deleted")
    extra_context = {'title': _('Delete status'),
                     'form_url': 'status_delete',
                     'button_name': _('Delete'), }

    def form_valid(self, form):
        if self.object.statuses.all().exists():
            messages.error(self.request, _('The status cannot be deleted because it is in use.'))
            return redirect('statuses')
        return super().form_valid(form)
