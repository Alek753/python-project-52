from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin


def index(request):
    return render(request, 'index.html')


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    next_page = 'home_page'
    success_message = 'Вы успешно вошли!'


class UserLogoutView(LogoutView):
    next_page = 'home_page'
    success_message = 'Вы успешно вышли!'

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Вы разлогинены")
        return super().dispatch(request, *args, **kwargs)

