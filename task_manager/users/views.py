from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.edit import DeletionMixin

from task_manager.mixins import ProtectedErrorMixin, UserAccessMixin
from .forms import RegistrationForm


# Create your views here.
class UsersListView(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users'
    ordering = ['id']


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('login')
    success_message = _('User successfully created')


class UserUpdateView(SuccessMessageMixin, UserAccessMixin, UpdateView):
    model = User
    form_class = RegistrationForm
    extra_context = {'title': _('Update user')}
    template_name = 'update.html'
    success_url = reverse_lazy('users:list')
    success_message = _('User successfully updated')
    permission_denied_message = _('You have no rights to update another user')
    permission_url = reverse_lazy('users:list')


class UserDeleteView(UserAccessMixin, ProtectedErrorMixin,
                     DeleteView):
    model = User
    error_message = _('Cannot remove this user because it is in use')
    template_name = 'delete.html'
    extra_context = {'title': _('Removing user')}
    permission_denied_message = _('You have no rights to delete another user')
    permission_url = reverse_lazy('users:list')
    success_url = reverse_lazy('users:list')
    success_message = _('User successfully removed')

