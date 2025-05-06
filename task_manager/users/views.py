from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .forms import RegistrationForm
# from .models import User
from task_manager.mixins import UserAccessMixin, ProtectedErrorMixin

# Create your views here.
class UsersListView(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users'

class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('login')
    success_message = 'Пользователь успешно создан!'

class UserUpdateView(SuccessMessageMixin, UserAccessMixin, UpdateView):
    model = User
    form_class = RegistrationForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:list')
    success_message = 'Пользователь успешно отредактирован!'
    permission_denied_message =  'У вас нет прав для изменения другого пользователя.'
    permission_url = reverse_lazy('users:list')

class UserDeleteView(SuccessMessageMixin, UserAccessMixin, ProtectedErrorMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:list')
    success_message = 'Пользователь успешно удален!'
    permission_denied_message =  'У вас нет прав для удаления другого пользователя.'
    permission_url = reverse_lazy('users:list')
    error_message = "Невозможно удалить пользователя, потому что он используется!"
