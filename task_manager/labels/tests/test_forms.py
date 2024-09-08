from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from task_manager.labels.forms import LabelCreateForm




class LabelTestView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model()
        cls.form = LabelCreateForm

    def test_create_form(self):
        self.user.objects.create_user(username='testuser', password='123456')
        login = self.client.login(username='testuser', password='123456')
        response = self.client.get(reverse('label_create'))
        self.assertTemplateUsed(response, 'layouts/create.html')
        self.assertContains(response, '<form')
        self.assertTrue(issubclass(self.form, LabelCreateForm))
        self.assertTrue('name', self.form.Meta.fields)