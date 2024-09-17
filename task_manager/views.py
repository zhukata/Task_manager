from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext as _

class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'layouts/create.html'
    success_message = _("You are login")
    extra_context = {'title': _('Authorization'),
                     'button_name': _('Login'), }


class UserLogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _("You are logged out"))
        return super().dispatch(request, *args, **kwargs)
