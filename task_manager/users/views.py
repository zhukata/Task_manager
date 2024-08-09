from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
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
    success_url = reverse_lazy('user_create')
    

# class UserRegisterView(CreateView):

#     def get(self, request, *args, **kwargs):
#         form = UserRegisterForm()
#         return render(request, 'users/sign_up.html', {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = UserRegisterForm(request.POST)
#         if form.is_valid(): 
#             form.save()
#             return redirect('articles')

#         return render(request, 'users/sign_up.html', {'form': form})


# class UsersUpdateView(View):

#     def get(self, request, *args, **kwargs):
#         form = UserCreateForm()
#         return render(request, 'users/sign_up.html', {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = UserCreateForm(request.POST)
#         if form.is_valid(): 
#             form.save()


# class UsersDeleteView(View):

#     def get(self, request, *args, **kwargs):
#         form = UserCreateForm()
#         return render(request, 'users/sign_up.html', {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = UserCreateForm(request.POST)
#         if form.is_valid(): 
#             form.save()