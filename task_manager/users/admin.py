from django.contrib import admin

from task_manager.users.models import User

@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    search_fields = ['name', 'nickname']
