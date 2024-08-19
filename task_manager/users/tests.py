from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from task_manager.users.forms import UserRegisterForm

class UserTest(TestCase):
    def setUp(self):
        self.form = UserRegisterForm
        # self.test_user = get_user_model().objects.create(
        #     username='test_user',
        #     password1='000000',
        #     password2='000000')

    def test_users(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users.html')

    def test_register_get(self):
        response = self.client.get(reverse('user_create'))
        self.assertTemplateUsed(response, 'users/sign_up.html')
        self.assertContains(response, '<form')
        self.assertTrue(issubclass(self.form, UserRegisterForm))
        self.assertTrue('username', self.form.Meta.fields)

    def test_register_post(self):

        response = self.client.post('/users/create', {
            'username': 'user1',
            'password1': '123456',
            'password2': '123456',
        })
        # print(get_user_model())
        # self.assertTrue(get_user_model().objects.first().username, 'user1' )
        # self.assertRedirects(response, expected_url=reverse('user_login')) # why 301
        # self.assertEqual(get_user_model().objects.count(), 0)

        # form = self.form({
        #     'username': 'login',
        #     'password' : '123456'
        # })
