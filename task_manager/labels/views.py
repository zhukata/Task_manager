from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

from task_manager.labels.forms import LabelCraeteForm
from task_manager.labels.models import Label


class LabelIndexView(ListView):
    model = Label
    template_name = 'labels/labels.html'
    context_object_name = 'labels'
    extra_context = {'title': _('labels'),
                     'button_name': _('Create label'), }


class LabelCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = LabelCraeteForm
    template_name = 'layouts/create.html'
    success_url = reverse_lazy('labels')
    success_message = _("Label was created successfully")
    extra_context = {'title': _('Create label'),
                     'form_url': 'label_create',
                     'button_name': _('Create'), }


class LabelUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    form_class = LabelCraeteForm
    model = Label
    template_name = 'layouts/update.html'
    success_url = reverse_lazy('labels')
    success_message = _("Label was updated successfully")
    extra_context = {'title': _('Update label'),
                     'form_url': 'label_update',
                     'button_name': _('Update'), }


class LabelDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'layouts/delete.html'
    success_url = reverse_lazy('labels')
    success_message = _("Label was deleted")
    extra_context = {'title': _('Delete label'),
                     'form_url': 'label_delete',
                     'button_name': _('Delete'), }

