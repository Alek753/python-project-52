from django import forms
from django_filters import BooleanFilter, FilterSet, ModelChoiceFilter
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from .models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']


class TaskFilter(FilterSet):
    user_tasks = BooleanFilter(
        widget=forms.CheckboxInput(),
        label=_('Only your own tasks'),
        method='get_user_tasks')

    labels = ModelChoiceFilter(
        queryset=Label.objects.all(),
	label=_('Label')
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'user_tasks']

    def get_user_tasks(self, queryset, name, value):
        return queryset.filter(author=self.request.user) if value else queryset
