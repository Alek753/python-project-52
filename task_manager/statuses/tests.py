from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase  # noqa: F401
from django.urls import reverse

from .models import Status


class StatusTest(TestCase):

    def setUp(self):
        user_data = {
            'username': 'User1',
            'first_name': 'Name1',
            'last_name': 'Last1',
            'password1': '12q',
            'password2': '12q',
        }
        self.client.post(reverse('users:create'), user_data)
        self.client.login(username=user_data['username'], password='12q')

    def test_create(self):
        status_data = {'name': 'Status1'}
        response = self.client.post(reverse('statuses:create'), status_data)
        self.assertRedirects(response, reverse('statuses:list'))
        status = Status.objects.get(name=status_data['name'])
        self.assertEqual(status.name, status_data['name'])

    def test_update(self):
        status_data = {'name': 'Status1'}
        self.client.post(reverse('statuses:create'), status_data)
        status = Status.objects.get(name=status_data['name'])
        self.assertEqual(status.name, status_data['name'])
        status_update_data = {'name': 'Status11'}
        self.client.post(
            reverse('statuses:update', args=[status.id]), status_update_data
        )
        status_new = Status.objects.get(name=status_update_data['name'])
        self.assertEqual(status_new.name, status_update_data['name'])

    def test_delete(self):
        status_data = {'name': 'Status1'}
        self.client.post(reverse('statuses:create'), status_data)
        status = Status.objects.get(name=status_data['name'])
        self.assertEqual(status.name, status_data['name'])
        self.client.post(reverse('statuses:delete', args=[status.id]))
        with self.assertRaises(ObjectDoesNotExist):
            Status.objects.get(name=status_data['name'])
