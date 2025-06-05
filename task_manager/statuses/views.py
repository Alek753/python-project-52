from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import StatusCreateForm
from .models import Status
from task_manager.mixins import ProtectedErrorMixin


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
    success_message = _('Status successfully created')


class StatusUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusCreateForm
    extra_context = {'title': _('Update status')}
    template_name = 'update.html'
    success_url = reverse_lazy('statuses:list')
    success_message = _('Status successfully updated')


class StatusDeleteView(SuccessMessageMixin, LoginRequiredMixin, 
                       ProtectedErrorMixin,DeleteView):
    model = Status
    error_message = _('Cannot remove this status because it is in use')
    template_name = 'delete.html'
    extra_context = {'title': _('Removing status')}
    success_url = reverse_lazy('statuses:list')
    permission_url = reverse_lazy('statuses:list')
    success_message = _('Status successfully removed')
