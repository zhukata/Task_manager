from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib import messages

from task_manager.labels.forms import LabelCreateForm
from task_manager.labels.models import Label
from task_manager.mixins import CreateMixin, DeleteMixin, IndexMixin, UpdateMixin


class LabelIndexView(IndexMixin):
    model = Label
    template_name = 'labels/labels.html'
    context_object_name = 'labels'
    extra_context = {'title': _('labels'),
                     'button_name': _('Create label'), }


class LabelCreateView(CreateMixin):
    form_class = LabelCreateForm
    success_url = reverse_lazy('labels')
    success_message = _("Label was created successfully")
    extra_context = {'title': _('Create label'),
                     'form_url': 'label_create',
                     'button_name': _('Create'), }


class LabelUpdateView(UpdateMixin):
    form_class = LabelCreateForm
    model = Label
    success_url = reverse_lazy('labels')
    success_message = _("Label was updated successfully")
    extra_context = {'title': _('Update label'),
                     'form_url': 'label_update',
                     'button_name': _('Update'), }


class LabelDeleteView(DeleteMixin):
    model = Label
    success_url = reverse_lazy('labels')
    success_message = _("Label was deleted")
    extra_context = {'title': _('Delete label'),
                     'form_url': 'label_delete',
                     'button_name': _('Delete'), }

    def post(self, request, *args, **kwargs):
        if self.get_object().labels.all().exists():
            messages.error(self.request, _('The label cannot be deleted because it is in use.'))
            return redirect('labels')
        return super().post(self, request, *args, **kwargs)
    