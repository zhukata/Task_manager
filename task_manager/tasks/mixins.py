from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.utils.translation import gettext as _

class CheckAuthorMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user != self.get_object().author:
                messages.error(request, _("A task can only be deleted by its author."))
                return redirect('tasks')
        return super().dispatch(request, *args, **kwargs)