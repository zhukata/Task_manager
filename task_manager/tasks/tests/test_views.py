from django.test import TestCase
from django.urls import reverse

from task_manager.tasks.models import Label

class TaskListViewTest(TestCase):
    fixtures = [
        "labels.json",
        'statuses.json',
        'tasks.json',
        'users.json',
    ]

    def setUp(self):
        self.client.login(username='test_user', password='123456')
    
    def test_list_view(self):
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/tasks.html')
        self.assertEqual(len(response.context["tasks"]), 1)
        self.assertEqual(response.context["title"], 'tasks')