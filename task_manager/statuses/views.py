from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Status
from .forms import StatusCreateForm

# Create your views here.
class StatusesListView(ListView):
    model = Status
    template_name = 'statuses/statuses_list.html'
    context_object_name = 'statuses'

class StatusCreateView(SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusCreateForm
    template_name = 'statuses/status_create.html'
    success_url = reverse_lazy('statuses:list')
    success_message = 'Статус успешно создан!'

class StatusUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusCreateForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses:list')
    success_message = 'Статус успешно отредактирован!'
#    permission_denied_message =  'У вас нет прав для изменения другого пользователя.'

class StatusDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses:list')
    success_message = 'Статус успешно удален!'
#    permission_denied_message =  'У вас нет прав для удаления другого пользователя.'
