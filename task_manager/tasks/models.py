from django.db import models

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from django.contrib.auth import get_user_model


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    author = models.ForeignKey(get_user_model(), related_name='author', on_delete=models.PROTECT)
    executor = models.ForeignKey(get_user_model(), related_name='executor', on_delete=models.PROTECT, blank=True)
    labels = models.ManyToManyField(Label, related_name='labels', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
