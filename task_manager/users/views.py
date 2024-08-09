from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model

from task_manager.users.forms import UserRegisterForm
# from task_manager.users.models import User

class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = get_user_model().objects.all()
        return render(request, 'users/users.html', context={
            'users': users,
        })



class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/sign_up.html'
    success_url = reverse_lazy('users')


class UsersUpdateView(UpdateView):
    form_class = UserRegisterForm
    model = get_user_model()
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')


class UsersDeleteView(DeleteView):
    model = get_user_model()
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')