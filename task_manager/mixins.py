from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class UserAccessMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user == self.get_object()

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect(self.permission_url)


class TaskAccessMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user == self.get_object().author

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect(self.permission_url)


class ProtectedErrorMixin:
    error_message = None
    permission_url = '/'

    def post(self, request, *args, **kwargs):
        try:
            response = super().delete(request, *args, **kwargs)
            messages.success(self.request, self.success_message)
            return response
        except ProtectedError:
            messages.error(self.request, self.error_message)
            return redirect(self.permission_url)


class UserLoginMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request, _("You are not logged in! Please sign in."))
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
