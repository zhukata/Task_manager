from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
# from django.contrib import messages


class UserTestView(TestCase):
    fixtures = ["labels.json",
                'statuses.json',
                'tasks.json',
                'users.json',
                ]

    def test_list_users(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users.html')
        self.assertEqual(len(response.context["users"]), 2)
        # self.assertEqual(response.context["title"], 'users')###

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/users/login/?next=/tasks/')

    def test_logged(self):
        self.client.login(username='test_user', password='123456')
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        response = self.client.post(reverse('user_create'), {
            'username': 'test_user3',
            'first_name': 'test',
            'last_name': 'test',
            'password1': '123456test',
            'password2': '123456test',
        })
        self.assertTrue(get_user_model().objects.filter(username='test_user3').exists())
        self.assertRedirects(response, expected_url=reverse('user_login'))

    def test_update_user(self):
        self.client.login(username='test_user', password='123456')
        response = self.client.post(reverse('user_update', args=[1]), {
            'username': 'test_current',
            'first_name': 'test',
            'last_name': 'test',
            'password1': '123456test',
            'password2': '123456test',
        })
        self.assertRedirects(response, expected_url=reverse('users'))
        self.assertFalse(get_user_model().objects.filter(username='test_user').exists())
        self.assertTrue(get_user_model().objects.get(id=1).username == 'test_current')

    def test_user_has_no_permission_update(self):
        self.client.login(username='test_user_2', password='123456')
        response = self.client.get(reverse('user_update', args=[1]))
        self.assertRedirects(response, expected_url=reverse('users'))
        self.assertFalse(get_user_model().objects.filter(username='test_current').exists())
        # self.assertEqual(
        #     messages.get_messages(response.request)[0],
        #     'You do not have permission to modify another user.'
        # )

    def test_user_delete(self):
        self.client.login(username='test_user_2', password='123456')
        response = self.client.post(reverse('user_delete', args=[2]))
        self.assertRedirects(response, expected_url=reverse('users'))
        self.assertFalse(get_user_model().objects.filter(username='test_user_2').exists())

    def test_user_has_no_permission_delete(self):
        self.client.login(username='test_user_2', password='123456')
        response = self.client.get(reverse('user_delete', args=[1]), )
        self.assertRedirects(response, expected_url=reverse('users'))
        self.assertTrue(get_user_model().objects.filter(username='test_user_2').exists())
        # self.assertEqual(
        #     messages.get_messages(response.request)[0],
        #     'You do not have permission to modify another user.'
        # )

    def test_user_with_task_delete(self):
        self.client.login(username='test_user', password='123456')
        self.client.get(reverse('user_delete', args=[1]))
        # self.assertRedirects(response, expected_url=reverse('users'))
        self.assertTrue(get_user_model().objects.filter(username='test_user').exists())
