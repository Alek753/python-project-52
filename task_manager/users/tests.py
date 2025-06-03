from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase  # noqa: F401
from django.urls import reverse


class UsersTest(TestCase):

    def test_registration(self):
        user_data = {
            'first_name': 'Name1',
            'last_name': 'Last1',
            'username': 'User1',
            'password1': '12q',
            'password2': '12q'
        }
        response = self.client.post(reverse('users:create'), user_data)
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='User1').exists())

    def test_update(self):
        user_data = {
            'first_name': 'Name1',
            'last_name': 'Last1',
            'username': 'User1',
            'password1': '12q',
            'password2': '12q'
        }
        response = self.client.post(reverse('users:create'), user_data)
        self.client.login(username=user_data['username'], password='12q')
        user_updated_data = {
            'first_name': 'Name11',
            'last_name': 'Last11',
            'username': 'User11',
            'password1': '12qW',
            'password2': '12qW'
        }
        user = User.objects.get(username=user_data['username'])
        response = self.client.post(
            reverse('users:user_update', args=[user.id]), user_updated_data
        )
        self.assertRedirects(response, reverse('users:list'))

    def test_delete(self):
        user_data = {
            'first_name': 'Name11',
            'last_name': 'Last11',
            'username': 'User11',
            'password1': '12qW',
            'password2': '12qW'
        }
        response = self.client.post(reverse('users:create'), user_data)
        self.client.login(username=user_data['username'], password='12qW')
        user = User.objects.get(username=user_data['username'])
        response = self.client.post(reverse(
            'users:user_delete', 
            args=[user.id])
        )
        self.assertRedirects(response, reverse('users:list'))
        with self.assertRaises(ObjectDoesNotExist):
            User.objects.get(username=user_data['username'])

    def test_read(self):
        user_data = {
            'first_name': 'Name11',
            'last_name': 'Last11',
            'username': 'User11',
            'password1': '12qW',
            'password2': '12qW'
        }
        self.client.post(reverse('users:create'), user_data)
        user = User.objects.get(username=user_data['username'])
        self.assertEqual(user.first_name, user_data['first_name'])
        self.assertEqual(user.last_name, user_data['last_name'])
        self.assertEqual(user.username, user_data['username'])
