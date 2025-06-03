from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.mixins import ProtectedErrorMixin

from .forms import LabelCreateForm
from .models import Label


# Create your views here.
class LabelsListView(ListView):
    model = Label
    template_name = 'labels/labels_list.html'
    context_object_name = 'labels'


class LabelCreateView(SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelCreateForm
    extra_context = {'title': _('Create label'), }
    template_name = 'simple_create.html'
    success_url = reverse_lazy('labels:list')
    success_message = _('Label successfully creted')


class LabelUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Label
    form_class = LabelCreateForm
    extra_context = {'title': _('Update label'), }
    template_name = 'update.html'
    success_url = reverse_lazy('labels:list')
    success_message = _('Label successfully updated')


class LabelDeleteView(SuccessMessageMixin, LoginRequiredMixin, 
                      ProtectedErrorMixin, DeleteView):
    model = Label
    template_name = 'delete.html'
    success_url = reverse_lazy('labels:list')
    success_message = _('Label successfully removed')
    permission_url = reverse_lazy('labels:list')
    error_message = _('Cannot delete label because its in use')
