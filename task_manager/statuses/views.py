from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from .models import Status
from .forms import StatusCreateForm

# Create your views here.
class StatusesListView(ListView):
    model = Status
    template_name = 'statuses/statuses_list.html'
    context_object_name = 'statuses'

class StatusCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Status
    form_class = StatusCreateForm
    template_name = 'simple_create.html'
    extra_context = {'title': _('Create status')}
    success_url = reverse_lazy('statuses:list')
    success_message = _('Status succesfully created')

class StatusUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusCreateForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses:list')
    success_message = _('Status successfully updated')

class StatusDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'delete.html'
    extra_context = {'title': _('Removing status')}
    success_url = reverse_lazy('statuses:list')
    success_message = _('Status successfully removed')
