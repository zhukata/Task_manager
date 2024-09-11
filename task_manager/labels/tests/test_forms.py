from django.test import TestCase
from django.urls import reverse

from task_manager.labels.forms import LabelCreateForm




class LabelTestForm(TestCase):
    fixtures = [
        "labels.json",
        'statuses.json',
        'tasks.json',
        'users.json',
    ]

    def setUp(self):
        self.form = LabelCreateForm
        self.login = self.client.login(username='test_user', password='123456')

    def test_create_form(self):
        response = self.client.get(reverse('label_create'))
        self.assertTemplateUsed(response, 'layouts/create.html')
        self.assertContains(response, '<form')
        self.assertTrue(issubclass(self.form, LabelCreateForm))
        self.assertTrue('name', self.form.Meta.fields)