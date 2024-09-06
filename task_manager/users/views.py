from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from task_manager.mixins import CheckUserMixin, CreateUserMixin, DeleteMixin, UpdateMixin
from task_manager.users.forms import UserRegisterForm, UserUpdateForm
from django.utils.translation import gettext as _


class UserIndexView(ListView):
    model = get_user_model()
    template_name = 'users/users.html'
    context_object_name = 'users'
    extra_context = {'title': _('Users'), }


class UserRegisterView(CreateUserMixin):
    form_class = UserRegisterForm
    success_url = reverse_lazy('user_login')
    success_message = _("User was created successfully")
    extra_context = {'title': _('Create user'),
                     'form_url': 'user_create',
                     'button_name': _('Create'), }


class UserUpdateView(CheckUserMixin, UpdateMixin):
    form_class = UserUpdateForm
    model = get_user_model()
    success_url = reverse_lazy('users')
    success_message = _("User was updated successfully")
    extra_context = {'title': _('Update user'),
                     'form_url': 'user_update',
                     'button_name': _('Update'), }


class UserDeleteView(CheckUserMixin, DeleteMixin):
    model = get_user_model()
    success_url = reverse_lazy('users')
    success_message = _("User was deleted")
    extra_context = {'title': _('Delete user'),
                     'form_url': 'user_delete',
                     'button_name': _('Delete'), }

    def form_valid(self, form):
        if self.object.author.all().exists() or self.object.executor.all().exists():
            messages.error(self.request, _('Cannot delete user because it is in use'))
            return redirect('users')
        return super().form_valid(form)


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'layouts/create.html'
    success_message = _("You are login")
    extra_context = {'title': _('Login'),
                     'form_url': 'user_login',
                     'button_name': _('Login'), }


class UserLogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _("You are logged out"))
        return super().dispatch(request, *args, **kwargs)
