from django.db import models

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from django.contrib.auth import get_user_model


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='author')
    executor = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, null=True, blank=True, related_name='executor')
    labels = models.ManyToManyField(Label, related_name='labels', blank=True)#on_delete=models.PROTECT
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
