from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.utils.translation import gettext as _

class UserPassesMixin(AccessMixin):
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.is_authenticated:
            if request.user.id != self.get_object().id or request.user.is_staff:
                messages.error(request, _('You do not have permission to modify another user.'))
                return redirect('users')
        return super().dispatch(request, *args, **kwargs)


class AuthorRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.is_authenticated:
            if request.user != self.get_object().author or request.user.is_staff:
                messages.info(request, _("A task can only be deleted by its author."))
                return redirect('tasks')
        return super().dispatch(request, *args, **kwargs)

    