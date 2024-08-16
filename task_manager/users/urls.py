from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from task_manager.users import views

urlpatterns = [
    path('', views.UserIndexView.as_view(), name='users'),
    path('create/', views.UserRegisterView.as_view(), name='user_create'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
]
