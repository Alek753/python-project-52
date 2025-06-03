from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase  # noqa: F401
from django.urls import reverse

from .models import Label


class LabelTest(TestCase):

    def setUp(self):
        user_data = {
            'username': 'User1',
            'first_name': 'Name`',
            'last_name': 'Last1',
            'password1': '12q',
            'password2': '12q',
        }
        self.client.post(reverse('users:create'), user_data)
        self.client.login(username=user_data['username'], password='12q')

    def test_create(self):
        label_data = {'name': 'Label1'}
        response = self.client.post(reverse('labels:create'), label_data)
        self.assertRedirects(response, reverse('labels:list'))
        label = Label.objects.get(name=label_data['name'])
        self.assertEqual(label.name, label_data['name'])

    def test_update(self):
        label_data = {'name': 'Label1'}
        self.client.post(reverse('labels:create'), label_data)
        label = Label.objects.get(name=label_data['name'])
        self.assertEqual(label.name, label_data['name'])
        label_data_update = {'name': 'Label11'}
        self.client.post(reverse('labels:update', args=[label.id]),
                         label_data_update)
        label_new = Label.objects.get(name=label_data_update['name'])
        self.assertEqual(label_new.name, label_data_update['name'])

    def test_delete(self):
        label_data = {'name': 'Label1'}
        self.client.post(reverse('labels:create'), label_data)
        label = Label.objects.get(name=label_data['name'])
        self.assertEqual(label.name, label_data['name'])
        self.client.post(reverse('labels:delete', args=[label.id]))
        with self.assertRaises(ObjectDoesNotExist):
            Label.objects.get(name=label_data['name'])
