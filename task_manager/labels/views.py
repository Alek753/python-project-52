from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Label
from .forms import LabelCreateForm

# Create your views here.
class LabelsListView(ListView):
    model = Label
    template_name = 'labels/labels_list.html'
    context_object_name = 'labels'

class LabelCreateView(SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelCreateForm
    template_name = 'labels/label_create.html'
    success_url = reverse_lazy('labels:list')
    success_message = 'Метка успешно создана!'

class LabelUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Label
    form_class = LabelCreateForm
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels:list')
    success_message = 'Метка успешно отредактирована!'

class LabelDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels:list')
    success_message = 'Метка успешно удалена!'
