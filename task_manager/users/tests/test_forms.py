from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from task_manager.users.forms import UserRegisterForm


class UserTestView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model()
        cls.form = UserRegisterForm

    def test_register_form(self):
        response = self.client.get(reverse('user_create'))
        self.assertTemplateUsed(response, 'layouts/create.html')
        self.assertContains(response, '<form')
        self.assertTrue(issubclass(self.form, UserRegisterForm))
        self.assertTrue('username', self.form.Meta.fields)