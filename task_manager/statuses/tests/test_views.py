from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status


class StatusViewTest(TestCase):
    fixtures = ["labels.json",
                'statuses.json',
                'tasks.json',
                'users.json',
                ]

    def setUp(self):
        self.client.login(username='test_user', password='123456')

    def test_list_view(self):
        response = self.client.get(reverse('statuses'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/statuses.html')
        self.assertEqual(len(response.context["statuses"]), 2)

    def test_create_view(self):
        response = self.client.post(reverse('status_create'), {
            'name': 'current_test',
        })
        self.assertRedirects(response, expected_url=reverse('statuses'))
        self.assertTrue(Status.objects.filter(name='current_test').exists())

    def test_update_view(self):
        response = self.client.post(reverse('status_update', args=[1]), {
            'name': 'current_test',
        })
        self.assertRedirects(response, expected_url=reverse('statuses'))
        self.assertEqual(Status.objects.get(id=1).name, 'current_test')
        self.assertFalse(Status.objects.filter(name='test_status_1').exists())

    def test_delete(self):
        self.client.post(reverse('status_delete', args=[2]))
        response = self.client.get(reverse('statuses'))
        self.assertEqual(len(response.context["statuses"]), 1)
        self.assertFalse(Status.objects.filter(name='test_status_2').exists())

    def test_delete_with_task(self):
        self.client.post(reverse('status_delete', args=[1]))
        self.assertTrue(Status.objects.filter(id=1).exists())
