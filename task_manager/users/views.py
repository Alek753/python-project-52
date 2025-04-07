from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import RegistrationForm

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

class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = RegistrationForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')
    success_message = 'Пользователь успешно отредактирован!'
#    context_object_name = 'user_update'
