from django import forms
from django_filters import FilterSet, BooleanFilter, ModelChoiceFilter
from .models import Task
from task_manager.labels.models import Label

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']


class TaskFilter(FilterSet):
    user_tasks = BooleanFilter(
        widget=forms.CheckboxInput(),
        label='Только свои задачи',
        method='get_user_tasks')

    labels = ModelChoiceFilter(
        queryset=Label.objects.all()
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'user_tasks']

    def get_user_tasks(self, queryset, name, value):
        return queryset.filter(author=self.request.user) if value else queryset
