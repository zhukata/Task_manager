from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class BaseIndexView(ListView, LoginRequiredMixin):
    pass


class BaseCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'layouts/create.html'


class BaseUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'layouts/update.html'


class BaseDeleteView(SuccessMessageMixin, DeleteView):
    template_name = 'layouts/delete.html'
