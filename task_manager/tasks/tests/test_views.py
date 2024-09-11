from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task

class TaskViewTest(TestCase):
    fixtures = [
        "labels.json",
        'statuses.json',
        'tasks.json',
        'users.json',
    ]

    def setUp(self):
        self.client.login(username='test_user', password='123456')
        self.status = Status.objects.get(id=1)
    
    def test_show_view(self):
        response = self.client.get(reverse('task_show', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/show.html')
        self.assertEqual((response.context['object'].name), Task.objects.get(id=1).name)
    
    def test_list_view(self):
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/tasks.html')
        self.assertEqual(len(response.context["tasks"]), 1)

    def test_create_view(self):
        response = self.client.post(reverse('task_create'), {
            'name': 'current_test',
            'status': self.status.id,
        })
        self.assertRedirects(response, expected_url=reverse('tasks'))
        self.assertTrue(Task.objects.filter(name='current_test').exists())

    def test_update_view(self):
        response = self.client.post(reverse('task_update', args=[1]), {
            'name': 'current_test',
            'description': 'test',
            'status': self.status.id,
        })
        self.assertRedirects(response, expected_url=reverse('tasks'))
        self.assertEqual(Task.objects.get(id=1).name, 'current_test')
        self.assertFalse(Task.objects.filter(name='test_task').exists())

    def test_delete(self):
        self.client.post(reverse('task_delete', args=[1]))
        response = self.client.get(reverse('tasks'))
        self.assertEqual(len(response.context["tasks"]), 0)
        self.assertFalse(Task.objects.filter(name='test_task').exists())

    def test_delete_no_author(self):
        self.client.login(username='test_user_2', password='123456')
        response = self.client.get(reverse('task_delete', args=[1]), )
        self.assertRedirects(response, expected_url=reverse('tasks'))
        self.assertTrue(Task.objects.filter(name='test_task').exists())