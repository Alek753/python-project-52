from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy

class UserAccessMixin(UserPassesTestMixin):
#    login_url = reverse_lazy('login')
    permission_url = reverse_lazy('users:list')
#    permission_denied_message = 'У вас нет прав для изменения другого пользователя.'

    def test_func(self):
        return self.request.user == self.get_object()

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect(self.permission_url)
