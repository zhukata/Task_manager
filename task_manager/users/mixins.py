from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class CheckUserMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('You are not logged in! Please sign in.'))
            return redirect('user_login')
        if request.user.id != self.get_object().id:
            messages.error(request, _('You do not have permission to modify another user.'))
            return redirect('users')
        return super().dispatch(request, *args, **kwargs)
