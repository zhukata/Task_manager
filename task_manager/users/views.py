from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView
from django.utils.translation import gettext as _

from task_manager.base_views import BaseDeleteView, BaseUpdateView
from task_manager.users.forms import UserRegisterForm, UserUpdateForm
from task_manager.users.mixins import CheckUserMixin


class UserIndexView(ListView):
    model = get_user_model()
    template_name = 'users/users.html'
    context_object_name = 'users'
    extra_context = {'title': _('Users'), }


class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    template_name = 'layouts/create.html'
    success_url = reverse_lazy('user_login')
    success_message = _("User was created successfully")
    extra_context = {'title': _('Sign Up'),
                     'button_name': _('Register'), }


class UserUpdateView(CheckUserMixin, BaseUpdateView):
    form_class = UserUpdateForm
    model = get_user_model()
    success_url = reverse_lazy('users')
    success_message = _("User was updated successfully")
    extra_context = {'title': _('Update user'),
                     'button_name': _('Update'), }


class UserDeleteView(CheckUserMixin, BaseDeleteView):
    model = get_user_model()
    success_url = reverse_lazy('users')
    success_message = _("User was deleted")
    extra_context = {'title': _('Delete user'),
                     'button_name': _('Delete'), }

    def form_valid(self, form):
        if self.object.author.all().exists() or self.object.executor.all().exists():
            messages.error(self.request, _('Cannot delete user because it is in use'))
            return redirect('users')
        return super().form_valid(form)
