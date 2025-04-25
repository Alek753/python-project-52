from django.db import models
from django.contrib.auth.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='status')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')
    executor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='executor', blank=True, null=True)
    labels = models.ManyToManyField(Label, through='TaskLabelRelation',related_name='labels', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TaskLabelRelation(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
