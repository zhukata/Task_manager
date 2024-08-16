from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from task_manager.mixins import UserPassesMixin
from task_manager.users.forms import UserRegisterForm, UserUpdateForm
from django.utils.translation import gettext as _



class UserIndexView(ListView):
    model = get_user_model()
    template_name = 'users/users.html'
    context_object_name = 'users'


class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    template_name = 'users/sign_up.html'
    success_url = reverse_lazy('user_login')
    success_message = _("User was created successfully")
    

class UserUpdateView(SuccessMessageMixin, UserPassesMixin, UpdateView):
    form_class = UserUpdateForm
    model = get_user_model()
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')
    success_message = _("User was updated successfully")


class UserDeleteView(SuccessMessageMixin, UserPassesMixin, DeleteView):
    model = get_user_model()
    # context_object_name = 'object'
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
    success_message = _("User was deleted")


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    success_message = _("You are login")



class UserLogoutView(SuccessMessageMixin, LogoutView):
    success_message = _("You are logged out")
    
    # def form_valid(self):
    #     response = super().form_valid(self.form)
    #     success_message = self.get_success_message(self.form.cleaned_data)
    #     if success_message:
    #         messages.info(self.request, _("You are logged out"))
    #     return response
