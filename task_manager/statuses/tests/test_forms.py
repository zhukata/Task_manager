from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from task_manager.statuses.forms import StatusCraeteForm




class UserTestView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model()
        cls.form = StatusCraeteForm

    def test_create_form(self):
        response = self.client.get(reverse('user_create'))
        self.assertTemplateUsed(response, 'layouts/create.html')
        self.assertContains(response, '<form')
        self.assertTrue(issubclass(self.form, StatusCraeteForm))
        self.assertTrue('name', self.form.Meta.fields)