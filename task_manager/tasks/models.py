from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status


# Create your models here.
class UserFullName(User):
    class Meta:
        proxy = True

    def __str__(self):
        return self.get_full_name()


class Task(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_('Name')
    )
    description = models.TextField(
        blank=True,
        verbose_name=_('Description')
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='status',
        verbose_name=_('Status')
    )
    author = models.ForeignKey(
        UserFullName,
        on_delete=models.PROTECT,
        related_name='author',
        verbose_name=_('Author')
    )
    executor = models.ForeignKey(
        UserFullName,
        on_delete=models.PROTECT,
        related_name='executor',
        blank=True,
        null=True,
        verbose_name=_('Executor')
    )
    labels = models.ManyToManyField(
        Label,
        through='TaskLabelRelation',
        related_name='labels',
        blank=True, verbose_name=_('Labels')
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TaskLabelRelation(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE
    )
    label = models.ForeignKey(
        Label,
        on_delete=models.PROTECT
    )
