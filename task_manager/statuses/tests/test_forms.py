from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.forms import StatusCraeteForm




class LabelTestForm(TestCase):
    fixtures = [
        "labels.json",
        'statuses.json',
        'tasks.json',
        'users.json',
    ]

    def setUp(self):
        self.form = StatusCraeteForm
        self.login = self.client.login(username='test_user', password='123456')

    def test_create_form(self):
        response = self.client.get(reverse('status_create'))
        self.assertTemplateUsed(response, 'layouts/create.html')
        self.assertContains(response, '<form')
        self.assertTrue(issubclass(self.form, StatusCraeteForm))
        self.assertTrue('name', self.form.Meta.fields)
