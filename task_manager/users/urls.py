from django.urls import path

from task_manager.users import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='users'),
    path('create/', views.UserRegisterView.as_view(), name='user_create'),
    # path('<int:pk>/update/', views.UsersUpdateView.as_view(), name='user_update'),
    # path('<int:pk>/delete/', views.UsersDeleteView.as_view(), name='user_delete'),
]