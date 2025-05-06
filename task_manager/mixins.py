from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db.models import ProtectedError


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
    error_message = ''
    permission_url = '/'

    def post(self, request, *args, **kwargs):
        try:
            response = super().delete(request, *args, **kwargs)
            return response
        except ProtectedError:
            messages.error(request, self.error_message)
            return redirect(self.permission_url)
