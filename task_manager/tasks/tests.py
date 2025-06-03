from django.contrib.auth.models import User
from django.test import TestCase  # noqa: F401
from django.urls import reverse

from task_manager.labels.models import Label
from task_manager.statuses.models import Status

from .models import Task


class TaskModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="User1",
            password="12q",
            first_name="Name1",
            last_name="Last1",
        )

        self.another_user = User.objects.create_user(
            username="User2",
            password="12w",
            first_name="Name2",
            last_name="Last2",
        )

        self.status = Status.objects.create(name="Status1")

        self.status2 = Status.objects.create(name="Status2")

        self.label = Label.objects.create(name="Label1")
        self.label2 = Label.objects.create(name="Label2")

        self.task = Task.objects.create(
            name="Task1",
            description="Task1 description",
            status=self.status,
            author=self.user,
            executor=self.user,
        )

        self.task.labels.add(self.label, self.label2)

        self.tasks_url = reverse("tasks:list")
        self.task_detail_url = reverse(
            "tasks:details",
            kwargs={"pk": self.task.id})
        self.task_create_url = reverse("tasks:create")
        self.task_update_url = reverse(
            "tasks:update",
            kwargs={"pk": self.task.id})
        self.task_delete_url = reverse(
            "tasks:delete",
            kwargs={"pk": self.task.id})
        self.login_url = reverse("login")

    def test_task_list_view(self):
        response = self.client.get(self.tasks_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url,
                         f'{self.login_url}?next={self.tasks_url}')

        self.client.login(username="User1", password="12q")
        response = self.client.get(self.tasks_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/tasks_list.html")
        self.assertContains(response, "Task1")
        self.assertContains(response, "Status1")
        self.assertContains(response, "Name1 Last1")

        tasks = response.context["tasks"]
        self.assertEqual(len(tasks), 1)
        self.assertIn(self.task, tasks)

    def test_task_detail_view(self):
        response = self.client.get(self.task_detail_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url,
                         f'{self.login_url}?next={self.task_detail_url}')

        self.client.login(username="User1", password="12q")
        response = self.client.get(self.task_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/details.html")
        self.assertContains(response, "Task1")
        self.assertContains(response, "Task1 description")
        self.assertContains(response, "Status1")
        self.assertContains(response, "Label1")
        self.assertContains(response, "Label2")

        task = response.context["task"]
        self.assertEqual(task.id, self.task.id)
        self.assertEqual(task.name, "Task1")
        self.assertEqual(task.status, self.status)
        self.assertEqual(task.author, self.user)
        self.assertEqual(task.executor, self.user)
        self.assertEqual(list(task.labels.all()), [self.label, self.label2])

    def test_task_create_view(self):
        response = self.client.get(self.task_create_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url,
                         f'{self.login_url}?next={self.task_create_url}')

        self.client.login(username="User1", password="12q")
        response = self.client.get(self.task_create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "simple_create.html")
#        self.assertContains(response, "Создать")

        task_data = {
            "name": "Task2",
            "description": "Task2 description",
            "status": self.status.id,
            "executor": self.another_user.id,
            "labels": [self.label.id, self.label2.id],
        }

        response = self.client.post(self.task_create_url, task_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.tasks_url)

        self.assertEqual(Task.objects.count(), 2)
        new_task = Task.objects.get(name="Task2")

        self.assertEqual(new_task.description, "Task2 description")
        self.assertEqual(new_task.status, self.status)
        self.assertEqual(new_task.executor, self.another_user)
        self.assertEqual(new_task.author, self.user)

        invalid_task_data = {
            "name": "",
            "description": "Invalid Task",
            "status": self.status.id,
        }

        response = self.client.post(self.task_create_url, invalid_task_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.count(), 2)

    def test_task_update_view(self):
        response = self.client.get(self.task_update_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url,
                         f'{self.login_url}?next={self.task_update_url}')

        self.client.login(username="User1", password="12q")
        response = self.client.get(self.task_update_url)
        self.assertEqual(response.status_code, 200)

        task_data = {
            "name": "Updated Task",
            "description": "Updated description",
            "status": self.status2.id,
            "executor": self.another_user.id,
            "labels": [self.label.id],
        }

        response = self.client.post(self.task_update_url, task_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.tasks_url)
        self.task.refresh_from_db()
        self.assertEqual(self.task.name, "Updated Task")
        self.assertEqual(self.task.description, "Updated description")
        self.assertEqual(self.task.status, self.status2)
        self.assertEqual(self.task.executor, self.another_user)

        invalid_task_data = {
            "name": "",
            "description": "Invalid Update",
            "status": self.status.id,
            "executor": self.user.id,
        }

        response = self.client.post(self.task_update_url, invalid_task_data)
        self.assertEqual(response.status_code, 200)
        self.task.refresh_from_db()
        self.assertEqual(self.task.name, "Updated Task")

    def test_task_delete_view(self):
        response = self.client.get(self.task_delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, self.tasks_url)

        self.client.login(username="User1", password="12q")
        response = self.client.get(self.task_delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "delete.html")
#        self.assertContains(response, "Да, удалить")

        response = self.client.post(self.task_delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    def test_task_delete_by_not_author(self):
        self.client.login(username="User2", password="12w")
        response = self.client.get(self.task_delete_url)
        self.assertEqual(response.status_code, 302)

        response = self.client.post(self.task_delete_url)
        self.assertEqual(response.status_code, 302)

        self.assertEqual(Task.objects.count(), 1)
        self.assertTrue(Task.objects.filter(id=self.task.id).exists())

    def test_task_filter(self):
        self.client.login(username="User2", password="12w")

        response = self.client.get(self.tasks_url, {"status": self.status2.id})
        self.assertEqual(response.status_code, 200)

        tasks = response.context["tasks"]
        self.assertNotIn(self.task, tasks)
