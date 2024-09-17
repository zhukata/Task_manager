from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib import messages

from task_manager.base_views import BaseCreateView, BaseDeleteView, BaseIndexView, BaseUpdateView
from task_manager.statuses.forms import StatusCraeteForm
from task_manager.statuses.models import Status


class StatusIndexView(BaseIndexView):
    model = Status
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'
    extra_context = {'title': _('Statuses'),
                     'button_name': _('Create status'), }


class StatusCreateView(BaseCreateView):
    form_class = StatusCraeteForm
    success_url = reverse_lazy('statuses')
    success_message = _("Status was created successfully")
    extra_context = {'title': _('Create status'),
                     'button_name': _('Create'), }


class StatusUpdateView(BaseUpdateView):
    form_class = StatusCraeteForm
    model = Status
    success_url = reverse_lazy('statuses')
    success_message = _("Status was updated successfully")
    extra_context = {'title': _('Update status'),
                     'button_name': _('Update'), }


class StatusDeleteView(BaseDeleteView):
    model = Status
    success_url = reverse_lazy('statuses')
    success_message = _("Status was deleted")
    extra_context = {'title': _('Delete status'),
                     'button_name': _('Yes, delete'), }

    def post(self, request, *args, **kwargs):
        if self.get_object().statuses.all().exists():
            messages.error(self.request, _('The status cannot be deleted because it is in use.'))
            return redirect('statuses')
        return super().post(self, request, *args, **kwargs)
