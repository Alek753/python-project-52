from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskCreateForm
from task_manager.mixins import UserAccessMixin

# Create your views here.
class TasksListView(ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'

class TaskCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('tasks:list')
    success_message = 'Задача успешно создана!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks:list')
    success_message = 'Задача успешно отредактирована!'
#    permission_denied_message =  'У вас нет прав для изменения чужой задачи'

class TaskDeleteView(SuccessMessageMixin, UserAccessMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks:list')
    success_message = 'Задача успешно удалена!'
    permission_denied_message =  'Задачу может удалить только ее автор'
    permission_url = reverse_lazy('tasks:list')
