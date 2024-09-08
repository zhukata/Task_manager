from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class CheckUserMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('You are not logged in! Please sign in.'))
            return redirect('user_login')
        if request.user.id != self.get_object().id:
            messages.error(request, _('You do not have permission to modify another user.'))
            return redirect('users')
        return super().dispatch(request, *args, **kwargs)


class CheckAuthorMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user != self.get_object().author:
                messages.error(request, _("A task can only be deleted by its author."))
                return redirect('tasks')
        return super().dispatch(request, *args, **kwargs)


class IndexMixin(ListView, LoginRequiredMixin):
    pass


class CreateUserMixin(SuccessMessageMixin, CreateView): # base class
    template_name = 'layouts/create.html'


class CreateMixin(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'layouts/create.html'


class UpdateMixin(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'layouts/update.html'


class DeleteMixin(SuccessMessageMixin, DeleteView):
    template_name = 'layouts/delete.html'
